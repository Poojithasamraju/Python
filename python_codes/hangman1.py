import random
word_list=["advarak","baboon","camel"]
chosen_word=random.choice(word_list)
#print(chosen_word)
total_letters=len(chosen_word)
#print(total_letters)
guess=""
guess=input("guess the letter: ")
for letter in chosen_word:

    if letter==guess:
        print("right")
    else: 
        print("wrong")
