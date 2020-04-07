import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
possibilities = ['python', 'java', 'kotlin', 'javascript']
typed_words =[]
rand = random.choice(possibilities)

word_display = '-' * (len(rand))
while True:
    print("H A N G M A N")
    play_exit = input('Type "play" to play the game, "exit" to quit: ')
    if play_exit == "play" or play_exit == '"play"':
        i = 0
        while i < 8:
            print()
            print(word_display)
            a = input("Input a letter: ")

            if a in typed_words:
                print("You already typed this letter")
                continue
            elif len(a) > 1:
                print("You should print a single letter")
                continue
            elif a not in alphabet:
                print("It is not an ASCII lowercase letter")
                continue
            elif a == "exit" or a == '"exit"':
                break
            
            typed_words.append(a)
            if a in rand:
                for x in range(len(word_display)):
                    if rand[x] == a:
                        new_list = list(word_display)
                        new_list[x] = a
                        word_display = "".join(new_list)
            else:
                print("No such letter in the word")
                i += 1

            if word_display == rand:
                print(word_display)
                print("You guessed the word!")
                print("You survived!")
                break
        else:
            print("You are hanged!")
    
    elif a == "exit" or a == '"exit"':
         break
    
    elif play_exit == "exit" or play_exit == '"exit"':
        break

# print("Thanks for playing!")
