from constants import *
import random
import math

class planet:
    def __init__(self, center, mass, radius, vector):
        self.center = center
        self.mass = mass
        self.radius = radius
        self.vector = vector
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def travel(self):
        self.center[0] += math.cos(math.radians(self.vector[0])) * (self.vector[1] / 10)
        self.center[1] += math.sin(math.radians(self.vector[0])) * (self.vector[1] / 10)

    def draw(self):
        temp_center = [int(self.center[0]), int(self.center[1])]
        pygame.draw.circle(gameDisplay, GRAY, temp_center, self.radius, 1)
        pygame.display.update()
        pygame.draw.line(gameDisplay, GRAY, self.center,
                         [self.center[0] + math.cos(math.radians(self.vector[0])) * self.radius,
                          self.center[1] + math.sin(math.radians(self.vector[0])) * self.radius])
        pygame.draw.polygon(gameDisplay, GRAY,
                            [(self.center[0] + math.cos(math.radians(self.vector[0])) * self.radius,
                              self.center[1] + math.sin(math.radians(self.vector[0])) * self.radius),
                             (self.center[0] + math.cos(math.radians(self.vector[0])) * self.radius + math.cos(
                                 math.radians(self.vector[0] - 160)) * 6,
                              self.center[1] + math.sin(math.radians(self.vector[0])) * self.radius + math.sin(
                                  math.radians(self.vector[0] - 160)) * 6),
                             (self.center[0] + math.cos(math.radians(self.vector[0])) * self.radius + math.cos(
                                 math.radians(self.vector[0] + 160)) * 6,
                              self.center[1] + math.sin(math.radians(self.vector[0])) * self.radius + math.sin(
                                  math.radians(self.vector[0] + 160)) * 6)])
        pygame.display.update()
        pygame.draw.line(gameDisplay, RED, self.center,
                         [self.center[0] + math.cos(math.radians(self.vector[0])) * self.vector[1] * 3,
                          self.center[1] + math.sin(math.radians(self.vector[0])) * self.vector[1] * 3])
        pygame.draw.polygon(gameDisplay, RED,
                            [(self.center[0] + math.cos(math.radians(self.vector[0])) * self.vector[1] * 3,
                              self.center[1] + math.sin(math.radians(self.vector[0])) * self.vector[1] * 3),
                             (self.center[0] + math.cos(math.radians(self.vector[0])) * self.vector[1] * 3 + math.cos(
                                 math.radians(self.vector[0] - 160)) * 6,
                              self.center[1] + math.sin(math.radians(self.vector[0])) * self.vector[1] * 3 + math.sin(
                                  math.radians(self.vector[0] - 160)) * 6),
                             (self.center[0] + math.cos(math.radians(self.vector[0])) * self.vector[1] * 3 + math.cos(
                                 math.radians(self.vector[0] + 160)) * 6,
                              self.center[1] + math.sin(math.radians(self.vector[0])) * self.vector[1] * 3 + math.sin(
                                  math.radians(self.vector[0] + 160)) * 6)])
