import face_recognition
import cv2
import pandas as pd
from datetime import datetime
import os
import glob

# Cargar rostros conocidos
known_encodings, known_names = [], []
for path in glob.glob("known_faces/*.jpg") + glob.glob("known_faces/*.png"):
    name = os.path.splitext(os.path.basename(path))[0]
    img = face_recognition.load_image_file(path)
    encs = face_recognition.face_encodings(img)
    if encs:
        known_encodings.append(encs[0])
        known_names.append(name)

if not known_encodings:
    print("No hay rostros registrados. Ejecuta register.py primero.")
    exit()

# CSV de asistencia del día
os.makedirs("attendance", exist_ok=True)
today = datetime.now().strftime("%Y-%m-%d")
csv_path = f"attendance/{today}.csv"
df = pd.read_csv(csv_path) if os.path.exists(csv_path) else pd.DataFrame(columns=["nombre", "hora"])
registered = set(df["nombre"].tolist())

cap = cv2.VideoCapture(0)
print("Sistema iniciado. Presiona Q para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

    locations = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, locations)

    for enc, loc in zip(encodings, locations):
        dists = face_recognition.face_distance(known_encodings, enc)
        name = "Desconocido"
        if len(dists) and dists.min() < 0.5:
            name = known_names[dists.argmin()]
            if name not in registered:
                hora = datetime.now().strftime("%H:%M:%S")
                df = pd.concat([df, pd.DataFrame([{"nombre": name, "hora": hora}])], ignore_index=True)
                df.to_csv(csv_path, index=False)
                registered.add(name)
                print(f"✓ {name} — {hora}")

        top, right, bottom, left = [v * 4 for v in loc]
        color = (0, 200, 0) if name != "Desconocido" else (0, 0, 200)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    cv2.imshow("Asistencia — Q para salir", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
