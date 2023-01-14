print("Question No.01:-")
while True:
    def calculation(x,y):
        return print("Summation=:",x+y,"\nDifference=:",x-y) 
    calculation(x=float(input("Enter Value of x:")),y=float(input("Enter Value of y:")))
    next_step=input("Want to Continue Calcuation? (yes/no):")
    if next_step=="no":
        break
