import os
from yt_dlp import YoutubeDL
import imageio_ffmpeg as ffmpeg
import flet as ft

# Carpeta donde almacena la música descargada
carpeta = "./descargas"

# Descarga la música con yt-dlp y convierte con FFmpeg
def yt_dl(url):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    descarga = {
        'format': 'bestaudio/best',
        'outtmpl': f'{carpeta}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': ffmpeg.get_ffmpeg_exe(),
        'noplaylist': True
    }
    with YoutubeDL(descarga) as ydl:
        informacion = ydl.extract_info(url, download=True)
        ruta_musica = f"{carpeta}/{informacion['title']}.mp3"
        return ruta_musica, informacion['title']

# Interfaz gráfica con Flet
def main(page: ft.Page):
    page.title = "YouTube DL"
    page.window_width = 400
    page.window_height = 250
    page.window_resizable = False
    page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    url_input = ft.TextField(label="Link de YouTube", width=350)
    output_text = ft.Text(value="", size=20)

    def descargar_cancion(e):
        url = url_input.value
        if not url:
            output_text.value = "Por favor, ingrese un link válido."
            page.update()
            return
        
        output_text.value = "Procesando descarga..."
        page.update()
        ruta_musica, nombre_musica = yt_dl(url)
        output_text.value = f"Canción descargada: {nombre_musica}\nGuardada en: {ruta_musica}"
        page.update()

    download_button = ft.ElevatedButton(
        text="Descargar",
        on_click=descargar_cancion
    )

    page.add(
        ft.Column(
            [
                ft.Text("Descarga youtube a mp3", size=18, weight=ft.FontWeight.BOLD),
                url_input,
                download_button,
                output_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)

#info
"""
https://youtu.be/bRqbHpXklPU?si=4nezoLN9h_78sc4R
https://flet.dev/docs/
"""