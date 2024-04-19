import os



import platform 







# Color snippets



black="\033[0;30m"



red="\033[0;31m"



bred="\033[1;31m"



green="\033[0;32m"



bgreen="\033[1;32m"



yellow="\033[0;33m"



byellow="\033[1;33m"



blue="\033[0;34m"



bblue="\033[1;34m"



purple="\033[0;35m"



bpurple="\033[1;35m"



cyan="\033[0;36m"



bcyan="\033[1;36m"



white="\033[0;37m"



nc="\033[00m"



version="1.0"



# Regular Snippets



ask  =     f"{green}[{white}?{green}] {yellow}"



success = f"{yellow}[{white}√{yellow}] {green}"



error  =    f"{blue}[{white}!{blue}] {red}"



info  =   f"{yellow}[{white}+{yellow}] {cyan}"



info2  =   f"{green}[{white}•{green}] {purple}"



i = f"{red}[+]"



# def for slowing write and style



import sys, time



st = 0.05



# i called it sp for slowPrint



def sp1(str):



	for letter in str:



		sys.stdout.write(letter)



		sys.stdout.flush()



		time.sleep(st)



# Color snippets



black="\033[0;30m"



red="\033[0;31m"



bred="\033[1;31m"



green="\033[0;32m"



bgreen="\033[1;32m"



yellow="\033[0;33m"



byellow="\033[1;33m"



blue="\033[0;34m"



bblue="\033[1;34m"



purple="\033[0;35m"



bpurple="\033[1;35m"



cyan="\033[0;36m"



bcyan="\033[1;36m"



white="\033[0;37m"



nc="\033[00m"



version="1.0"



# Regular Snippets



ask  =     f"{green}[{white}?{green}] {yellow}"



success = f"{yellow}[{white}√{yellow}] {green}"



error  =    f"{blue}[{white}!{blue}] {red}"



info  =   f"{yellow}[{white}+{yellow}] {cyan}"



info2  =   f"{green}[{white}•{green}] {purple}"



i = f"{red}[+]"



# def for slowing write and style



import sys, time



st = 0.05



# i called it sp for slowPrint



def sp1(str):



	for letter in str:



		sys.stdout.write(letter)



		sys.stdout.flush()



		time.sleep(st)























commands="sudo apt install wget -y && sudo apt install android-libandroidfw android-liblog android-libutils libzopfli1 -y && sudo apt remove zipalign -y && wget http://ftp.de.debian.org/debian/pool/main/a/android-platform-build/zipalign_8.1.0+r23-2_amd64.deb && sudo dpkg -i zipalign_8.1.0+r23-2_amd64.deb && sudo chmod +x config/apktool.jar && sudo chmod +x config/apktool && sudo cp config/apktool.jar /usr/local/bin && sudo cp config/apktool /usr/local/bin"











def install():

       try:

        with open("setting.json", "r") as file:

                content = file.read()

                if "X1h5s78m9_NURA3V0WSN8" in content:

                        print(f"{info}you alredy install apktool")

                        exit()

                else:

                       pass

       except FileNotFoundError:

              pass



       os.system("clear")



       

       sp1(f"{yellow}Tool Designed by Bad Boy, youtube ==> http://www.youtube.com/@user-en4kg8zy4p")

       print("")

       print("")

       sp1(f"{red}NOTE!!!: this script will install apktool 2.9.0 in your system one time!!!")



       print("")



       print("")



       print("")



       print("")



       start = input(f"{green}Press {red}ENTER {green}to start download .")



       if start == "":



              os.system(commands)



              print(f"{success}Apktool download was successfly!!, check it with 'apktool' command  ")

              with open("setting.json", "w") as file:

                     file.write("X1h5s78m9_NURA3V0WSN8")

                     file.close()





































print(f"{ask}check your system for start downloading...........")



time.sleep(5)



if platform.system() == 'Linux':



        # Check if it's Kali Linux



        with open('/etc/os-release', 'r') as file:



            os_info = file.read()



            if 'Kali' in os_info:



                print(f"{success}Welcome! we can download Apktool in your system..")



                







                time.sleep(5)



                install()



            else:



                print(f"{error}Sorry, your system is Linux but not Kali... :(")



                exit()



else:



        print(f"{error}Sorry, your system is not supported.")



        exit()





