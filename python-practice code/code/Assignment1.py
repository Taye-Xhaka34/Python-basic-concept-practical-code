#list with username and password
us_list = ["Nathan", '2313', "Geez", 'pass231', "Abebe", '092313133', "Miki", "pl3s34D0n'tH4ckM3"]
#list to dictionary
users = { }
index = 0
while index < len(us_list):
    username = us_list[index]
    password = us_list[index + 1]
    users[username] = password
    index = index + 2   # go to next pair

# give 5 tries
t = 0
success = False

while t < 5 and success == False:
    name = input("Enter username: ")
    passwd = input("Enter password: ")

    if name in users:
        if passwd == users[name]:
            print("Welcome to GTST Company!")
            success = True
        else:
            print("Incorrect Login!")
            t = t + 1
    else:
        print("Incorrect Login!")
        t = t + 1

if success == False:
    print("Sorry u are limited!")
