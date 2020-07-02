import os
import prev_esc as pesc
import time 

uni_cnt = 70
def line(count):
    print('-'*count)

def welcome():
    os.system("clear")
    line(uni_cnt)
    welcome =    """
    \t\t▄   ▄
    \t\t█▀█▀█    
    \t\t█▄█▄█        WELCOME TO SUID          
    \t\t─███──▄▄     BINARIES EXPLOIT
    \t\t─████▐█─█                       
    \t\t─████───█
    \t\t─▀▀▀▀▀▀▀
    """
    print(welcome)
    line(uni_cnt)

def menu():
    os.system("clear")
    line(uni_cnt)
    welcome = """
    Choose an option from the list:

    1> List all SUID binaries in system
    2> List all SUID binaries commom with listed in GTFOBins
    3> Search information on particular GTFOBins listed binaries
    4> Exit 
    """
    print(welcome)
    line(uni_cnt)
    option = int(input("    Enter your choice >> "))    
    return option

def iscontinue_exec():
    option = input("\nPress enter to choose again or any other key to exit...\n")
    if not option :
        return False
    else:
        return True


if __name__ =='__main__':
    welcome()
    time.sleep(2)
    while (True):
        try:
            option = menu()
        except:
            print("Please enter a numeric value !!")
            break

        if option == 1:
            list_suid = pesc.list_suid()
            # save in file
            print(list_suid)
            print("\nYour results are saved in suid-list.txt")
            with open("suid-list.txt", "w") as fout:
                print(*list_suid, sep="\n", file=fout)
            if iscontinue_exec():
                break
        elif option == 2:
            list_suid = pesc.list_suid()
            list_vul_suid = pesc.list_vul_suid(list_suid)
            print(list_vul_suid)
            print("\nYour results are saved in vul-suid-list.txt")
            with open("vul-suid-list.txt", "w") as fout:
                print(*list_vul_suid, sep="\n", file=fout)
            if iscontinue_exec():
                break
        elif option == 3:
            option = input("    Enter SUID binary name : ")
            try:
                data = pesc.get_doc(option)
                os.system("clear")
                print("\t"+option +" binary details\n")
                print(data)
            except:
                print("Document not found")
            if iscontinue_exec():
                break
        elif option == 4:
            break