import random

if __name__ == "__main__":
    green = "\033[42m"
    orange = "\033[43m"
    gray = "\033[1;100m"
    reset = "\033[0m"

    clear_ligne = "\033[2K"
    move_up = "\033[1A"

    with open("wordlist.txt", "r", encoding="utf-8") as fichier:
        liste_mots = fichier.read().splitlines()
        word = liste_mots[random.randint(0, 2977)]
    for i in range(len(word)):
        print("#", end='')
    for try_number in range(7, 0, -1):
        print(f"\n{try_number} remaining")
        while True:
            user_input = input("")
            if len(user_input) == len(word):
                break
            else:
                print(f"{move_up}{clear_ligne}{move_up}{clear_ligne}mauvaise longueure")
        print(f"{move_up}{clear_ligne}{move_up}{clear_ligne}", end="\r")
        for i in range(len(word)):
            if user_input[i] == word[i]:
                print(green, end='')
            elif user_input[i] in word:
                print(orange, end='')
            else:
                print(gray, end='')
            print(f"{user_input[i]}", end='')
            print(reset, end='')
        if user_input == word:
            print(f"\nfinded ! the word is {word}")
            break
    print(f"\ngame over, the word was {word}")
