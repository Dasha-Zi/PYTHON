user_login = "adam"
user_pass = "Qwerty123456"

login = input ("Login: ")
password = input ("Password: ")

if (login == user_login) and (password == user_pass):
    print ("Secret is open")
else:
    print ("Locked")

crit1 = "red"
crit2 = "lock"

color = input ("Color:")
featrue = input ("Featrue: ")

if (color == crit1) or (featrue == crit2):
    print ("Buy it!")
else:
    print ("Еще посмотрю")