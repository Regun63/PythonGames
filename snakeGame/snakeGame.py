import pygame
import random

pygame.mixer.pre_init(44100,-16,2,312)
pygame.init()
pygame.mixer.init()
# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("SnakesWithHarry")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
apple=pygame.image.load("apple1.jpg").convert_alpha()


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        if [x,y]==snk_list[-1]:
           color=(190,120,70)
           pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])  
        else: 
           pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((150,40,190))
        text_screen("Welcome to Snakes", black, 260, 250)
        text_screen("Press Space Bar To Play", black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE :
                    pygame.mixer.music.load("start.mp3")
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)


# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    with open("HighScore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(20, 700)
    food_y = random.randint(20,500)
    score = 0
    init_velocity = 3
    snake_size = 30
    fps = 60
    
    while not exit_game:
        if game_over:
            with open("HighScore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill((210,90,84))
            text_screen("GAME OVER! Press Enter To Continue", (50,60,130), 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score +=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            

            gameWindow.fill((60,250,130))
            text_screen("Score: " + str(score) + "  Highscore: "+str(hiscore), (210,120,70), 5, 5)
            fruit_draw=pygame.Rect(food_x,food_y,snake_size,snake_size)
            # pygame.draw.ellipse(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            gameWindow.blit(apple,fruit_draw)
            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                pygame.mixer.music.load("pop.mp3")
                pygame.mixer.music.play()
                score +=10
                food_x = random.randint(20, 700)
                food_y = random.randint(20, 500)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score
            head = []
            head.append(snake_x)
            head.append(snake_y)
           
            snk_list.append(head)
            

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("itselfeat.mp3")
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load("fail.mp3")
                pygame.mixer.music.play()
            plot_snake(gameWindow, (60,70,170), snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()