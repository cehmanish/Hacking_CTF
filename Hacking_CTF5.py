import sys
import socket
import getopt
import threading
import subprocess
import os
import random
import Hacking_CTF6

def level5():
	os.system('clear')
	print '----------------------------------------------------------------------------\n'
	print 'Great !!!!!!! My Hacker Your are in Level 5'
	print 'In This Level You Need to do Some Praticle Task To crack Our Challages'
	print 'This Phase is very Essential in Every Hacker Life'
	print 'So Try to crack our Challanges'
	print '-----------------------------------------------------------------------------\n'

	print ' Link of a website is given. You Need to Give Some Answer\n'
	print 'Link: "http://pwoah7foa6au2pul.onion" \n'
	
	while True:
		print 'Enter the Title of Website (Same as give in Website Login Page)'
		answer = raw_input()
		if (answer == 'Login | Alphabay Market'):
			print 'Great !!!! You Known What are the importance of Anonymous for A Hacker'
		
			while True:
				print 'Enter The Charge Taken by Company form Seller'
				answer1= raw_input()
				if (answer1 == '3.9'):
					print "Wow You Have Sucessfully Complete this Level "
					Hacking_CTF6.level6()
					break 
				else: 
					print 'Wrong Try Again !!!'
			break 
		else :
			print 'Wrong Try Again !!!!'
		















