# LFI - Local File Inclusion
# Data: 27.09.2020

IP:`10.10.0.88`
------------------

(...)page=
	../../etc/passwd
found user: falcon

	../../home/falcon/.ssh/id_rsa
found id_rsa in falcons home dir

login via ssh using login: falcon and id_rsa key

found flag in user.txt

------Privilege Escalation------

sudo -l


root.txt flag in root home dir 


