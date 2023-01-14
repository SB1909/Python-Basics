print("Question No.03:-")

#Ans1:
def word(x):
    vowels=0
    consonants=0
    for i in x:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            vowels=vowels+1
        else:
            consonants=consonants+1   
    print("Number of vowels present=:",vowels,"\nNumber of consonants present=:",consonants)
    return
y=(input("Enter a word:"))
word(y.lower())


#Ans2:
def word_1(x):
    vowels=list(filter(lambda i:i=="a" or i=="e" or i=="i" or i=="o" or i=="u",x))
    consonants=len(x)-len(vowels)
    print("Number of vowels present=:",len(vowels),"\nNumber of consonants present=:",consonants)
    return
y=(input("Enter a word:"))
word_1(y.lower())
