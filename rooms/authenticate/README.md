# Authenticate
# Data: 27.09.2020

IP:`10.10.74.10`
------------------
<IP>:8888

Burp -> proxy -> add to scope -> intruder
intruder found pass for user jack:12345678
(its easier to copy flag via devtools)
intruder found pass for user mike:12345
(its easier to copy flag via devtools)

-------------------
<IP>:8888

register new user with space fr. " darren" oraaz " arthur"
and get the flags (again, easier to copy flag using devtools)

-------------------
<IP>:5000
same steps as in example, in repeater change Auth.
JWT `J0eXAiOiJKV1QiLCJhbGciOiJOT05FIn0K.eyJleHAiOjE1ODY3MDUyOTUsImlhdCI6MTU4NjcwNDk5NSwibmJmIjoxNTg2NzA0OTk1LCJpZGVudGl0eSI6MH0K.`

-------------------
<IP>:7777

create user (me:123)

goto private space, and change in URL users/1 to users/2

for superadmin pass and flag just change it to ... ;)