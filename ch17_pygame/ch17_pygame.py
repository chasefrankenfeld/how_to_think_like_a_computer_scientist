import pygame
import time


def main():
    """ Set up the game and run the main game loop. """
    pygame.init()  # Prepare the pygame module for use

    # Create surface of (width, height), and its window
    main_surface = pygame.display.set_mode((480, 240))

    # Load an image to draw
    bear = pygame.image.load("grizzly_bear.jpg")
    bear = pygame.transform.scale(bear, (40, 40))

    # Create a font for rendering text
    my_font = pygame.font.SysFont('Courier', 16)

    frame_count = 0
    frame_rate = 0
    t0 = time.clock()

    while True:
        ev = pygame.event.poll()  # Look for an event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break  # Leave the game loop

        # Update your game objects and data structures here....
        frame_count += 1
        if frame_count % 500 == 0:
            t1 = time.clock()
            frame_rate = 500 / (t1-t0)
            t0 = t1

        # Completely redraw the surface, starting with background
        main_surface.fill((0, 200, 255))

        # Over paint a smaller rectangle on the main surface
        main_surface.fill((255, 0, 0), (300, 100, 150, 90))

        # Copy our image to the surface, at this (x,y) position
        main_surface.blit(bear, (100, 200))

        # Make a new surface with an image of the text
        the_text = my_font.render('Frame = {0}, rate = {1:.2f} fps'
                                  .format(frame_count, frame_rate), True, (0, 0, 0))
        # Copy the text surface to themain surface
        main_surface.blit(the_text, (10, 10))

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()  # Once we leave the loop, close the window.

main()