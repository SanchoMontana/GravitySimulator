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
                     [int(center[0] + math.cos(math.radians(theta)) * radius),
                      int(center[1] + math.sin(math.radians(theta)) * radius)])
    pygame.draw.polygon(gameDisplay, GRAY,
                        [(int(center[0] + math.cos(math.radians(theta)) * radius),
                          int(center[1] + math.sin(math.radians(theta)) * radius)),
                         (int(center[0] + math.cos(math.radians(theta)) * radius + math.cos(
                             math.radians(theta - 160)) * 6),
                          int(center[1] + math.sin(math.radians(theta)) * radius + math.sin(
                              math.radians(theta - 160)) * 6)),
                         (int(center[0] + math.cos(math.radians(theta)) * radius + math.cos(
                             math.radians(theta + 160)) * 6),
                          int(center[1] + math.sin(math.radians(theta)) * radius + math.sin(
                              math.radians(theta + 160)) * 6))])
    pygame.display.update()
    speed = int(input("Speed (m/s): "))
    pygame.draw.line(gameDisplay, RED, center,
                     [int(center[0] + math.cos(math.radians(theta)) * speed * 3),
                      int(center[1] + math.sin(math.radians(theta)) * speed * 3)])
    pygame.draw.polygon(gameDisplay, RED,
                        [(int(center[0] + math.cos(math.radians(theta)) * speed * 3),
                          int(center[1] + math.sin(math.radians(theta)) * speed * 3)),
                         (int(center[0] + math.cos(math.radians(theta)) * speed * 3 + math.cos(
                             math.radians(theta - 160)) * 6),
                          int(center[1] + math.sin(math.radians(theta)) * speed * 3 + math.sin(
                              math.radians(theta - 160)) * 6)),
                         (int(center[0] + math.cos(math.radians(theta)) * speed * 3 + math.cos(
                             math.radians(theta + 160)) * 6),
                          int(center[1] + math.sin(math.radians(theta)) * speed * 3 + math.sin(
                              math.radians(theta + 160)) * 6))])
    pygame.display.update()
    ready = input("Confirm [y/N]: ")
    if ready == "" or ready.lower() == "y" or ready.lower == "yes":
        return Planet.Planet(center, mass, radius,
                             [speed * math.cos(math.radians(theta)), speed * math.sin(math.radians(theta))])
    return None


bodies = [Planet.Planet([600, 400], 1000, 80, [-5, -1]), Planet.Planet([400, 400], 100, 20, [5, 1]),
          Planet.Planet([300, 400], 100, 60, [2, 6]), Planet.Planet([400, 300], 120, 10, [5, 3]),
          Planet.Planet([400, 500], 10, 20, [0, -6]), Planet.Planet([400, 700], 3, 10, [0, 0])]
game_exit = False
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
    if pygame.mouse.get_pressed()[0] == 1:
        new_planet = create()
        if new_planet:
            bodies.append(new_planet)

    gameDisplay.fill(BLACK)
    for body in bodies:
        body.calculate_force(bodies)
    for body in bodies:
        body.travel()
        if body.test_collision(bodies):
            bodies.remove(body)
        body.draw()
    pygame.display.update()
    clock.tick(FPS)
