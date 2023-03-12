#galaga tractor beam code

import pygame #bring in pygame library
pygame.init #initialize pygame
pi = 3.1415
screen = pygame.display.set_mode((800, 800)) #create game screen
pygame.display.set_caption("galaga beam") #window title

#load alien ship image
alienShip = pygame.image.load("boss.jpg")

#draw alien ship
screen.blit(alienShip, (210, 180))
pygame.display.flip()

#top arc
pygame.draw.arc(screen, (5, 100, 200), (200, 200, 100, 100),  pi, 2*pi, 10)
pygame.display.flip() #update screen 
pygame.time.wait(2000)

#second arc
pygame.draw.arc(screen, (50, 200, 100), (190, 230, 120, 100),  pi, 2*pi, 10)
pygame.display.flip() #update screen 
pygame.time.wait(2000)

#add more here!

#last arc
pygame.draw.arc(screen, (5, 100, 200), (115, 400, 300, 100),  pi, 2*pi, 10)
pygame.display.flip() #update screen 
pygame.time.wait(2000)