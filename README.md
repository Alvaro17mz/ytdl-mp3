
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flet](https://img.shields.io/badge/Flet-0.4.x-green)](https://flet.dev/)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-2024.x-orange)](https://github.com/yt-dlp/yt-dlp)

Una herramienta sencilla para descargar audios de YouTube en formato MP3 con una interfaz gráfica construida usando [Flet](https://flet.dev/). Combina la potencia de **yt-dlp** y **FFmpeg**.
---

## 🚀 Características

- Descarga de audio de YouTube en buena calidad (192 kbps).
- Interfaz gráfica intuitiva y fácil de usar.
- Conversión automática usando **FFmpeg**.
- Almacenamiento en una carpeta local.

---

## ⚙️ Requisitos

- Python 3.8 o superior.
- Las siguientes bibliotecas de Python:
  - `yt-dlp`
  - `flet`
  - `imageio_ffmpeg` (incluye una versión integrada de FFmpeg).

---

## 🛠️ Instalación

1. **Clona este repositorio**:
    ```bash
    git clone https://github.com/Alvaro17mz/ytdl-mp3.git
    cd ytdl-mp3
    ```

2. **Instala las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

3. ¡Listo! No necesitas instalar FFmpeg por separado, ya que la librería `imageio_ffmpeg` lo incluye automáticamente.

---

## 🖥️ Uso

1. Ejecuta la aplicación:
    ```bash
    python app.py
    ```

2. Ingresa un enlace válido de YouTube en el campo de texto.

3. Haz clic en **"Descargar"** y espera a que se procese la descarga.

4. El archivo MP3 descargado estará disponible en la carpeta `./descargas`.

---

## ⚠️ Advertencia

Este proyecto es de uso personal y no está afiliado ni respaldado por YouTube, ni ninguna otra plataforma mencionada. Asegúrate de cumplir con los términos de servicio de YouTube y otros servicios utilizados.

