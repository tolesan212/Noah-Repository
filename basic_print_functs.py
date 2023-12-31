#print out the introduction
def print_intro():
    print("---Welcome to Python!---")

#print out a newline character
def print_newline():
    print("\n")

#define a function
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

#editing directly with Github editor is probably not a good practice...
#better practice: create a local branch with git 
#push local branch onto Github branch

#had to use git pull to retrieve lines 27 and 28

#created new branch on local machine
#executed git branch newlocal1, git checkout newlocal1 (to switch)
#made changes, git add ., git commit -m, git push (results in error: no upstream branch)
#to resolve error, use "git push --set-upstream origin newlocal1" instead of git push