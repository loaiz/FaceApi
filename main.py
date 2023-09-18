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


from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException, status,Form
from facenet_pytorch import InceptionResnetV1, MTCNN
import torchvision.transforms as transforms
from sagemaker import get_execution_role
from datetime import datetime, timedelta
from passlib.context import CryptContext
from matplotlib import pyplot as plt
from fastapi import UploadFile, File
from jose import JWTError, jwt
from pydantic import BaseModel
from Modelo import candas
from PIL import Image
import seaborn as sns
import pandas as pd
import numpy as np
import pickle
import boto3
import h5py
import cv2
import os
import tempfile
from io import BytesIO
# import base64 
import base64 
from io import BytesIO
from PIL import Image
import cv2
import numpy as np
import os
import tempfile
from fastapi import FastAPI
from fastapi.responses import FileResponse
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi.middleware.cors import CORSMiddleware


scheduler = BackgroundScheduler()

base_dir = os.path.dirname(os.path.abspath(__file__))

# upload_dir = os.path.join(os.path.dirname(__file__), "uploads")
upload_dir = tempfile.mkdtemp(prefix="uploads")

Model = os.path.join(os.path.dirname(__file__), "Modelo")

edit_dir = os.path.join(os.path.dirname(__file__),)

# def accion_a_ejecutar():
#     # Coloca aquí la acción que deseas ejecutar cada 2 minutos
#     print("Acción ejecutada cada 2 minutos")

def borrar_archivos_en_directorio():
    directorio = base_dir + '/uploads' 
    try:
        # Verificar si el directorio existe
        if not os.path.exists(directorio):
            print(f"El directorio '{directorio}' no existe.")
            return

        # Listar los archivos en el directorio
        archivos = os.listdir(directorio)

        # Eliminar todos los archivos en el directorio
        for archivo in archivos:
            archivo_ruta = os.path.join(directorio, archivo)
            if os.path.isfile(archivo_ruta):
                os.remove(archivo_ruta)
                print(f"Archivo eliminado: {archivo_ruta}")

        print(f"Se han eliminado todos los archivos en el directorio '{directorio}'.")

    except Exception as e:
        print(f"Ocurrió un error al eliminar archivos en el directorio '{directorio}': {str(e)}")

# Programar la función para que se ejecute cada 2 minutos
scheduler.add_job(borrar_archivos_en_directorio, "interval", minutes=2)

# Iniciar el scheduler
scheduler.start()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes reemplazar "*" con la lista de orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Puedes reemplazar "*" con los métodos permitidos (GET, POST, etc.)
    allow_headers=["*"],  # Puedes reemplazar "*" con los encabezados permitidos
)

# @app.post("/mp3")
# # async def upload_image_gray(file: UploadFile = File(...)):
# async def mp3(Link: str= Form(...)):
#     ruta_mp3,nombre_archivo = candas.mp3(Link,base_dir)
    
#     ruta_mp3 = ruta_mp3+'/'+nombre_archivo
#         # Ruta al archivo MP3 que deseas devolver
#     # ruta_mp3 = "ruta/al/archivo.mp3"  # Reemplaza con la ruta de tu archivo MP3

#     # # Definir el nombre del archivo (puedes personalizarlo)
#     # nombre_archivo = "mi_audio.mp3"

#     # Devolver el archivo MP3 como una respuesta de descarga
#     return FileResponse(
#         ruta_mp3,
#         headers={
#             "Content-Disposition": f"attachment; filename={nombre_archivo}",
#             "Content-Type": "audio/mpeg",  # Tipo de contenido para MP3
#         }
#     )

@app.post("/mp3")
# async def upload_image_gray(file: UploadFile = File(...)):
async def mp3(Link: str= Form(...)):
    ruta_mp3,nombre_archivo = candas.mp33(Link,base_dir)
    
    ruta_mp3 = ruta_mp3+'/'+nombre_archivo
        # Ruta al archivo MP3 que deseas devolver
    # ruta_mp3 = "ruta/al/archivo.mp3"  # Reemplaza con la ruta de tu archivo MP3

    # # Definir el nombre del archivo (puedes personalizarlo)
    # nombre_archivo = "mi_audio.mp3"

    # Devolver el archivo MP3 como una respuesta de descarga
    return FileResponse(
        ruta_mp3,
        headers={
            "Content-Disposition": f"attachment; filename={nombre_archivo}",
            "Content-Type": "audio/mpeg",
            # Tipo de contenido para MP3
        }
        
    )
    
@app.post("/mp3/nombre")
# async def upload_image_gray(file: UploadFile = File(...)):
async def mp3(Link: str= Form(...)):
    ruta_mp3,nombre_archivo = candas.mp33(Link,base_dir)
    
    ruta_mp3 = ruta_mp3+'/'+nombre_archivo
        # Ruta al archivo MP3 que deseas devolver
    # ruta_mp3 = "ruta/al/archivo.mp3"  # Reemplaza con la ruta de tu archivo MP3

    # # Definir el nombre del archivo (puedes personalizarlo)
    # nombre_archivo = "mi_audio.mp3"

    # Devolver el archivo MP3 como una respuesta de descarga
    return nombre_archivo

@app.post("/mp4")
# async def upload_image_gray(file: UploadFile = File(...)):
async def mp4(Link: str= Form(...)):

    return Link


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8081)
