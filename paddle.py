import pygame
class Paddle:
    def __init__(self, x, y, width, height, color, speed, screenWidth) -> None:
        self.rect = pygame.Rect(x,y,width, height)
        self.color = color
        self.speed, self.screenWidth = speed, screenWidth
    def move(self):
        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_a] or keysPressed[pygame.K_LEFT]:
            if self.rect.left > (0+self.speed): self.rect.x -= self.speed
        if keysPressed[pygame.K_b] or keysPressed[pygame.K_RIGHT]:
            if self.rect.left+self.rect.width < (self.screenWidth-self.speed): self.rect.x += self.speed
    def display(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
