label venus_BB:

    init python:
        import random

    $ d2unplayed = True
    $ d3unplayed = True
    $ d4unplayed = True
    $ d5unplayed = True
    $ d6unplayed = True
    $ d7unplayed = True
    $ d8unplayed = True
    $ d9unplayed = True
    $ d10unplayed = True
    $ djunplayed = True
    $ dqunplayed = True
    $ dkunplayed = True
    $ daunplayed = True

    play sound "fx/riffle.ogg"

    scene black with dissolvemed
    $ renpy.pause (0.5)
    scene table

    #shows the player's hand
    show 2d at Position (xpos = 120, xanchor = "center", ypos = 0.95, yanchor = 0.4)
    show 3d at Position (xpos = 260, xanchor = "center", ypos = 0.95, yanchor = 0.4)
    show 4d at Position (xpos = 400, xanchor = "center", ypos = 0.95, yanchor = 0.4)
    show 5d at Position (xpos = 540, xanchor = "center", ypos = 0.95, yanchor = 0.4)
    show 6d at Position (xpos = 680, xanchor = "center", ypos = 0.95, yanchor = 0.4)
    show 7d at Position (xpos = 820, xanchor = "center", ypos = 0.95, yanchor = 0.4)
    show 8d at Position (xpos = 960, xanchor = "center", ypos = 0.95, yanchor = 0.4)
    show 9d at Position (xpos = 1100, xanchor = "center", ypos = 0.95, yanchor = 0.4)
    show 10d at Position (xpos = 1240, xanchor = "center", ypos = 0.95, yanchor = 0.4)
    show jd at Position (xpos = 1380, xanchor = "center", ypos = 0.95, yanchor = 0.4)
    show qd at Position (xpos = 1520, xanchor = "center", ypos = 0.95, yanchor = 0.4)
    show kd at Position (xpos = 1660, xanchor = "center", ypos = 0.95, yanchor = 0.4)
    show ad at Position (xpos = 1800, xanchor = "center", ypos = 0.95, yanchor = 0.4)

    #shows the opponent's hand
    show back2 at Position (xpos = 120, xanchor = "center", ypos = 1, yanchor = 0.4)
    show back3 at Position (xpos = 260, xanchor = "center", ypos = 1, yanchor = 0.4)
    show back4 at Position (xpos = 400, xanchor = "center", ypos = 1, yanchor = 0.4)
    show back5 at Position (xpos = 540, xanchor = "center", ypos = 1, yanchor = 0.4)
    show back6 at Position (xpos = 680, xanchor = "center", ypos = 1, yanchor = 0.4)
    show back7 at Position (xpos = 820, xanchor = "center", ypos = 1, yanchor = 0.4)
    show back8 at Position (xpos = 960, xanchor = "center", ypos = 1, yanchor = 0.4)
    show back9 at Position (xpos = 1100, xanchor = "center", ypos = 1, yanchor = 0.4)
    show back10 at Position (xpos = 1240, xanchor = "center", ypos = 1, yanchor = 0.4)
    show backj at Position (xpos = 1380, xanchor = "center", ypos = 1, yanchor = 0.4)
    show backq at Position (xpos = 1520, xanchor = "center", ypos = 1, yanchor = 0.4)
    show backk at Position (xpos = 1660, xanchor = "center", ypos = 1, yanchor = 0.4)
    show backa at Position (xpos = 1800, xanchor = "center", ypos = 1, yanchor = 0.4)

    #shows the middle row
    $ card_positions = [
        (120, "center", 540, 0.5),
        (260, "center", 0.5, 0.5),
        (400, "center", 0.5, 0.5),
        (540, "center", 0.5, 0.5),
        (680, "center", 0.5, 0.5),
        (820, "center", 0.5, 0.5),
        (960, "center", 0.5, 0.5),
        (1100, "center", 0.5, 0.5),
        (1240, "center", 0.5, 0.5),
        (1380, "center", 0.5, 0.5),
        (1520, "center", 0.5, 0.5),
        (1660, "center", 0.5, 0.5),
        (1800, "center", 0.5, 0.5)
    ]

    # $ random.shuffle(card_positions)

    $ xpos, xanchor, ypos, yanchor = card_positions[0]
    show 2c at Position (xpos = xpos, xanchor = xanchor, ypos = ypos, yanchor = yanchor)

    $ xpos, xanchor, ypos, yanchor = card_positions[1]
    show 3c at Position (xpos = xpos, xanchor = xanchor, ypos = ypos, yanchor = yanchor)

    $ xpos, xanchor, ypos, yanchor = card_positions[2]
    show 4c at Position (xpos = xpos, xanchor = xanchor, ypos = ypos, yanchor = yanchor)

    $ xpos, xanchor, ypos, yanchor = card_positions[3]
    show 5c at Position (xpos = xpos, xanchor = xanchor, ypos = ypos, yanchor = yanchor)

    $ xpos, xanchor, ypos, yanchor = card_positions[4]
    show 6c at Position (xpos = xpos, xanchor = xanchor, ypos = ypos, yanchor = yanchor)

    $ xpos, xanchor, ypos, yanchor = card_positions[5]
    show 7c at Position (xpos = xpos, xanchor = xanchor, ypos = ypos, yanchor = yanchor)

    $ xpos, xanchor, ypos, yanchor = card_positions[6]
    show 8c at Position (xpos = xpos, xanchor = xanchor, ypos = ypos, yanchor = yanchor)

    $ xpos, xanchor, ypos, yanchor = card_positions[7]
    show 9c at Position (xpos = xpos, xanchor = xanchor, ypos = ypos, yanchor = yanchor)

    $ xpos, xanchor, ypos, yanchor = card_positions[8]
    show 10c at Position (xpos = xpos, xanchor = xanchor, ypos = ypos, yanchor = yanchor)

    $ xpos, xanchor, ypos, yanchor = card_positions[9]
    show jc at Position (xpos = xpos, xanchor = xanchor, ypos = ypos, yanchor = yanchor)

    $ xpos, xanchor, ypos, yanchor = card_positions[10]
    show qc at Position (xpos = xpos, xanchor = xanchor, ypos = ypos, yanchor = yanchor)

    $ xpos, xanchor, ypos, yanchor = card_positions[11]
    show kc at Position (xpos = xpos, xanchor = xanchor, ypos = ypos, yanchor = yanchor)

    $ xpos, xanchor, ypos, yanchor = card_positions[12]
    show ac at Position (xpos = xpos, xanchor = xanchor, ypos = ypos, yanchor = yanchor)

    with dissolvemed

    label venus_sebgamestart:

    stop music fadeout 1.0

    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb1 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (2.0)

    hide eyesseb
    hide roundb1
    with dissolvemed


    $ mcpoints = 0
    $ sebpoints = 0
    $ pointsthisround = 1

    play music "mx/chronos.ogg"

    $ cards = [
        {"image": "2d", "hovered": "se/sounds/select.ogg", "clicked": "se/sounds/select3.ogg", "value": "2", "xpos": 120},
        {"image": "3d", "hovered": "se/sounds/select.ogg", "clicked": "se/sounds/select3.ogg", "value": "3", "xpos": 260},
        {"image": "4d", "hovered": "se/sounds/select.ogg", "clicked": "se/sounds/select3.ogg", "value": "4", "xpos": 400},
        {"image": "5d", "hovered": "se/sounds/select.ogg", "clicked": "se/sounds/select3.ogg", "value": "5", "xpos": 540},
        {"image": "6d", "hovered": "se/sounds/select.ogg", "clicked": "se/sounds/select3.ogg", "value": "6", "xpos": 680},
        {"image": "7d", "hovered": "se/sounds/select.ogg", "clicked": "se/sounds/select3.ogg", "value": "7", "xpos": 820},
        {"image": "8d", "hovered": "se/sounds/select.ogg", "clicked": "se/sounds/select3.ogg", "value": "8", "xpos": 960},
        {"image": "9d", "hovered": "se/sounds/select.ogg", "clicked": "se/sounds/select3.ogg", "value": "9", "xpos": 1100},
        {"image": "10d", "hovered": "se/sounds/select.ogg", "clicked": "se/sounds/select3.ogg", "value": "10", "xpos": 1240},
        {"image": "jd", "hovered": "se/sounds/select.ogg", "clicked": "se/sounds/select3.ogg", "value": "j", "xpos": 1380},
        {"image": "qd", "hovered": "se/sounds/select.ogg", "clicked": "se/sounds/select3.ogg", "value": "q", "xpos": 1520},
        {"image": "kd", "hovered": "se/sounds/select.ogg", "clicked": "se/sounds/select3.ogg", "value": "k", "xpos": 1660},
        {"image": "ad", "hovered": "se/sounds/select.ogg", "clicked": "se/sounds/select3.ogg", "value": "a", "xpos": 1800}
    ]

    python:
        def displayCards():
            for card in cards:
                if eval("d" + card['value'] + "unplayed"):
                    renpy.ui.imagebutton("pc/" + card['image'] + ".png", "pc/" + card['image'] + "h.png", clicked=[ui.returns(card['value']), Play("audio", card['clicked'])], xpos=card['xpos'], xanchor="center", ypos=0.95, yanchor=0.4, hovered=Play("audio", card['hovered']))

    $ displayCards()

    $ userSelection = ui.interact()

    if userSelection == "2":

        hide 2d
        hide back2
        with dissolve
        show 2d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "tie"

    if userSelection == "3":

        hide 3d
        hide back2
        with dissolve
        show 3d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "tie"

    if userSelection == "4":

        hide 4d
        hide back2
        with dissolve
        show 4d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "tie"

    if userSelection == "5":

        hide 5d
        hide back2
        with dissolve
        show 5d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "tie"

    if userSelection == "6":

        hide 6d
        hide back2
        with dissolve
        show 6d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "win"

    if userSelection == "7":

        hide 7d
        hide back2
        with dissolve
        show 7d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "win"

    if userSelection == "8":

        hide 8d
        hide back2
        with dissolve
        show 8d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "win"

    if userSelection == "9":

        hide 9d
        hide back2
        with dissolve
        show 9d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "win"

    if userSelection == "10":

        hide 10d
        hide back2
        with dissolve
        show 10d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "win"

    if userSelection == "j":

        hide jd
        hide back2
        with dissolve
        show jd at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "win"

    if userSelection == "q":

        hide qd
        hide back2
        with dissolve
        show qd at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "win"

    if userSelection == "k":

        hide kd
        hide back2
        with dissolve
        show kd at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "win"

    if userSelection == "a":

        hide ad
        hide back2
        with dissolve
        show ad at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ daunplayed = False

        $ roundresult = "tie"

    if roundresult == "win":
        play sound "fx/win.ogg"
        show win1 at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show lose1 at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ mcpoints += pointsthisround
        $ pointsthisround = 1

    elif roundresult == "tie":
        play sound "fx/tie.ogg"
        show tie1 at Position (xpos = 120, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1

    else:
        play sound "fx/lose.ogg"
        show lose1 at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show win1 at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ sebpoints += pointsthisround
        $ pointsthisround = 1

    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb2 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb2
    with dissolvemed

    $ displayCards()

    $ userSelection = ui.interact()

    if userSelection == "2":

        hide 2d
        hide back3
        with dissolve
        show 2d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "tie"

    if userSelection == "3":

        hide 3d
        hide back3
        with dissolve
        show 3d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "tie"

    if userSelection == "4":

        hide 4d
        hide back3
        with dissolve
        show 4d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "tie"

    if userSelection == "5":

        hide 5d
        hide back3
        with dissolve
        show 5d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "tie"

    if userSelection == "6":

        hide 6d
        hide back3
        with dissolve
        show 6d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "tie"

    if userSelection == "7":

        hide 7d
        hide back3
        with dissolve
        show 7d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "tie"

    if userSelection == "8":

        hide 8d
        hide back3
        with dissolve
        show 8d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "tie"

    if userSelection == "9":

        hide 9d
        hide back3
        with dissolve
        show 9d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "tie"

    if userSelection == "10":

        hide 10d
        hide back3
        with dissolve
        show 10d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "tie"

    if userSelection == "j":

        hide jd
        hide back3
        with dissolve
        show jd at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "tie"

    if userSelection == "q":

        hide qd
        hide back3
        with dissolve
        show qd at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "tie"

    if userSelection == "k":

        hide kd
        hide back3
        with dissolve
        show kd at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "tie"

    if userSelection == "a":

        hide ad
        hide back3
        with dissolve
        show ad at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ daunplayed = False

        $ roundresult = "ace"

    if roundresult == "tie":
        play sound "fx/tie.ogg"
        show tie2 at Position (xpos = 260, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1

    else:
        play sound "fx/tie.ogg"
        show tie2 at Position (xpos = 260, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1

    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb3 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb3
    with dissolvemed

    $ displayCards()

    $ userSelection = ui.interact()

    if userSelection == "2":

        hide 2d
        hide back10
        with dissolve
        show 2d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "lose"

    if userSelection == "3":

        hide 3d
        hide back10
        with dissolve
        show 3d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "lose"

    if userSelection == "4":

        hide 4d
        hide back10
        with dissolve
        show 4d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "lose"

    if userSelection == "5":

        hide 5d
        hide back10
        with dissolve
        show 5d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "lose"

    if userSelection == "6":

        hide 6d
        hide back10
        with dissolve
        show 6d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "lose"

    if userSelection == "7":

        hide 7d
        hide back10
        with dissolve
        show 7d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "lose"

    if userSelection == "8":

        hide 8d
        hide back10
        with dissolve
        show 8d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "lose"

    if userSelection == "9":

        hide 9d
        hide back10
        with dissolve
        show 9d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "lose"

    if userSelection == "10":

        hide 10d
        hide back10
        with dissolve
        show 10d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "tie"

    if userSelection == "j":

        hide jd
        hide back10
        with dissolve
        show jd at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "win"

    if userSelection == "q":

        hide qd
        hide back10
        with dissolve
        show qd at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "win"

    if userSelection == "k":

        hide kd
        hide back10
        with dissolve
        show kd at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "win"

    if userSelection == "a":

        hide ad
        hide back10
        with dissolve
        show ad at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ daunplayed = False

        $ roundresult = "lose"

    if roundresult == "win":

        play sound "fx/win.ogg"
        show win3 at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show lose3 at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ mcpoints += pointsthisround
        $ pointsthisround = 1

    elif roundresult == "tie":

        play sound "fx/tie.ogg"
        show tie3 at Position (xpos = 400, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1

    else:


        play sound "fx/lose.ogg"
        show lose3 at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show win3 at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ sebpoints += pointsthisround
        $ pointsthisround = 1

    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb4 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb4
    with dissolvemed

    $ displayCards()

    $ userSelection = ui.interact()

    if userSelection == "2":

        hide 2d
        hide backq
        with dissolve
        show 2d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "lose"

    if userSelection == "3":

        hide 3d
        hide backq
        with dissolve
        show 3d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "lose"

    if userSelection == "4":

        hide 4d
        hide backq
        with dissolve
        show 4d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "lose"

    if userSelection == "5":

        hide 5d
        hide backq
        with dissolve
        show 5d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "lose"

    if userSelection == "6":

        hide 6d
        hide backq
        with dissolve
        show 6d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "lose"

    if userSelection == "7":

        hide 7d
        hide backq
        with dissolve
        show 7d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "lose"

    if userSelection == "8":

        hide 8d
        hide backq
        with dissolve
        show 8d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "lose"

    if userSelection == "9":

        hide 9d
        hide backq
        with dissolve
        show 9d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "lose"

    if userSelection == "10":

        hide 10d
        hide backq
        with dissolve
        show 10d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "lose"

    if userSelection == "j":

        hide jd
        hide backq
        with dissolve
        show jd at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "lose"

    if userSelection == "q":

        hide qd
        hide backq
        with dissolve
        show qd at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "tie"

    if userSelection == "k":

        hide kd
        hide backq
        with dissolve
        show kd at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "win"

    if userSelection == "a":

        hide ad
        hide backq
        with dissolve
        show ad at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ daunplayed = False

        $ roundresult = "tie"

    if roundresult == "win":

        play sound "fx/win.ogg"
        show win4 at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show lose4 at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ mcpoints += pointsthisround
        $ pointsthisround = 1


    elif roundresult == "tie":

        play sound "fx/tie.ogg"
        show tie4 at Position (xpos = 540, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1
    else:

        play sound "fx/lose.ogg"
        show lose4 at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show win4 at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ sebpoints += pointsthisround
        $ pointsthisround = 1

    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb5 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb5
    with dissolvemed

    $ displayCards()

    $ userSelection = ui.interact()

    if userSelection == "2":

        hide 2d
        hide backj
        with dissolve
        show 2d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "lose"

    if userSelection == "3":

        hide 3d
        hide backj
        with dissolve
        show 3d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "lose"

    if userSelection == "4":

        hide 4d
        hide backj
        with dissolve
        show 4d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "lose"

    if userSelection == "5":

        hide 5d
        hide backj
        with dissolve
        show 5d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "lose"

    if userSelection == "6":

        hide 6d
        hide backj
        with dissolve
        show 6d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "lose"

    if userSelection == "7":

        hide 7d
        hide backj
        with dissolve
        show 7d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "lose"

    if userSelection == "8":

        hide 8d
        hide backj
        with dissolve
        show 8d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "lose"

    if userSelection == "9":

        hide 9d
        hide backj
        with dissolve
        show 9d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "lose"

    if userSelection == "10":

        hide 10d
        hide backj
        with dissolve
        show 10d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "lose"

    if userSelection == "j":

        hide jd
        hide backj
        with dissolve
        show jd at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "tie"

    if userSelection == "q":

        hide qd
        hide backj
        with dissolve
        show qd at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "win"

    if userSelection == "k":

        hide kd
        hide backj
        with dissolve
        show kd at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "win"

    if userSelection == "a":

        hide ad
        hide backj
        with dissolve
        show ad at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ daunplayed = False

        $ roundresult = "tie"

    if roundresult == "win":

        play sound "fx/win.ogg"
        show win5 at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show lose5 at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ mcpoints += pointsthisround
        $ pointsthisround = 1

    elif roundresult == "tie":

        play sound "fx/tie.ogg"
        show tie5 at Position (xpos = 680, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1

    else:


        play sound "fx/lose.ogg"
        show lose5 at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show win5 at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ sebpoints += pointsthisround
        $ pointsthisround = 1


    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb6 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb6
    with dissolvemed

    $ displayCards()

    $ userSelection = ui.interact()

    if userSelection == "2":

        hide 2d
        hide back9
        with dissolve
        show 2d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "lose"

    if userSelection == "3":

        hide 3d
        hide back9
        with dissolve
        show 3d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "lose"

    if userSelection == "4":

        hide 4d
        hide back9
        with dissolve
        show 4d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "lose"

    if userSelection == "5":

        hide 5d
        hide back9
        with dissolve
        show 5d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "lose"

    if userSelection == "6":

        hide 6d
        hide back9
        with dissolve
        show 6d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "lose"

    if userSelection == "7":

        hide 7d
        hide back9
        with dissolve
        show 7d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "lose"

    if userSelection == "8":

        hide 8d
        hide back9
        with dissolve
        show 8d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "lose"

    if userSelection == "9":

        hide 9d
        hide back9
        with dissolve
        show 9d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "tie"

    if userSelection == "10":

        hide 10d
        hide back9
        with dissolve
        show 10d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "win"

    if userSelection == "j":

        hide jd
        hide back9
        with dissolve
        show jd at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "tie"

    if userSelection == "q":

        hide qd
        hide back9
        with dissolve
        show qd at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "tie"

    if userSelection == "k":

        hide kd
        hide back9
        with dissolve
        show kd at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "tie"

    if userSelection == "a":

        hide ad
        hide back9
        with dissolve
        show ad at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ daunplayed = False

        $ roundresult = "tie"


    if roundresult == "win":

        play sound "fx/win.ogg"
        show win6 at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show lose6 at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ mcpoints += pointsthisround
        $ pointsthisround = 1

    elif roundresult == "tie":

        play sound "fx/tie.ogg"
        show tie6 at Position (xpos = 820, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1

    else:

        play sound "fx/lose.ogg"
        show lose6 at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show win6 at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ sebpoints += pointsthisround
        $ pointsthisround = 1


    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb7 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb7
    with dissolvemed

    $ displayCards()

    $ userSelection = ui.interact()

    if userSelection == "2":

        hide 2d
        hide back4
        with dissolve
        show 2d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "tie"

    if userSelection == "3":

        hide 3d
        hide back4
        with dissolve
        show 3d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "tie"

    if userSelection == "4":

        hide 4d
        hide back4
        with dissolve
        show 4d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "tie"

    if userSelection == "5":

        hide 5d
        hide back4
        with dissolve
        show 5d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "tie"

    if userSelection == "6":

        hide 6d
        hide back4
        with dissolve
        show 6d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "tie"

    if userSelection == "7":

        hide 7d
        hide back4
        with dissolve
        show 7d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "tie"

    if userSelection == "8":

        hide 8d
        hide back4
        with dissolve
        show 8d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "tie"

    if userSelection == "9":

        hide 9d
        hide back4
        with dissolve
        show 9d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "tie"

    if userSelection == "10":

        hide 10d
        hide back4
        with dissolve
        show 10d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "tie"

    if userSelection == "j":

        hide jd
        hide back4
        with dissolve
        show jd at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "tie"

    if userSelection == "q":

        hide qd
        hide back4
        with dissolve
        show qd at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "win"

    if userSelection == "k":

        hide kd
        hide back4
        with dissolve
        show kd at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "win"

    if userSelection == "a":

        hide ad
        hide back4
        with dissolve
        show ad at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ daunplayed = False

        $ roundresult = "tie"

    if roundresult == "win":

        play sound "fx/win.ogg"
        show win7 at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show lose7 at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ mcpoints += pointsthisround
        $ pointsthisround = 1


    elif roundresult == "tie":

        play sound "fx/tie.ogg"
        show tie7 at Position (xpos = 960, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1
    else:



        play sound "fx/lose.ogg"
        show lose7 at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show win7 at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ sebpoints += pointsthisround
        $ pointsthisround = 1

    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb8 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb8
    with dissolvemed

    $ displayCards()

    $ userSelection = ui.interact()

    if userSelection == "2":

        hide 2d
        hide backa
        with dissolve
        show 2d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "tie"

    if userSelection == "3":

        hide 3d
        hide backa
        with dissolve
        show 3d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "tie"

    if userSelection == "4":

        hide 4d
        hide backa
        with dissolve
        show 4d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "tie"

    if userSelection == "5":

        hide 5d
        hide backa
        with dissolve
        show 5d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "tie"

    if userSelection == "6":

        hide 6d
        hide backa
        with dissolve
        show 6d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "tie"

    if userSelection == "7":

        hide 7d
        hide backa
        with dissolve
        show 7d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "tie"

    if userSelection == "8":

        hide 8d
        hide backa
        with dissolve
        show 8d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "tie"

    if userSelection == "9":

        hide 9d
        hide backa
        with dissolve
        show 9d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "tie"

    if userSelection == "10":

        hide 10d
        hide backa
        with dissolve
        show 10d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "tie"

    if userSelection == "j":

        hide jd
        hide backa
        with dissolve
        show jd at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "lose"

    if userSelection == "q":

        hide qd
        hide backa
        with dissolve
        show qd at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "lose"

    if userSelection == "k":

        hide kd
        hide backa
        with dissolve
        show kd at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "lose"

    if userSelection == "a":

        hide ad
        hide backa
        with dissolve
        show ad at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ daunplayed = False

        $ roundresult = "tie"

    if roundresult == "win":

        play sound "fx/win.ogg"
        show win8 at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show lose8 at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ mcpoints += pointsthisround
        $ pointsthisround = 1


    elif roundresult == "tie":

        play sound "fx/tie.ogg"
        show tie8 at Position (xpos = 1100, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1

    else:

        play sound "fx/lose.ogg"
        show lose8 at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show win8 at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ sebpoints += pointsthisround
        $ pointsthisround = 1

    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb9 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb9
    with dissolvemed

    $ displayCards()

    $ userSelection = ui.interact()

    if userSelection == "2":

        hide 2d
        hide backk
        with dissolve
        show 2d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "lose"

    if userSelection == "3":

        hide 3d
        hide backk
        with dissolve
        show 3d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "lose"

    if userSelection == "4":

        hide 4d
        hide backk
        with dissolve
        show 4d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "lose"

    if userSelection == "5":

        hide 5d
        hide backk
        with dissolve
        show 5d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "lose"

    if userSelection == "6":

        hide 6d
        hide backk
        with dissolve
        show 6d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "lose"

    if userSelection == "7":

        hide 7d
        hide backk
        with dissolve
        show 7d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "lose"

    if userSelection == "8":

        hide 8d
        hide backk
        with dissolve
        show 8d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "lose"

    if userSelection == "9":

        hide 9d
        hide backk
        with dissolve
        show 9d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "lose"

    if userSelection == "10":

        hide 10d
        hide backk
        with dissolve
        show 10d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "lose"

    if userSelection == "j":

        hide jd
        hide backk
        with dissolve
        show jd at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "lose"

    if userSelection == "q":

        hide qd
        hide backk
        with dissolve
        show qd at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "lose"

    if userSelection == "k":

        hide kd
        hide backk
        with dissolve
        show kd at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "tie"

    if userSelection == "a":

        hide ad
        hide backk
        with dissolve
        show ad at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ daunplayed = False

        $ roundresult = "tie"




    if roundresult == "win":

        play sound "fx/win.ogg"
        show win9 at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show lose9 at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ mcpoints += pointsthisround
        $ pointsthisround = 1

        Sb "Oh, well..."

    elif roundresult == "tie":

        play sound "fx/tie.ogg"
        show tie9 at Position (xpos = 1240, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1

        Sb "Oh my..."
    else:


        play sound "fx/lose.ogg"
        show lose9 at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show win9 at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ sebpoints += pointsthisround
        $ pointsthisround = 1

        Sb "Yee-haw."

    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb10 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb10
    with dissolvemed

    $ displayCards()

    $ userSelection = ui.interact()

    if userSelection == "2":

        hide 2d
        hide back8
        with dissolve
        show 2d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "lose"

    if userSelection == "3":

        hide 3d
        hide back8
        with dissolve
        show 3d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "lose"

    if userSelection == "4":

        hide 4d
        hide back8
        with dissolve
        show 4d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "lose"

    if userSelection == "5":

        hide 5d
        hide back8
        with dissolve
        show 5d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "lose"

    if userSelection == "6":

        hide 6d
        hide back8
        with dissolve
        show 6d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "lose"

    if userSelection == "7":

        hide 7d
        hide back8
        with dissolve
        show 7d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "lose"

    if userSelection == "8":

        hide 8d
        hide back8
        with dissolve
        show 8d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "tie"

    if userSelection == "9":

        hide 9d
        hide back8
        with dissolve
        show 9d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "win"

    if userSelection == "10":

        hide 10d
        hide back8
        with dissolve
        show 10d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "win"

    if userSelection == "j":

        hide jd
        hide back8
        with dissolve
        show jd at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "win"

    if userSelection == "q":

        hide qd
        hide back8
        with dissolve
        show qd at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "win"

    if userSelection == "k":

        hide kd
        hide back8
        with dissolve
        show kd at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "win"

    if userSelection == "a":

        hide ad
        hide back8
        with dissolve
        show ad at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ daunplayed = False

        $ roundresult = "lose"

    if roundresult == "win":

        play sound "fx/win.ogg"
        show win10 at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show lose10 at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ mcpoints += pointsthisround
        $ pointsthisround = 1

    elif roundresult == "tie":

        play sound "fx/tie.ogg"
        show tie10 at Position (xpos = 1380, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1

    else:


        play sound "fx/lose.ogg"
        show lose10 at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show win10 at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ sebpoints += pointsthisround
        $ pointsthisround = 1


    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb11 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb11
    with dissolvemed

    $ displayCards()

    $ userSelection = ui.interact()

    if userSelection == "2":

        hide 2d
        hide back7
        with dissolve
        show 2d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "lose"

    if userSelection == "3":

        hide 3d
        hide back7
        with dissolve
        show 3d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "lose"

    if userSelection == "4":

        hide 4d
        hide back7
        with dissolve
        show 4d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "lose"

    if userSelection == "5":

        hide 5d
        hide back7
        with dissolve
        show 5d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "lose"

    if userSelection == "6":

        hide 6d
        hide back7
        with dissolve
        show 6d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "lose"

    if userSelection == "7":

        hide 7d
        hide back7
        with dissolve
        show 7d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "tie"

    if userSelection == "8":

        hide 8d
        hide back7
        with dissolve
        show 8d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "win"

    if userSelection == "9":

        hide 9d
        hide back7
        with dissolve
        show 9d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "win"

    if userSelection == "10":

        hide 10d
        hide back7
        with dissolve
        show 10d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "win"

    if userSelection == "j":

        hide jd
        hide back7
        with dissolve
        show jd at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "win"

    if userSelection == "q":

        hide qd
        hide back7
        with dissolve
        show qd at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "win"

    if userSelection == "k":

        hide kd
        hide back7
        with dissolve
        show kd at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "win"

    if userSelection == "a":

        hide ad
        hide back7
        with dissolve
        show ad at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ daunplayed = False

        $ roundresult = "lose"


    if roundresult == "win":

        play sound "fx/win.ogg"
        show win11 at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show lose11 at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ mcpoints += pointsthisround
        $ pointsthisround = 1


    elif roundresult == "tie":

        play sound "fx/tie.ogg"
        show tie11 at Position (xpos = 1520, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1
    else:



        play sound "fx/lose.ogg"
        show lose11 at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show win11 at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ sebpoints += pointsthisround
        $ pointsthisround = 1


    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb12 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb12
    with dissolvemed

    $ displayCards()

    $ userSelection = ui.interact()

    if userSelection == "2":

        hide 2d
        hide back5
        with dissolve
        show 2d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "tie"

    if userSelection == "3":

        hide 3d
        hide back5
        with dissolve
        show 3d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "tie"

    if userSelection == "4":

        hide 4d
        hide back5
        with dissolve
        show 4d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "tie"

    if userSelection == "5":

        hide 5d
        hide back5
        with dissolve
        show 5d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "tie"

    if userSelection == "6":

        hide 6d
        hide back5
        with dissolve
        show 6d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "tie"

    if userSelection == "7":

        hide 7d
        hide back5
        with dissolve
        show 7d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "tie"

    if userSelection == "8":

        hide 8d
        hide back5
        with dissolve
        show 8d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "tie"

    if userSelection == "9":

        hide 9d
        hide back5
        with dissolve
        show 9d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "tie"

    if userSelection == "10":

        hide 10d
        hide back5
        with dissolve
        show 10d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "win"

    if userSelection == "j":

        hide jd
        hide back5
        with dissolve
        show jd at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "win"

    if userSelection == "q":

        hide qd
        hide back5
        with dissolve
        show qd at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "win"

    if userSelection == "k":

        hide kd
        hide back5
        with dissolve
        show kd at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "win"

    if userSelection == "a":

        hide ad
        hide back5
        with dissolve
        show ad at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ daunplayed = False

        $ roundresult = "tie"

    if roundresult == "win":

        play sound "fx/win.ogg"
        show win12 at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show lose12 at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ mcpoints += pointsthisround
        $ pointsthisround = 1


    elif roundresult == "tie":

        play sound "fx/tie.ogg"
        show tie12 at Position (xpos = 1660, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1
    else:



        play sound "fx/lose.ogg"
        show lose12 at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show win12 at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ sebpoints += pointsthisround
        $ pointsthisround = 1

    $ renpy.pause (0.5)



    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb13 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb13
    with dissolvemed

    $ displayCards()

    $ userSelection = ui.interact()

    if userSelection == "2":

        hide 2d
        hide back6
        with dissolve
        show 2d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "lose"

    if userSelection == "3":

        hide 3d
        hide back6
        with dissolve
        show 3d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "lose"

    if userSelection == "4":

        hide 4d
        hide back6
        with dissolve
        show 4d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "lose"

    if userSelection == "5":

        hide 5d
        hide back6
        with dissolve
        show 5d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "lose"

    if userSelection == "6":

        hide 6d
        hide back6
        with dissolve
        show 6d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "tie"

    if userSelection == "7":

        hide 7d
        hide back6
        with dissolve
        show 7d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "win"

    if userSelection == "8":

        hide 8d
        hide back6
        with dissolve
        show 8d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "win"

    if userSelection == "9":

        hide 9d
        hide back6
        with dissolve
        show 9d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "win"

    if userSelection == "10":

        hide 10d
        hide back6
        with dissolve
        show 10d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "win"

    if userSelection == "j":

        hide jd
        hide back6
        with dissolve
        show jd at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "win"

    if userSelection == "q":

        hide qd
        hide back6
        with dissolve
        show qd at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "win"

    if userSelection == "k":

        hide kd
        hide back6
        with dissolve
        show kd at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "win"

    if userSelection == "a":

        hide ad
        hide back6
        with dissolve
        show ad at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ daunplayed = False

        $ roundresult = "lose"




    if roundresult == "win":

        play sound "fx/win.ogg"
        show win13 at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show lose13 at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ mcpoints += pointsthisround
        $ pointsthisround = 1


    elif roundresult == "tie":

        play sound "fx/tie.ogg"
        show tie13 at Position (xpos = 1800, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1
    else:



        play sound "fx/lose.ogg"
        show lose13 at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show win13 at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ sebpoints += pointsthisround
        $ pointsthisround = 1

    jump venus_BB_end
