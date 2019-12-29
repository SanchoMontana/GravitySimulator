from constants import *
import Planet
import math


def create():
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
        return Planet.planet(center, mass, radius, [theta, speed])
    return None


entities = []

# Temporary
entities.append(Planet.planet([50, 750], 20, 30, [0, 40]))
entities.append(Planet.planet([750, 50], 20, 30, [180, 40]))

game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
    if pygame.mouse.get_pressed()[0] == 1:
        new_planet = create()
        if new_planet:
            entities.append(new_planet)

    gameDisplay.fill(DEEP_BLUE)
    for entity in entities:
        entity.travel()
        entity.draw()
    pygame.display.update()
    clock.tick(FPS)


