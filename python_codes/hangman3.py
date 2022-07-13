import random
word_list=["advarak","baboon","camel"]
chosen_word=random.choice(word_list)
print(f"the chosen word is {chosen_word}")
display=[]
for _ in chosen_word:
    display+="_"
print(display)
guess=input("guess a letter: ")
for position in range(len(chosen_word)):
    letter=chosen_word[position]
    if letter==guess:
        display[position]=letter
print(display)