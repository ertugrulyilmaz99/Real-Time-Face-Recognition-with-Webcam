import face_recognition

image = face_recognition.load_image_file('team1.jpg')

#Array which keeps face coordinates
face_locations=face_recognition.face_locations(image)

print(face_locations)

print(len(face_locations)," number of people")