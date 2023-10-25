#print out the introduction
def print_intro():
    print("---Welcome to Python!---")

#print out a newline character
def print_newline():
    print("\n")

def change_str_case(string_var):
    new_string = ''
    
    for letter in string_var:
        if (letter.isupper()) == False:
            new_string += letter.upper()

        elif (letter.islower()) == False:
            new_string += letter.lower()

        elif (letter.isspace()) == True:
            new_string += (letter - 1).upper()


    return(new_string)