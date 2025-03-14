import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
is_blue = True
done = False
x= 180
y= 120

clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type== pygame.KEYDOWN and event.key== pygame.K_SPACE:
            is_blue= not is_blue
        if event.type== pygame.QUIT:
            done =True
        
        pressed= pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y-=20
        if pressed[pygame.K_DOWN]: y+= 20
        if pressed[pygame.K_LEFT]: x-=20
        if pressed[pygame.K_RIGHT]: x+=20
        screen.fill((0,0,0))
        if is_blue: color = (0, 128, 255)
        else: color = (255,100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y,60, 60))
        pygame.display.flip()
        clock.tick(60)