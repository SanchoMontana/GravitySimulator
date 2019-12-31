from constants import *
import math
import Planet


def check_quit(event):
    if event.type == pygame.QUIT:
        quit()


def create_planet():
    center = [None, None]
    center[0] = pygame.mouse.get_pos()[0]
    center[1] = pygame.mouse.get_pos()[1]
    pygame.draw.circle(gameDisplay, RED, center, 3)
    pygame.display.update()
    mass = int(input("Mass (kg): "))
    radius = int(input("Radius (m): "))
    pygame.draw.circle(gameDisplay, GRAY, center, radius, 1)
    pygame.display.update()
    theta = int(input("Theta (degrees): ")) - 90
    pygame.draw.line(gameDisplay, GRAY, center,
                     [center[0] + math.cos(math.radians(theta)) * radius,
                      center[1] + math.sin(math.radians(theta)) * radius])
    pygame.draw.polygon(gameDisplay, GRAY,
                        [(center[0] + math.cos(math.radians(theta)) * radius,
                          center[1] + math.sin(math.radians(theta)) * radius),
                         (center[0] + math.cos(math.radians(theta)) * radius + math.cos(
                             math.radians(theta - 160)) * 6,
                          center[1] + math.sin(math.radians(theta)) * radius + math.sin(
                              math.radians(theta - 160)) * 6),
                         (center[0] + math.cos(math.radians(theta)) * radius + math.cos(
                             math.radians(theta + 160)) * 6,
                          center[1] + math.sin(math.radians(theta)) * radius + math.sin(
                              math.radians(theta + 160)) * 6)])
    pygame.display.update()
    speed = int(input("Speed (m/s): "))
    pygame.draw.line(gameDisplay, RED, center,
                     [center[0] + math.cos(math.radians(theta)) * speed * 3,
                      center[1] + math.sin(math.radians(theta)) * speed * 3])
    pygame.draw.polygon(gameDisplay, RED,
                        [(center[0] + math.cos(math.radians(theta)) * speed * 3,
                          center[1] + math.sin(math.radians(theta)) * speed * 3),
                         (center[0] + math.cos(math.radians(theta)) * speed * 3 + math.cos(
                             math.radians(theta - 160)) * 6,
                          center[1] + math.sin(math.radians(theta)) * speed * 3 + math.sin(
                              math.radians(theta - 160)) * 6),
                         (center[0] + math.cos(math.radians(theta)) * speed * 3 + math.cos(
                             math.radians(theta + 160)) * 6,
                          center[1] + math.sin(math.radians(theta)) * speed * 3 + math.sin(
                              math.radians(theta + 160)) * 6)])
    pygame.display.update()
    ready = input("Confirm [y/N]: ")
    if ready == "" or ready.lower() == "y" or ready.lower == "yes":
        return Planet.Planet(center, mass, radius,
                             [speed * math.cos(math.radians(theta)), speed * math.sin(math.radians(theta))])
    return None