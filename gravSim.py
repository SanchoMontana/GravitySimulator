from constants import *
import Planet
import viewingTools

bodies = [Planet.Planet([0, 0], 10000, 40, [0, 0]),
          Planet.Planet([200, 0], 100, 20, [0, -10]),
          Planet.Planet([-200, 0], 100, 20, [0, 10]),
          Planet.Planet([0, 350], 50, 10, [-5, -2]),
          Planet.Planet([0, -350], 50, 10, [5, 2])]

game_exit = False
while not game_exit:
    viewingTools.check_view()
    viewingTools.translate()
    viewingTools.dilate()

    gameDisplay.fill(BLACK)
    for body in bodies:
        body.calculate_force(bodies)
    for body in bodies:
        body.translate()
        body.draw_trail()
        body.dilate()
        body.travel()
        if body.test_collision(bodies):
            bodies.remove(body)
        body.draw()

    # Draw grid lines
    # Temporary
    # for i in range(int(DISPLAY_WIDTH / 100)):
    #    for j in range(int(DISPLAY_HEIGHT / 100)):
    #        pygame.draw.line(gameDisplay, RED, (0, j * 100), (800, j * 100))
    #        pygame.draw.line(gameDisplay, RED, (i * 100, 0), (i * 100, 800))
    pygame.display.update()
    clock.tick(FPS)
