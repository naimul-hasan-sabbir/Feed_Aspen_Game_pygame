import pygame

#pygame setup
pygame.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("Naimul's Pygame Tutorial")
clock = pygame.time.Clock()
running = True

dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    #poll for events
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #pick screen color
    screen.fill("silver")
    
    #render our game
    pygame.draw.circle(screen, '#033660', player_pos, 40)
    
    #move the circle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
        
    #use the mouse
    #if event.type == pygame.MOUSEMOTION:
    #    pos = pygame.mouse.get_pos()
        
    #    player_pos.x = pos[0]
    #    player_pos.y = pos[1]
     
    if pygame.mouse.get_pressed()[0]:
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            
            player_pos.x = pos[0]
            player_pos.y = pos[1]   
    
    #flip the display
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
    
    
    
pygame.quit()
