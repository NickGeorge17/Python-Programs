with open('numbers.txt',"r") as n:
    data = n.readlines()
#search algorithm
search = int(input('What number would you like to call? 1-100'))
print(data[search - 1])
n.close()

#edit algorithm
yn = input('Would you like to make a change?')
showStr = str(search)
if yn ==('yes'):
    with open('numbers.txt',"r+") as r:
        lines = r.readlines()
        print('Now editing', lines[search - 1])
        edit = input('What would you like it to say?')
        for i, line in enumerate(lines):
            if line.startswith(showStr):
                lines[i] = (edit)
                r.seek(0)
                for line in lines:
                    r.write(line)
        print('Your edit:', lines[search - 1])
elif yn ==('no'):
    print('Ok!')

r.close()
