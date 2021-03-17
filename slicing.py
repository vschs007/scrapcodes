s=input()     #taking input
n=len(s)
s1 = s[0:n-1:2]      #slicing the string starting from 0 index to second last with 2 steps
s2= s[1:n:2]         #slicing the string starting from 1 index to last index with 2 steps
print("Phrase 1:"+s1)       #printing
print("Phrase 2:"+s2)
