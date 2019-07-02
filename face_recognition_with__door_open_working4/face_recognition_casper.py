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
from tkinter import filedialog
#from finalGui import gui
import shutil
from sound import SOUND

class CasperFaceID:

    canOpen=True
    canThreadStartable=True

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
        from PIL import Image
        # Choose with cam you want to use for adding a person
        cameraId = 0

        # The new persons name take it as a popup input
        personName = simpledialog.askstring("Name","Enter the Persons Name")

        # Decide which location you are going to save
        list = os.listdir(r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\database")

        ###CONTROL###
        print(list)
        ###CONTROL###
        # make statements for input error
        for i in range(len(list)):
            while personName==list[i] or personName=='':
                if personName==list[i]:
                    personName = simpledialog.askstring("Input Name", "This Person Exist, Type Another one")
                elif personName=='':
                    personName = simpledialog.askstring("Input Name", "Enter a Person NAME!")
        # Start capturing video
        video_capture = cv2.VideoCapture(cameraId)
        if personName==None:
            video_capture.release()
            cv2.destroyAllWindows()
            return None
        # Specify the location where you are going to save
        directoryNamePath = "database/"+str(personName)
        os.mkdir(directoryNamePath)

        ###CONTROL###
        print(directoryNamePath)
        ###CONTROL###
        # Read the frame of the video
        ret, frame = video_capture.read()
        # How many images saved
        countForSavedImages = 1
        while True:

            # Grab a single frame of video
            (ret, frame) = video_capture.read()

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_frame = frame[:, :, ::-1]

            # Find all the faces and face encodings in the frame of video
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
            # Counting and saving 5 different images
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
        # Door can open or not
        canOpen = True
        # Initializing the cam1
        cameraId = 0;
        video_capture = cv2.VideoCapture(cameraId)
        # Initializing the cam2
        cameraId1 = 1
        video_capture1 = cv2.VideoCapture(cameraId1)
        # Looking the files that includes database
        list = os.listdir(r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\database")

        ###CONTROL###
        print(list)
        number_files = len(list)
        print(number_files)
        ###CONTROL###
        # Creating an array to store data
        files = []
        # Initializing the files[] array
        for r, d, f in os.walk(r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\database"):
            for file in f:
                if '.jpg' or '.JPG' in file:
                    files.append(os.path.join(r, file))

        # Declaring variables for faces in database
        known_face_names = [0 for x in range(len(list))]
        image_of_people = [0 for x in range(len(files))]
        known_face_encodings = [0 for x in range(len(files))]

        ###CONTROL###
        print(files)
        print(len(image_of_people))
        print(len(known_face_encodings))
        print(len(files))
        ###CONTROL###

        # Inıtialzing Variable for known face names
        for i in range(len(list)):
            known_face_names[i] = list[i]

        # Inıtialzing Variable for known faces
        for i in range(len(files)):
            image_of_people[i] = face_recognition.load_image_file(files[i])
        # Initializing Variable for known face encodingS
        for j in range(len(files)):
            known_face_encodings[j] = face_recognition.face_encodings(image_of_people[j])[0]

        ###CONTROL###
        print(known_face_names)
        print(image_of_people)
        print(known_face_encodings)
        ###CONTROL###

        while True:
            # Grab a single frame of video
            ret, mainFrame = video_capture.read()
            ret1, mainFrame1 = video_capture1.read()
            defaultFrame = mainFrame
            # Resizing frame for easy encoding
            frame = cv2.resize(mainFrame, (0, 0), fx=0.25, fy=0.25)
            frame1 = cv2.resize(mainFrame1, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_frame = frame[:, :, ::-1]
            rgb_frame1 = frame1[:, :, ::-1]
            # Find all the faces and face encodings in the frame of both videos
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
            face_locations1 = face_recognition.face_locations(rgb_frame1)
            face_encodings1 = face_recognition.face_encodings(rgb_frame1, face_locations1)
            ## If a frame does not include any faces we do not need to compare it
            if not face_locations or not face_encodings:
                face_locations = face_locations1
                face_encodings = face_encodings1
                defaultFrame = mainFrame1

            # Loop through each face in this frame of video
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

                name = "Unknown"
                # Look all faces to see how much it like with the frame of the video
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

                ###CONTROL###
                print(face_distances)
                ###CONTROL###

                # Find which faces that frame similar with
                best_match_index = np.argmin(face_distances)
                # If it matches
                if matches[best_match_index]:
                    # Divide the 'best_match_index/5' because every person has 5 faces in databese
                    name = (known_face_names[math.floor(((best_match_index) / 5))])
                    # If distance bitween them is greater than 0.50 that person can open the door
                    if canOpen and face_distances[best_match_index] < 0.50:

                        ###CONTROL###
                        print("Buldum:")
                        print(face_distances)
                        print(known_face_names[math.floor(((best_match_index) / 5))])
                        ###CONTROL###

                        # self.open()
                        _thread.start_new_thread(self.WaitForOpen, ())
                # 4 because we resize the frames with 0.25
                multi = 4
                # Draw a box around the face
                cv2.rectangle(defaultFrame, (left * multi, top * multi), (right * multi, bottom * multi), (0, 0, 255),2)

                # Draw a label with a name below the face
                cv2.rectangle(defaultFrame, (left * multi, bottom * multi - 35), (right * multi, bottom * multi),(0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                # Put text in that box
                cv2.putText(defaultFrame, name, (left * multi + 6, bottom * multi - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Video', mainFrame)
            cv2.imshow('USB Camera', mainFrame1)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()

    def remove(self,selectedFile):
        list = os.listdir(r"C:\Users\12\PycharmProjects\face_recognition_with__door_open\database")
        print(list)
        shutil.rmtree(os.path.join(selectedFile))



