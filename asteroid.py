import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, "white", self.position, self.radius , LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            asteroid1_vel = self.velocity.rotate(random_angle)
            asteroid2_vel = self.velocity.rotate(- random_angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position[0], self.position[1], new_rad)
            asteroid2 = Asteroid(self.position[0], self.position[1], new_rad)  
            asteroid1.velocity = asteroid1_vel * 1.2
            asteroid2.velocity = asteroid2_vel * 1.2
            