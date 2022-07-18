import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')    # Coloque o arquivo e nome dele;
pygame.mixer.music.play()
pygame.event.wait()
