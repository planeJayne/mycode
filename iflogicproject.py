def main():

    ascii = """ 

    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣼⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⡍⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣤⣾⠿⠛⠛⠛⠿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠿⠟⠛⠛⠿⢷⣦⡀⠀⠀⠀⠀
⠀⠀⢠⣿⢟⡄⠀⠀⠀⠀⠀⠀⠹⣷⡄⠀⠀⠀⠀⠀⢀⣾⠟⡁⠀⠀⠀⠀⠀⠀⠙⢿⣆⠀⠀⠀
⠀⠀⣿⠇⣾⠁⠀⠀⠀⠀⠀⠀⠀⢹⣷⣾⠿⠛⠻⣷⣾⡟⣸⡇⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄⠀⠀
⠿⠿⣿⡀⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⠀⠀⠀⠈⢿⡇⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠿⠂
⠀⠀⢻⣧⠹⣧⡀⠀⠀⠀⠀⠀⢀⣾⡏⠀⠀⠀⠀⠀⠸⣿⡘⢷⣄⠀⠀⠀⠀⠀⠀⣰⡿⠀⠀⠀
⠀⠀⠀⠻⣷⣬⣛⠁⠀⠀⣀⣤⣾⠏⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⣝⡃⠀⠀⢀⣠⣾⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠛⠿⠿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠛⠛⠁⠀⠀⠀⠀⠀
"""
    print(ascii)

    print("Welcome to the Harry Potter Spell Quiz!")

    questions ={
        charms: [
            (""),
            (""),
            (""),
            (""),

        ],
    }


    category = (input("Please choose a spell category: charms, curses, summoning, or transifiguration\n")).strip().lower()

    if category == "charms":
        print("Ah, you've chosen Charms! Ready to add a little magic to your day?")
    elif category == "curses":
        print("Dive into curses, where dark spells ignite, face your fears and conquer the night!")
    elif category == "transfiguration":
        print("It`s time to turn your quiz skills into pure magical brilliance!")
    elif category == "summoning":
        print("Unlock the magic, and summon with grace, bring objects to you from any place!")
    else:
        print("Please pick a valid Category")




main()