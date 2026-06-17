import pygame

print('Setup start')
pygame.init()
window = pygame.display.set_mode(size=(960, 540))
print('Setup end')

print('Loop start')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()