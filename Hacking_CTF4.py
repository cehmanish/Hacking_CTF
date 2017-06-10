import sys
import socket
import getopt
import threading
import subprocess
import os
import random
import Hacking_CTF5

passwd='''root:x:0:0:root:/root:/bin/bash \n
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin \n 
bin:x:2:2:bin:/bin:/usr/sbin/nologin \n
sys:x:3:3:sys:/dev:/usr/sbin/nologin \n
sync:x:4:65534:sync:/bin:/bin/sync   \n
games:x:5:60:games:/usr/games:/usr/sbin/nologin \n
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin \n
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin \n
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin \n
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin \n
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin \n
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin \n
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin \n
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin \n
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin \n
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin  \n
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin \n
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin \n
systemd-timesync:x:100:103:systemd Time Synchronization,,,:/run/systemd:/bin/false \n
systemd-network:x:101:104:systemd Network Management,,,:/run/systemd/netif:/bin/false \n
systemd-resolve:x:102:105:systemd Resolver,,,:/run/systemd/resolve:/bin/false \n
systemd-bus-proxy:x:103:106:systemd Bus Proxy,,,:/run/systemd:/bin/false \n
mysql:x:104:109:MySQL Server,,,:/nonexistent:/bin/false  \n
messagebus:x:105:110::/var/run/dbus:/bin/false  \n
avahi:x:106:112:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false \n
miredo:x:107:65534::/var/run/miredo:/bin/false  \n
ntp:x:108:114::/home/ntp:/bin/false \n
stunnel4:x:109:116::/var/run/stunnel4:/bin/false \n
uuidd:x:110:117::/run/uuidd:/bin/false \n
Debian-exim:x:111:118::/var/spool/exim4:/bin/false\n
statd:x:112:65534::/var/lib/nfs:/bin/false\n
arpwatch:x:113:121:ARP Watcher,,,:/var/lib/arpwatch:/bin/sh\n
colord:x:114:123:colord colour management daemon,,,:/var/lib/colord:/bin/false\n
dnsmasq:x:115:65534:dnsmasq,,,:/var/lib/misc:/bin/false\n
dradis:x:116:125::/var/lib/dradis:/bin/false\n
geoclue:x:117:126::/var/lib/geoclue:/bin/false\n
pulse:x:118:127:PulseAudio daemon,,,:/var/run/pulse:/bin/false\n
speech-dispatcher:x:119:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/sh\n
sshd:x:120:65534::/var/run/sshd:/usr/sbin/nologin\n
snmp:x:121:129::/var/lib/snmp:/usr/sbin/nologin\n
postgres:x:122:132:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash\n
iodine:x:123:65534::/var/run/iodine:/bin/false\n
redis:x:124:135::/var/lib/redis:/bin/false\n
redsocks:x:125:136::/var/run/redsocks:/bin/false\n
rwhod:x:126:65534::/var/spool/rwho:/bin/false\n
sslh:x:127:137::/nonexistent:/bin/false\n
rtkit:x:128:138:RealtimeKit,,,:/proc:/bin/false\n
saned:x:129:139::/var/lib/saned:/bin/false\n
usbmux:x:130:46:usbmux daemon,,,:/var/lib/usbmux:/bin/false\n
beef-xss:x:131:140::/var/lib/beef-xss:/bin/false\n
Debian-gdm:x:132:142:Gnome Display Manager:/var/lib/gdm3:/bin/false'''



shadow='''root:X014elvznJq7E:17325:0:99999:7:::\n
daemon:*:16658:0:99999:7:::\n
bin:*:16658:0:99999:7:::\n
sys:*:16658:0:99999:7:::\n
sync:*:16658:0:99999:7:::\n
games:*:16658:0:99999:7:::\n
man:*:16658:0:99999:7:::\n
lp:*:16658:0:99999:7:::\n
mail:*:16658:0:99999:7:::\n
news:*:16658:0:99999:7:::\n
uucp:*:16658:0:99999:7:::\n
proxy:*:16658:0:99999:7:::\n
www-data:*:16658:0:99999:7:::\n
backup:*:16658:0:99999:7:::\n
list:*:16658:0:99999:7:::\n
irc:*:16658:0:99999:7:::\n
gnats:*:16658:0:99999:7:::\n
nobody:*:16658:0:99999:7:::\n
systemd-timesync:*:16658:0:99999:7:::\n
systemd-network:*:16658:0:99999:7:::\n
systemd-resolve:*:16658:0:99999:7:::\n
systemd-bus-proxy:*:16658:0:99999:7:::\n
mysql:!:16658:0:99999:7:::\n
messagebus:*:16658:0:99999:7:::\n
avahi:*:16658:0:99999:7:::\n
miredo:*:16658:0:99999:7:::\n
ntp:*:16658:0:99999:7:::\n
stunnel4:!:16658:0:99999:7:::\n
uuidd:*:16658:0:99999:7:::\n
Debian-exim:!:16658:0:99999:7:::\n
statd:*:16658:0:99999:7:::\n
arpwatch:!:16658:0:99999:7:::\n
colord:*:16658:0:99999:7:::\n
dnsmasq:*:16658:0:99999:7:::\n
dradis:*:16658:0:99999:7:::\n
geoclue:*:16658:0:99999:7:::\n
pulse:*:16658:0:99999:7:::\n
speech-dispatcher:!:16658:0:99999:7:::\n
sshd:*:16658:0:99999:7:::\n
snmp:*:16658:0:99999:7:::\n
postgres:*:16658:0:99999:7:::n
iodine:*:16658:0:99999:7:::\n
redis:*:16658:0:99999:7:::\n
redsocks:!:16658:0:99999:7:::\n
rwhod:*:16658:0:99999:7:::\n
sslh:!:16658:0:99999:7:::\n
rtkit:*:16658:0:99999:7:::\n
saned:*:16658:0:99999:7:::\n
usbmux:*:16658:0:99999:7:::\n
beef-xss:*:16658:0:99999:7:::\n
Debian-gdm:*:16658:0:99999:7:::'''

def level4():
	os.system('clear')
	print '------------------------------------------------------------------------------'
	print 'Congratulation You are in Level 2'
	print 'If You Crack this level then You will achive our Special Life Line Scheme'
	print '------------------------------------------------------------------------------\n'

	print '!!!HELP!!!HELP!!!!HELP!!!!!HELP!!!!!HELP'
	print 'I am Forget my Laptop Login Details \t Someone Suggest me to take the help of Hacker'
	print 'I have Two Files Where My Password are Store . So Please Recover My Password'
	print 'These Two Files are Created on Your System by this Application '
	print 'Recover The File and Enter the password in Appropriate Location \n'

	file1=open("file1.txt","w")
	file1.write(passwd)
	file1.close()

	file2=open("file2.txt","w")
	file2.write(shadow)
	file2.close()

	while True:
		print 'Enter Decrypted User Name:\t'
		decrypt_user=raw_input()

		if (decrypt_user == "root"):
			while True:
				print 'Enter Decrypted Password:\t'
				decrypt_pass = raw_input()
				if (decrypt_pass ==  "toor"):
					print 'Congratulation !!!!!!!!!!!! You Crack The Challage\n'
					Hacking_CTF5.level5()
					break
				else :	
					print 'InCorrect Password !!!!!! Try Again !!!!!!!!!'
			break 	 
		else:	
			print 'InCorrect User Name!! Try Again !!!!!!!!!'











