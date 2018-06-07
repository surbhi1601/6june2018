#! /usr/bin/python2
import os
import commands
import webbrowser
import time
print "Press 1 to check time and date \n Press 2 to create a file \n Press 3 to create a directory \n Press 4 to logout from a system \n Press 5 to search something on google \n Press 6 to shutdown our O.S \n Press 7 to check internet connection in your PC \n Press 8 to LOGIN whatsapp on browser \n Press 9 to check all connected IP in your Network"

choice=raw_input("Enter your choice : ")
if choice=="1":
	print "showing current date and time :"
	print time.ctime().split()[3]
elif choice=="2":
	print "Creating a file...."
	fi=raw_input("Enter file name : ")
	commands.getoutput("gedit " + fi)
elif choice=="3":
	print "Creating a directory : "
	dir=raw_input("Enter the directory name : \n ")	
	commands.getoutput("mkdir " + dir)
elif choice=="4":
	print "logging out from the system "
	os.system("gnome-session-quit")
elif choice=="5":
	print "Searching something on Google..."
	msg=raw_input("Type to search : ")
	webbrowser.open_new_tab("https://www.google.com/search?="+msg)
elif choice=="6": 
	print "close all your apps system is rebooting.."
	msg1="acha theek hai thoda sa time aur dte hai "
	os.system("echo " +msg1+" | festival --tts")
	time.sleep(2)
	msg2="are apps band kar naaa"
	os.system("echo "+msg2+" | festival -tts")
	time.sleep(3)
	os.system("reboot")
elif choice=="7":
	os.system("ping 8.8.8.8")
elif choice=="8":
	webbrowser.open_new_tab("https://web.whatsapp.com/")
elif choice=="9":
	os.system("netstat -tn")	
else :
	print "wrong option"




