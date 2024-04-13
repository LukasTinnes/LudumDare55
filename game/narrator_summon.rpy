label narrator_summoned:

    define fur = "red"
    define claws = "short"
    define eyes = "slitted"
    define hair = "short"
    define tail = "a"

    label narrator_creature:

    you "The creature currently has [fur] fur, [claws] claws, [eyes] eyes, [hair] hair and [tail] tail. It needs to have blue fur, long claws, round eyes, long hair and a tail."

    you "What offering should I make?"

    menu:
        "Carrots":
            if fur == "blue":
                $ fur = "red"
            else:
                $ fur = "blue"

            if eyes == "round":
                $ eyes = "slitted"
            else:
                $ eyes = "round"
        "Cookies":
            if claws == "short":
                $ claws = "long"
            else:
                $ claws = "short"

            if eyes == "round":
                $ eyes = "slitted"
            else:
                $ eyes = "round"
        "Apples":
            if fur == "blue":
                $ fur = "red"
            else:
                $ fur = "blue"

            if tail == "not a":
                $ tail = "a"
            else:
                $ tail = "not a"
        "Pencils":
            if hair == "short":
                $ hair = "long"
            else:
                $ hair = "short"

            if tail == "not a":
                $ tail = "a"
            else:
                $ tail = "not a"
    if fur == "blue" and claws == "long" and eyes == "round" and tail == "a":
        refi "You did it!"
        refi "Let me open the box."
        narrator "Refi opens the box and you find learning materials for your math exam."
        narrator "You feel confident."
        $ final_score += 1
    else:
        jump narrator_creature
