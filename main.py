import pygame
from button import Button
from paddle import Paddle
from ball import Ball
pygame.init()
#Initialize Shit
screenHeight, screenWidth = 1000, 800
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
state = "Start"
#Colors!
WHITE, BLACK, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, PURPLE, BROWN = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (128, 128, 128), (255, 165, 0), (128, 0, 128), (165, 42, 42)
#Calculate scale difference based on distance from default size (1000, 800)
xScale, yScale = screenWidth/1000, screenHeight/800


# Calculate font size dynamically based on screen height (GPT code)
def get_scaled_font(scale_factor=10):
    global yScale,xScale
    font_size = int(scale_factor * ((yScale+xScale)/2))
    return pygame.font.SysFont(None, font_size)
#Display text to screen 
def draw_text(text: str, font: pygame.font.Font, x: int, y: int, color: tuple, rectColor = WHITE, rect = False) :
    textObj = font.render(text, True, color)
    rectCoords = textObj.get_rect(center=(x,y))
    if rect:
        rectObj = pygame.draw.rect(screen, rectColor, rectCoords, rectCoords.width)
    screen.blit(textObj, rectCoords)
#Button class


#Start screen loop __________________________________
def startScreen():
    global state
    #Make the scaled fonts
    titleFont = get_scaled_font(100)
    buttonFont = get_scaled_font(90)
    #init buttons
    easyButton = Button("Easy", buttonFont, (screenWidth//2, 3*screenHeight//6), WHITE, BLACK)
    mediumButton = Button("Medium", buttonFont, (screenWidth//2, 4*screenHeight//6), WHITE, BLACK)
    hardButton = Button("Hard", buttonFont, (screenWidth//2, 5*screenHeight//6), WHITE, BLACK)

    while state == "Start":
        #Fill screen w color
        screen.fill(WHITE)
        #Draw text and buttons
        draw_text("Brick Breaker!", titleFont, screenWidth//2, screenHeight//5, BLACK)
        easyButton.draw(screen)
        mediumButton.draw(screen)
        hardButton.draw(screen)
        #Events checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = "Quit"
            #If click on a button, change the difficulty, state and then call the main game loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easyButton.isClicked(event): 
                    difficulty, state = "Easy", "Main"
                    gameLoop(difficulty)
                if mediumButton.isClicked(event): 
                    difficulty, state = "Medium", "Main"
                    gameLoop(difficulty)
                if hardButton.isClicked(event): 
                    difficulty, state = "Hard", "Main"
                    gameLoop(difficulty)
        #Update Screen
        clock.tick(60)
        pygame.display.flip()



#Main Game Loop________________________________________________
def gameLoop(difficulty):
    global state, xScale, yScale
    offsetFromBottom = 100*yScale #Offset of paddle from bottom of screen (Like everything else this will be scaled)
    paddleWidth, paddleHeight = 100 * xScale, 25*xScale 
    paddle = Paddle((screenWidth/2)-(paddleWidth/2),screenHeight-offsetFromBottom, paddleWidth, paddleHeight, WHITE, 10*xScale, screenWidth ) #x, y, width, height, color, speed, screenWidth
    ballRad = 15* (xScale+yScale)/2
    ball = Ball((screenWidth/2)-(paddleWidth/2),screenHeight-(offsetFromBottom*2), ballRad, BLUE, screenWidth, screenHeight)
    while state == "Main":
        screen.fill(BLACK)
        #Paddle movement and display
        paddle.move()
        paddle.display(screen)
        #Ball movement and display
        ball.collision(paddle)
        ball.move()
        ball.display(screen)
        #Events checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = "Quit"

        clock.tick(100)
        pygame.display.flip()
startScreen()