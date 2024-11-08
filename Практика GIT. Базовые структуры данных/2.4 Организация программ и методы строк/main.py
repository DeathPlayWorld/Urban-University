print("Hi, user! Please type first random word that appeared in your head (if you type nothing you will make Gregg mad!):")
my_string = str(input())
print("Ok, you typed word","'"+my_string+"'","it...")
#Checking letters:
if(len(my_string) > 1 or len(my_string) == 0):
    print("Contains", len(my_string),"letters!")
else:
    print("Contains", len(my_string),"letter!")
#Writing word with different cases:
print("With uppercase it will look like this:","'"+my_string.upper()+"'")
print("And with lowercase it will look like this:","'"+my_string.lower()+"'")
#Checking if there is difference with spaces and without them:
if(my_string.replace(" ", "") != my_string):
    print("If we remove all the spaces it will look like this:","'"+my_string.replace(" ", "")+"'")
else:
    print("If we remove all the spaces it will not change it's look:", "'"+my_string.replace(" ", "")+"'")
#Checking if you make Gregg mad!
if(len(my_string) != 0 and len(my_string) != 1):
    print("And finally, first and last letters of your word are:", "'"+my_string[0]+"'", "and", "'"+my_string[-1]+"'")
if(len(my_string) == 1):
    print("And finally, first and last letters of your word are same because you type only one letter as the word >:D :",
          "'"+my_string[0]+"'")
if(len(my_string) == 0):
    print("And finally, there is no first and last letter because you type nothing >:( "
          "(You thought Gregg would miss it!? Gregg is disappointed in you!")
