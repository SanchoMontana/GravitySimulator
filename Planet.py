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
        self.velocity = [self.velocity[0] + acceleration[0], self.velocity[1] + acceleration[1]]
        self.center[0] += self.velocity[0] / 10
        self.center[1] += self.velocity[1] / 10

    def calculate_force(self, bodies):
        self.force = [0, 0]
        for body in bodies:
            if body != self:
                distance = math.sqrt((self.center[0] - body.center[0]) ** 2 + (self.center[1] - body.center[1]) ** 2)
                resultant_force = self.mass * body.mass / (distance ** 2)
                theta = math.acos((self.center[0] - body.center[0]) / distance) + math.pi
                if self.center[1] < body.center[1]:
                    theta *= -1
                self.force[0] += resultant_force * math.cos(theta)
                self.force[1] += resultant_force * math.sin(theta)

    def draw(self):
        speed = math.sqrt(self.velocity[0] ** 2 + self.velocity[1] ** 2)
        theta = math.acos(self.velocity[0]/speed)
        if self.center[1] > self.center[1] + self.velocity[1]:
            theta *= -1
        temp_center = [int(self.center[0]), int(self.center[1])]
        pygame.draw.circle(gameDisplay, WHITE, temp_center, self.radius, 1)
        if speed * 2 > 5:
            pygame.draw.line(gameDisplay, WHITE, self.center,
                             [self.center[0] + self.velocity[0] * self.radius / speed,
                              self.center[1] + self.velocity[1] * self.radius / speed])
            pygame.draw.line(gameDisplay, RED, self.center,
                             [self.center[0] + self.velocity[0] * 2,
                              self.center[1] + self.velocity[1] * 2])
            pygame.draw.polygon(gameDisplay, RED,
                                [(self.center[0] + self.velocity[0] * 2,
                                  self.center[1] + self.velocity[1] * 2),
                                 (self.center[0] + self.velocity[0] * 2 + math.cos(theta - math.radians(160)) * 6,
                                  self.center[1] + self.velocity[1] * 2 + math.sin(theta - math.radians(160)) * 6),
                                 (self.center[0] + self.velocity[0] * 2 + math.cos(theta + math.radians(160)) * 6,
                                  self.center[1] + self.velocity[1] * 2 + math.sin(theta + math.radians(160)) * 6)])
        if math.sqrt(self.force[0] ** 2 + self.force[1] ** 2) > 5:
            pygame.draw.line(gameDisplay, BLUE, self.center,
                             [self.center[0] + self.force[0] * 10,
                              self.center[1] + self.force[1] * 10])
        pygame.draw.circle(gameDisplay, GREEN, temp_center, 2)

