from constants import *
import Planet
import Events
import math
import viewingTools

bodies = [Planet.Planet([0, 0], 10000, 40, [0, 0]),
          Planet.Planet([200, 0], 100, 20, [0, -10]),
          Planet.Planet([-200, 0], 100, 20, [0, 10]),
          Planet.Planet([0, 350], 50, 10, [-5, -5]),
          Planet.Planet([0, -350], 50, 10, [5, 5])]

game_exit = False
while not game_exit:
    viewingTools.check_view()
    viewingTools.translate()
    viewingTools.dilate()

    if pygame.mouse.get_pressed()[0] == 1:
        new_planet = Events.create_planet()
        if new_planet:
            bodies.append(new_planet)

    gameDisplay.fill(BLACK)
    for body in bodies:
        body.calculate_force(bodies)
    for body in bodies:
        body.translate(viewingTools.translation)
        body.draw_trail(viewingTools.translation, viewingTools.translation_old, viewingTools.dilation_index, viewingTools.dilation_index_old)
        body.dilate(viewingTools.dilation_index)
        body.travel()
        if body.test_collision(bodies):
            bodies.remove(body)
        body.draw()

    # Temporary
    # for i in range(int(DISPLAY_WIDTH / 100)):
    #    for j in range(int(DISPLAY_HEIGHT / 100)):
    #        pygame.draw.line(gameDisplay, RED, (0, j * 100), (800, j * 100))
    #        pygame.draw.line(gameDisplay, RED, (i * 100, 0), (i * 100, 800))
    pygame.display.update()
    clock.tick(FPS)
