import pygame

from sprites import QueenSprite, DukeSprite


def draw_board(the_board):
    """ Draw a chess board with queens, as determined by the the_board. """

    pygame.init()
    my_clock = pygame.time.Clock()
    colors = [(255, 0, 0), (0, 0, 0)]  # Set up colors [red, black]

    n = len(the_board)  # This is an NxN chess board.
    surface_sz = 480  # Proposed physical surface size.
    sq_sz = surface_sz // n  # sq_sz is length of a square.
    surface_sz = n * sq_sz  # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    all_sprites = []  # Keep a list of all sprites in the game

    ball = pygame.image.load("grizzly_bear.jpg")
    ball = pygame.transform.scale(ball, (40, 40))

    # Load the sprite sheet
    duke_sprite_sheet = pygame.image.load("duke_spritesheet.png")

    # Instantiate two duke instances, pt them on the chessboard
    duke1 = DukeSprite(duke_sprite_sheet, (sq_sz * 2, 0))
    duke2 = DukeSprite(duke_sprite_sheet, (sq_sz * 5, sq_sz))

    # Add them to the list of sprites which our game loop manages
    all_sprites.append(duke1)
    all_sprites.append(duke2)

    # Use an extra offset to centre the ball in its square.
    # If the square is too small, offset becomes negative,
    #   but it will still be centered :-)
    ball_offset = (sq_sz - ball.get_width()) // 2

    # Create a sprite object for each queen, and populate our list.
    for (col, row) in enumerate(the_board):
        a_queen = QueenSprite(ball,
                  (col * sq_sz + ball_offset, row * sq_sz + ball_offset))
        all_sprites.append(a_queen)

    while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()

        if ev.type == pygame.QUIT:
            break

        if ev.type == pygame.KEYDOWN:
            key = ev.dict['key']
            if key == 27:  # On Escape Key
                break  # Leave the game loop
            if key == ord('r'):
                colors[0] = (255, 0, 0)  # Change the color to red
            elif key == ord('g'):
                colors[0] = (0, 255, 0)  # Change the color to green
            elif key == ord('b'):
                colors[0] = (0, 0, 255)  # Change the color to blue

        if ev.type == pygame.MOUSEBUTTONDOWN:
            posn_of_click = ev.dict['pos']
            for sprite in all_sprites:
                if sprite.contains_point(posn_of_click):
                    sprite.handle_click()
                    break

        # Ask every sprite to update itself
        for sprite in all_sprites:
            sprite.update()

        # Draw a fresh background (a blank chess board)
        for row in range(n):  # Draw each row of the board.
            c_indx = row % 2  # Alternate starting color
            for col in range(n):  # Run through cols drawing squares
                the_square = (col * sq_sz, row * sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                # Now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        # Now that squares are drawn, draw the queens.
        for sprite in all_sprites:
            sprite.draw(surface)

        pygame.display.flip()
        my_clock.tick(60)  # Waste time so that frame rate becomes 60 frames per sec (fps)

    pygame.quit()


if __name__ == "__main__":
    draw_board([0, 5, 3, 1, 6, 4, 2])  # 7 x 7 to test window size
    # draw_board([6, 4, 2, 0, 5, 7, 1, 3])
    # draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])  # 13 x 13
    # draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])
