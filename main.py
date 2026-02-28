import pygame 

WINDOW_SIZE = [800, 600 ]
MAX_FPS = 60

window = pygame.Window('Tower Defence', WINDOW_SIZE)
surface = window.get_surface()
clock = pygame.Clock()

running = True 
while running :
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False

    surface.fill('black')

    clock.tick()
    print(clock.get_fps)
