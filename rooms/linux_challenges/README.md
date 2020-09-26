# Linux Challenges

#14.09.2020

IP: `10.10.103.237`

recevie new credentials: garry:letmein

flag1.txt found ne credentials: bob:linuxrules

flag2 in /home/bob/

flag3 in home/bob/.bash_history

flag4 crontab -e 

flag5 find / -name flag5* | grep "flag5" and then at /lib/terminfo/E/flag5.txt

flag6 find / -name flag6* | grep "flag6" and then cat /home/flag6.txt | grep "c9"

flag7: ps -ef

flag8: tar -zxvf flag8.tar.gz  and then cat flag8.txt

flag9: cat /etc/hosts

flag10: cat /etc/passwd

flag11: run flag11 and then cat .bashrc

flag12: cat /etc/update-motd.d/00-header

flag13: cd /home/bob/flag13 then diff script1 script2

flag14: cat /var/log/flagfourteen.txt

flag15: *hard one* uname -a :( hostnamectl :( cat /prc/version :( byt finaly cat /etc/*release

flag16: nothing in /mnt/ but ... /media/ and few tabs ... get U flag :)

flag17: relog to alice and there is flag17

flag18: same place as flag17

flag19: awk 'NR==2345'

flag20: cat flag20 and its `MDJiOWFhYjhhMjk5NzBkYjA4ZWM3N2FlNDI1ZjZlNjg=` ... base64

flag21: less /home/bob/flag21.php 

flag22: xxd -r -p

flag23: cat flag23 | rev

flag24: strings /home/garry/flag24

flag25:

flag26: `OMFG` find / -xdev -type f -print0 2>/dev/null | xargs -0 grep -E '^[a-z0-9]{32}$' 2>/dev/null

flag27: sudo -l   and sudo cat /home/flag27

flag28:

flag29: cat /home/garry/flag29 | tr -d "\n" > file.txt | cat file.txt last few words

flag30: curl localhost

flag31: mysql -u root -p | show databases;

flag32: use db...; show tables; SELECT * FROM flags;

flag33: cat /home/bob/.profile

flag34: printenv | grep flag

flag35: cat /etc/group | grep flag

flag36: 83d233f2ffa388e5f0b053848caed1eb








