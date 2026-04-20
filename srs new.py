import pygame
import random
pygame.init()

fps=pygame.time.Clock()
timer=pygame.USEREVENT+1
pygame.time.set_timer(timer, 60000)

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("sss")
screen.fill((200,200,200))
font=pygame.font.SysFont("Times New Roman",30)

black_surf=pygame.Surface((40,40),pygame.SRCALPHA)
black_rect=black_surf.get_rect(center=(300,300))
green_surf=pygame.Surface((20,20),pygame.SRCALPHA)
red_surf=pygame.Surface((20,20),pygame.SRCALPHA)
score=0
red=[]
green=[]
for i in range(6):
    green_rect = green_surf.get_rect(topleft=(random.randint(0, 580), random.randint(0, 580)))
    green.append(green_rect)
for i in range(3):
    red_rect = red_surf.get_rect(topleft=(random.randint(0, 580), random.randint(0, 580)))
    red.append(red_rect)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==timer:
            for i in red:
                i.x,i.y=random.randint(0,580),random.randint(0,580)
                screen.blit(red_surf,i)
    for i in green:
        if i.colliderect(black_rect):
            score+=1
            i.x,i.y=random.randint(0,580),random.randint(0,580)
    for i in red:
        if i.colliderect(black_rect):
            running=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        black_rect.x-=5
    elif keys[pygame.K_RIGHT]:
        black_rect.x+=5
    elif keys[pygame.K_UP]:
        black_rect.y-=5
    elif keys[pygame.K_DOWN]:
        black_rect.y+=5

    if black_rect.x<=0:
        black_rect.x=0
    elif black_rect.x>=560:
        black_rect.x=560
    elif black_rect.y<=0:
        black_rect.y=0
    elif black_rect.y>=560:
        black_rect.y=560

    screen.fill((200, 200, 200))
    text=font.render(f"Score:{score}",True,(255,255,255),2)
    screen.blit(text,(490,10))
    pygame.draw.circle(black_surf,(0,0,0),(20,20),20)
    pygame.draw.circle(green_surf,(0,255,0),(10,10),10)
    pygame.draw.circle(red_surf,(255,0,0),(10,10),10)
    screen.blit(black_surf,black_rect)
    for r in red:
        screen.blit(red_surf,r)
    for g in green:
        screen.blit(green_surf,g)
    pygame.display.update()
    fps.tick(60)
pygame.quit()
