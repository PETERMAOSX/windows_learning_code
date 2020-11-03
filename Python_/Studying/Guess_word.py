import random
WORDS = ("python","jumble","easy","difficult","answer","continue","phone","position","pose","game")
print(
    '''
        Welcom to The guess word game
    make the random become the right word
    
    '''
)
iscontinue = "y"
while iscontinue=="y" or iscontinue=="Y":
    word = random.choice(WORDS)
    correct = word
    jumble = ""
    while word:
        position = random.randrange(len(word))
        jumble+=word[position]
        word = word[:position]+word[(position)+1:]
    print("Random word is : "+jumble)
    guess = input("\nPlease guess: ")
    while guess != correct and guess!="":
        print("sorry you are wrong")
        guess = input("contiune guess: ")
        if guess == correct:
            print("year you are right")
        iscontinue = input("is contiune?(Y/N): ")