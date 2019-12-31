from constants import *
import math
import random


class Planet:
    def __init__(self, center, mass, radius, velocity, fixed=False):
        self.center = [center[0] + DISPLAY_WIDTH / 2, center[1] + DISPLAY_HEIGHT / 2]
        self.drawn_center = self.center
        self.mass = mass
        self.radius = radius
        self.velocity = velocity
        self.fixed = fixed
        self.force = [0, 0]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.collect_trail = True
        self.trail = []

    def draw_trail(self):
        if self.collect_trail:
            point = (int(self.center[0]), int(self.center[1]))
            if not self.trail or self.trail[-1] != point:
                self.trail.append(point)
            for i in self.trail:
                gameDisplay.set_at(i, self.color)

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

    
    def draw(self, dilation_index):
        speed = math.sqrt(self.velocity[0] ** 2 + self.velocity[1] ** 2)
        drawn_center = [self.center[0] + translation[0], self.center[1] + translation[1]]
        distance_from_center = [drawn_center[0] - DISPLAY_WIDTH / 2, drawn_center[1] - DISPLAY_HEIGHT / 2]
        #drawn_center[0] = int(drawn_center[0] + distance_from_center[0] * dilation_index)
        #drawn_center[1] = int(drawn_center[1] + distance_from_center[1] * dilation_index)

        drawn_center[0] = int(DISPLAY_WIDTH / 2 + distance_from_center[0] * dilation_index)
        drawn_center[1] = int(DISPLAY_HEIGHT / 2 + distance_from_center[1] * dilation_index)

        drawn_radius = int(self.radius * dilation_index)


        pygame.draw.circle(gameDisplay, WHITE, drawn_center, drawn_radius, 1)
        if speed:
            theta = math.acos(self.velocity[0]/speed)
            if drawn_center[1] > drawn_center[1] + self.velocity[1]:
                theta *= -1
            pygame.draw.line(gameDisplay, WHITE, drawn_center,
                             [drawn_center[0] + self.velocity[0] * drawn_radius / speed,
                              drawn_center[1] + self.velocity[1] * drawn_radius / speed])
            pygame.draw.line(gameDisplay, RED, drawn_center,
                             [drawn_center[0] + self.velocity[0] * math.log10(speed),
                              drawn_center[1] + self.velocity[1] * math.log10(speed)])
            if math.log10(speed) >= 1.2:
                pygame.draw.polygon(gameDisplay, RED,
                                    [(drawn_center[0] + self.velocity[0] * math.log10(speed),
                                      drawn_center[1] + self.velocity[1] * math.log10(speed)),
                                     (drawn_center[0] + self.velocity[0] * math.log10(speed) + math.cos(
                                         theta - math.radians(160)) * 6,
                                      drawn_center[1] + self.velocity[1] * math.log10(speed) + math.sin(
                                          theta - math.radians(160)) * 6),
                                     (drawn_center[0] + self.velocity[0] * math.log10(speed) + math.cos(
                                         theta + math.radians(160)) * 6,
                                      drawn_center[1] + self.velocity[1] * math.log10(speed) + math.sin(
                                          theta + math.radians(160)) * 6)])

        total_force = math.sqrt(self.force[0] ** 2 + self.force[1] ** 2)
        if self.force[0] or self.force[1]:
            theta = math.acos(self.force[0] / total_force)
            if drawn_center[1] > drawn_center[1] + self.force[1]:
                theta *= -1
            pygame.draw.line(gameDisplay, BLUE, drawn_center,
                             [drawn_center[0] + self.force[0] * math.log10(total_force),
                              drawn_center[1] + self.force[1] * math.log10(total_force)])
            if math.log10(total_force) >= 1.2:
                pygame.draw.polygon(gameDisplay, BLUE,
                                    [(drawn_center[0] + self.force[0] * math.log10(total_force),
                                      drawn_center[1] + self.force[1] * math.log10(total_force)),
                                     (drawn_center[0] + self.force[0] * math.log10(total_force) + math.cos(
                                         theta - math.radians(160)) * 6,
                                      drawn_center[1] + self.force[1] * math.log10(total_force) + math.sin(
                                          theta - math.radians(160)) * 6),
                                     (drawn_center[0] + self.force[0] * math.log10(total_force) + math.cos(
                                         theta + math.radians(160)) * 6,
                                      drawn_center[1] + self.force[1] * math.log10(total_force) + math.sin(
                                          theta + math.radians(160)) * 6)])
        pygame.draw.circle(gameDisplay, GREEN, drawn_center, 2)
