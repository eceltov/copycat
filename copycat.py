import shutil
import os

def userInput(answer):
    global whitelist
    if (answer.lower() == "i"):
        whitelist = ["png", "gif", "jpg", "jpeg"]
        return True
    if (answer.lower() == "m"):
        whitelist = ["mp3", "wav", "mp4"]
        return True
    if (answer.lower() == "c"):
        print("Please write the extensions of expected files: (example format: wav jpeg png)")
        whitelist = input().split()
        return True
    else:
        return False

def copytree(src, dst, symlinks=False, ignore=None):
    global cnt
    global min_file_size
    global blacklist
    global whitelist
    global flag

    dirs = os.listdir(src)

    for i in range(len(dirs)):
        s = os.path.join(src, dirs[i])
        d = os.path.join(dst, dirs[i])
        #print(s)
        cnt = cnt + 1
        if (cnt%1000 == 0):
            print(cnt)
        if not(any(x in s.lower() for x in blacklist)):
            try:
                if os.path.isdir(s):
                    copytree(s, dst)
                else:
                    tokens = s.split('.')
                    if len(tokens) > 0:
                        last = tokens[-1]
                        for x in whitelist:
                            if x == last and (os.path.getsize(s) > min_file_size):
                                print(flag)
                                print("Copying: " + s)
                                shutil.copy(s, d)
                                print("Copying Successfull")
                                print(flag)

            except:
                print("Failed to access directory: " + s)


flag = "-----------------------------------------------------------------------------"
whitelist = []
blacklist = ["microsoft", "windows"]
min_file_size = 1024*1024

print(flag)
print("Welcome to CopyCat, your friendly file retriever")
print("This program will copy all selected file types from source drives to destination_drive:/depository")
print("Please mind that it will not copy from protected or otherwise inaccessible directories")
print(flag)

print("Which types of files would you like to copy? Enter I for images, M for music or C for custom:")
while not(userInput(input())):
    print("Wrong input, please enter I, M or C to continue")

print("Source Drives: (example format: C D E)")
source_drives = input().split()

print("Output Drive: (example format: I)")
output_drive = input().upper()
destination = output_drive + ":\depository"
if not(os.path.isdir(destination)):
    os.mkdir(destination)

cnt = 0

for drive in source_drives:
    cnt = 0
    print(flag)
    print("Copying from drive " + drive.upper() + ":/")
    print(flag)
    copytree(drive.upper() + ":/", destination)
