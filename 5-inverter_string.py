mystring = input('Favor digite uma string qualquer: ')

reversed_string = []
string_reverse_index = len(mystring)

for i in range(string_reverse_index):
    reversed_string.append(mystring[string_reverse_index - 1])
    string_reverse_index -= 1

print(''.join(reversed_string))