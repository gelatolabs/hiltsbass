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
            self.show.x = -150
            if note == 1:
                self.show.y = 252
            elif note == 2:
                self.show.y = 396
            elif note == 3:
                self.show.y = 540
            elif note == 4:
                self.show.y = 677
            self.moving = False

        def update(self, time):
            d = (self.delay - time) * store.speed
            if d <= 1229:
                self.moving = True
                self.x = 1229 - d
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
            self.sprite = Image("/images/mc/normal.png")
            self.show = manager.create(Image("/images/mc/normal.png"))
            self.show.x = 1200
            self.show.y = 170

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
            player.x = 1229
            if ev.key in [pygame.K_1, pygame.K_KP1]:
                player.y = 252
            elif ev.key in [pygame.K_2, pygame.K_KP2]:
                player.y = 396
            elif ev.key in [pygame.K_3, pygame.K_KP3]:
                player.y = 540
            elif ev.key in [pygame.K_4, pygame.K_KP4]:
                player.y = 677

            hit = False
            for sprite in sprites[:]:
                if sprite.moving and (ev.key in [pygame.K_1, pygame.K_KP1] and sprite.y == 252 or ev.key in [pygame.K_2, pygame.K_KP2] and sprite.y == 396 or ev.key in [pygame.K_3, pygame.K_KP3] and sprite.y == 540 or ev.key in [pygame.K_4, pygame.K_KP4] and sprite.y == 677) and int(sprite.x) in store.targets:
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
            player.show = manager.create(Image("/images/mc/normal.png"))
            player.x = 1200
            player.y = 170
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
        xalign 0.8

