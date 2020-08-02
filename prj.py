'''
this program will prompt user to enter username and password, 
then will run sha256 encryption to confirm that the password is correct

@Author: Arturo Reyes
'''
import subprocess

users = dict()

with open('users','r') as file:
    for i in file.readlines():
        users[i.split()[0]] = i.split()[1]
        
cont = 'y'
while cont == 'y':
    user = raw_input('Enter Username: ')
    paswd = raw_input('Enter Password: ')
    out = subprocess.Popen("./sha256.exe",stdin=subprocess.PIPE,stdout=subprocess.PIPE).communicate(paswd)[0]
    if user in users:
        if users[user] == out:
            print('Username and Password Correct!\n')
            
        else:
            print('Username or Password Incorrect\n')
    else:
        print('UserName or Password Incorrect\n')

    cont = raw_input('Continue?(y/n) ')
    
