import random

print("hello")
print("""  __   __
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/""")
Max_tries=random.randint(5,100)
print(Max_tries)
player_guss=input("guss a letter")
print(player_guss)

#3.5.2
x=input("please enter a word:")
word_legth=len(x)
word_legth*=1
y=word_legth*"_"
print(y)

#4.3.1



if(len(player_guss)==1):
    if(player_guss.isalpha()):
        print(player_guss.lower())
    else:
        print("E2 letter is not english")
elif (player_guss.isalpha()):
    print("E1-type please only one letter")
else:
    print("E3")

#5.5.1
# התנאי  if name מפריע לפעילות התוכנית ??
def is_valid_input(letter_guesed):
    """פונקציה המקבלת תו ובודקת ואם חוקי מחזירה ערך TRUE"""
    if len(letter_guesed) == 1 and letter_guesed.isalpha():
        return True
    else:
        return False


def main():
    kelet=input("pls")
    print(is_valid_input(kelet))
#if _name_ == "_main_":
main()

# 6.4.1
def check_valid_input(letter_guessed ,old_letter_guessed):
    if len(letter_guessed) == 1 and letter_guessed.isalpha():
        if  letter_guessed not in old_letter_guessed:
            old_letter_guessed+=letter_guessed

            print(old_letter_guessed)
            return True
        else:
            print("X\n"+"->".join(old_letter_guessed))
            return False


    else:
       print("elegal")
       return False

def main():
    x="abddddd"
    y="a"
    print(check_valid_input(y,x))


main()

#7.3
def check_valid_input(secret_word ,old_letter_guessed):
    s=""
    for i in secret_word:
        if i in old_letter_guessed:
            s+=(" " + i)
        else:
            s+=" _"
    return s

def main():
    secret="avinoam"
    old=["a","o","m","b"]
    print(check_valid_input(secret,old))


main()

#8.2.1
x=("self","py",1.543)
y="hello %s %s lerner you have only %.1f units left before you master the  course!"
print (y %x)

#8.4.2
def print_hangman(a,num_of_tries):
    print(a[num_of_tries])


def main():
    d={1:"""    x-------x""",
       2:"""    x-------x
    |
    |
    |
    |
    |""",
       3:"""x-------x
    |       |
    |       0
    |
    |
    |""",
       4:"""    x-------x
    |       |
    |       0
    |       |
    |
    |""",
       5:""" x-------x
    |       |
    |       0
    |      /|\\
    |
    |""",
       6:"""    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""",
       7:"""    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}

    print_hangman(d,6)
main()