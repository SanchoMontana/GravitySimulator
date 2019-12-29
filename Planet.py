from constants import *
import random
import math


class planet:
    def __init__(self, center, mass, radius, velocity):
        self.center = center
        self.mass = mass
        self.radius = radius
        self.velocity = velocity
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.force = [0, 0]

    def travel(self):
        acceleration = [0, 0]
        acceleration = [self.force[0] / self.mass, self.force[1] / self.mass]
        self.center[0] += self.velocity[0] / 10
        self.center[1] += self.velocity[1] / 10

    def calculate_force(self, bodies):
        self.force = [0, 0]
        for body in bodies:
            if body != self:
                distance = math.sqrt((self.center[0] - body.center[0]) ** 2 + (self.center[1] - body.center[1]) ** 2)
                resultant_force = G * self.mass * body.mass / (distance ** 2)
                print(resultant_force)
                theta = math.acos((body.center[0] - self.center[0])/(math.sqrt((body.center[0] - self.center[0]) ** 2 + (body.center[1] - self.center[1]) ** 2) ** 2))
                self.force[0] += resultant_force * math.cos(theta)
                self.force[1] += resultant_force * math.sin(theta)

    def draw(self):
        speed = math.sqrt(self.velocity[0] ** 2 + self.velocity[1] ** 2)
        temp_center = [int(self.center[0]), int(self.center[1])]
        pygame.draw.circle(gameDisplay, GRAY, temp_center, self.radius, 1)
        pygame.draw.line(gameDisplay, GRAY, self.center,
                         [self.center[0] + self.velocity[0] * self.radius / speed,
                          self.center[1] + self.velocity[1] * self.radius / speed])
        pygame.draw.line(gameDisplay, RED, self.center,
                         [self.center[0] + self.velocity[0] * 2,
                          self.center[1] + self.velocity[1] * 2])
        pygame.draw.polygon(gameDisplay, RED,
                            [(self.center[0] + self.velocity[0] * 2,
                              self.center[1] + self.velocity[1] * 2),
                             (self.center[0] + self.velocity[0] * 2 + math.cos(math.radians(self.velocity[0] / speed - 160)) * 6,
                              self.center[1] + self.velocity[1] * 2 + math.sin(math.radians(self.velocity[1] / speed - 160)) * 6),
                             (self.center[0] + self.velocity[0] * 2 + math.cos(math.radians(self.velocity[0] / speed + 160)) * 6,
                              self.center[1] + self.velocity[1] * 2 + math.sin(math.radians(self.velocity[1] / speed + 160)) * 6)])
