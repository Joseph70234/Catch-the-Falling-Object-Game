# import necessary packages
import pygame
import random

 # initialize pygame
pygame.init()

# set display dimensions and title
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Catch the Object')

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# set game clock
clock = pygame.time.Clock() # this controls the FPS

# player settings
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2 # positions in center of screen; the player_width // 2 part ensures that we are not centering based on the top-left corner of the player
player_y = HEIGHT - player_height - 10 # positions near bottom of screen
player_speed = 8 # player movement speed

# falling object settings
object_width = 20
object_height = 20
object_x = random.randint(0, WIDTH-object_width) # random x position
object_y = 0 # top of the screen
object_speed = 5 # falling speed of object

# score settings
score = 0
font = pygame.font.Font(None, 36) # first argument is for specific font file (none is for default font); second is for font size

# set game loop
running = True
while running == True:
 
    # loop through all events in game
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if user clicks the x on the window
            running = False

    # keyboard controls for movement
    keys = pygame.key.get_pressed() # get current state of all keys
    if keys[pygame.K_a] and player_x > 0: # move left
        player_x -= player_speed
    if keys[pygame.K_d] and player_x < WIDTH - player_width: #move right
        player_x += player_speed

    # update position of falling object
    object_y += object_speed

    # reset object when it falls off screen
    if object_y > HEIGHT:
        object_y = 0
        object_x = random.randint(0, WIDTH-object_width)
    
    # collision detection
    if (player_x < object_x + object_width and
        player_x + player_width > object_x and
        player_y < object_y + object_height and
        player_y + player_height > object_y):
        # increment score
        score += 1
        # reset object
        object_y = 0
        object_x = random.randint(0, WIDTH-object_width)
    
    # screen background color
    screen.fill(WHITE)

    # draw player
    pygame.draw.rect(screen, BLACK, [player_x, player_y, player_width, player_height])
        # screen = chooses our screen as the destination to draw the player on
        # BLACK = color of object
        # final tuple = position (x and y) and shape (width and height) of player

    # draw falling object
    pygame.draw.rect(screen, RED, [object_x, object_y, object_width, object_height])

    # display score
    score_text = font.render(f'Score: {score}', True, BLACK) # sets score text
        # first argument is score text
        # second is option for antialiasing (smoothing out jagged text edges)
        # third is color
    screen.blit(score_text, (10,10)) # places score over screen
        # first argument is text
        # second is where to place text

    # update display
    pygame.display.flip() # flips visible screen with buffer screen

    # control frame rate
    clock.tick(60) # 60 fps

# quit game when game loop ends
pygame.quit()