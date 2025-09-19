import pygame

# Inicializa o pygame
pygame.init()

# Inicializa o mixer
pygame.mixer.init()

# Carrega a música
pygame.mixer.music.load('audio-do-fdp.mp3')

# Reproduz a música
pygame.mixer.music.play()

# Mantém o programa rodando enquanto a música toca
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)