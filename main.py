import pygame
pygame.init()
#Initialize Shit
screenHeight, screenLength = 800, 600
screen = pygame.display.set_mode((screenLength, screenHeight))
clock = pygame.time.Clock()
state = "Start"
difficulty = ""
#Colors!
WHITE, BLACK, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, PURPLE, BROWN = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (128, 128, 128), (255, 165, 0), (128, 0, 128), (165, 42, 42)



# Calculate font size dynamically based on screen height (GPT code)
def get_scaled_font(scale_factor=10):
    font_size = screenHeight // scale_factor  # Scale factor controls the size
    return pygame.font.SysFont(None, font_size)
#Display text to screen 
def draw_text(text: str, font: pygame.font.Font, x: int, y: int, color: tuple, rectColor = WHITE, rect = False) :
    textObj = font.render(text, True, color)
    rectCoords = textObj.get_rect(center=(x,y))
    if rect:
        rectObj = pygame.draw.rect(screen, rectColor, rectCoords, rectCoords.width)
    screen.blit(textObj, rectCoords)
#Button class
class Button:
    def __init__(self, text, font, pos, color, buttonColor) -> None:
        self.text = text
        self.font = font
        self.pos = pos
        self.color = color
        self.buttonColor = buttonColor
        self.textObj = font.render(text, True, color)
        self.rect = self.textObj.get_rect(center=pos)
    def draw(self, screen):
        pygame.draw.rect(screen, self.buttonColor, self.rect, self.rect.width)
        screen.blit(self.textObj, self.rect)
    def isClicked(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False



def startScreen():
    global state, difficulty
    #Make the scaled fonts
    titleFont = get_scaled_font(8)
    buttonFont = get_scaled_font(15)
    #init buttons
    easyButton = Button("Easy", buttonFont, (screenLength//2, 3*screenHeight//6), WHITE, BLACK)
    mediumButton = Button("Medium", buttonFont, (screenLength//2, 4*screenHeight//6), WHITE, BLACK)
    hardButton = Button("Hard", buttonFont, (screenLength//2, 5*screenHeight//6), WHITE, BLACK)

    while state == "Start":
        #Fill screen w color
        screen.fill(WHITE)
        #Draw text and buttons
        draw_text("Brick Breaker!", titleFont, screenLength//2, screenHeight//5, BLACK)
        easyButton.draw(screen)
        mediumButton.draw(screen)
        hardButton.draw(screen)
        #Events checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = "Quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easyButton.isClicked(event): difficulty, state = "Easy", "Main"
                if mediumButton.isClicked(event): difficulty, state = "Medium", "Main"
                if hardButton.isClicked(event): difficulty, state = "Hard", "Main"
        #Update Screen
        clock.tick(60)
        pygame.display.flip()
startScreen()

