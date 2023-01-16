from random import *
from sys import *

username_list = ["user1","user2","user3","user4"]
password_list = ["psw1","psw2","psw3","psw4"]
def password_generation(number_of_initials:int):
    """Parooli isegenereerimine
    Args:
        number_of_initials (int): _sümbolite arv_
    Returns:
        _type_: _tagastab uus parrol_
    """
    
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3 
    ls = list(str4)
    shuffle(ls)
    # Извлекаем из списка 12 произвольных значений
    psword = ''.join([choice(ls) for x in range(number_of_initials)])
    # Пароль готов
    print("Yours generated password is: ", psword)
    return psword

def user_choises():
    """Funktsioon annab kasutajale valik: kas sisseloogida voi registreeruda
    """
    print("Hello! I'm yours helper! \nPlease, make an accout or log in!")
    while True:
        try:
            valik = int(input("\nIf you want to make a new accout - enter number 1,\nif you want to log in - enter number 2,\nif you want to exit - enter number 3\n--------> "))
        except:
            print("Enter the number!")
        if valik == 2:
            user_login()
        elif valik == 1:
            user_reg()
            user_login()
        elif valik == 3:
            exit()

def user_login():
    """Funktsioon teeb sisselogimis protsessi

    """
    username = input("\nPlease enter your username --> \n")
    try:
        if username in username_list:
            a = username_list.index(username)
            for i in range(3):
                password = input("\nPlease, enter the password --> \n")
                if password == password_list[a]:
                    print("Log in succesfully!")
                    break
                else:
                    print("\nWrong password!",(1+i))
        else:
            print("Worng username!")
    except:
        print("Error!")
              
def user_reg():
    """Kasutaja loob endale uus konto.
    Returns:
        _type_: tagastab password
    """
    username = input("Please, enter a new username --> \n")
    while username in username_list:
        print("This username in used! Please, choose the other one!")
        username = input("Please, enter a new username --> \n")
    else:    
        username_list.append(username)
    password = input("If you want to generate password - enter number 1,\nif you want to use yours password - enter number 2.\n ------> ")
    if password == "1":
        try:
            num = int(input("Enter the initials amount --> "))
        except:
            print("You must enter a number!")
        password_generation(num)
        password_list.append(password_generation(num))
    elif password == "2":
        sala = input("Enter new password --> \n")
        while password_control(sala) != True:
            sala = input("Enter new password --> \n") 
            if password_control(sala) == True:
                password_list.append(sala)
    return password
        
def password_control(password:str):
    """Func kontrollib salasona.
    Args:
        password (str): _salasona mis paneb ise kasutaja_
    Returns:
        _type_: return True or False.
    """
    password = list(password)

    num = len(password)
    k = 0
    l = 0
    o = 0
    for i in range(num):
        if password[i].isdigit():
            k += 1
        else:
            k += 0
        if password[i].isupper():
            l += 1
        else:
            l += 0
        if password[i].isalpha() == True:
            o += 1
        else:
            o += 0
    if k > 0 and l > 0 and o > 0:
        #print(True)
        return True
    else:
        print("Password must be consist of digits letters and capital letters!")
        return False


user_choises()
