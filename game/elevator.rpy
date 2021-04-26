# plagiarized with love from xela @ https://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=29439#p348727

init python:
    config.screen_width=1920
    config.screen_height=1080
    import time
    import pygame

    class Note(object):
        def __init__(self, sprite, speed, delay, ypos=0):
            self.sprite = sprite
            self.speed = speed
            self.delay = delay
            self.show = manager.create(sprite)
            self.show.x = -100
            self.show.y = ypos
            self.moving = False

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

    class Player(object):
        def __init__(self):
            self.sprite = Image("/images/elevator/player.png")
            self.show = manager.create(Image("/images/elevator/player.png"))
            self.show.x = 1250
            self.show.y = 350

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
                update_health(-10)
                sprite.show.destroy()
                sprites.remove(sprite)
                renpy.restart_interaction()

        if time.time() - store.t >= 10:
            store.song_over = True
            renpy.timeout(0)

        return 0.05

    def sprites_event(ev, x, y, st):
        if ev.type == pygame.KEYDOWN and ev.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
            player.show.destroy()
            player.show = manager.create(Image("/images/elevator/player_punch.png"))
            player.x = 950
            if ev.key == pygame.K_1:
                player.y = -35
            elif ev.key == pygame.K_2:
                player.y = 115
            elif ev.key == pygame.K_3:
                player.y = 265
            elif ev.key == pygame.K_4:
                player.y = 415

            hit = False
            for sprite in sprites[:]:
                if sprite.moving and (ev.key == pygame.K_1 and sprite.y == 265 or ev.key == pygame.K_2 and sprite.y == 415 or ev.key == pygame.K_3 and sprite.y == 565 or ev.key == pygame.K_4 and sprite.y == 715) and int(sprite.x) in store.targets:
                    update_health(2)
                    hit = True
                    sprite.show.destroy()
                    sprites.remove(sprite)
                    break
            if not hit:
                update_health(-10)
            renpy.restart_interaction()
        elif ev.type == pygame.KEYUP:
            if ev.key == pygame.K_0: # debug skip
                store.song_over = True

            player.show.destroy()
            player.show = manager.create(Image("/images/elevator/player.png"))
            player.x = 1250
            player.y = 350
            renpy.restart_interaction()

        if store.song_over:
            renpy.hide_screen("health")
            quick_menu = True # doesn't work
            return True
        else:
            raise renpy.IgnoreEvent()

    def update_health(amount):
        store.health = min(store.health + amount, 100)
        if store.health <= 0:
            renpy.hide_screen("health")
            quick_menu = True # doesn't work
            renpy.jump("gameOver")

screen health:
    bar:
        value health
        range 100
        xalign 0.5

label elevator:
    scene bg elevator
    python:
        quick_menu = False
        difficulty = 10 + difficulty * 3
        health = 100
        t = time.time()
        song_over = False
        manager = SpriteManager(update=sprites_update, event=sprites_event)
        targets = set(1300+i for i in xrange(-85, 85))
        sprites = [
            Note(Image("/images/elevator/enemy.png"), difficulty, 0, 265),
            Note(Image("/images/elevator/enemy.png"), difficulty, 1, 415),
            Note(Image("/images/elevator/enemy.png"), difficulty, 2, 565),
            Note(Image("/images/elevator/enemy.png"), difficulty, 3, 715)
        ]
        player = Player()

        renpy.show_screen("health")
        renpy.show("_", what=manager, zorder=1)

    $ ui.interact()
