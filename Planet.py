from constants import *
import math


class Planet:
    def __init__(self, center, mass, radius, velocity, fixed=False):
        self.center = center
        self.mass = mass
        self.radius = radius
        self.velocity = velocity
        self.fixed = fixed
        self.force = [0, 0]

    def travel(self):
        if not self.fixed:
            acceleration = [self.force[0] / self.mass, self.force[1] / self.mass]
            for i in range(2):
                self.velocity[i] += acceleration[i]
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

    def test_collision(self, bodies):
        for body in bodies:
            if body != self:
                distance = math.sqrt((self.center[0] - body.center[0]) ** 2 + (self.center[1] - body.center[1]) ** 2)
                if distance < COLLISION_DISTANCE:
                    # Calculate new velocity
                    body.velocity[0] = (self.mass * self.velocity[0] + body.mass * body.velocity[0]) / (
                            body.mass + self.mass)
                    body.velocity[1] = (self.mass * self.velocity[1] + body.mass * body.velocity[1]) / (
                            body.mass + self.mass)
                    # Calculate new mass
                    body.mass += self.mass
                    # Calculate new radius
                    body.radius = int(math.sqrt((math.pi * body.radius ** 2 + math.pi * self.radius ** 2) / math.pi))
                    del self
                    return True

    def draw(self):
        speed = math.sqrt(self.velocity[0] ** 2 + self.velocity[1] ** 2)
        temp_center = [int(self.center[0]), int(self.center[1])]
        pygame.draw.circle(gameDisplay, WHITE, temp_center, self.radius, 1)
        if speed:
            theta = math.acos(self.velocity[0]/speed)
            if self.center[1] > self.center[1] + self.velocity[1]:
                theta *= -1
            pygame.draw.line(gameDisplay, WHITE, self.center,
                             [self.center[0] + self.velocity[0] * self.radius / speed,
                              self.center[1] + self.velocity[1] * self.radius / speed])
            pygame.draw.line(gameDisplay, RED, self.center,
                             [self.center[0] + self.velocity[0] * math.log10(speed),
                              self.center[1] + self.velocity[1] * math.log10(speed)])
            if math.log10(speed) >= 1.2:
                pygame.draw.polygon(gameDisplay, RED,
                                    [(self.center[0] + self.velocity[0] * math.log10(speed),
                                      self.center[1] + self.velocity[1] * math.log10(speed)),
                                     (self.center[0] + self.velocity[0] * math.log10(speed) + math.cos(
                                         theta - math.radians(160)) * 6,
                                      self.center[1] + self.velocity[1] * math.log10(speed) + math.sin(
                                          theta - math.radians(160)) * 6),
                                     (self.center[0] + self.velocity[0] * math.log10(speed) + math.cos(
                                         theta + math.radians(160)) * 6,
                                      self.center[1] + self.velocity[1] * math.log10(speed) + math.sin(
                                          theta + math.radians(160)) * 6)])

        total_force = math.sqrt(self.force[0] ** 2 + self.force[1] ** 2)
        if self.force[0] or self.force[1]:
            theta = math.acos(self.force[0] / total_force)
            if self.center[1] > self.center[1] + self.force[1]:
                theta *= -1
            pygame.draw.line(gameDisplay, BLUE, self.center,
                             [self.center[0] + self.force[0] * math.log10(total_force),
                              self.center[1] + self.force[1] * math.log10(total_force)])
            if math.log10(total_force) >= 1.2:
                pygame.draw.polygon(gameDisplay, BLUE,
                                    [(self.center[0] + self.force[0] * math.log10(total_force),
                                      self.center[1] + self.force[1] * math.log10(total_force)),
                                     (self.center[0] + self.force[0] * math.log10(total_force) + math.cos(
                                         theta - math.radians(160)) * 6,
                                      self.center[1] + self.force[1] * math.log10(total_force) + math.sin(
                                          theta - math.radians(160)) * 6),
                                     (self.center[0] + self.force[0] * math.log10(total_force) + math.cos(
                                         theta + math.radians(160)) * 6,
                                      self.center[1] + self.force[1] * math.log10(total_force) + math.sin(
                                          theta + math.radians(160)) * 6)])
        pygame.draw.circle(gameDisplay, GREEN, temp_center, 2)
