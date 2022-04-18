#user inputs for the day, color, and first name
dayofMonth = str(input('Enter the day you were born (ie. 03): '))
favoriteColor = str(input('Enter your favorite color: '))
firstName = str(input('Enter your first name: '))

#All of my string slices and capitalize function
passwordFirstName = firstName[-2:]
passwordColor = favoriteColor[0:3]
passwordCapitalFirstName = firstName.capitalize()[0:1]

#Final print, there is two different lines so
#I can use the sep= function to put all the leters together without spaces
print('Based off of that information, your new password is: ')
print(passwordFirstName,dayofMonth,passwordColor,passwordCapitalFirstName,'**',sep='')
