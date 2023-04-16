import pygame
import random

class CardSprite:
    def __init__(self, img, card_dimen):
        self.img = img
        self.card_dimen = card_dimen

    def draw(self, surface, posn):
        card = (71 * self.card_dimen[0], 96 * self.card_dimen[1], 71, 96) # Width of card is 71px and height of card is 96
        surface.blit(self.img, posn, card)

def main():
    surface = pygame.display.set_mode((71 * 5, 96))
    cards_spritesheet = pygame.image.load("cards_spritesheet.png")
    cards = []
    for col in range(4):
        for row in range(13):
            cards.append(CardSprite(cards_spritesheet, (row, col)))

    random.shuffle(cards)
    cards_in_hand = cards[:5]
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        surface.fill((0, 0, 0))
        for ix, card in enumerate(cards_in_hand):
            card.draw(surface, (71 * ix, 0))
        pygame.display.flip()
    pygame.quit()

main()

