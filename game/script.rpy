﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Soldier")
define i = Character(what_italic = True)
define y = Character("Young Woman")
define v = Character("Villager")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show girl neutral

    # These display lines of dialogue.

    "The Young Woman struggles to place the Soldier's supper on the table"

    menu:
        "Are you single?":

            jump choice1

        "...":

            jump choice1
    label choice1:
        y "..."

    "You've forgotten how incompetent you are with women and think you should shut up now and accept your fate as being some sort of sacrificial lamb for this village."

    return
