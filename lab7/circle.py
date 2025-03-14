import pygame
pygame.init()
screen= pygame.display.set_mode((400,400))
pygame.display.set_caption("Pink circle")
done= False
x, y = 180, 150
while not done:
    screen.fill((0,0,0))
    color = (237,12, 128)
    pygame.draw.circle(screen, color, (x,y), 25 )
    for event in pygame.event.get():
        if event.type== pygame.KEYDOWN and event.key== pygame.K_SPACE:
            is_blue= not is_blue
        if event.type== pygame.QUIT:
            done =True

        pressed= pygame.key.get_pressed()
        if x> 370 : x-=50
        if x<30 : x+=50
        if y<30: y+=50
        if y> 370 : y-=50
        if pressed[pygame.K_UP]: y-=20
        if pressed[pygame.K_DOWN]: y+= 20
        if pressed[pygame.K_LEFT]: x-=20
        if pressed[pygame.K_RIGHT]: x+=20

        pygame.display.flip()
        #clock.tick(60)