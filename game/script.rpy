label start:
    "Part I: The Exposition"
    "You got run over by a truck hauling $300,000 of stolen/smuggled MVidiot RTA6900 graphics cards. You find yourself in purgatory facing the Clerk of Learning and Information for Perpetual Pergatorial Imprisonment."
    clippy "NEXT!"

    # fade from black
    show mc normal
    "wha..."
    "*where the hell am I?*"
    "*why does it look like I'm in the backrooms?*"
    clippy "c'mon dude, my shift's supposed to end in five minutes, and I gotta get home to watch Desperate Housewives"

    python:
        pname = renpy.input("so hurry it up and tell me your name").strip()

    clippy "alright [pname], looks like you got creamed by a truck"
    mc "wha..."
    clippy "*sigh* isn't it obvious?"
    clippy "YOU ARE DEAD."
    mc "whaaaaaaaaaaaaaaaaaaa-"
    clippy "WILL YOU STOP THAT?"
    clippy "*sigh*"
    clippy "you're in purgatory, for now at least"
    clippy "we gotta figure out if you're fit to go meet the big man in the sky or not"
    mc "and how do we figure that out?"
    clippy "well, we're just gonna wait around until you do something that's either heaven-worthy or hell-worthy"
    mc "okay..."

    label toShitOrNotToShit:
        menu:
            "well, do something!"

            "take a shit on his desk":
                pass

            "don't take a shit on his desk":
                clippy "come on now, I haven't got all day"
                jump toShitOrNotToShit

    # Lust
    # Intro
    # Event
    # Crime

    # Gluttony
    # Intro
    # Event
    # Crime

    # Greed
    # Intro
    # Event
    # Crime

    # Wrath
    # Intro
    # Event
    # Crime

    # Heresy
    # Intro
    # Event
    # Crime

    # Violence
    # Intro
    # Event
    # Crime

    # Fraud
    # Intro
    # Event
    # Crime

    # Treachery
    # Path A: Kill Satan
    # Path B: Kill God
    # Path C: Lose the game

    return
