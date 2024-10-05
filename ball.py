import pygame
class Ball:
    def __init__(self, x, y, radius, color, screenWidth, screenHeight) -> None:
        self.pos, self.radius = (x,y), radius
        self.color, self.screenWidth, self.screenHeight = color, screenWidth, screenHeight
        self.xVelocity, self.yVelocity = 5, -10
    def display(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
    def move(self):
        self.pos = (pygame.math.clamp(self.pos[0] + self.xVelocity, 0+self.radius, self.screenWidth - self.radius), pygame.math.clamp(self.pos[1] + self.yVelocity, 0+self.radius, self.screenHeight - self.radius)) 
    def collision(self, paddle):
        #collision with walls
        if self.pos[0] <= 0+self.radius:
            self.xVelocity = -self.xVelocity
        elif self.pos[0] >= self.screenWidth-self.radius:
            self.xVelocity = -self.xVelocity
        if self.pos[1] <= 0+self.radius:
            self.yVelocity = -self.yVelocity
        elif self.pos[1] >= self.screenHeight-self.radius:
            self.yVelocity = -self.yVelocity
        #collision with paddle
        if pygame.Rect.colliderect(pygame.Rect(self.pos[0], self.pos[1], self.radius, self.radius), paddle.getRect()):
            self.yVelocity = -self.yVelocity
    