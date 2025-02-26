#word_count.py

#lists
list_yes = ["yes", "yeah", "sure", "ok", "okay", "y", "yep", "yea", "ya", "ye"]
list_no = ["no", "nope", "n", "nah", "no thanks", "no thank you"]

#defining functions
#y_or_n
def y_or_n1():
    game_start = input("Do you want to try it out? ")
    while True:
        if game_start.lower() in list_yes:
            return "y"
        elif game_start.lower() in list_no:
            return "n"
        else:
            game_start = input("I'm sorry, I didn't understand that. Do you want me to count the words in a sentence? ")
def y_or_n2():
    game_start = input("Do you want to try it out again? ")
    while True:
        if game_start.lower() in list_yes:
            return "y"
        elif game_start.lower() in list_no:
            return "n"
        else:
            game_start = input("I'm sorry, I didn't understand that. Do you want me to count the words in a sentence? ")

#counting
def counting_words(sentence):
    words = sentence.split()
    count = len(words)
    print("The number of words in your sentence is: " + str(count) + ".")

#presentation
name = input("Hello! What's your name? ").strip().title()
name_sep = (name.split())
first_name = name_sep[0]
print("Nice to meet you, " + first_name + "!")
print("My name is EVA and I'm a program whose task is to count the number of words in a sentence.")

#game
answer = y_or_n1()

if answer == "y":
    sentence = input("Great! Let's get started. Type in a sentence and I'll count the number of words in it. ")
    counting_words(sentence)
    while True:
        answer = y_or_n2()
        if answer == "y":
            sentence = input("Let's go! Type in another sentence. ")
            counting_words(sentence)
        elif answer == "n":
            print("Okay. Thank you for playing! Bye!")
            break
elif answer == "n":
    print("That's okay. Sadly that's the only thing I can do... for now. Maybe next time. Bye!")