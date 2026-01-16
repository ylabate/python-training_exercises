from random import randint
from time import sleep
from keyboard_setup import keyboard_setup

green = "\033[42m"
orange = "\033[43m"
red = "\033[41m"
blue = "\033[44m"
reset = "\033[0m"
height = 15
width = 30
direction = 0
score = 0


def clear_screen():
    clear_line = "\033[2K"
    move_up = "\033[1A"
    for _ in range(height + 1):
        print(f"{clear_line}{move_up}", end='')
    print("\r", end='')


def print_screen():
    for current_height in range(height + 1):
        for current_width in range(width + 1):
            if current_width == 0 or current_width == width or current_height == 0 or current_height == height:
                print(f"{green} {reset}", end='')
                continue
            for current_fruit in fruit:
                if current_fruit["height"] == current_height and current_fruit["width"] == current_width:
                    print(f"{red} {reset}", end='')
                    break
            else:
                for current_player in player:
                    if current_player["height"] == current_height and current_player["width"] == current_width:
                        print(f"{blue} {reset}", end='')
                        break
                else:
                    print(f"{orange} {reset}", end='')
        print()


def update_pos():
    global direction
    local_dir = direction
    if touche is not None:
        if touche == 'z' or touche == "HAUT":
            local_dir = 1
        elif touche == 's' or touche == "BAS":
            local_dir = 3
        elif touche == 'q' or touche == "GAUCHE":
            local_dir = 2
        elif touche == 'd' or touche == "DROITE":
            local_dir = 4
        elif touche == 'x':
            return (1)
    if direction != 0:
        if local_dir == direction - 2 or local_dir == direction + 2:
            return (0)
    head = player[0]
    if local_dir == 1:
        head["height"] -= 1
    elif local_dir == 3:
        head["height"] += 1
    elif local_dir == 2:
        head["width"] -= 1
    elif local_dir == 4:
        head["width"] += 1
    for i in range(1, len(player)):
        player[i] = player[i - 1]
    direction = local_dir
    return (0)


def eat():
    index = 0
    for i in fruit:
        if player[0]["height"] == i["height"] and player[0]["width"] == i["width"]:
            fruit[index]["height"] = randint(1, height)
            fruit[index]["width"] = randint(1, width)
            score += 1
        index += 1


def gen_fruit():
    global fruit
    fruit = [
        {"height": randint(1, height), "width": randint(1, width)},
        {"height": randint(1, height), "width": randint(1, width)},
        {"height": randint(1, height), "width": randint(1, height)}
    ]

if __name__ == "__main__":

    gen_fruit()
    player = [{"height": height // 2, "width": width // 2}]
    player.append({"height": player[0]["height"] - 1, "width": width // 2})

    with keyboard_setup() as kb:
        print_screen()
        while True:
            touche = kb.get_input()
            if update_pos():
                break
            eat()
            clear_screen()
            print_screen()
            sleep(0.6)
