import random


#to create the hanged man picture
def hangman(wrong):
    if wrong == 1:
        print ("        ______")
        print ("       |      |")
        print ("       |      |")
        print ("       |      O")
        print ("       |")
        print ("       |")
        print ("    -------")
        print ("   |       |")
        print ("   |       |")
        print ("    -------")

    elif wrong == 2:
        print ("        ______")
        print ("       |      |")
        print ("       |      |")
        print ("       |      O")
        print ("       |      |")
        print ("       |")
        print ("    -------")
        print ("   |       |")
        print ("   |       |")
        print ("    -------")

    elif wrong == 3:
        print ("        ______")
        print ("       |      |")
        print ("       |      |")
        print ("       |      O")
        print ("       |     /|")
        print ("       |")
        print ("    -------")
        print ("   |       |")
        print ("   |       |")
        print ("    -------")

    elif wrong == 4:
        print ("        ______")
        print ("       |      |")
        print ("       |      |")
        print ("       |      O")
        print ("       |     /|\\")
        print ("       |")
        print ("    -------")
        print ("   |       |")
        print ("   |       |")
        print ("    -------")

    elif wrong == 5:
        print ("        ______")
        print ("       |      |")
        print ("       |      |")
        print ("       |      O")
        print ("       |     /|\\")
        print ("       |      ^")
        print ("    -------  |")
        print ("   |       |")
        print ("   |       |")
        print ("    -------")

    else:
        print ("        ______")
        print ("       |      |")
        print ("       |      |")
        print ("       |      O")
        print ("       |     /|\\")
        print ("       |      ^")
        print ("    -------  | |")
        print ("   |       |")
        print ("   |       |")
        print ("    -------")



    





#the word options
cat = ["C", "A", "T"]
bat = ["B", "A", "T"]
sketch = ["S", "K", "E", "T", "C", "H"]
monkey = ["M", "O", "N", "K", "E", "Y"]
fish = ["F", "I", "S", "H"]
pony = ["P", "O", "N", "Y"]
money = ["M", "O", "N", "E", "Y"]
monster = ["M", "O", "N", "S", "T", "E", "R"]
word_list = [cat, bat, sketch, monkey, fish, pony, money, monster]


#welcome them
print ("Welcome to hangman!")

start = 0

while start == 0:

    #do they want to play
    play = input("""
Do you want to play? (yes or no) """)






    #to make sure they didn't have a typo
    if play.isalpha() == True and (play.lower() == "yes" or play.lower() == "y" or play.lower() == "no" or play.lower() == "n"):




        #if they want to play
        while play.lower() == "yes" or play.lower() == "y":
            #the alphabet/letter choices
            alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

            #pick the word
            word = random.choice(word_list)

            #number of guesses
            number_of_guesses = 6




            #number of times wrong
            wrong = 0

            #the parts of the word that are revealed
            revealed_parts_of_word = []

            #this will store the number of letters that still need to be figured out
            letters_left = len(word)

            #stores the used letters
            used_letters= []

            









            while (number_of_guesses > 0) and (letters_left != 0):
                #this list will hold the indexes of the letters
                revealed_letters_index = []

                #determines if a letters been used before
                used = "no"
                

                
                
                print ("""
You have %s guesses
""" % (number_of_guesses))

                print (" ".join(alphabet))
                print ("")







                

                #for the first try
                if len(revealed_parts_of_word) == 0:
                    #this creates as many blank spaces as there are letters in the word
                    letter_spaces = len(word) * ["_"]

                    print (" ".join(letter_spaces))

                else:
                    print (" ".join(revealed_parts_of_word))

                








                
                #to get their guess
                guess = input("""
What letter do you guess? """)




                #checks and sees if the player entered letters
                if guess.isalpha() == True and len(guess) == 1:

                    for letter in used_letters:
                        if guess.upper() == letter:

                            used = "yes"

                    if used == "no":

                        #adds used letters to the used letters list
                        used_letters.append(guess.upper())


                            #checks to see if the letter is in the word
                        if (guess.upper() in word) == True:
                            letters_left -= 1
                                
                            print("""
That's one of the letters!""")

                            if letters_left == 0:
                                print ("""
You win!""")


                            #to check and see if there are multiples of the same letters
                            for letter in word:
                                if guess.upper() == letter:
                                    revealed_letters_index.append(word.index(guess.upper()))

                            #to show the parts of the word that are revealed for the first time
                            if len(revealed_parts_of_word) == 0:
                                blank_spaces = (len(word) - len(revealed_letters_index)) * ["_"]

                                revealed_parts_of_word = blank_spaces

                                for index in revealed_letters_index:
                                    revealed_parts_of_word.insert(index, guess.upper())

                            else:
                                for index in revealed_letters_index:
                                    #removes blank spaces
                                    revealed_parts_of_word.pop(index)
                                    #puts the letter in the list
                                    revealed_parts_of_word.insert(index, guess.upper())



                            #Removes the answer from the list of options
                            alphabet.remove(guess.upper())

                                







                        #if the letter isn't in the word
                        else:
                            print("""
That letter is not in the word.""")

                            number_of_guesses -= 1
                            wrong += 1

                            #removes the option from the choices
                            alphabet.remove(guess.upper())

                            #prints the hangman
                            hangman(wrong)

                            if number_of_guesses == 0:
                                print ("""
You lose!""")




                    else:
                        print ("""
You already typed that letter!""")



                else:
                    print ("""
You need to print only one letter!""")




                

            play = input("""
Do you want to play again? (yes or no) """)
                








        if play.lower() == "no" or play.lower() == "n":
            print ("""
Thank you for coming to hangman!  Have a nice day!""")

            start = 1

            input()



    else:
        print ("""
You need to enter yes or no!""")








