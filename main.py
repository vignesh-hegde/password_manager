from random import randint as ri
import time
import password_manager
import display

cs = display.ClearScreen()

def start_up_screen():

    print("+--------------------------------------------------+")
    print('|                PASSWORD MANAGER v 1.0            |')
    print("+--------------------------------------------------+")
    items = list(range(0, 10))

    for item in display.progressBar(items, prefix='Progress:', suffix='Complete', length=50):
        time.sleep(0.1)
    cs.clear()


def end_screen():

    print("+--------------------------------------------------+")
    print('|    THANK YOU FOR USING PASSWORD MANAGER v 1.0    |')
    print('|                 by Vignesh Hegde                 |')
    print("+--------------------------------------------------+")
    items = list(range(0, 20))

    for item in display.progressBar(items, prefix='Progress:', suffix='Complete', length=50):
        time.sleep(0.1)
    cs.clear()

if __name__ == "__main__":
    m_p_reset_ch = chr(ri(58, 91)) + str(ri(0, 9)) + chr(ri(97, 125)) + str(ri(0, 9))


    start_up_screen()


    try:
        m_pass = input("Enter Master Password : ")
        pm = password_manager.PasswordManager(m_pass)
        cs.clear()

    except :
        print("Wrong Password.")
        input()
        exit()

    while True:
        print("++===========================================++")
        print("||                    MENU                   ||")
        print("++===========================================++")
        print("||   1. List all password.                   ||")
        print("||   2. Password by site.                    ||")
        print("||   3. New password.                        ||")
        print("||   4. Update password.                     ||")
        print("||   5. Delete password.                     ||")
        print("||   x. Exit                                 ||")
        print("++-------------------------------------------++")
        print(f"||  ENTER {m_p_reset_ch} to update Master password.    ||")
        print("++===========================================++")

        ch = input(">> ").strip()
        
        cs.clear()
        
        if ch == '1':
            data = pm.get_all_pass()
            for site, pass_wrd in data.items():
                print(f"{site} : {pass_wrd}")

        elif ch == '2':
            key = input("Enter Site : ")
            print(pm.get_pass_by_key(key))

        elif ch == '3':
            key = input("Enter New Site : ")
            value = input("Enter Site Password : ")

            if pm.add_new_entrie(key, value):
                print("Succefully added.")
            else:
                print("Already Exist, Try Updating.")

        elif ch == "4":
            key = input("Enter Site : ")
            value = input("Enter Site Password")

            if pm.update_entrie(key, value):
                print("Succefully updated.")
            else:
                print("Does not Exist, Try adding new.")

        elif ch == "5":
            key = input("Enter Site : ")

            if pm.del_entrie(key):
                print("Succefully deleted.")
            else:
                print("Does not Exist, Try again.")

        elif ch == m_p_reset_ch:

            print("YOU ARE ABOUT TO RESET YOUR MASTER PASSWORD MAKE SURE YOU REMEMBER IT.")

            sure = input("ARE YOU SURE TO CONTINUE? [y/n] ").upper()

            if sure == 'Y':
                mp_1 = input("ENTER NEW MASTER PASSWORD : ")
                mp_2 = input("RE-ENTER NEW MASTER PASSWORD : ")

                if mp_1 == mp_2:
                    pm.update_password(mp_2)
                    print("PASSWORD UPDATED.")
                    print("NOTE: Remember the password, there is no way to reset the password if forgotten!")
                else:
                    print("PASSWORD DIDNT MATCH.")
        
        elif ch.upper() == 'X':
            cs.clear()
            end_screen()
            exit()

        else:
            print("Invalid Choice.")
        
        cs.wait_and_clear(content= "\n  << GO BCAK")
