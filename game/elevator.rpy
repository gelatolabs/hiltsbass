init python:
    config.screen_width=1920
    config.screen_height=1080
    import time
    import pygame
    MOUSEBUTTONDOWN=pygame.MOUSEBUTTONDOWN

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
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 1:
                hit = False
                for sprite in sprites[:]:
                    if sprite.moving:
                        if int(sprite.x) in store.targets:
                            store.hits += 1
                            hit = True
                            # We destroy the sprite, making it impossible to it twice :)
                            sprite.show.destroy()
                            sprites.remove(sprite)
                            break
                if not hit:
                    store.misses += 1
                renpy.restart_interaction()

screen show_vars:
    text "Misses: [misses], Hits: [hits]!" xalign 0.5
    text "A":
        pos (1300, 315)
    text "S":
        pos (1300, 465)
    text "D":
        pos (1300, 615)
    text "F":
        pos (1300, 765)

label elevator:
    scene bg elevator
    python:
        have_map = False
        difficulty = difficulty + 10
        hits = 0
        misses = 0
        t = time.time()
        manager = SpriteManager(update=sprites_update, event=sprites_event)
        targets = set(1300+i for i in xrange(-60, 60))
        sprites = [
            RhythmD(Image("/images/elevator/enemy.png"), difficulty, 0, 315),
            RhythmD(Image("/images/elevator/enemy.png"), difficulty, 1, 465),
            RhythmD(Image("/images/elevator/enemy.png"), difficulty, 2, 615),
            RhythmD(Image("/images/elevator/enemy.png"), difficulty, 3, 765)
        ]

        renpy.show_screen("show_vars")
        renpy.show("_", what=manager, zorder=1)

    while True:
        $ result = ui.interact()
