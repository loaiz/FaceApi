# -*- coding: utf-8 -*-
"""
@author: 

██╗░░░██╗███████╗███████╗███████╗██████╗░░██████╗░█████╗░███╗░░██╗  ██╗░░░░░░█████╗░░█████╗░██╗███████╗░█████╗░
╚██╗░██╔╝██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗████╗░██║  ██║░░░░░██╔══██╗██╔══██╗██║╚════██║██╔══██╗
░╚████╔╝░█████╗░░█████╗░░█████╗░░██████╔╝╚█████╗░██║░░██║██╔██╗██║  ██║░░░░░██║░░██║███████║██║░░███╔═╝███████║
░░╚██╔╝░░██╔══╝░░██╔══╝░░██╔══╝░░██╔══██╗░╚═══██╗██║░░██║██║╚████║  ██║░░░░░██║░░██║██╔══██║██║██╔══╝░░██╔══██║
░░░██║░░░███████╗██║░░░░░███████╗██║░░██║██████╔╝╚█████╔╝██║░╚███║  ███████╗╚█████╔╝██║░░██║██║███████╗██║░░██║
░░░╚═╝░░░╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚══╝  ╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝╚══════╝╚═╝░░╚═╝
"""

from facenet_pytorch import InceptionResnetV1, MTCNN
from pytube import YouTube
from yt_dlp import YoutubeDL
import pytube
from matplotlib import pyplot as plt
from PIL import Image
import seaborn as sns
import pandas as pd
import numpy as np
import pickle
import h5py
import cv2
import os
import re
# from pytube import YouTube
import tempfile
import os 
    
def descargar_youtube_mp3_temporal(url):
    try:
        # Crear un objeto YouTube
        yt = YouTube(url)

        # Elegir la mejor calidad de audio disponible en formato MP4
        audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()

        # Descargar el audio en formato MP4 y guardar en un archivo temporal
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            audio_stream.download(output_path=temp_file.name)
            mp3_filename = temp_file.name
            
        return mp3_filename  # Devolver el nombre del archivo MP3 temporal

    except Exception as e:
        print(f"Error al descargar el audio: {str(e)}")
        return None

def mp4(link,base):
    
    youlink = pytube.YouTube(link)
    # audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()

    # titulo = 'aoachurrao'
    titulo = youlink.title
    formato= '.mp3'
    titulo1 = titulo +formato
    ruta_descarga = base + '/uploads'
    print('titulo',youlink.title)
    print('Autor',youlink.author)
    audio_stream = youlink.streams.filter(abr='160kbps',progressive=False).first().download(output_path=ruta_descarga,filename= 'ola.mp3')
    print('descarga con exito de :',link)
    return link

def mp33(link, base):
    
    ruta_descarga = base + '/uploads'
    
    ydl_opts = {
    'format': 'bestaudio/best',
    'noplaylist': True,
    #'outtmpl': f'{ruta_descarga}/%(title)s.%(ext)s'
    'outtmpl': f'{ruta_descarga}/%(title)s.mp3'# Ruta con el nombre de la canción
    }

# Crea una instancia de YoutubeDL con las opciones
    with YoutubeDL(ydl_opts) as ydl:
        # Descarga el video
        ydl.download([link])
        
        # Obtiene la información del video
        info_dict = ydl.extract_info(link, download=False)
        
        # Obtiene el nombre del video (título de la canción)
        video_title = info_dict.get('title', 'Desconocido')
    titulo1 = f'fer{video_title}.mp3'
    titulo1 = f'{video_title}.mp3'
    print(f"El nombre del video descargado (nombre de la canción) es: {video_title}")
    return ruta_descarga,titulo1

def mp3(link,base):
    youlink = pytube.YouTube(link)
    # titulo = 'aoachurrao'
    titulo = youlink.title
    titulo.replace(' ','_')
    
    formato= '.mp3'
    titulo1 = f'fer{titulo}.mp3'
    print(titulo)
    ruta_descarga = base + '/uploads'
    print('titulo',youlink.title)
    print('Autor',youlink.author)
    # stream = video.streams.filter(only_audio=True).order_by('abr').desc().first()
        
    youlink.streams.filter(abr='160kbps',progressive=False).first().download(output_path=ruta_descarga,filename= f'fer{titulo}.mp3')
    # youlink.streams.filter(only_audio=True).order_by('abr').desc().first().download(output_path=ruta_descarga,filename= f'fer{titulo}.mp3')
    print('descarga con exito de :',link)
    return ruta_descarga,titulo1
    
