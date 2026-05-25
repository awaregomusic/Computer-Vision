import face_recognition
import cv2
import os

name = input("Nombre: ").strip()
os.makedirs("known_faces", exist_ok=True)

cap = cv2.VideoCapture(0)
print("Presiona ESPACIO para capturar, Q para cancelar.")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Registro", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord(" "):
        path = f"known_faces/{name}.jpg"
        cv2.imwrite(path, frame)
        img = face_recognition.load_image_file(path)
        if face_recognition.face_encodings(img):
            print(f"Rostro registrado: {path}")
        else:
            os.remove(path)
            print("No se detectó un rostro. Intenta de nuevo.")
        break
    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
