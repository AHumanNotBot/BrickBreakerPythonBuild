import pygame
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