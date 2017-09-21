import pygame, random, os.path

from sprites import Cards


def main():
    """ Set up the game and run the main game loop. """

    pygame.init()

    cards_sheet = pygame.image.load("cards_sprite.gif")

    card_width = cards_sheet.get_width() / 13  # This is an NxN chess board.
    surface_width = int(13 * card_width)  # Adjust to exactly fit n squares.

    card_height = cards_sheet.get_height() / 5
    surface_height = int(card_height * 5)

    card_offset_width = (surface_width - card_width) // 2

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_width, surface_height))

    card_1 = Cards(cards_sheet, 0, 4)

    card_index = []

    for x in range(52):
        card_index.append(x)

    random.Random().shuffle(card_index)

    sprites = []

    for x in range(4):
        for i in range(13):
            sprites.append(Cards(cards_sheet, i, x))

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        if ev.type == pygame.MOUSEBUTTONDOWN:
            posn_of_click = ev.dict['pos']
            if card_1.contains_point(posn_of_click, (card_offset_width, card_height), card_width, card_height):
                random.Random().shuffle(card_index)

        # Draw the background
        main_surface.fill((0, 255, 0))

        # Draw the sprites
        card_1.draw(main_surface, (card_offset_width, card_height), card_width, card_height)

        i = 2
        for x in range(5):
            sprites[card_index[x]].draw(main_surface, (card_width * i, 3 * card_height), card_width, card_height)
            i += 2

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
