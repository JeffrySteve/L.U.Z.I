import os
import eel
import cv2
import face_recognition
from engine.features import *

def face_recognition_setup():
    # Load an image containing the face(s) you want to recognize
    known_image_path = r"A:\\Luzi\\www\\assests\\img\\Jeffry\\Jeffry8.jpg"
    known_image = face_recognition.load_image_file(known_image_path)
    known_face_encoding = face_recognition.face_encodings(known_image)[0]

    # Create an array of known face encodings and corresponding names
    known_face_encodings = [known_face_encoding]
    known_face_names = ["Jeffry8"]

    return known_face_encodings, known_face_names

def start_face_recognition():
    # Setup face recognition
    known_face_encodings, known_face_names = face_recognition_setup()

    # Start capturing video from the default camera (change index if using an external camera)
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture each frame
        ret, frame = video_capture.read()

        # Find all face locations and face encodings in the current frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Loop through each face found in the frame
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Check if the face matches any known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

                # Trigger actions based on the recognized face
                if name == "Jeffry8":
                    PlayAssistantSound()
                    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
                    eel.start('index.html', mode=None, host='localhost', block=True)

            # Draw a rectangle and label the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    video_capture.release()
    cv2.destroyAllWindows()

eel.init("www")
start_face_recognition()
