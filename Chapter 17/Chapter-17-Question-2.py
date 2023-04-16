import pygame
import time

gravity = 0.01

class QueenSprite:
    def __init__(self, img, target_posn):
        self.img = img
        self.target_posn = target_posn
        (x, y) = self.target_posn
        self.posn = (x, 0)
        self.y_velocity = 0

    def update(self):
        self.y_velocity += gravity
        (x, y) = self.posn
        new_y_pos = y + self.y_velocity
        (target_x, target_y) = self.target_posn

        if target_y - new_y_pos < 0:
            self.y_velocity *= -0.65
            new_y_pos = target_y + target_y - new_y_pos

        self.posn = (x, new_y_pos)

    def draw(self, target_surface):
        target_surface.blit(self.img, self.posn)

    def contains_point(self, pt):
        (my_x, my_y) = self.posn
        (x, y) = pt
        width = self.img.get_width()
        height = self.img.get_height()

        return (x >= my_x and x < my_x + width and
               y >= my_y and y < my_y  + height)

    def handle_click(self):
        self.y_velocity += -1.5

class DukeSprite:
    def __init__(self, img, target_posn):
        self.img = img
        self.posn = target_posn
        self.curr_patch_num = 0
        self.anim_frame_count = 0

    def update(self):
        if self.anim_frame_count > 0:
            self.anim_frame_count = (self.anim_frame_count + 1) % 60
            self.curr_patch_num = self.anim_frame_count // 6

    def draw(self, target_surface):
        patch_rect = (self.curr_patch_num * 50, 0, 50, self.img.get_height())
        target_surface.blit(self.img, self.posn, patch_rect)

    def contains_point(self, pt):
        (my_x, my_y) = self.posn
        (x, y) = pt
        width = 50
        height = self.img.get_height()

        return (x >= my_x and x < my_x + width and
               y >= my_y and y < my_y  + height)

    def handle_click(self):
        if self.anim_frame_count == 0:
            self.anim_frame_count = 5

def draw_board(the_board):
    pygame.init()
    colors = [(0, 200, 255), (0, 0, 0)]

    surface_sz = 480
    n = len(the_board)
    sq_sz = surface_sz / n
    surface_sz = n * sq_sz

    queen = pygame.image.load("ball.png")
    queen_offset = abs((sq_sz - queen.get_width()) // 2)

    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    all_sprites = []

    for (col, row) in enumerate(the_board):
        a_queen = QueenSprite(queen, (col*sq_sz+queen_offset,
                                      row*sq_sz+queen_offset))
        all_sprites.append(a_queen)

    duke_sprite_sheet = pygame.image.load("duke_spritesheet.png")
    duke1 = DukeSprite(duke_sprite_sheet,(sq_sz*2, 0))
    duke2 = DukeSprite(duke_sprite_sheet,(sq_sz*5, sq_sz))

    all_sprites.append(duke1)
    all_sprites.append(duke2)

    my_clock = pygame.time.Clock()
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.KEYDOWN:
            key = ev.dict["key"]
            if key == 27:
                break
            if key == ord('r'):
                colors[0] = (255, 0, 0)
            elif key == ord('g'):
                colors[0] = (0, 255, 0)
            elif key == ord('b'):
                colors[0] = (0, 0, 255)

        if ev.type == pygame.MOUSEBUTTONDOWN:
            posn_of_click = ev.dict['pos']
            for sprite in all_sprites:
                if sprite.contains_point(posn_of_click):
                    sprite.handle_click()

        for sprite in all_sprites:
            sprite.update()

        for row in range(n):
            col_index = row % 2
            for col in range(n):
                main_surface.fill(colors[col_index], (col*sq_sz, row*sq_sz, sq_sz, sq_sz))
                col_index = (col_index + 1) % 2

        for sprite in all_sprites:
            sprite.draw(main_surface)

        pygame.display.flip()
        my_clock.tick(60)
    pygame.quit()

draw_board([6, 4, 2, 0, 5, 7, 1, 3])
