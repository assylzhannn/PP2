import pygame
import time
import math
pygame.init()

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
pygame.display.set_caption("Micky clock")

left=pygame.image.load("images/leftarm.png")
right=pygame.image.load("images/rightarm.png")
mainclock=pygame.image.load("images/clock.png")

done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done= True
    current_time= time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec

    m_angle= minute*6 + (second/60)*6
    s_angle= second*6

    screen.blit(mainclock,(-5,-5))

    rotated_rightarm = pygame.transform.rotate(pygame.transform.scale(right, (800, 800)), -m_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(800 // 2, 800 // 2 + 12))
    screen.blit(rotated_rightarm, rightarmrect)
    
    #сол қол секундты орналастыру
    rotated_leftarm = pygame.transform.rotate(pygame.transform.scale(left, (40.95, 682.5)), -s_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(800 // 2, 800 // 2 + 10))
    screen.blit(rotated_leftarm, leftarmrect)
    
    pygame.display.flip() #окноны жаңартады
    clock.tick(60) #fps
    
