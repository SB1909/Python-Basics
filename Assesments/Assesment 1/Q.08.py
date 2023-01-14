#Ans:1
def limit(x):
    t_sum=0
    for i in range(x+1):        #in range function: it will take number until limit-1, so we have to add 1
        if i%3==0 or i%5==0:
            t_sum=t_sum+i       #t_sum=t_sum(previous value)+i(new multiple)
            i=i+1               #i=i+1 is not necessary in this...why?
    return  print("Total sum of multiples of 3 & 5 between 0 to",x,":",t_sum)
limit(int(input("Enter the limit number:")))


#Ans:2
def limit(x):
    L=list(range(x+1))
    l=list(filter(lambda i:i%3==00 or i%5==0,L))
    return print("Total sum of multiples of 3 & 5 between 0 to",x,":",sum(l))
limit(int(input("Enter the limit number:")))
       
