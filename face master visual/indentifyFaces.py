import face_recognition
from PIL import Image, ImageDraw
import os

image_of_ertugrul = face_recognition.load_image_file('Ertugrul.jpg')
ertugrul_face_encoding = face_recognition.face_encodings(image_of_ertugrul)[0]

image_of_burak = face_recognition.load_image_file('Burak.JPG')
burak_face_encoding = face_recognition.face_encodings(image_of_burak)[0]

#An array of encoding and names

known_face_encodings = [
    ertugrul_face_encoding,
    burak_face_encoding
]

known_face_names = [
    #"ertugrul",
    #"burak"
    os.path.splitext("Ertugrul.jpeg")[0],
    os.path.splitext("Burak.jpep")[0]
]

#Loading Test Image and Finding Faces in it

test_image = face_recognition.load_image_file('Ertugrul2.JPG')

#Find Faces in Test Image

face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image,face_locations)

#Converting to PIL Format

pil_image = Image.fromarray(test_image)

#Create a Image Draw Instance

draw = ImageDraw.Draw(pil_image)

#Look Through Faces in Test Image

for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown Person"

    #If Matches
    if True in matches:
        first_macth_index = matches.index(True)
        name = known_face_names[first_macth_index]

    #Draw a Box 

    draw.rectangle(((left, bottom),(right, bottom)), outline=(0,0,0))

    #Draw a Label

    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 1000), (right, bottom)),  outline=(0,150,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))

del draw

#Display Image
pil_image.show()