label elevator:
    scene bg elevator
    python:
        quick_menu = False
        health = 100
        start = datetime.utcnow()
        song_over = False
        manager = SpriteManager(update=sprites_update, event=sprites_event)
        player = Player()
        targets = set(1229+i for i in xrange(-300, 300))

        if level == 1:
            duration = 69700 # song ends after 60000ms
            speed = 0.8 # cosmetic: notes move 1px/ms
            sprites = [
                Note(2229, 1),
                Note(4341, 2),
                Note(6570, 3),
                Note(8704, 4),
                Note(15264, 1),
                Note(16512, 3),
                Note(17514, 1),
                Note(19690, 3),
                Note(21866, 1),
                Note(26250, 4),
                Note(27370, 1),
                Note(28458, 2),
                Note(29493, 3),
                Note(30592, 4),
                Note(34912, 4),
                Note(36032, 3),
                Note(37120, 2),
                Note(38229, 1),
                Note(43669, 1),
                Note(44789, 2),
                Note(45866, 1),
                Note(46976, 2),
                Note(54037, 4),
                Note(56224, 4),
                Note(61130, 2),
                Note(62229, 4),
                Note(63317, 2),
                Note(64394, 4)
            ]
        elif level == 2:
            duration = 69700
            speed = 0.8
            sprites = [
                Note(2186, 1),
                Note(4341, 2),
                Note(6538, 3),
                Note(8714, 4),
                Note(10922, 1),
                Note(13088, 4),
                Note(17450, 2),
                Note(18581, 3),
                Note(19146, 3),
                Note(20757, 1),
                Note(21312, 1),
                Note(22965, 4),
                Note(23456, 4),
                Note(25120, 3),
                Note(25674, 3),
                Note(26250, 2),
                Note(27349, 3),
                Note(28448, 2),
                Note(29493, 1),
                Note(34997, 4),
                Note(36085, 3),
                Note(37152, 4),
                Note(38261, 1),
                Note(38784, 2),
                Note(43690, 1),
                Note(44778, 2),
                Note(45866, 3),
                Note(46976, 4),
                Note(52384, 1),
                Note(53493, 3),
                Note(54058, 4),
                Note(56768, 2),
                Note(57866, 3),
                Note(58421, 4),
                Note(61141, 1),
                Note(62229, 2),
                Note(63317, 3),
                Note(64405, 4)
            ]
        elif level == 3:
            duration = 64000
            speed = 0.8
            sprites = [
                Note(8021, 1),
                Note(10016, 2),
                Note(12021, 3),
                Note(16032, 1),
                Note(17568, 2),
                Note(18997, 1),
                Note(19226, 2),
                Note(19493, 3),
                Note(19813, 4),
                Note(20416, 2),
                Note(21530, 2),
                Note(23013, 3),
                Note(23274, 2),
                Note(23792, 2),
                Note(24544, 2),
                Note(25029, 3),
                Note(25541, 4),
                Note(26042, 4),
                Note(26533, 3),
                Note(27034, 2),
                Note(27562, 1),
                Note(32037, 3),
                Note(33045, 4),
                Note(34080, 3),
                Note(35088 , 1),
                Note(40032, 2),
                Note(41034, 1),
                Note(42037, 4),
                Note(43082, 3),
                Note(44042, 1),
                Note(44384, 2),
                Note(44757, 3),
                Note(45077, 1),
                Note(48042, 1),
                Note(49536, 4),
                Note(50026, 1),
                Note(51520, 4),
                Note(52032, 1),
                Note(53546, 4),
                Note(56042, 1),
                Note(57077, 2),
                Note(58048, 3),
                Note(59040, 4)
            ]
        elif level == 4:
            duration = 64000
            speed = 0.8
            sprites = [
                Note(8021, 1),
                Note(10016, 2),
                Note(12021, 3),
                Note(16032, 1),
                Note(17568, 2),
                Note(19483, 2),
                Note(21516, 2),
                Note(23013, 3),
                Note(23274, 2),
                Note(23536, 1),
                Note(23792, 2),
                Note(24032, 1),
                Note(24544, 2),
                Note(25029, 3),
                Note(25541, 4),
                Note(26042, 4),
                Note(26533, 3),
                Note(27034, 2),
                Note(27562, 1),
                Note(29516, 3),
                Note(32037, 3),
                Note(32516, 2),
                Note(33045, 4),
                Note(33500, 2),
                Note(34080, 3),
                Note(34516, 2),
                Note(35088, 1),
                Note(23274, 2),
                Note(40032, 2),
                Note(40500, 2),
                Note(41034, 1),
                Note(41500, 1),
                Note(42037, 4),
                Note(42516, 4),
                Note(43082, 3),
                Note(43483, 3),
                Note(44042, 1),
                Note(44384, 2),
                Note(44757, 3),
                Note(45077, 1),
                Note(48042, 1),
                Note(49536, 4),
                Note(50026, 1),
                Note(51520, 4),
                Note(52032, 1),
                Note(53546, 4),
                Note(56042, 1),
                Note(57077, 2),
                Note(58048, 3),
                Note(59040, 4)
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
            duration = 61000
            speed = 1.0
            sprites = [
                Note(1933, 1),
                Note(3883, 2),
                Note(5750, 3),
                Note(15383, 1),
                Note(15833, 2),
                Note(16100, 2),
                Note(16566, 1),
                Note(16983, 2),
                Note(17300, 3),
                Note(17766, 4),
                Note(18050, 4),
                Note(19233, 1),
                Note(19683, 3),
                Note(19966, 3),
                Note(21166, 2),
                Note(21650, 4),
                Note(21866, 4),
                Note(22833, 1),
                Note(23283, 1),
                Note(23616, 2),
                Note(24083, 3),
                Note(24466, 4),
                Note(25216, 1),
                Note(25516, 2),
                Note(25966, 3),
                Note(26400, 4),
                Note(27150, 2),
                Note(29066, 1),
                Note(30816, 1),
                Note(31216, 2),
                Note(31750, 3),
                Note(32166, 3),
                Note(34550, 2),
                Note(35616, 3),
                Note(36466, 2),
                Note(37450, 4),
                Note(38683, 2),
                Note(39033, 2),
                Note(40583, 1),
                Note(40983, 2),
                Note(42500, 1),
                Note(42866, 2),
                Note(43316, 1),
                Note(43950, 3),
                Note(44416, 1),
                Note(44733, 2),
                Note(45150, 4),
                Note(45600, 4),
                Note(45900, 3),
                Note(53750, 1),
                Note(54250, 2),
                Note(54700, 3),
                Note(55183, 4),
                Note(55733, 4),
                Note(56233, 3),
                Note(56650, 2),
                Note(57133, 1)
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
            duration = 56888
            speed = 1.0
            sprites = [
                Note(7111, 1),
                Note(10666, 2),
                Note(14208, 1),
                Note(14666, 2),
                Note(15114, 1),
                Note(15552, 2),
                Note(15989, 3),
                Note(16437, 4),
                Note(16885, 3),
                Note(17322, 4),
                Note(17777, 1),
                Note(17984, 2),
                Note(18229, 1),
                Note(18464, 2),
                Note(18666, 1),
                Note(18901, 1),
                Note(19125, 1),
                Note(19370, 2),
                Note(19552, 1),
                Note(19808, 2),
                Note(20000, 3),
                Note(20234, 4),
                Note(20448, 1),
                Note(20661, 2),
                Note(20885, 3),
                Note(21109, 4),
                Note(21333, 1),
                Note(21770, 2),
                Note(22218, 1),
                Note(22666, 4),
                Note(23114, 1),
                Note(23562, 2),
                Note(24000, 1),
                Note(24437, 1),
                Note(24885, 1),
                Note(25120, 2),
                Note(25333, 3),
                Note(25578, 4),
                Note(25792, 4),
                Note(26016, 3),
                Note(26208, 2),
                Note(26453, 1),
                Note(28437, 4),
                Note(30208, 4),
                Note(23000, 2),
                Note(33792, 2),
                Note(35555, 3),
                Note(35904, 3),
                Note(36266, 2),
                Note(36896, 3),
                Note(37216, 4),
                Note(37589, 4),
                Note(38240, 4),
                Note(38485, 3),
                Note(38666, 2),
                Note(38933, 1),
                Note(40444, 1),
                Note(41770, 2),
                Note(41952, 3),
                Note(42229, 4),
                Note(42517, 1),
                Note(42677, 1),
                Note(43125, 2),
                Note(43555, 1),
                Note(44000, 2),
                Note(44444, 1),
                Note(44888, 2),
                Note(45333, 3),
                Note(45777, 4),
                Note(46222, 3),
                Note(46666, 4),
                Note(47111, 3),
                Note(47555, 4),
                Note(48000, 1),
                Note(48444, 2),
                Note(48888, 3),
                Note(49333, 4),
                Note(49777, 1)
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

        renpy.music.play("/sound/elevator/" + str(level) + ".ogg", loop=False)
        renpy.show_screen("health")
        renpy.show("_", what=manager, zorder=1)
        ui.interact()
