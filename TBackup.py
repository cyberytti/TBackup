import os
os.system('neofetch')
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
def create():
    os.system('mkdir tbackup')
    os.system('mv tbackup /sdcard/')
def home():
    os.system('cd .. && cp -r home /sdcard/tbackup')
    print (y+'done')
def bal():
    os.system('cd .. && cp -r usr /sdcard/tbackup')
    print (y+'done')
def restore():
    print (b+'>>',"",r+'restoring.....')
    os.system('cd /sdcard/ && mv  tbackup /data/data/com.termux/files/home')
    print (y+'your data is saved in tbackup directory')

usr=input('''
1.Backup
2.restore
>>''')
if '1' in usr:
    create()
    usr2=input('''
1.Home
2.Usr
>>''')
    if '1' in usr2:
        print (b+'>>',"",r+'processing.....')
        home()
    elif '2' in usr2:
        print (b+'>>',"",r+'processing.....')
        bal()
    else:
        os.system('python TBackup.py')

elif '2' in usr:
    restore()
else:
    os.system('python TBackup.py')

