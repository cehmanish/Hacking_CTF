import sys
import socket
import getopt
import threading
import subprocess
import os
import random
import Hacking_CTF3


def level2():
	os.system('clear')
	print '----------------------------------------------------------------------\n'
	print "Wow You are in Level 2 \n"
	print 'In This level you Need to use your creativity '
	print 'Check your active connection and try to connect them '
	print '-----------------------------------------------------------------------\n'
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(('127.0.0.1',random.randint(1,10000)))
	server.listen(1)
	
	client_socket, addr = server.accept()
	num=0
	while True:
		num=num+1
		client_socket.send("Enter Password For root user for Login ")
		ans=client_socket.recv(1024) 	
		if (num== 11):
			client_socket.send("Hurry!!!!You are Sucessfully Login ")			
			client_socket.close()
			
			print "Now Enter Your Flag Here \n "
			
			while True:
				flag=raw_input()
				if (flag == '11') :
					print ("Great You have Quality to become a Hacker Because you have Creative Mind\n")
					Hacking_CTF3.level3()
					break 
				else :
					print ("OOPS!!My Dear Hacker Use your Mind and Creativity\n")
			break 		
		else:
			continue 


