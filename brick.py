import pygame
class Brick:
    def __init__(self, x, y, width, height, color, borderColor, exists=True) -> None:
        self.rect = pygame.Rect(x,y,width,height)
        self.color,self.borderColor = color, borderColor
        self.exists = exists
    def display(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        #print(self.rect)
        pygame.draw.rect(screen, self.borderColor, self.rect, 100//self.rect.width)
    def collision(self, ball):
        if pygame.Rect.colliderect(self.rect,pygame.Rect(ball.pos[0], ball.pos[1], ball.radius, ball.radius)):
            return True