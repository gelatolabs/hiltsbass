init python:
    config.screen_width=1920
    config.screen_height=1080
    import time
    import pygame

    class RhythmD(object):
        def __init__(self, sprite, speed, delay, ypos=0):
            self.sprite = sprite
            self.speed = speed
            self.delay = delay
            self.show = manager.create(sprite)
            self.show.x = -50
            self.show.y = ypos
            self.moving = False # No point in checking if it isn't.

        def update(self):
            if store.t + self.delay < time.time():
                self.moving = True
                self.x = self.x + self.speed
            else:
                pass

        @property
        def x(self):
            return self.show.x
        @x.setter
        def x(self, value):
            self.show.x = value

        @property
        def y(self):
            return self.show.y
        @y.setter
        def y(self, value):
            self.show.y = value

    def sprites_update(st):
        for sprite in sprites[:]:
            sprite.update()
            if sprite.x > config.screen_width:
                sprite.show.destroy()
                sprites.remove(sprite)
        return 0.05

    def sprites_event(ev, x, y, st):
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_1 or ev.key == pygame.K_2 or ev.key == pygame.K_3 or ev.key == pygame.K_4:
                hit = False
                for sprite in sprites[:]:
                    if sprite.moving and (ev.key == pygame.K_1 and sprite.y == 265 or ev.key == pygame.K_2 and sprite.y == 415 or ev.key == pygame.K_3 and sprite.y == 565 or ev.key == pygame.K_4 and sprite.y == 715):
                        if int(sprite.x) in store.targets:
                            store.health = min(store.health + 2, 100)
                            hit = True
                            # We destroy the sprite, making it impossible to it twice :)
                            sprite.show.destroy()
                            sprites.remove(sprite)
                            break
                if not hit:
                    store.health = max(store.health - 10, 0)
                renpy.restart_interaction()

screen show_vars:
    bar:
        value health
        range 100
        xalign 0.5

    text "1":
        pos (1300, 315)
        align (0.5, 0.5)
    text "2":
        pos (1300, 465)
        align (0.5, 0.5)
    text "3":
        pos (1300, 615)
        align (0.5, 0.5)
    text "4":
        pos (1300, 765)
        align (0.5, 0.5)

label elevator:
    scene bg elevator
    python:
        have_map = False
        difficulty = 10 + difficulty * 3
        health = 100
        t = time.time()
        manager = SpriteManager(update=sprites_update, event=sprites_event)
        targets = set(1300+i for i in xrange(-85, 85))
        sprites = [
            RhythmD(Image("/images/elevator/enemy.png"), difficulty, 0, 265),
            RhythmD(Image("/images/elevator/enemy.png"), difficulty, 1, 415),
            RhythmD(Image("/images/elevator/enemy.png"), difficulty, 2, 565),
            RhythmD(Image("/images/elevator/enemy.png"), difficulty, 3, 715)
        ]

        renpy.show_screen("show_vars")
        renpy.show("_", what=manager, zorder=1)

    while True:
        $ result = ui.interact()
