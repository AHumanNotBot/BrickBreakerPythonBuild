import pygame
class Brick:
    def __init__(self, x, y, width, height, color, borderColor, containsPowerup=False, exists=True) -> None:
        self.rect = pygame.Rect(x,y,width,height)
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery
        self.circle= pygame.Rect(self.centerx-height/4,self.centery-height/4,height/2,height/2)
        self.plus1 = pygame.Rect(self.centerx-height/20, self.centery-height/8, height/10, height/4)
        self.plus2 = pygame.Rect(self.centerx-height/8, self.centery-height/20, height / 4, height / 10)
        self.color,self.borderColor = color, borderColor
        self.containsPowerup = containsPowerup
        self.exists = exists
    def display(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.containsPowerup:
            pygame.draw.ellipse(screen, self.borderColor, self.circle)
            pygame.draw.rect(screen, (0,255,0), self.plus1)
            pygame.draw.rect(screen, (0,255,0), self.plus2)
        #print(self.rect)
        pygame.draw.rect(screen, self.borderColor, self.rect, 100//self.rect.width)
    def collision(self, ball):
        if pygame.Rect.colliderect(self.rect,pygame.Rect(ball.pos[0], ball.pos[1], ball.radius, ball.radius)):
            return True