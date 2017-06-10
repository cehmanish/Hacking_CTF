import sys
import socket
import getopt
import threading
import subprocess
import os
import random
import Hacking_CTF4

def level3():
	os.system('clear')
	print '---------------------------------------------------------------------------------------\n'
	print 'Congratulation You are in Level3 !!!!!!!!\n'
	print 'This is A little bit Difficult Level. So Use you hacking Skills\n'
	print 'In this level there are two phase so you need to clear both phase to Crack Challanges\n'
	print 'Decode the Give Message "VjFaV2ExSXlSblJTV0d4WFltMXpPUT09" to Prove your skills\n '
	print '----------------------------------------------------------------------------------------\n'
	
	print 'Phase 1: \n'
	while True:
		print 'Enter The Encoding Scheme Name:\t'
		encoding=raw_input()
		if (encoding == 'base64' or encoding == 'Base64'):
			print "WoW !!! My hacker your crack Our Challanges\n Now you are move to Phase 2\n"	
			while True:
				
				print 'Enter Decoded Message \t'
				message =raw_input()
				if (message == 'hacker'):
					print 'Wooooooow You Prove that you have skill to Hack Everything\n'
					print 'You Have Sucessfully Complete Level 3\n'
					Hacking_CTF4.level4()
					break
				else :
					print 'Wrong Flag Try Again \n'
			break 		 
		else:

			print 'Wrong Flag try Again\n'
		







			
	
