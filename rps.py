p1=input("Player 1?")
p2=input("Player 2?")
if p1 not in ('rock','paper','scissors'):      # validating the input
    print("This is not a valid Object selection")
if p2 not in ('rock','paper','scissors'):       # validating the input
    print("This is not a valid Object selection")

if(p1==p2):
    print("tie")
elif(p1=="rock" and p2=="scissors"):
    print("Player 1 wins.")
elif(p1=="rock" and p2=="paper"):
    print("Player 2 wins.")
elif(p1=="paper" and p2=="scissors"):
    print("Player  wins.")