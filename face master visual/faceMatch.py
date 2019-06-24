import face_recognition

image_of_ertugrul=face_recognition.load_image_file('Ertugrul.jpg')
ertugrul_face_encoding=face_recognition.face_encodings(image_of_ertugrul)[0]

unknown_image=face_recognition.load_image_file('Burak.JPG')
unknown_face_encoding=face_recognition.face_encodings(unknown_image)[0]

#Comparing Faces
result=face_recognition.compare_faces([ertugrul_face_encoding],unknown_face_encoding)

if result[0]:
    print("Same Person")
else:
    print("Not same person")