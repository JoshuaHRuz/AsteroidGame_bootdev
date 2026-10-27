import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH


class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius = SHOT_RADIUS):
        super().__init__(x, y, radius)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, "white", self.position, self.radius , LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt