import _thread,os
import asyncio
import time
import tkinter as tk
from tkinter import simpledialog
import numpy as np
import face_recognition,cv2,sys, os,serial
from PIL import Image
from tkinter import *
import sys
import math

from sound import SOUND

class CasperFaceID:
    canOpen=True

    def WaitForOpen(self):
        count = 0
        self.canOpen = False
        while count < 4:
            time.sleep(1)
            count += 1
        self.canOpen = True

    def open(self):
        ser = serial.Serial("com3", 9600)

        t = 130
        while (t > 0):
            ser.write(str.encode('done'))
    #        a = str(ser.readable())
            t -= 1

        print("Seri Porta 'done' gönderildi")

    def addPerson(self):
        cameraId = 1
        from PIL import Image
        #popup = tk.Tk()

        personName = simpledialog.askstring("Name","Enter the Persons Name")
        #popup.destroy()
        #popup.mainloop()
        list = os.listdir(r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\database")
        print(list)
        for i in range(len(list)):
            while personName==list[i] or personName=='':
                if personName==list[i]:
                    personName = simpledialog.askstring("Input Name", "This Person Exist, Type Another one")
                elif personName=='':
                    personName = simpledialog.askstring("Input Name", "Enter a Person NAME!")
        video_capture = cv2.VideoCapture(cameraId)
        if personName==None:
            video_capture.release()
            cv2.destroyAllWindows()
            return None

        directoryNamePath = "database/"+str(personName)
        print(directoryNamePath)
        os.mkdir(directoryNamePath)

        ret, frame = video_capture.read()
        countForSavedImages = 1
        while True:

            # Grab a single frame of video
            ret, frame = video_capture.read()

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_frame = frame[:, :, ::-1]

            # Find all the faces and face enqcodings in the frame of video
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for face_location in face_locations:
                if countForSavedImages<6:
                    top, right, bottom, left = face_location
                    face_locations = face_recognition.face_locations(rgb_frame)
                    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
                    face_image = rgb_frame[top:bottom, left:right]
                    pil_image = Image.fromarray(face_image)
                    savePath = "database/" + str(personName)+"/" + str(personName) + "-" + str(countForSavedImages) + ".jpg"
                    pil_image.save(savePath)
                    pil_image._close_exclusive_fp_after_loading
                    countForSavedImages += 1
                    print(countForSavedImages)

            # Loop through each face in this frame of video
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                name = personName

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Video', frame)

            # Hit 'q' on the keyboard to quit!
            cv2.waitKey(1)
            if(countForSavedImages>=6):
                video_capture.release()
                cv2.destroyAllWindows()
                break

        # Release handle to the webcam
        #video_capture.release()
        #cv2.destroyAllWindows()

    def detect(self):
        cameraId=0;
        canOpen = True
        video_capture = cv2.VideoCapture(cameraId)

        cameraId1=1
        video_capture1=cv2.VideoCapture(cameraId1)


        list = os.listdir(r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\database")
        print(list)
        number_files = len(list)
        print(number_files)



        files = []

        for r, d, f in os.walk(r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\database"):
            for file in f:
                if '.jpg' or '.JPG' in file:
                    files.append(os.path.join(r, file))

        # Declaring variables for faces
        known_face_names = [0 for x in range(len(list))]
        image_of_people = [0 for x in range(len(files))]
        known_face_encodings = [0 for x in range(len(files))]
        print(files)
        print(len(image_of_people))
        print(len(known_face_encodings))
        print(len(files))
        # Inıtialzing Variables for known faces
        for i in range(len(list)):
            known_face_names[i] = list[i]

        # Inıtialzing Variables for known faces
        for i in range(len(files)):


            image_of_people[i] = face_recognition.load_image_file(files[i])

        for j in range(len(files)):

            known_face_encodings[j] = face_recognition.face_encodings(image_of_people[j])[0]


        print(known_face_names)
        print(image_of_people)

        while True:
            # Grab a single frame of video
            ret, frame = video_capture.read()
            ret1, frame1 = video_capture1.read()
            defaultFrame = frame
            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_frame = frame[:, :, ::-1]
            rgb_frame1 = frame1[:, :, ::-1]
            # Find all the faces and face enqcodings in the frame of video
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
            face_locations1 = face_recognition.face_locations(rgb_frame1)
            face_encodings1 = face_recognition.face_encodings(rgb_frame1,face_locations1)
            if not face_locations or not face_encodings:
                face_locations=face_locations1
                face_encodings=face_encodings1
                defaultFrame = frame1

            # Loop through each face in this frame of video
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

                name = "Unknown"

                # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                print(face_distances)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = (known_face_names[math.floor(((best_match_index)/5))])
                    if canOpen and face_distances[best_match_index] <0.50:
                        # loop = asyncio.get_event_loop()
                        # sound = asyncio.ensure_future(SOUND.welcome(known_face_names[best_match_index]))
                         #sound1 = asyncio.ensure_future(SOUND.beep(self))
                            #loop.run_until_complete(sound1)
                        # loop.run_until_complete(sound)"""
                        print("Buldum:")
                        print(face_distances)

                        print(known_face_names[math.floor(((best_match_index)/5))])
                        #self.open()
                        _thread.start_new_thread(self.WaitForOpen, ())

                #Draw a box around the face
                cv2.rectangle(defaultFrame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(defaultFrame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(defaultFrame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


            # Display the resulting image
            cv2.imshow('Video', frame)
            cv2.imshow('USB Camera',frame1)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()
