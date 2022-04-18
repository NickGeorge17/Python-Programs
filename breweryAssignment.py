#This part opens the texts file and creates a new one for processed data
try:
    inFile = open('breweries_us.txt', 'r')
    outFile = open('breweries_ny.txt', 'w')
    counter = 0
except:
    print('File ', inFile,  'not found.')
else:
    line = inFile.readline()
#It reads the line, and if 'new-york' is in the line it adds a counter
#prints it in the file, prints a space, and then I strip the line it read
#print it on the line of the new text file, then create a new line
#it then reads the line below it and repeats the process
    while line:
        if 'new-york' in line:
            counter = counter + 1
            outFile.write(str(counter))
            outFile.write('    ')
            outFile.write(line.rstrip())
            outFile.write('\n')
        line = inFile.readline()

#Prints two new lines and then prints a sentence and then prints the final
#counter
    outFile.write('\n')
    outFile.write('\n')
    outFile.write('The amount of breweries in NY is, ')
    outFile.write(str(counter))

#Print final counter for troubleshooting purposes and then closes the file
    print(counter)
    inFile.close()
    outFile.close()
