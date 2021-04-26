# plagiarized with love from xela @ https://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=29439#p348727

init python:
    config.screen_width=1920
    config.screen_height=1080
    from datetime import datetime
    import pygame

    class Note(object):
        def __init__(self, delay, note):
            self.sprite = Image("/images/elevator/enemy.png")
            self.delay = delay
            self.show = manager.create(Image("/images/elevator/enemy.png"))
            self.show.x = -100
            self.show.y = 115 + note * 150
            self.moving = False

        def update(self, time):
            d = (self.delay - time) * store.speed
            if d <= 1300:
                self.moving = True
                self.x = 1300 - d
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
            self.show.x = 1575
            self.show.y = 675

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
        time = int((datetime.utcnow() - store.start).total_seconds() * 1000.0)
        for sprite in sprites[:]:
            sprite.update(time)
            if sprite.x > config.screen_width:
                update_health(-10)
                sprite.show.destroy()
                sprites.remove(sprite)
                renpy.restart_interaction()

        if time > store.duration:
            store.song_over = True
            renpy.timeout(0)

        return 0.05

    def sprites_event(ev, x, y, st):
        if ev.type == pygame.KEYDOWN and ev.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4]:
            player.show.destroy()
            player.show = manager.create(Image("/images/elevator/player_punch.png"))
            player.x = 1275
            if ev.key == pygame.K_1 or ev.key == pygame.K_KP1:
                player.y = 290
            elif ev.key == pygame.K_2 or ev.key == pygame.K_KP2:
                player.y = 440
            elif ev.key == pygame.K_3 or ev.key == pygame.K_KP3:
                player.y = 590
            elif ev.key == pygame.K_4 or ev.key == pygame.K_KP4:
                player.y = 740

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
            player.x = 1575
            player.y = 675
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
        health = 100
        start = datetime.utcnow()
        song_over = False
        manager = SpriteManager(update=sprites_update, event=sprites_event)
        player = Player()
        targets = set(1300+i for i in xrange(-85, 85))

        if level == 1:
            duration = 60000 # song ends after 60000ms
            speed = 1.0 # cosmetic: notes move 1px/ms
            sprites = [
                Note(1234, 1),
                Note(2345, 2),
                Note(3456, 3),
                Note(4567, 4)
            ]
        elif level == 2:
            duration = 60000
            speed = 1.0
            sprites = [
                Note(1234, 1),
                Note(2345, 2),
                Note(3456, 3),
                Note(4567, 4)
            ]
        elif level == 3:
            duration = 60000
            speed = 1.0
            sprites = [
                Note(1234, 1),
                Note(2345, 2),
                Note(3456, 3),
                Note(4567, 4)
            ]
        elif level == 4:
            duration = 60000
            speed = 1.0
            sprites = [
                Note(1234, 1),
                Note(2345, 2),
                Note(3456, 3),
                Note(4567, 4)
            ]
        elif level == 5:
            duration = 60000
            speed = 1.0
            sprites = [
                Note(1234, 1),
                Note(2345, 2),
                Note(3456, 3),
                Note(4567, 4)
            ]
        elif level == 6:
            duration = 60000
            speed = 1.0
            sprites = [
                Note(1234, 1),
                Note(2345, 2),
                Note(3456, 3),
                Note(4567, 4)
            ]
        elif level == 7:
            duration = 60000
            speed = 1.0
            sprites = [
                Note(1234, 1),
                Note(2345, 2),
                Note(3456, 3),
                Note(4567, 4)
            ]
        elif level == 8:
            duration = 60000
            speed = 1.0
            sprites = [
                Note(1234, 1),
                Note(2345, 2),
                Note(3456, 3),
                Note(4567, 4)
            ]
        elif level == 9:
            duration = 60000
            speed = 1.0
            sprites = [
                Note(1234, 1),
                Note(2345, 2),
                Note(3456, 3),
                Note(4567, 4)
            ]
        elif level == satan:
            duration = 60000
            speed = 1.0
            sprites = [
                Note(1234, 1),
                Note(2345, 2),
                Note(3456, 3),
                Note(4567, 4)
            ]
        elif level == god:
            duration = 60000
            speed = 1.0
            sprites = [
                Note(1234, 1),
                Note(2345, 2),
                Note(3456, 3),
                Note(4567, 4)
            ]

        renpy.music.play("/sound/elevator/" + str(level) + ".mp3", loop=False)
        renpy.show_screen("health")
        renpy.show("_", what=manager, zorder=1)
        ui.interact()
