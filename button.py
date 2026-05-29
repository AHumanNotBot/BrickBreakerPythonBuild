from functools import lru_cache
from io import BytesIO

import matplotlib
import pygame

matplotlib.use("Agg")
import matplotlib.pyplot as plt


@lru_cache(maxsize=128)
def render_latex(text, color, font_size):
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.patch.set_alpha(0)

    rendered_text = fig.text(
        0,
        0,
        text,
        color=tuple(channel / 255 for channel in color),
        fontsize=font_size,
    )
    fig.canvas.draw()

    bounds = rendered_text.get_window_extent()
    width = max(int(bounds.width) + 12, 1)
    height = max(int(bounds.height) + 12, 1)
    fig.set_size_inches(width / fig.dpi, height / fig.dpi)
    rendered_text.set_position((6 / width, 6 / height))
    fig.canvas.draw()

    image_data = BytesIO()
    fig.savefig(
        image_data,
        format="png",
        transparent=True,
        dpi=fig.dpi,
        bbox_inches="tight",
        pad_inches=0.08,
    )
    plt.close(fig)

    image_data.seek(0)
    surface = pygame.image.load(image_data, "latex.png").convert_alpha()
    bounds = surface.get_bounding_rect()
    if bounds.width == 0 or bounds.height == 0:
        return surface

    padding = 6
    cropped = surface.subsurface(bounds).copy()
    padded = pygame.Surface(
        (cropped.get_width() + (2 * padding), cropped.get_height() + (2 * padding)),
        pygame.SRCALPHA,
    )
    padded.blit(cropped, (padding, padding))
    return padded


class Button:
    def __init__(self, text, font, pos, color, buttonColor, size=None, padding=16) -> None:
        self.text = text
        self.font = font
        self.pos = pos
        self.color = color
        self.buttonColor = buttonColor
        self.padding = padding
        if "$" in text:
            self.textObj = render_latex(text, tuple(color), font.get_height())
        else:
            self.textObj = font.render(text, True, color)
        if size:
            self.rect = pygame.Rect(0, 0, int(size[0]), int(size[1]))
            self.rect.center = pos
        else:
            self.rect = self.textObj.get_rect(center=pos).inflate(40, 24)
        self.fitTextToButton()

    def fitTextToButton(self):
        max_width = max(self.rect.width - (2 * self.padding), 1)
        max_height = max(self.rect.height - (2 * self.padding), 1)
        text_width = self.textObj.get_width()
        text_height = self.textObj.get_height()

        if text_width > max_width or text_height > max_height:
            scale = min(max_width / text_width, max_height / text_height)
            new_size = (
                max(int(text_width * scale), 1),
                max(int(text_height * scale), 1),
            )
            self.textObj = pygame.transform.smoothscale(self.textObj, new_size)

        self.textRect = self.textObj.get_rect(center=self.rect.center)

    def draw(self, screen):
        pygame.draw.rect(screen, self.buttonColor, self.rect)
        screen.blit(self.textObj, self.textRect)

    def isClicked(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False
