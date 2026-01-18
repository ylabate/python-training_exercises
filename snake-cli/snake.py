from random import randint
from time import sleep
from keyboard_setup import keyboard_setup

green = "\033[42m"
orange = "\033[43m"
red = "\033[41m"
blue = "\033[44m"
reset = "\033[0m"
height = 15
width = 15
direction = 0
score = 0
speed = 0.5
finish = False


def clear_screen():
    clear_line = "\033[2K"
    move_up = "\033[1A"
    for _ in range(height + 1):
        print(f"{clear_line}{move_up}", end='')
    print("\r", end='')


def print_screen():
    for current_height in range(height + 1):
        for current_width in range(width + 1):
            if current_height == 0 and current_width == 0:
                print(f"{orange}{score:02}{reset}", end='')
                continue
            elif current_width == 0 or current_width == width or current_height == 0 or current_height == height:
                print(f"{green}  {reset}", end='')
                continue
            for current_fruit in fruit:
                if current_fruit["height"] == current_height and current_fruit["width"] == current_width:
                    print(f"{red}  {reset}", end='')
                    break
            else:
                for current_player in player:
                    if current_player["height"] == current_height and current_player["width"] == current_width:
                        print(f"{blue}  {reset}", end='')
                        break
                else:
                    print(f"{orange}  {reset}", end='')
        print()


def update_pos():
    global direction
    local_dir = direction
    if touche is not None:
        if touche == 'z' or touche == "UP":
            local_dir = 1
        elif touche == 's' or touche == "DOWWN":
            local_dir = 3
        elif touche == 'q' or touche == "LEFT":
            local_dir = 2
        elif touche == 'd' or touche == "RIGHT":
            local_dir = 4
        elif touche == 'x':
            return (1)
    if direction != 0:
        if local_dir == direction - 2 or local_dir == direction + 2:
            return (0)
    for i in range(len(player) - 1, 0, -1):
        player[i] = player[i - 1].copy()
    head = player[0]
    if local_dir == 1:
        head["height"] -= 1
    elif local_dir == 3:
        head["height"] += 1
    elif local_dir == 2:
        head["width"] -= 1
    elif local_dir == 4:
        head["width"] += 1
    direction = local_dir
    return (0)


def eat():
    global score
    index = 0
    for i in fruit:
        if player[0]["height"] == i["height"] and player[0]["width"] == i["width"]:
            fruit[index]["height"] = randint(1, height - 1)
            fruit[index]["width"] = randint(1, width - 1)
            score += 1
            player.append(player[-1].copy())
        index += 1


def gen_fruit():
    global fruit
    fruit = [
        {"height": randint(1, height - 1), "width": randint(1, width - 1)},
        {"height": randint(1, height - 1), "width": randint(1, width - 1)},
        {"height": randint(1, height - 1), "width": randint(1, width - 1)}
    ]


def check_end():
    global finish
    if len(player) >= (height - 2) * (width - 2):
        finish = True
        return (1)
    if player[0]["height"] == 0 or player[0]["height"] == height or player[0]["width"] == 0 or player[0]["width"] == width:
        return (1)
    for i in player[1:]:
        if i == player[0]:
            return (1)
    else:
        return (0)


def end_screen():
    for current_height in range(height + 1):
        current_width = 0
        while current_width < width + 1:
            if current_height == height // 2 and current_width == width // 2 - 2:
                if finish == True:
                    print(f"{red}VICTORY !!{reset}", end='')
                    current_width += 5
                else:
                    print(f"{red}GAME  OVER{reset}", end='')
                    current_width += 5
            elif current_height == (height // 2) + 1 and current_width == width // 2 - 2:
                print_score = "SCORE = " + f"{score:02}"
                print(f"{red}{print_score}{reset}", end='')
                current_width += len(print_score) // 2
            else:
                print(f"{orange}  {reset}", end='')
                current_width += 1
        print()


if __name__ == "__main__":
    first_loop = True
    gen_fruit()
    player = [{"height": height // 2, "width": width // 2}]
    player.append(player[0].copy())

    with keyboard_setup() as kb:
        print_screen()
        while True:
            touche = kb.get_input()
            if update_pos():
                break
            if direction != 0:
                first_loop = False
                if speed > 0.1:
                    speed *= 0.99
            eat()
            clear_screen()
            if check_end() == 1 and first_loop == False:
                end_screen()
                break
            print_screen()
            sleep(speed)
