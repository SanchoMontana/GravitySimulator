from constants import *
import Planet
import Events
import math


bodies = [Planet.Planet([0, 0], 1000, 50, [2, 0]), Planet.Planet([100, 0], 100, 10, [0, -10])]


game_exit = False
while not game_exit:
    for event in pygame.event.get():
        Events.check_quit(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ctrl:
                    delta_dilation_index = DELTA_DILATION
                else:
                    delta_translation[1] = 1
            elif event.key == pygame.K_DOWN:
                if ctrl:
                    delta_dilation_index = -DELTA_DILATION
                else:
                    delta_translation[1] = -1
            elif event.key == pygame.K_LEFT:
                delta_translation[0] = 1
            elif event.key == pygame.K_RIGHT:
                delta_translation[0] = -1
            elif event.key == pygame.K_LCTRL:
                ctrl = 1
        if event.type == pygame.KEYUP:
            if ctrl:
                if event.key == pygame.K_UP and delta_dilation_index != -DELTA_DILATION:
                    delta_dilation_index = 0
                elif event.key == pygame.K_DOWN and delta_dilation_index != DELTA_DILATION:
                    delta_dilation_index = 0
            else:
                if event.key == pygame.K_UP and delta_translation[1] != -1:
                    delta_translation[1] = 0
                elif event.key == pygame.K_DOWN and delta_translation[1] != 1:
                    delta_translation[1] = 0
                elif event.key == pygame.K_LEFT and delta_translation[0] != -1:
                    delta_translation[0] = 0
                elif event.key == pygame.K_RIGHT and delta_translation[0] != 1:
                    delta_translation[0] = 0
            if event.key == pygame.K_LCTRL:
                ctrl = 0

    translation[0] += delta_translation[0]
    translation[1] += delta_translation[1]
    dilation_iterator += delta_dilation_index
    dilation_index = math.e ** dilation_iterator

    if pygame.mouse.get_pressed()[0] == 1:
        new_planet = Events.create_planet()
        if new_planet:
            bodies.append(new_planet)

    gameDisplay.fill(BLACK)
    for body in bodies:
        body.calculate_force(bodies)
    for body in bodies:
        body.draw_trail()
        body.travel()
        if body.test_collision(bodies):
            bodies.remove(body)
        body.draw(dilation_index)



    # Temporary
    #for i in range(int(DISPLAY_WIDTH / 100)):
    #    for j in range(int(DISPLAY_HEIGHT / 100)):
    #        pygame.draw.line(gameDisplay, RED, (0, j * 100), (800, j * 100))
    #        pygame.draw.line(gameDisplay, RED, (i * 100, 0), (i * 100, 800))
    pygame.display.update()
    clock.tick(FPS)
