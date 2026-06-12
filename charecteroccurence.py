string = input("Please enter ypur own word: ")
char = input("Please emter your own Character :")
i = 0 
count = 0 
while(i < len(string)):
    if(string[i] == char):
        count = count + 1
    i = i + 1
print("The total Number of Times ", char, "has Occured=", count)
        