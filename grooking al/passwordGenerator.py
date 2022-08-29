import random
import string
from databaseConnection import createConnection, execute_query,execute_read_query
password = ''
username = ''

connection = createConnection('passwords.sqlite')

characters = string.punctuation + string.ascii_letters + string.digits
char_Array = []
for i in characters:
    char_Array.append(i)

def authenticate():
    global username, password
    
    if password == '' and username == '':
        username = input('enter username:  ')
        password = input('enter password:  ')
        if password != '' and username != '':
            select_user = f"""SELECT * FROM  users WHERE username = {username} AND password ={password};"""
            result = execute_read_query(connection, select_user)
            if result != None:
                print(result)
                return True
            else:
                user = f"""INSERT INTO users(username,password) VALUES({username}, {password});"""
                execute_query(connection,user)
                return True
    return False


def generatePassword(num):
    print(authenticate())
    password = ''
    for i in range(num):                     
        password =  password + random.choice(char_Array)
    return password

print(generatePassword(8))
print(generatePassword(8))
print(generatePassword(16))