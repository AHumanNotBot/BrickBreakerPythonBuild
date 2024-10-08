import pygame
class Ball:
    def __init__(self, x, y, radius, color, screenScaleX, screenScaleY, exists = True) -> None:
        self.pos, self.radius = (x,y), radius
        self.color, self.screenWidth, self.screenHeight = color, screenScaleX*800, screenScaleY*1000
        self.xVelocity, self.yVelocity = 5*screenScaleX, -10*screenScaleY
        self.exists = exists
    def display(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
    def move(self):
        self.pos = (pygame.math.clamp(self.pos[0] + self.xVelocity, 0+self.radius, self.screenWidth - self.radius), self.pos[1] + self.yVelocity)
    def collision(self, paddle):
        #collision with walls
        if self.pos[0] <= 0+self.radius:
            self.xVelocity = -self.xVelocity
        elif self.pos[0] >= self.screenWidth-self.radius:
            self.xVelocity = -self.xVelocity
        if self.pos[1] <= 0+self.radius:
            self.yVelocity = -self.yVelocity
        #collision with paddle
        if pygame.Rect.colliderect(pygame.Rect(self.pos[0], self.pos[1], self.radius, self.radius), paddle.getRect()):
            self.yVelocity = -self.yVelocity
    def bounce(self):
        self.yVelocity = -self.yVelocity
    def checkOutOfBounds(self):
        #Since exists is assigned to the output if it is out of bounds we want exists to be false
        if self.pos[1] >= self.screenHeight:
            return False
        return True 
        