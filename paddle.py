import pygame
class Paddle:
    def __init__(self, x, y, width, height, color, speed, screenWidth) -> None:
        self.rect = pygame.Rect(x,y,width, height)
        self.color = color
        self.speed, self.screenWidth = speed, screenWidth
    def move(self, key):
        if key == pygame.K_a or key == pygame.K_LEFT:
            if self.rect.left > (0+self.speed): self.rect.x -= self.speed
        if key == pygame.K_d or key == pygame.K_RIGHT:
            if self.rect.left < (self.screenWidth+self.speed): self.rect.x += self.speed
    def display(self, screen):
        screen.blit(self.rect)
