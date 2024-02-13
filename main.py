import requests

PEXELS_API_KEY = ''
query = 'sad'
page = 1
per_page = 1
size= 'large'
orientation='portrait'

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
        
        # Guardar el video en un archivo
        with open(f"{video['id']}.mp4", 'wb') as outfile:
            outfile.write(r.content)
else:
    print('Error al realizar la solicitud a la API de Pexels.')
