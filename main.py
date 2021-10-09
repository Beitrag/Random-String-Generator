import random
import string

def get_random_string(length):
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    file = open("String.txt", "a")
    file.write(result_str +"\n")
    file.close 
for x in range(1): # How many should be created?
     print(x)
     get_random_string(3) # lenght of the String 

# Creator : Beitrag Github
