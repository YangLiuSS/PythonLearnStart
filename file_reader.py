with open('pi_digits.txt') as file_object:
    #contents = file_object.read()
    #~ for line in file_object:
    #~ print(contents.rstrip())
            #~ print(line.rstrip())
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    #~ pi_string += line.rstrip()
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))
            

