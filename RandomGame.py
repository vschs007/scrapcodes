import random
def main():
  myNumber=random.randint(1,10)   # generates random number between 1-10 and stores in myNumber
  print("Welcome to my Guess the number program!")
  count=1                         #initialising count to 10
  while True:                     #loops always runs, no conditions checked
    guess=input("Please guess a number between 1 and 10:")
    if guess.isalpha()==True:      # check if the input has alphabets
      print ("Number only!")
      continue                     # go back to the beginning of the loop , i.e if input in alphanumeric, prompts user to reinput the number
    else:
      guess=int(guess)             #converting the input to int vaues
      if guess==myNumber:          # if input number becomes equal to the guess number then print success and print the count value
        print("You guessed it! It took you",count,"attempts")
        break
      elif guess<0:           #if we have entered negative number, takes us back to the starting of the loop to re enter the number.
        continue
      elif guess<myNumber:
        print("Too low")      #if input number is less than generated number print too low
        count+=1              # increase the count to 1 as we have taken one attempt to valid guess
      elif guess>myNumber:    #if input number is greater than generated number print too high
        print("Too high")
        count+=1              # increase the count to 1 as we have taken one attempt to valid guess

if __name__ =="__main__":        # calling main function
   main()