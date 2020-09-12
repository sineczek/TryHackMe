# Web Fundamentals

# Date 12.09.2020

IP: `10.10.139.204`

1. GET by using `curl 10.10.139.204:8081/ctf/get` 
	FLAG: thm{162520bec925bd7979e9ae65a725f99f}
2. POST by using `curl -v -d "flag_please" -X POST 10.10.139.204:8081/ctf/post`
	FLAG: thm{3517c902e22def9c6e09b99a9040ba09}
3. GET in FF `http://10.10.139.204:8081/ctf/getcookie` (in cookie flag)
	FLAG: thm{91b1ac2606f36b935f465558213d7ebd}

4. create new cookie name `flagpls` and value `flagpls` in FF devtools and send it to: `http://10.10.139.204:8081/ctf/sendcookie`
	FLAG: thm{c10b5cb7546f359d19c747db2d0f47b3}