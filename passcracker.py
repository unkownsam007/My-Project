import hashlib

 
 
def hash(wordlistpassword):
    result = hashlib.sha1(wordlistpassword.encode())
    return result.hexdigest()
 
 
def bruteforce(guesspasswordlist, actual_password_hash):
    for guess_password in guesspasswordlist:
        if hash(guess_password) == actual_password_hash:
            print("Hey! your password is:", guess_password,
                  "\n please change this, it was present in the wordlist ")
            # If the password is found then it will terminate the script here
            exit()
 

actual_password = 'django123'
actual_password_hash = hash(actual_password)
#print(actual_password_hash)

with open('/home/rocky/cvp/dictionary.txt') as f:
    wordlist = f.read()
guesspasswordlist = wordlist.split()
# Running the Brute Force attack
bruteforce(guesspasswordlist, actual_password_hash)
 
# It would be executed if your password was not there in the wordlist
print(" It was not in the wordlist ")
 