print("This program detects if two words are a palindrome!")

#This is my two counters to match the letters of the palindrome
counter1 = 0
counter2 = -1

#This is where I ask the User for the two words
forwardword = input("Enter your first word:")
backwordword = input("Enter your second word:")

#This is where the actual loop runs
if len(forwardword) == len(backwordword): 
    while forwardword[counter1] == backwordword[counter2] or backwordword[counter1] == forwardword[counter2]:
        counter1 += 1
        counter2 -= 1
        #print(counter1)
        #print(counter2)
        if len(forwardword) == counter1 + 1:
            print("It is a palindrome")
            break
        #else:
            #print("It is not a palindrome")
    else:
        print("It is not a palindrome")
else:
    print("It is not a palindrome")
