'''
Python Exercise 021:
Write a Python program that opens and plays the audio of an MP3 file.
'''

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()