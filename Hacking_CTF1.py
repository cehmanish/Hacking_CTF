import sys
import socket
import getopt
import threading
import subprocess
import os
import random
import Hacking_CTF2


def level1():

	print "Now You are in Level 1 \n"
	print "Use your Hacking Skill and Try to find out Open Port and Capture the Flag\n"
	print "Enter the Flag in Appropriate Locate to move to next level \n"
	print "If your crack your basic challenge then Flag option is shown\n"

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(('127.0.0.1',random.randint(1,10000)))
	server.listen(1)
	
	client_socket, addr = server.accept()
	client_socket.send("ASASASASASA")

	flag=0
	res=raw_input("Enter Your Flag Here\n")
	
	while flag == 0:
		if (res == "ASASASASASA"):
			print "Congratulation !!!!!!!! \n"
			print "You are Crack Our Challanges \n"
			flag=1 
			server.close()
			client_socket.close()
			Hacking_CTF2.level2()
			

		else :
			print "OOPPSS !!!!!! Sorry !!! Try Again \n"
			print "To Become a Real Hacker you need more practices\n"
			res=raw_input("Enter Your Flag Here\n")





