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

    questions = {
         'charms': [
            {
                'question': 'What is the incantation for the Levitation Charm?',
                'options' : ['A. Accio', 'B. Wingardium Leviosa', 'C. Lumos', 'D. Expelliarmus'],
                'answer' : 'B',
                'bonus': False
            },
            {
                'question': 'What spell is used to unlock door?',
                'options' : ['A. Colloportus', 'B. Reparo', 'C. Alohomora', 'D. Nox'],
                'answer': 'C',
                'bonus': False
            },
            {
                'question': 'Which charm is used to disarm an opponent?',
                'options' : ['A. Protego', 'B. Stupefy', 'C. Incendio', 'D. Expelliarmus'],
                'answer': 'D',
                'bonus': False
            },
            {
                'question' : 'Which charm is creates light at the tip of your wand?',
                'options': ['A. Lumos', 'B. Incendio', 'C. Rictusempra', 'D. Reparo'],
                'answer': 'A',
                'bonus': False
            },
            {
                'question' : 'BONUS!!!! The Fidelius Charm is a complex spell that does what?',
                'options' : ['A. Prevents any sound from being heard outside a certain area','B. Makes a location invisible', 'C. Hides a secret within the sould of a person','D. Allows one to speak in a different language'],
                'answer' : 'C',
                'bonus': True
            
            }
    
         ],

         'curses': [
            {
                'question': 'Which curse is known to cause unbearable pain?',
                'options' : ['A. Sectumsepra', 'B. Avada Kedavra', 'C. Imperio','D. Crucio'],
                'answer' : 'D',
                'bonus': False

            },
            {
                'question' : 'Which curse did Professor Snape invent to cause sever lacerations on the target?/n',
                'options' : ['A. Reducto', 'B. Incendio', 'C. Sectumsempra', 'D. Diffindo'],
                'answer' : 'C',
                'bonus': False
            },
            {
                'question': 'What is the incantation for the Killing Curse?/n',
                'options' : ['A. Imperio', 'B. Avada Kedavra', 'C. Confringo', 'Rictumsempra'],
                'answer': 'B',
                'bonus': False
            },
            {
                'question': 'The Imperius Curse is used to do what?/n',
                'options': ['A. Control another persons actions', 'B. Kill the target instantly', 'C. Cause a person to speak in riddles','D. Trap the victim in an endless nightmare'],
                'answer': 'A',
                'bonus': False
            },
            {
                'question': 'BONUS!!!! What is the effect of the Morsmordre curse?/n',
                'options': ['A. Causes the target to fall asleep instantly', 'B. Cause intense itching and discomfort', 'C. Conjures the Dark Mark in the sky', 'D. Makes the targets tongue stick to the roof of their mouth'],
                'answer': 'C',
                'bonus': True
            }
        ],

         'summoning': [
            {
                'question': 'What is the incantation for the Summoning Charm?',
                'options' : ['A. Evanesco', 'B. Accio', 'C. Protego', 'D. Expelliarmus'],
                'answer' : 'B',
                'bonus': False
            },
            {
                'question' : 'What is the limitation of the summoning charm to retrieve the bag of galleons during a mission?',
                'options': ['A. It can only summon objects lighter than a feather', 'B. None. It can summon any object', 'C. It can only summon objects within a certain distance', 'D. '],
                'answer': 'C',
                'bonus': False
            },
            {
                'question': 'What magical object is specifically mentioned as being difficult to summon because of its complex properties?',
                'options': ['A. The Sorting Hat', 'B. The Sword of Gryffindor', 'C. The Marauder\'s Map', 'D. The Invisibility Cloak'],
                'answer': 'B',
                'bonus' : False
            },
            {
                'question' : 'Which ancient magical text is known to have first documented the summmoning charm?',
                'options' : ['A. The Book of Spells', 'B. History of Magic', 'C. Magical Theory and Practice', 'D. Advanced Magical Theory'],
                'answer': 'A',
                'bonus': False

            },
            {
                'question' : 'BONUS!!!! Which magical creature was known for its ability toavoid being summoned by the Accio charm due to its natural magical properties?',
                'options' : ['A. House Elf', 'B. Thestral', 'C. Niffler', 'D. Hippogriff'],
                'answer' : 'C',
                'bonus': True
            }
        ],
         'transfiguration': [
            {
                'question': 'What is the incantatopm for the spell used to turn a teacup into a tortoise?',
                'options': ['A. Tortus', 'B. Switching Spell', 'C. Transfiguro', 'D. Switcheroo'],
                'answer': 'B',
                'bonus': False
            },
            {
                'question': 'Which charm is used to perform partial Transfiguration, such as changing color or texture?',
                'options': ['A. Duro', 'B. Colorado', 'C. Reparo', 'D. Partus Transfigura'],
                'answer' : 'A',
                'bonus': False
            },
            {
                'question': 'What is the incantation used to transform a solid object into a liquid form?',
                'options': ['A. Aqua Transformare', 'B. Liquifacio', 'C. Aguamenti', 'D. Evanesco'],
                'answer' : 'C',
                'bonus': False

            },
            {
                'question' : 'What is the primary limitation of Transfiguration Spells?',
                'options' : ['A. They only work during the daylight', 'B. They are temporary and require constant concentration', 'C. They cannot be performed on living creatures', 'D. They require precise incantation and wand movement'],
                'answer' : 'D',
                'bonus': False
            },
            {
                'question' : 'BONUS !!!! Which book does Professor McGonagall demonstrate her Animagus form for the first time?',
                'options' : ['A. Harry Potter and the Philosopher\'s Stone', 'B. Harry Potter and the Chamber of Secrets', 'C. Harry Potter and the Prisoner of Azkaban', 'D. Harry Potter and the Half-Blood Prince'],
                'answer' : 'C',
                'bonus': True
            }
        ]
    }


    category = (input("Please choose a spell category: charms, curses, summoning, or transifiguration\n")).strip().lower()
    print()

    if category in questions: 
        if category == "charms":
            print("Ah, you've chosen Charms! Ready to add a little magic to your day?\n")
        elif category == "curses":
            print("Dive into curses, where dark spells ignite, face your fears and conquer the night!\n")
        elif category == "transfiguration":
            print("It`s time to turn your quiz skills into pure magical brilliance!\n")
        elif category == "summoning":
            print("Unlock the magic, and summon with grace, bring objects to you from any place!\n")

        score = 0
        for question in questions[category]:
            print(question['question'])
            for option in question['options']:
                print(option)
            print()

            while True:
                answer = input("Please select A, B, C, D:\n").strip().upper()
                if answer in ['A', 'B', 'C', 'D']:
                    break
                else:
                    print('Invalid selection. Please choose A, B, C, or D')

            if answer == question['answer']:
                print('Correct')
                if question.get('bonus', False):
                    score += 10  # Bonus question
                else:
                    score += 5  # Regular question
            else:
                print(f"Incorrect. The correct answer is {question['answer']}.")

            print()

        print(f"Your total score is: {score} points.")
    else:
        print("Please pick a valid category.")

main()