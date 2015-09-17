#MIT Coursware EE&CS

lastname = input('Enter your last name: ')
while lastname.isalpha() == False:
    lastname = input('Enter your last name: ')

firstname = input('Enter your first name: ')
while firstname.isalpha() == False:
    firstname = input('Enter your first name: ')

print(firstname +' ' + lastname)



