label start:
    "Part I: The Exposition"
    "You got run over by a truck hauling $300,000 of stolen/smuggled MVidiot RTA6900 graphics cards. You find yourself in purgatory facing a BORED PURGATORY OFFICE CLERK."
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

    return
