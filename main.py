import requests
import cv2
import numpy as np
import os

PEXELS_API_KEY = 'YVKnAcV4qx4wjXk72SdybECg3SayuBFbxO1vajKrn5a0E8MnRARLAJ7z'
query = 'fitness'
page = 2
per_page = 1
size = 'large'
orientation = 'portrait'
desired_width = 1080
desired_height = 1920

# Hacer la solicitud a la API de Pexels
url = f'https://api.pexels.com/videos/search?query={query}&per_page={per_page}&page={page}&size={size}&orientation={orientation}'
headers = {'Authorization': PEXELS_API_KEY}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    videos = data.get('videos', [])

    for video in videos:
        # Obtener la URL de descarga del video
        url_video = video['video_files'][0]['link']
        
        # Descargar el video
        r = requests.get(url_video)
        
        # Guardar el video en un archivo temporal
        with open(f"{video['id']}_temp.mp4", 'wb') as outfile:
            outfile.write(r.content)

        # Redimensionar el video a la resolución deseada
        cap = cv2.VideoCapture(f"{video['id']}_temp.mp4")
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(f"{video['id']}_resized.mp4", fourcc, 30, (desired_width, desired_height))

        while(cap.isOpened()):
            ret, frame = cap.read()
            if not ret:
                break
            resized_frame = cv2.resize(frame, (desired_width, desired_height))
            out.write(resized_frame)

        cap.release()
        out.release()
        
        # Eliminar el archivo temporal
        os.remove(f"{video['id']}_temp.mp4")

else:
    print('Error al realizar la solicitud a la API de Pexels.')
