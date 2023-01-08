import zipfile
from tqdm import tqdm

# Python external library tqdm, to create simple & hassle-free progress bars which you can add to your code and make it look lively! 

wordlist = "/usr/share/wordlists/rockyou.txt"
#kali-linux dictionary-attack file path: /usr/share/wordlists/rockyou.txt 
# the zip file you want to crack its password
zip_file = "/home/kali/Documents/crackit.zip"
#print(zip_file)
zip_file = zipfile.ZipFile(zip_file)
#print(type(zip_file))
# count the number of words in this wordlist
n_words = len(list(open(wordlist, "rb")))
# print the total number of passwords
print("Total passwords to test:", n_words)

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:                                       # extractall(pwd = password) 
            zip_file.extractall(pwd=word.strip()) #The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.")

