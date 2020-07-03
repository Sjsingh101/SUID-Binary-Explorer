#!/usr/bin/python3
#provide execute permission
import os
# scan system and find SUID Binaries
def scan_sys():
    os.system("echo `find / -perm -u=s -type f 2>/dev/null` > scan.txt")

#get data
def get_info():
    if not os.path.isdir("_gtfobins"):
        try:
            os.system("gitdir https://github.com/GTFOBins/GTFOBins.github.io/tree/master/_gtfobins")
        except:
            print("check whether svn is installed or not")

def list_suid():
    with open("scan.txt") as file:
        data = file.read()
    commands = data.split()
    bins=[]
    for command in commands:
        bins.append(command.split('/')[-1])
    bins= set(bins)
    return bins

def list_vul_suid(bins):
    vul=[]
    files = os.listdir('_gtfobins')
    for entry in bins:
        if entry+'.md'in files:
            #print(entry)
            vul.append(entry)
    return vul

def get_doc(cmd):
    with open('_gtfobins/'+cmd+'.md') as file:
        data = file.read()
    return data

if __name__ == "__main__":
    scan_sys()
    get_info()
    suid = list_suid()
    vul_suid = list_vul_suid(suid)
    for entry in vul_suid:
        print(get_doc(entry))
