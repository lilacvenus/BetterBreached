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

    $ random.shuffle(card_positions)

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


    Sb "As you can see, each of us starts with all cards of a given suit in their hands. You're diamonds and I'll be hearts."

    menu:
        "Of course.":


            pass
        "You've got my heart already.":


            Sb "Is that so?"

            Sb "Anyways..."
        "You stole all those hearts, didn't you?":


            Sb "Haha, well... Maybe I did."

            Sb "Anyways..."


    label venus_sebgameexplanation:

    show sebastian hand at Pan ((0, 650), (0, 350), 1.0) with dissolve

    $ renpy.pause (0.5)

    show sebastian hand at Pan ((0, 350), (-1000, 400), 3.0)

    $ renpy.pause (3.0)

    show sebastian hand at Pan ((-1000, 400), (-1000, 750), 1.0)

    $ renpy.pause (0.5)

    hide sebastian hand with dissolve

    Sb "What you see in the center is the {i}middle row{/i}, which is a line of shuffled cards from another suit."

    Sb "This way, each game is going to be unique since the middle row always changes between games."

    show sebastian hand at Pan ((300, 600), (400, 300), 3.0) with dissolve

    Sb "Now, this is how the game works: We will play a round for each card in the middle row, starting with the one you see at the very left."

    hide sebastian hand with dissolve

    hide backk with dissolve

    hide 8d with dissolve

    show back at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)

    show backk at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)

    with dissolve

    Sb "During each round, we both decide which card to play and put it there face down - like this."

    show kh at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
    show 8d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
    with dissolve

    Sb "Once we have both played a card, we flip them over. The highest card wins the round, and whoever played it gets a point."

    play sound "fx/lose.ogg"
    show lose at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
    show win at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
    with dissolve

    Sb "To clarify, 2 is the lowest card and the king is the highest. The ace is a special card - it beats every face card, but will lose against any number card."

    Sb "Now, the card from the middle row also counts, so it's possible that neither of us will get the point for a round."

    Sb "If there is a tie, no clear winner between the three cards, or the middle row has the highest card, no player will get a point for that round. However, the next round will give the winner an extra point to make up for it."

    Sb "At the end, the player with the most number of points wins the game."

    Sb "Did you get all that?"



    menu:
        "Yes. Let's get started.":


            hide back

            hide backk

            hide kh

            hide 8d

            show backk at Position (xpos = 1590, xanchor = "left", ypos = 1, yanchor = 0.4)

            show 8d at Position (xpos = 890, xanchor = "left", ypos = 0.95, yanchor = 0.4)

            hide win

            hide lose

            with dissolve

            jump venus_sebgamestart
        "No. Please explain it again.":


            hide back

            hide backk

            hide kh

            hide 8d

            show backk at Position (xpos = 1590, xanchor = "left", ypos = 1, yanchor = 0.4)

            show 8d at Position (xpos = 890, xanchor = "left", ypos = 0.95, yanchor = 0.4)

            hide win

            hide lose

            with dissolve

            jump venus_sebgameexplanation


    label venus_sebgamestart:

    Sb "So, this game is all about bluffing and mind games. We can always see what cards have been played, so each of us knows exactly what the other player has left."

    Sb "Alright, are you ready?"

    c "Sure."

    Sb "Don't worry, I'll go easy on you."

    Sb "Take all the time you need to make your selection."

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

    Sb "Ahh, a 5 for the first card makes for an interesting start."

    Sb "You could try to surpass it and play something higher, but if I'm going to do the same, you don't know how high I would go to not only beat the 5, but your higher card as well."

    Sb "Alternatively, you could count on me trying to beat a higher card and play a low one instead, thus making me waste mine."

    Sb "What's it going to be, [player_name]?"



    if d2unplayed == True:
        $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    if d3unplayed == True:
        $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d4unplayed == True:
        $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d5unplayed == True:
        $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d6unplayed == True:
        $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d7unplayed == True:
        $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d8unplayed == True:
        $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d9unplayed == True:
        $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d10unplayed == True:
        $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if djunplayed == True:
        $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dqunplayed == True:
        $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dkunplayed == True:
        $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if daunplayed == True:
        $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    $ result = ui.interact()

    $ renpy.block_rollback()

    if result == "2":

        hide 2d
        hide back2
        with dissolve
        show 2d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "tie"

    if result == "3":

        hide 3d
        hide back2
        with dissolve
        show 3d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "tie"

    if result == "4":

        hide 4d
        hide back2
        with dissolve
        show 4d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "tie"

    if result == "5":

        hide 5d
        hide back2
        with dissolve
        show 5d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "tie"

    if result == "6":

        hide 6d
        hide back2
        with dissolve
        show 6d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "win"

    if result == "7":

        hide 7d
        hide back2
        with dissolve
        show 7d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "win"

    if result == "8":

        hide 8d
        hide back2
        with dissolve
        show 8d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "win"

    if result == "9":

        hide 9d
        hide back2
        with dissolve
        show 9d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "win"

    if result == "10":

        hide 10d
        hide back2
        with dissolve
        show 10d at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "win"

    if result == "j":

        hide jd
        hide back2
        with dissolve
        show jd at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "win"

    if result == "q":

        hide qd
        hide back2
        with dissolve
        show qd at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "win"

    if result == "k":

        hide kd
        hide back2
        with dissolve
        show kd at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "win"

    if result == "a":

        hide ad
        hide back2
        with dissolve
        show ad at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 2h at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ daunplayed = False

        $ roundresult = "tie"



    Sb "As you can see, I played a lowly 2 just to see what would happen."

    Sb "Getting to know your opponent and their tendencies is just as important as analyzing potential moves and strategies."


    if roundresult == "win":

        play sound "fx/win.ogg"
        show win1 at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show lose1 at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ mcpoints += pointsthisround
        $ pointsthisround = 1

        Sb "The first point is yours, but now you'll have to ask yourself: Was it worth it?"

    elif roundresult == "tie":

        play sound "fx/tie.ogg"
        show tie1 at Position (xpos = 120, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1

        Sb "A tie. I guess we both tried to do the same thing here."
    else:


        play sound "fx/lose.ogg"
        show lose1 at Position (xpos = 120, xanchor = "center", ypos = 743, yanchor = 0.5)
        show win1 at Position (xpos = 120, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ sebpoints += pointsthisround
        $ pointsthisround = 1

        Sb "You played your ace, huh? Not exactly the best move for the first round."




    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb2 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb2
    with dissolvemed

    Sb "The king presents us with an interesting conundrum, especially when getting him early when most cards are still available. I'll let you figure this one out, though."

    if d2unplayed == True:
        $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    if d3unplayed == True:
        $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d4unplayed == True:
        $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d5unplayed == True:
        $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d6unplayed == True:
        $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d7unplayed == True:
        $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d8unplayed == True:
        $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d9unplayed == True:
        $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d10unplayed == True:
        $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if djunplayed == True:
        $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dqunplayed == True:
        $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dkunplayed == True:
        $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if daunplayed == True:
        $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    $ result = ui.interact()

    $ renpy.block_rollback()

    if result == "2":

        hide 2d
        hide back3
        with dissolve
        show 2d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "tie"

    if result == "3":

        hide 3d
        hide back3
        with dissolve
        show 3d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "tie"

    if result == "4":

        hide 4d
        hide back3
        with dissolve
        show 4d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "tie"

    if result == "5":

        hide 5d
        hide back3
        with dissolve
        show 5d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "tie"

    if result == "6":

        hide 6d
        hide back3
        with dissolve
        show 6d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "tie"

    if result == "7":

        hide 7d
        hide back3
        with dissolve
        show 7d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "tie"

    if result == "8":

        hide 8d
        hide back3
        with dissolve
        show 8d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "tie"

    if result == "9":

        hide 9d
        hide back3
        with dissolve
        show 9d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "tie"

    if result == "10":

        hide 10d
        hide back3
        with dissolve
        show 10d at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "tie"

    if result == "j":

        hide jd
        hide back3
        with dissolve
        show jd at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "tie"

    if result == "q":

        hide qd
        hide back3
        with dissolve
        show qd at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "tie"

    if result == "k":

        hide kd
        hide back3
        with dissolve
        show kd at Position (xpos = 260, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 3h at Position (xpos = 260, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "tie"

    if result == "a":

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

        Sb "Looks like a tie. Of course, the only card that beats a king is the ace, but playing it here would be a rookie mistake. It's definitely a safer play to just get rid of a low card here."
    else:


        play sound "fx/tie.ogg"
        show tie2 at Position (xpos = 260, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1

        Sb "You did the predictable thing and play the ace, the only card that beats a king. Since my 3 beats your ace, though, this round is considered a tie. You may think that's not so bad, but taking away your ace with just a lowly 3 gives me big advantage during the rest of the game."




    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb3 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb3
    with dissolvemed


    if d2unplayed == True:
        $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    if d3unplayed == True:
        $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d4unplayed == True:
        $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d5unplayed == True:
        $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d6unplayed == True:
        $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d7unplayed == True:
        $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d8unplayed == True:
        $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d9unplayed == True:
        $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d10unplayed == True:
        $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if djunplayed == True:
        $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dqunplayed == True:
        $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dkunplayed == True:
        $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if daunplayed == True:
        $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    $ result = ui.interact()

    $ renpy.block_rollback()

    if result == "2":

        hide 2d
        hide back10
        with dissolve
        show 2d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "lose"

    if result == "3":

        hide 3d
        hide back10
        with dissolve
        show 3d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "lose"

    if result == "4":

        hide 4d
        hide back10
        with dissolve
        show 4d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "lose"

    if result == "5":

        hide 5d
        hide back10
        with dissolve
        show 5d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "lose"

    if result == "6":

        hide 6d
        hide back10
        with dissolve
        show 6d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "lose"

    if result == "7":

        hide 7d
        hide back10
        with dissolve
        show 7d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "lose"

    if result == "8":

        hide 8d
        hide back10
        with dissolve
        show 8d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "lose"

    if result == "9":

        hide 9d
        hide back10
        with dissolve
        show 9d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "lose"

    if result == "10":

        hide 10d
        hide back10
        with dissolve
        show 10d at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "tie"

    if result == "j":

        hide jd
        hide back10
        with dissolve
        show jd at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "win"

    if result == "q":

        hide qd
        hide back10
        with dissolve
        show qd at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "win"

    if result == "k":

        hide kd
        hide back10
        with dissolve
        show kd at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 10h at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "win"

    if result == "a":

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

        Sb "Your point."

    elif roundresult == "tie":

        play sound "fx/tie.ogg"
        show tie3 at Position (xpos = 400, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1

        Sb "Looks like a tie."
    else:


        play sound "fx/lose.ogg"
        show lose3 at Position (xpos = 400, xanchor = "center", ypos = 743, yanchor = 0.5)
        show win3 at Position (xpos = 400, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ sebpoints += pointsthisround
        $ pointsthisround = 1

        Sb "My point."




    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb4 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb4
    with dissolvemed



    if d2unplayed == True:
        $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    if d3unplayed == True:
        $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d4unplayed == True:
        $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d5unplayed == True:
        $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d6unplayed == True:
        $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d7unplayed == True:
        $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d8unplayed == True:
        $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d9unplayed == True:
        $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d10unplayed == True:
        $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if djunplayed == True:
        $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dqunplayed == True:
        $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dkunplayed == True:
        $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if daunplayed == True:
        $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    $ result = ui.interact()

    $ renpy.block_rollback()

    if result == "2":

        hide 2d
        hide backq
        with dissolve
        show 2d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "lose"

    if result == "3":

        hide 3d
        hide backq
        with dissolve
        show 3d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "lose"

    if result == "4":

        hide 4d
        hide backq
        with dissolve
        show 4d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "lose"

    if result == "5":

        hide 5d
        hide backq
        with dissolve
        show 5d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "lose"

    if result == "6":

        hide 6d
        hide backq
        with dissolve
        show 6d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "lose"

    if result == "7":

        hide 7d
        hide backq
        with dissolve
        show 7d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "lose"

    if result == "8":

        hide 8d
        hide backq
        with dissolve
        show 8d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "lose"

    if result == "9":

        hide 9d
        hide backq
        with dissolve
        show 9d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "lose"

    if result == "10":

        hide 10d
        hide backq
        with dissolve
        show 10d at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "lose"

    if result == "j":

        hide jd
        hide backq
        with dissolve
        show jd at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "lose"

    if result == "q":

        hide qd
        hide backq
        with dissolve
        show qd at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "tie"

    if result == "k":

        hide kd
        hide backq
        with dissolve
        show kd at Position (xpos = 540, xanchor = "center", ypos = 743, yanchor = 0.5)
        show qh at Position (xpos = 540, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "win"

    if result == "a":

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


    if mcpoints > sebpoints:

        Sb "Guess I should start playing seriously."

    elif sebpoints > mcpoints:

        Sb "Don't worry, you can still win."
    else:


        Sb "You're not too bad so far."




    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb5 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb5
    with dissolvemed


    if d2unplayed == True:
        $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    if d3unplayed == True:
        $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d4unplayed == True:
        $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d5unplayed == True:
        $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d6unplayed == True:
        $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d7unplayed == True:
        $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d8unplayed == True:
        $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d9unplayed == True:
        $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d10unplayed == True:
        $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if djunplayed == True:
        $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dqunplayed == True:
        $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dkunplayed == True:
        $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if daunplayed == True:
        $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    $ result = ui.interact()

    $ renpy.block_rollback()

    if result == "2":

        hide 2d
        hide backj
        with dissolve
        show 2d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "lose"

    if result == "3":

        hide 3d
        hide backj
        with dissolve
        show 3d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "lose"

    if result == "4":

        hide 4d
        hide backj
        with dissolve
        show 4d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "lose"

    if result == "5":

        hide 5d
        hide backj
        with dissolve
        show 5d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "lose"

    if result == "6":

        hide 6d
        hide backj
        with dissolve
        show 6d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "lose"

    if result == "7":

        hide 7d
        hide backj
        with dissolve
        show 7d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "lose"

    if result == "8":

        hide 8d
        hide backj
        with dissolve
        show 8d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "lose"

    if result == "9":

        hide 9d
        hide backj
        with dissolve
        show 9d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "lose"

    if result == "10":

        hide 10d
        hide backj
        with dissolve
        show 10d at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "lose"

    if result == "j":

        hide jd
        hide backj
        with dissolve
        show jd at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "tie"

    if result == "q":

        hide qd
        hide backj
        with dissolve
        show qd at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "win"

    if result == "k":

        hide kd
        hide backj
        with dissolve
        show kd at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show jh at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "win"

    if result == "a":

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

        Sb "Damn."

    elif roundresult == "tie":

        play sound "fx/tie.ogg"
        show tie5 at Position (xpos = 680, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1

        Sb "A tie? Okay."
    else:


        play sound "fx/lose.ogg"
        show lose5 at Position (xpos = 680, xanchor = "center", ypos = 743, yanchor = 0.5)
        show win5 at Position (xpos = 680, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ sebpoints += pointsthisround
        $ pointsthisround = 1

        Sb "Nice."




    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb6 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb6
    with dissolvemed


    if d2unplayed == True:
        $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    if d3unplayed == True:
        $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d4unplayed == True:
        $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d5unplayed == True:
        $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d6unplayed == True:
        $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d7unplayed == True:
        $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d8unplayed == True:
        $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d9unplayed == True:
        $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d10unplayed == True:
        $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if djunplayed == True:
        $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dqunplayed == True:
        $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dkunplayed == True:
        $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if daunplayed == True:
        $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    $ result = ui.interact()

    $ renpy.block_rollback()

    if result == "2":

        hide 2d
        hide back9
        with dissolve
        show 2d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "lose"

    if result == "3":

        hide 3d
        hide back9
        with dissolve
        show 3d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "lose"

    if result == "4":

        hide 4d
        hide back9
        with dissolve
        show 4d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "lose"

    if result == "5":

        hide 5d
        hide back9
        with dissolve
        show 5d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "lose"

    if result == "6":

        hide 6d
        hide back9
        with dissolve
        show 6d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "lose"

    if result == "7":

        hide 7d
        hide back9
        with dissolve
        show 7d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "lose"

    if result == "8":

        hide 8d
        hide back9
        with dissolve
        show 8d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "lose"

    if result == "9":

        hide 9d
        hide back9
        with dissolve
        show 9d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "tie"

    if result == "10":

        hide 10d
        hide back9
        with dissolve
        show 10d at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "win"

    if result == "j":

        hide jd
        hide back9
        with dissolve
        show jd at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "tie"

    if result == "q":

        hide qd
        hide back9
        with dissolve
        show qd at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "tie"

    if result == "k":

        hide kd
        hide back9
        with dissolve
        show kd at Position (xpos = 820, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 9h at Position (xpos = 820, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "tie"

    if result == "a":

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



    $ difference = mcpoints - sebpoints

    if difference == -1:

        Sb "Looks like it's pretty even so far."

    elif difference == 0:

        Sb "Looks like it's pretty even so far."

    elif difference == 1:

        Sb "Looks like it's pretty even so far."

    elif difference < -1:

        Sb "It's not looking too great for you."
    else:


        Sb "Damn, you're better than I thought. Are you sure you haven't played this before?"




    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb7 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb7
    with dissolvemed


    if d2unplayed == True:
        $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    if d3unplayed == True:
        $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d4unplayed == True:
        $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d5unplayed == True:
        $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d6unplayed == True:
        $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d7unplayed == True:
        $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d8unplayed == True:
        $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d9unplayed == True:
        $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d10unplayed == True:
        $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if djunplayed == True:
        $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dqunplayed == True:
        $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dkunplayed == True:
        $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if daunplayed == True:
        $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    $ result = ui.interact()

    $ renpy.block_rollback()

    if result == "2":

        hide 2d
        hide back4
        with dissolve
        show 2d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "tie"

    if result == "3":

        hide 3d
        hide back4
        with dissolve
        show 3d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "tie"

    if result == "4":

        hide 4d
        hide back4
        with dissolve
        show 4d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "tie"

    if result == "5":

        hide 5d
        hide back4
        with dissolve
        show 5d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "tie"

    if result == "6":

        hide 6d
        hide back4
        with dissolve
        show 6d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "tie"

    if result == "7":

        hide 7d
        hide back4
        with dissolve
        show 7d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "tie"

    if result == "8":

        hide 8d
        hide back4
        with dissolve
        show 8d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "tie"

    if result == "9":

        hide 9d
        hide back4
        with dissolve
        show 9d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "tie"

    if result == "10":

        hide 10d
        hide back4
        with dissolve
        show 10d at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "tie"

    if result == "j":

        hide jd
        hide back4
        with dissolve
        show jd at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "tie"

    if result == "q":

        hide qd
        hide back4
        with dissolve
        show qd at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "win"

    if result == "k":

        hide kd
        hide back4
        with dissolve
        show kd at Position (xpos = 960, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 4h at Position (xpos = 960, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "win"

    if result == "a":

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


    if mcpoints == 7:

        Sb "Seriously, how could I lose seven times in a row? Guess you win this one, [player_name]. I won't be able to catch up, so let's just finish it for the sake of it."

    elif sebpoints == 7:

        Sb "I'm sorry to say this, but you just lost. The best you could do now is losing by one point, even if you win every round after this one."
    else:


        Sb "This is the halfway point, so now it's really going to get serious. Anyone can still win."




    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb8 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb8
    with dissolvemed


    if d2unplayed == True:
        $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    if d3unplayed == True:
        $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d4unplayed == True:
        $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d5unplayed == True:
        $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d6unplayed == True:
        $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d7unplayed == True:
        $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d8unplayed == True:
        $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d9unplayed == True:
        $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d10unplayed == True:
        $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if djunplayed == True:
        $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dqunplayed == True:
        $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dkunplayed == True:
        $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if daunplayed == True:
        $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    $ result = ui.interact()

    $ renpy.block_rollback()

    if result == "2":

        hide 2d
        hide backa
        with dissolve
        show 2d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "tie"

    if result == "3":

        hide 3d
        hide backa
        with dissolve
        show 3d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "tie"

    if result == "4":

        hide 4d
        hide backa
        with dissolve
        show 4d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "tie"

    if result == "5":

        hide 5d
        hide backa
        with dissolve
        show 5d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "tie"

    if result == "6":

        hide 6d
        hide backa
        with dissolve
        show 6d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "tie"

    if result == "7":

        hide 7d
        hide backa
        with dissolve
        show 7d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "tie"

    if result == "8":

        hide 8d
        hide backa
        with dissolve
        show 8d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "tie"

    if result == "9":

        hide 9d
        hide backa
        with dissolve
        show 9d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "tie"

    if result == "10":

        hide 10d
        hide backa
        with dissolve
        show 10d at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "tie"

    if result == "j":

        hide jd
        hide backa
        with dissolve
        show jd at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "lose"

    if result == "q":

        hide qd
        hide backa
        with dissolve
        show qd at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "lose"

    if result == "k":

        hide kd
        hide backa
        with dissolve
        show kd at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show ah at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "lose"

    if result == "a":

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

        Sb "This one's yours."


    elif roundresult == "tie":

        play sound "fx/tie.ogg"
        show tie8 at Position (xpos = 1100, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1

        Sb "Interesting..."
    else:


        play sound "fx/lose.ogg"
        show lose8 at Position (xpos = 1100, xanchor = "center", ypos = 743, yanchor = 0.5)
        show win8 at Position (xpos = 1100, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ sebpoints += pointsthisround
        $ pointsthisround = 1

        Sb "I'll take this one."





    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb9 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb9
    with dissolvemed


    if d2unplayed == True:
        $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    if d3unplayed == True:
        $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d4unplayed == True:
        $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d5unplayed == True:
        $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d6unplayed == True:
        $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d7unplayed == True:
        $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d8unplayed == True:
        $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d9unplayed == True:
        $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d10unplayed == True:
        $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if djunplayed == True:
        $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dqunplayed == True:
        $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dkunplayed == True:
        $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if daunplayed == True:
        $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    $ result = ui.interact()

    $ renpy.block_rollback()

    if result == "2":

        hide 2d
        hide backk
        with dissolve
        show 2d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "lose"

    if result == "3":

        hide 3d
        hide backk
        with dissolve
        show 3d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "lose"

    if result == "4":

        hide 4d
        hide backk
        with dissolve
        show 4d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "lose"

    if result == "5":

        hide 5d
        hide backk
        with dissolve
        show 5d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "lose"

    if result == "6":

        hide 6d
        hide backk
        with dissolve
        show 6d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "lose"

    if result == "7":

        hide 7d
        hide backk
        with dissolve
        show 7d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "lose"

    if result == "8":

        hide 8d
        hide backk
        with dissolve
        show 8d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "lose"

    if result == "9":

        hide 9d
        hide backk
        with dissolve
        show 9d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "lose"

    if result == "10":

        hide 10d
        hide backk
        with dissolve
        show 10d at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "lose"

    if result == "j":

        hide jd
        hide backk
        with dissolve
        show jd at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "lose"

    if result == "q":

        hide qd
        hide backk
        with dissolve
        show qd at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "lose"

    if result == "k":

        hide kd
        hide backk
        with dissolve
        show kd at Position (xpos = 1240, xanchor = "center", ypos = 743, yanchor = 0.5)
        show kh at Position (xpos = 1240, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "tie"

    if result == "a":

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


    if d2unplayed == True:
        $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    if d3unplayed == True:
        $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d4unplayed == True:
        $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d5unplayed == True:
        $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d6unplayed == True:
        $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d7unplayed == True:
        $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d8unplayed == True:
        $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d9unplayed == True:
        $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d10unplayed == True:
        $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if djunplayed == True:
        $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dqunplayed == True:
        $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dkunplayed == True:
        $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if daunplayed == True:
        $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    $ result = ui.interact()

    $ renpy.block_rollback()

    if result == "2":

        hide 2d
        hide back8
        with dissolve
        show 2d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "lose"

    if result == "3":

        hide 3d
        hide back8
        with dissolve
        show 3d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "lose"

    if result == "4":

        hide 4d
        hide back8
        with dissolve
        show 4d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "lose"

    if result == "5":

        hide 5d
        hide back8
        with dissolve
        show 5d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "lose"

    if result == "6":

        hide 6d
        hide back8
        with dissolve
        show 6d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "lose"

    if result == "7":

        hide 7d
        hide back8
        with dissolve
        show 7d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "lose"

    if result == "8":

        hide 8d
        hide back8
        with dissolve
        show 8d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "tie"

    if result == "9":

        hide 9d
        hide back8
        with dissolve
        show 9d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "win"

    if result == "10":

        hide 10d
        hide back8
        with dissolve
        show 10d at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "win"

    if result == "j":

        hide jd
        hide back8
        with dissolve
        show jd at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "win"

    if result == "q":

        hide qd
        hide back8
        with dissolve
        show qd at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "win"

    if result == "k":

        hide kd
        hide back8
        with dissolve
        show kd at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 8h at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "win"

    if result == "a":

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

        Sb "Darn."

    elif roundresult == "tie":

        play sound "fx/tie.ogg"
        show tie10 at Position (xpos = 1380, xanchor = "center", ypos = 540, yanchor = 0.5) with dissolve

        $ pointsthisround += 1

        Sb "Tie? Okay."
    else:


        play sound "fx/lose.ogg"
        show lose10 at Position (xpos = 1380, xanchor = "center", ypos = 743, yanchor = 0.5)
        show win10 at Position (xpos = 1380, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ sebpoints += pointsthisround
        $ pointsthisround = 1

        Sb "Phew."




    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb11 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb11
    with dissolvemed


    if d2unplayed == True:
        $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    if d3unplayed == True:
        $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d4unplayed == True:
        $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d5unplayed == True:
        $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d6unplayed == True:
        $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d7unplayed == True:
        $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d8unplayed == True:
        $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d9unplayed == True:
        $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d10unplayed == True:
        $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if djunplayed == True:
        $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dqunplayed == True:
        $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dkunplayed == True:
        $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if daunplayed == True:
        $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    $ result = ui.interact()

    $ renpy.block_rollback()

    if result == "2":

        hide 2d
        hide back7
        with dissolve
        show 2d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "lose"

    if result == "3":

        hide 3d
        hide back7
        with dissolve
        show 3d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "lose"

    if result == "4":

        hide 4d
        hide back7
        with dissolve
        show 4d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "lose"

    if result == "5":

        hide 5d
        hide back7
        with dissolve
        show 5d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "lose"

    if result == "6":

        hide 6d
        hide back7
        with dissolve
        show 6d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "lose"

    if result == "7":

        hide 7d
        hide back7
        with dissolve
        show 7d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "tie"

    if result == "8":

        hide 8d
        hide back7
        with dissolve
        show 8d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "win"

    if result == "9":

        hide 9d
        hide back7
        with dissolve
        show 9d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "win"

    if result == "10":

        hide 10d
        hide back7
        with dissolve
        show 10d at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "win"

    if result == "j":

        hide jd
        hide back7
        with dissolve
        show jd at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "win"

    if result == "q":

        hide qd
        hide back7
        with dissolve
        show qd at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "win"

    if result == "k":

        hide kd
        hide back7
        with dissolve
        show kd at Position (xpos = 1520, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 7h at Position (xpos = 1520, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "win"

    if result == "a":

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




    $ difference = mcpoints - sebpoints

    if difference == -1:

        Sb "This is getting interesting."

    elif difference == 0:

        Sb "This is getting interesting."

    elif difference == 1:

        Sb "This is getting interesting."
    else:


        Sb "Yeah, this game is pretty much over."




    play sound "fx/woosh4.ogg"

    show eyesseb at Pan ((500, 0), (0, 0), 0.7)
    show roundb12 at Pan ((-500, 0), (0, 0), 0.7)

    with dissolvemed

    $ renpy.pause (0.5)

    hide eyesseb
    hide roundb12
    with dissolvemed


    if d2unplayed == True:
        $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    if d3unplayed == True:
        $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d4unplayed == True:
        $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d5unplayed == True:
        $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d6unplayed == True:
        $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d7unplayed == True:
        $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d8unplayed == True:
        $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d9unplayed == True:
        $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d10unplayed == True:
        $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if djunplayed == True:
        $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dqunplayed == True:
        $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dkunplayed == True:
        $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if daunplayed == True:
        $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    $ result = ui.interact()

    $ renpy.block_rollback()

    if result == "2":

        hide 2d
        hide back5
        with dissolve
        show 2d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "tie"

    if result == "3":

        hide 3d
        hide back5
        with dissolve
        show 3d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "tie"

    if result == "4":

        hide 4d
        hide back5
        with dissolve
        show 4d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "tie"

    if result == "5":

        hide 5d
        hide back5
        with dissolve
        show 5d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "tie"

    if result == "6":

        hide 6d
        hide back5
        with dissolve
        show 6d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "tie"

    if result == "7":

        hide 7d
        hide back5
        with dissolve
        show 7d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "tie"

    if result == "8":

        hide 8d
        hide back5
        with dissolve
        show 8d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "tie"

    if result == "9":

        hide 9d
        hide back5
        with dissolve
        show 9d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "tie"

    if result == "10":

        hide 10d
        hide back5
        with dissolve
        show 10d at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "win"

    if result == "j":

        hide jd
        hide back5
        with dissolve
        show jd at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "win"

    if result == "q":

        hide qd
        hide back5
        with dissolve
        show qd at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "win"

    if result == "k":

        hide kd
        hide back5
        with dissolve
        show kd at Position (xpos = 1660, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 5h at Position (xpos = 1660, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "win"

    if result == "a":

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


    if d2unplayed == True:
        $ ui.imagebutton("pc/2d.png", "pc/2dh.png", clicked=[ui.returns("2"),Play("audio", "se/sounds/select3.ogg")], xpos=120, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    if d3unplayed == True:
        $ ui.imagebutton("pc/3d.png", "pc/3dh.png", clicked=[ui.returns("3"),Play("audio", "se/sounds/select3.ogg")], xpos=260, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d4unplayed == True:
        $ ui.imagebutton("pc/4d.png", "pc/4dh.png", clicked=[ui.returns("4"),Play("audio", "se/sounds/select3.ogg")], xpos=400, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d5unplayed == True:
        $ ui.imagebutton("pc/5d.png", "pc/5dh.png", clicked=[ui.returns("5"),Play("audio", "se/sounds/select3.ogg")], xpos=540, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d6unplayed == True:
        $ ui.imagebutton("pc/6d.png", "pc/6dh.png", clicked=[ui.returns("6"),Play("audio", "se/sounds/select3.ogg")], xpos=680, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d7unplayed == True:
        $ ui.imagebutton("pc/7d.png", "pc/7dh.png", clicked=[ui.returns("7"),Play("audio", "se/sounds/select3.ogg")], xpos=820, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d8unplayed == True:
        $ ui.imagebutton("pc/8d.png", "pc/8dh.png", clicked=[ui.returns("8"),Play("audio", "se/sounds/select3.ogg")], xpos=960, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d9unplayed == True:
        $ ui.imagebutton("pc/9d.png", "pc/9dh.png", clicked=[ui.returns("9"),Play("audio", "se/sounds/select3.ogg")], xpos=1100, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if d10unplayed == True:
        $ ui.imagebutton("pc/10d.png", "pc/10dh.png", clicked=[ui.returns("10"),Play("audio", "se/sounds/select3.ogg")], xpos=1240, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if djunplayed == True:
        $ ui.imagebutton("pc/jd.png", "pc/jdh.png", clicked=[ui.returns("j"),Play("audio", "se/sounds/select3.ogg")], xpos=1380, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dqunplayed == True:
        $ ui.imagebutton("pc/qd.png", "pc/qdh.png", clicked=[ui.returns("q"),Play("audio", "se/sounds/select3.ogg")], xpos=1520, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if dkunplayed == True:
        $ ui.imagebutton("pc/kd.png", "pc/kdh.png", clicked=[ui.returns("k"),Play("audio", "se/sounds/select3.ogg")], xpos=1660, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))

    if daunplayed == True:
        $ ui.imagebutton("pc/ad.png", "pc/adh.png", clicked=[ui.returns("a"),Play("audio", "se/sounds/select3.ogg")], xpos=1800, xanchor = "center", ypos = 0.95, yanchor = 0.4, hovered = Play("audio", "se/sounds/select.ogg"))



    $ result = ui.interact()

    $ renpy.block_rollback()

    if result == "2":

        hide 2d
        hide back6
        with dissolve
        show 2d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d2unplayed = False

        $ roundresult = "lose"

    if result == "3":

        hide 3d
        hide back6
        with dissolve
        show 3d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d3unplayed = False

        $ roundresult = "lose"

    if result == "4":

        hide 4d
        hide back6
        with dissolve
        show 4d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d4unplayed = False

        $ roundresult = "lose"

    if result == "5":

        hide 5d
        hide back6
        with dissolve
        show 5d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d5unplayed = False

        $ roundresult = "lose"

    if result == "6":

        hide 6d
        hide back6
        with dissolve
        show 6d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d6unplayed = False

        $ roundresult = "tie"

    if result == "7":

        hide 7d
        hide back6
        with dissolve
        show 7d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d7unplayed = False

        $ roundresult = "win"

    if result == "8":

        hide 8d
        hide back6
        with dissolve
        show 8d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d8unplayed = False

        $ roundresult = "win"

    if result == "9":

        hide 9d
        hide back6
        with dissolve
        show 9d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d9unplayed = False

        $ roundresult = "win"

    if result == "10":

        hide 10d
        hide back6
        with dissolve
        show 10d at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ d10unplayed = False

        $ roundresult = "win"

    if result == "j":

        hide jd
        hide back6
        with dissolve
        show jd at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ djunplayed = False

        $ roundresult = "win"

    if result == "q":

        hide qd
        hide back6
        with dissolve
        show qd at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dqunplayed = False

        $ roundresult = "win"

    if result == "k":

        hide kd
        hide back6
        with dissolve
        show kd at Position (xpos = 1800, xanchor = "center", ypos = 743, yanchor = 0.5)
        show 6h at Position (xpos = 1800, xanchor = "center", ypos = 337, yanchor = 0.5)
        with dissolve

        $ dkunplayed = False

        $ roundresult = "win"

    if result == "a":

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
