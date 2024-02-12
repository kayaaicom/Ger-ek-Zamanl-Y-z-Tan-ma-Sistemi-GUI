import face_recognition
import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk

known_face_encodings = []
known_face_metadata = []
known_faces_filenames = ["Elon_Musk.jpg", "Recep_Tayyip_Erdoğan.jpg", "Hadise.jpeg", "Kıvanç_Tatlıtuğ.png"] 

for filename in known_faces_filenames:
    image = face_recognition.load_image_file(filename)
    face_encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(face_encoding)

    name_surname_split = filename.split('.')[0].split('_')
    name = ' '.join(name_surname_split[:-1])  
    surname = name_surname_split[-1]  
    known_face_metadata.append({'name': name, 'surname': surname})


root = Tk()
root.title("Yüz Tanıma Sistemi")

info_frame = Frame(root)
info_frame.pack(side=BOTTOM, fill=X, expand=1)

label_info = Label(info_frame, text="Tanınan Kişi: Yok", font=('Helvetica', 18, 'bold'), bg='black', fg='white')
label_info.pack(side=LEFT, fill=X, expand=1)

image_label = Label(root)
image_label.pack()

video_capture = cv2.VideoCapture(0)

def update():

    ret, frame = video_capture.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_frame = Image.fromarray(rgb_frame)
    tk_frame = ImageTk.PhotoImage(pil_frame)

    image_label.configure(image=tk_frame)
    image_label.image = tk_frame

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Tanınan Kişi: Yok"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            matched_metadata = known_face_metadata[best_match_index]
            name = f"Tanınan Kişi: {matched_metadata['name'].title()} {matched_metadata['surname'].title()}"

        label_info.config(text=name)

    root.after(100, update)  

update() 
root.mainloop() 

video_capture.release() 
