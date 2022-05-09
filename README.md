# Web Login Page

Fast Modular Web Interfaces Bruteforcer

# :inbox_tray: Install
```
python3 -m pip install -r requirements.txt
```

# :fast_forward: Usage
```
$ python3 web-brutator.py -h

usage: web-brutator.py [-h] [--url URL] [--target TYPE] [-u USERNAME]
                       [-U USERLIST] [-p PASSWORD] [-P PASSLIST]
                       [-C COMBOLIST] [-t THREADS] [-s] [-v] [-e MAX_ERRORS]
                       [--timeout TIMEOUT]

optional arguments:
  -h, --help                   show this help message and exit
  --url URL                    Target URL
  --target TYPE                Target type
  -u, --username USERNAME      Single username
  -U, --userlist USERLIST      Usernames list
  -p, --password PASSWORD      Single password
  -P, --passlist PASSLIST      Passwords list
  -C, --combolist COMBOLIST    Combos username:password list
  -t, --threads THREADS        Number of threads [1-50] (default: 10)
  -v, --verbose                Print every tested creds
  -s, --stoponsuccess          Stop on success
  --timeout TIMEOUT            Time limit on the response (default: 20s)
```

Example:
```
python3 web-brutator.py --target jenkins --url https://mytarget.com -U ./usernames.txt -P ./passwords.txt -s -t 40
```

# :rocket: Available Modules
- axis2
- htaccess
- jenkins
- joomla
- standardform
- tomcat


Example:
```
python3 web-brutator.py --target standardform --url https://mytarget.com -U ./usernames.txt -P ./passwords.txt -s -t 40 -v
```