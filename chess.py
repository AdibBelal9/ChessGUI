import pygame

#Setting up display screen, font, and timer
pygame.init()
width = 1000
length = 1000
screen = pygame.display.set_mode([width, length])
pygame.display.set_caption('Two Player Chess')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 36)
timer = pygame.time.Clock()
rate = 60

#Setting up chess pieces
active = True
while active:
    timer.tick(rate)
    screen.fill('black')

    #event handling
    for event in pygame.event.get():
        if event.type == pygame.quit:
            active = False

    pygame.display.flip()
pygame.quit()
