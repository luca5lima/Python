# Faça um programa que abra e execute um áudio de um arquivo MP3.

import pygame
import time
# Inicializar o mixer e o pygame
pygame.init()

# Carregar o arquivo de áudio
arquivo_mp3 = 'C:/Users/lucas/OneDrive/Documentos/MeusProjetos/Python/Estudos/CursoEmVideo/Mundo01/Exercicios/musica.mp3'
pygame.mixer.music.load(arquivo_mp3)

# Tocar o áudio
pygame.mixer.music.play()

# Aguardar até que a música termine
while pygame.mixer.music.get_busy():
    time.sleep(1)
