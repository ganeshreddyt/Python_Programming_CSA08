#to_return_updated_string...
def updated_string(string, char):
     if len(char) > 1:
        return 'Why are you entered a string instead char...'+string
     else:
        return string.replace(char,'')
#main_function
string = input('Can I get a string pls :')
char = input('Put a char to hide it in string :')
print(updated_string(string, char))
