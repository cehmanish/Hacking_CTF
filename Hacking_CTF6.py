import sys
import socket
import getopt
import threading
import subprocess
import os
import random
import Hacking_CTF7

def level6():
	os.system('clear')
	print '----------------------------------------------------------------------------\n'
	print 'Great !!!!!!! My Hacker Your are in Level 6'
	print 'In This Level You Need to do Some Praticle Task To crack Our Challages'
	print 'You Need to Required Advance Understanding of Linux and Encoding '
	print '-----------------------------------------------------------------------------\n'
	a=str(random.randint(1,100))
	os.mkdir('.hidden_dir'+ a)
	os.chdir('.hidden_dir'+ a)

	file=open(".hidden_file.WCRY",'w')
	data = '68747470733a2f2f7777772e697361632e696f20'
	
	file.write("WebSite URL :  68747470733a2f2f7777772e697361632e696f20 ")
	file.close()
	
	print 'Analysis The URL and Enter Following Details,There is 5 Phase in this Level ' 
	print 'If You Enter One of Wrong Details then You Need to Enter All Detail from Starting (Phase 1)'
	print 'So Be Carefull\n'

	while True:

		print 'Phase 1: Enter The WebSite Url'
		website_name=raw_input()
		
		if (website_name == 'https://www.isac.io'):	
				print 'Phase 2 : Enter the ip address of website '
				ip_address=raw_input()

				if (ip_address == '75.119.203.84'):
					print 'Phase 3 : Enter the Name Server of Domain pointing'
					name_server =raw_input()

					if (name_server == 'ns1.dreamhost.com'):
						print 'Phase 4 : Enter SSL Certificate Serial Number '
						serial_no = raw_input()
					
						if (serial_no == '03:5C:A5:EC:2D:F3:19:89:81:27:79:81:2D:C5:3A:F4:E0:78') :
							print 'Phase 5: Enter Domain Owner Contact Name'
							owner_name = raw_input()
							if (owner_name == "Rajshekhar Murthy"):
				
								print "Congratulation You Have Crack The Challenges"												
								Hacking_CTF7.level7()
								break 









								
	







