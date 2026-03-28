import cv2
import face_recognition
import os
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk

# Function to get the encoding of an image
def get_face_encoding(image_path):
    image = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(image)[0]
    return face_encoding

# Update the 'persons' directory path
persons_folder = os.path.join(os.path.dirname(__file__), "persons")

# Load known face encodings and corresponding person IDs
known_face_encodings = []
person_ids = []

try:
    for filename in os.listdir(persons_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            path = os.path.join(persons_folder, filename)
            person_id = os.path.splitext(filename)[0]
            face_encoding = get_face_encoding(path)

            known_face_encodings.append(face_encoding)
            person_ids.append(person_id)
except FileNotFoundError:
    print("Error: The specified path does not exist.")
    # Add additional handling as needed

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# Create a Tkinter window
window = tk.Tk()
window.title("Face Recognition System")

# Define the layout
window.geometry("800x600")

# Create a label to display the video feed
video_label = Label(window)
video_label.pack(side="left", fill="both", expand=True)

# Create a label to display the recognized names
names_label = Label(window, text="IN FRAME FACES", font=("Arial", 14))
names_label.pack(side="top", padx=30, pady=30)

# Create a listbox to show names
names_listbox = tk.Listbox(window, font=("Arial", 12), bg="white", fg="black")
names_listbox.pack(side="top", padx=10, pady=10)

# Create a label to display all recognized names
all_names_label = Label(window, text="ALL RECOGNIZED FACES", font=("Arial", 14))
all_names_label.pack(side="top", padx=30, pady=30)

# Create a listbox to show all recognized names
all_names_listbox = tk.Listbox(window, font=("Arial", 12), bg="white", fg="black")
all_names_listbox.pack(side="top", padx=10, pady=10)

# Keep track of all recognized names
all_recognized_names_set = set()

# Function to update the video feed
def update_video():
    ret, frame = video_capture.read()
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally

    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    recognized_names = []

    # Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any known face
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        # Display the name of the recognized individual
        name = "Unknown"
        if True in matches:
            first_match_index = matches.index(True)
            name = person_ids[first_match_index]
            recognized_names.append(name)
            all_recognized_names_set.add(name)

        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        
        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 0, 0), 1)

    # Convert the frame to ImageTk format
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(image=img)

    # Update the video label
    video_label.config(image=img)
    video_label.image = img

    # Update the names listbox with current recognized names
    names_listbox.delete(0, tk.END)
    for name in recognized_names:
        names_listbox.insert(tk.END, name)

    # Update the all recognized names listbox
    all_names_listbox.delete(0, tk.END)
    for name in all_recognized_names_set:
        all_names_listbox.insert(tk.END, name)

    # Call this function again after 10 milliseconds
    window.after(10, update_video)

# Create a button to stop the application
stop_button = Button(window, text="Stop", command=window.quit, font=("Arial", 12))
stop_button.pack(side="bottom", padx=10, pady=10)

# Start the video update loop
update_video()

# Run the Tkinter main loop
window.mainloop()

# Release the webcam and close all windows
video_capture.release()
cv2.destroyAllWindows()
