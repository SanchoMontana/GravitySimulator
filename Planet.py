from constants import *
import math
import random


class Planet:
    def __init__(self, center, mass, radius, velocity, fixed=False):
        self.center = [center[0] + DISPLAY_WIDTH / 2, center[1] + DISPLAY_HEIGHT / 2]
        self.drawn_center = self.center
        self.mass = mass
        self.radius = radius
        self.drawn_radius = radius * dilation_index
        self.velocity = velocity
        self.fixed = fixed
        self.force = [0, 0]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.collect_trail = True
        self.trail = []
        self.drawn_trail = []

    def draw_trail(self, translation, translation_old, dilation_index, dilation_index_old):
        # if dilation_index changes
        if not self.trail or self.trail[-1] != self.drawn_center:
            self.trail.append((self.drawn_center[0], self.drawn_center[1]))
            self.drawn_trail.append((self.drawn_center[0], self.drawn_center[1]))
            self.drawn_trail[-1] = (DISPLAY_WIDTH / 2 + (self.drawn_trail[-1][0] - DISPLAY_WIDTH / 2) * dilation_index, DISPLAY_HEIGHT / 2 + (self.drawn_trail[-1][1] - DISPLAY_HEIGHT / 2) * dilation_index)
            #self.drawn_trail.append((DISPLAY_WIDTH / 2 + (self.trail[-1][0] - DISPLAY_WIDTH / 2) * dilation_index, DISPLAY_HEIGHT / 2 + (self.trail[-1][1] - DISPLAY_HEIGHT / 2)))
        if dilation_index != dilation_index_old:
            self.drawn_trail = [(DISPLAY_WIDTH / 2 + (i[0] - DISPLAY_WIDTH / 2) * dilation_index, DISPLAY_HEIGHT / 2 + (i[1] - DISPLAY_HEIGHT / 2) * dilation_index) for i in self.trail]
        for i in self.drawn_trail:
            gameDisplay.set_at((int(i[0]), int(i[1])), self.color)

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
                # TODO: Add G
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

    def translate(self, translation):
        self.drawn_center = [self.center[0] + translation[0], self.center[1] + translation[1]]

    def dilate(self, dilation_index):
        distance_from_center = [self.drawn_center[0] - DISPLAY_WIDTH / 2, self.drawn_center[1] - DISPLAY_HEIGHT / 2]
        self.drawn_center = [int(DISPLAY_WIDTH / 2 + distance_from_center[0] * dilation_index), int(DISPLAY_HEIGHT / 2 + distance_from_center[1] * dilation_index)]
        self.drawn_radius = int(self.radius * dilation_index)

    def draw(self):
        speed = math.sqrt(self.velocity[0] ** 2 + self.velocity[1] ** 2)
        pygame.draw.circle(gameDisplay, WHITE, self.drawn_center, self.drawn_radius, 1)
        if speed:
            theta = math.acos(self.velocity[0]/speed)
            if self.drawn_center[1] > self.drawn_center[1] + self.velocity[1]:
                theta *= -1
            pygame.draw.line(gameDisplay, WHITE, self.drawn_center,
                             [self.drawn_center[0] + self.velocity[0] * self.drawn_radius / speed,
                              self.drawn_center[1] + self.velocity[1] * self.drawn_radius / speed])
            pygame.draw.line(gameDisplay, RED, self.drawn_center,
                             [self.drawn_center[0] + self.velocity[0] * math.log10(speed),
                              self.drawn_center[1] + self.velocity[1] * math.log10(speed)])
            if math.log10(speed) >= 1.2:
                pygame.draw.polygon(gameDisplay, RED,
                                    [(self.drawn_center[0] + self.velocity[0] * math.log10(speed),
                                      self.drawn_center[1] + self.velocity[1] * math.log10(speed)),
                                     (self.drawn_center[0] + self.velocity[0] * math.log10(speed) + math.cos(
                                         theta - math.radians(160)) * 6,
                                      self.drawn_center[1] + self.velocity[1] * math.log10(speed) + math.sin(
                                          theta - math.radians(160)) * 6),
                                     (self.drawn_center[0] + self.velocity[0] * math.log10(speed) + math.cos(
                                         theta + math.radians(160)) * 6,
                                      self.drawn_center[1] + self.velocity[1] * math.log10(speed) + math.sin(
                                          theta + math.radians(160)) * 6)])

        total_force = math.sqrt(self.force[0] ** 2 + self.force[1] ** 2)
        if self.force[0] or self.force[1]:
            theta = math.acos(self.force[0] / total_force)
            if self.drawn_center[1] > self.drawn_center[1] + self.force[1]:
                theta *= -1
            pygame.draw.line(gameDisplay, BLUE, self.drawn_center,
                             [self.drawn_center[0] + self.force[0] * math.log10(total_force),
                              self.drawn_center[1] + self.force[1] * math.log10(total_force)])
            if math.log10(total_force) >= 1.2:
                pygame.draw.polygon(gameDisplay, BLUE,
                                    [(self.drawn_center[0] + self.force[0] * math.log10(total_force),
                                      self.drawn_center[1] + self.force[1] * math.log10(total_force)),
                                     (self.drawn_center[0] + self.force[0] * math.log10(total_force) + math.cos(
                                         theta - math.radians(160)) * 6,
                                      self.drawn_center[1] + self.force[1] * math.log10(total_force) + math.sin(
                                          theta - math.radians(160)) * 6),
                                     (self.drawn_center[0] + self.force[0] * math.log10(total_force) + math.cos(
                                         theta + math.radians(160)) * 6,
                                      self.drawn_center[1] + self.force[1] * math.log10(total_force) + math.sin(
                                          theta + math.radians(160)) * 6)])
        pygame.draw.circle(gameDisplay, GREEN, self.drawn_center, 2)
