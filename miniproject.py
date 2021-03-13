
## welcome message 

print("\t\t\tWelcome to mini proj! \nThis application helps you to find the percentage of a letter in a message. \nKindly input your message here. \nKindly input the letter here.")

## User message input

user_message = input("This is my message ")

## user letter input

user_letter = input("this is my letter ")

## count letter in message 

letter_freq = user_message.count(user_letter)

## calculate percentage

total_chr = len(user_message)
percentage = int(letter_freq/total_chr*100)


# # print result 

print ("the count of", user_letter, "is", letter_freq )
print (f"the percentage of '{user_letter}' in '{user_message}' is {percentage} percent" )

