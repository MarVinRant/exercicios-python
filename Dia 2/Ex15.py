# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

import pygame

pygame.init() # Inicializa o pygame
pygame.mixer.music.load("Dia 2/01 - 5 Da Manhã_57674160.mp3") # Carrega o arquivo de áudio
pygame.mixer.music.play() # Reproduz o áudio

input("Pressione Enter para parar a música...") # Mantém o programa rodando até que o usuário pressione Enter