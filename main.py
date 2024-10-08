import pygame
from button import Button
from paddle import Paddle
from ball import Ball
from brick import Brick
pygame.init()
#Initialize Shit
screenHeight, screenWidth = 1000, 800
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
state = "Start"
ballSpeed = 10
#Colors!
WHITE, BLACK, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, PURPLE, BROWN = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (128, 128, 128), (255, 165, 0), (128, 0, 128), (165, 42, 42)
#Calculate scale difference based on distance from default size (1000, 800)
xScale, yScale = screenWidth/800, screenHeight/1000

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
#Generate bricks
def generateBricks(difficulty):
    global xScale, yScale
    bricks = []
    color = RED
    borderCol = WHITE
    if difficulty == "Easy": numBricks = 32
    elif difficulty == "Medium": numBricks = 48
    elif difficulty == "Hard": numBricks = 64
    #collumbs = 10 rows depend on numBricks
    for i in range(numBricks//8):
        for j in range(8):
            bricks.append(Brick((j*100*xScale)+(2*xScale), (i*50*yScale)+(5*yScale*i), 92*xScale, 50*yScale, color, borderCol))
    return bricks



#Start screen loop __________________________________
def startScreen():
    global state
    #Make the scaled fonts
    titleFont = get_scaled_font(100)
    buttonFont = get_scaled_font(90)
    #init buttons
    easyButton = Button("Easy", buttonFont, (screenWidth//2, 3*screenHeight//7), WHITE, BLACK)
    mediumButton = Button("Medium", buttonFont, (screenWidth//2, 4*screenHeight//7), WHITE, BLACK)
    hardButton = Button("Hard", buttonFont, (screenWidth//2, 5*screenHeight//7), WHITE, BLACK)
    settingsButton = Button("Settings", buttonFont, (screenWidth//2, 6*screenHeight//7), WHITE, BLACK)
    while state == "Start":
        #Fill screen w color
        screen.fill(WHITE)
        #Draw text and buttons
        draw_text("Brick Breaker!", titleFont, screenWidth//2, screenHeight//5, BLACK)
        easyButton.draw(screen)
        mediumButton.draw(screen)
        hardButton.draw(screen)
        settingsButton.draw(screen)
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
                if settingsButton.isClicked(event):
                    state = "Settings"
                    settings()
        #Update Screen
        clock.tick(60)
        pygame.display.flip()

#Settings Screen loop______________________
def settings():
    global state, ballSpeed
    buttonFont = get_scaled_font(75)
    decSpeed = Button("<", buttonFont, (200*xScale, 400*yScale), WHITE, BLACK)
    incSpeed = Button(">", buttonFont, (600*xScale, 400*yScale), WHITE, BLACK)
    apply = Button("Apply", buttonFont, (400*xScale, 600*yScale), WHITE, BLACK)
    while state == "Settings":
        screen.fill(WHITE)
        decSpeed.draw(screen)
        incSpeed.draw(screen)
        apply.draw(screen)
        draw_text("Ball Speed: {}".format(ballSpeed), buttonFont, 400*xScale, 400*yScale, BLACK, True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = "Quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if apply.isClicked(event): 
                    state = "Start"
                    startScreen()
                if incSpeed.isClicked(event):
                    ballSpeed += 1
                if decSpeed.isClicked(event):
                    ballSpeed-=1                
        pygame.display.flip()
#Main Game Loop________________________________________________
def gameLoop(difficulty):
    global state, xScale, yScale, ballSpeed
    #Generate Original ball and paddle 
    offsetFromBottom = 100*yScale #Offset of paddle from bottom of screen (Like everything else this will be scaled)
    paddleWidth, paddleHeight = 100 * xScale, 25*xScale 
    paddle = Paddle((screenWidth/2)-(paddleWidth/2),screenHeight-offsetFromBottom, paddleWidth, paddleHeight, WHITE, ballSpeed*xScale, screenWidth ) #x, y, width, height, color, speed, screenWidth
    ballRad = 15* (xScale+yScale)/2
    ball = Ball((screenWidth/2)-(paddleWidth/2),screenHeight-(offsetFromBottom*2), ballRad, BLUE, xScale, yScale, ballSpeed)
    bricks = generateBricks(difficulty)
    #Set lives value
    if difficulty == "Easy": lives = 5
    elif difficulty == "Medium": lives = 4
    elif difficulty == "Hard": lives = 3
    #initialize lives font
    livesFont = get_scaled_font(25)
    while state == "Main":
        screen.fill(BLACK)
        #Paddle movement and display
        paddle.move()
        paddle.display(screen)
        #Ball movement and display
        ball.exists = ball.checkOutOfBounds()
        #Ball function called based on its existance
        if ball.exists:
            ball.collision(paddle)
            ball.move()
            ball.display(screen)
        else:
            lives-=1
            ball = Ball((screenWidth/2)-(paddleWidth/2),screenHeight-(offsetFromBottom*2), ballRad, BLUE, xScale, yScale, ballSpeed)
        #disp lives:
        draw_text("Lives: {}".format(lives), livesFont, 100*xScale, 950*yScale, WHITE)
        #Check if they are ded:
        if lives == 0: state = "Lost"
        #Check if they won
        if all(brick.exists == False for brick in bricks): state = "Win"
        #Loop through all bricks
        for brick in bricks:
            if brick.exists:
                brick.display(screen)
                if brick.collision(ball): 
                    ball.bounce()
                    brick.exists = False
        #Events checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             state = "Quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                for brick in bricks: brick.exists = False

        clock.tick(100)
        pygame.display.flip()
startScreen()
