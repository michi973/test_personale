#word_count.py

#lists
list_yes = ["yes", "yeah", "sure", "ok", "okay", "y", "yep", "yea", "ya", "ye"]
list_no = ["no", "nope", "n", "nah", "no thanks", "no thank you"]

#defining functions
def get_yes_or_no(prompt):
    response = input(prompt).lower()
    while True:
        if response in list_yes:
            return "y"
        elif response in list_no:
            return "n"
        else:
            response = input("I'm sorry, I didn't understand that. Do you want me to count the words in a sentence? ")

def counting_words(sentence):
    words = sentence.split()
    count = len(words)
    print(f"The number of words in your sentence is: {count}.")

#presentation
name = input("Hello! What's your name? ").strip().title()
name_sep = (name.split())
first_name = name_sep[0]
print(f"Nice to meet you, {first_name}!")
print("My name is EVA, I'm a program whose task is to count the number of words in a sentence.")

#game
answer = get_yes_or_no("Do you want to try it out? ")

if answer == "y":
    sentence = input("Great! Let's get started. Type in a sentence and I'll count the number of words in it. ")
    counting_words(sentence)
    while True:
        answer = get_yes_or_no("Do you want to try it out again? ")
        if answer == "y":
            sentence = input("Let's go! Type in another sentence. ")
            counting_words(sentence)
        elif answer == "n":
            print("Okay. Thank you for playing! Bye!")
            break
else:
    print("That's okay. Sadly that's the only thing I can do... for now. Maybe next time. Bye!")