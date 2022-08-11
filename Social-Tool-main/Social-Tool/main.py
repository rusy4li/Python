try:
    import requests
except ImportError:
    print(">>> 'requests' modül hatası!")
try:
    import colorama
    from colorama import Fore, Style
    colorama.init()
except ImportError:
    print(">>> 'colorama' modül hatası!")

import datetime
# Kütüphaneler: 
import os
import time

datetime_modulü = datetime.datetime.now()
vakitT = datetime_modulü.strftime("%Y-%M-%D")
vakits = datetime_modulü.strftime("%I:%M:%S")
green = Fore.GREEN
temizle = Style.RESET_ALL
green2 = Fore.GREEN
temizle2 = Style.RESET_ALL

os.system("cls")

print(Fore.CYAN + """
   SSSSSSSSSSSSSSS                                        iiii                    lllllll
 SS:::::::::::::::S                                      i::::i                   l:::::l
S:::::SSSSSS::::::S                                       iiii                    l:::::l
S:::::S     SSSSSSS                                                               l:::::l
S:::::S               ooooooooooo       cccccccccccccccciiiiiii   aaaaaaaaaaaaa    l::::l
S:::::S             oo:::::::::::oo   cc:::::::::::::::ci:::::i   a::::::::::::a   l::::l
 S::::SSSS         o:::::::::::::::o c:::::::::::::::::c i::::i   aaaaaaaaa:::::a  l::::l
  SS::::::SSSSS    o:::::ooooo:::::oc:::::::cccccc:::::c i::::i            a::::a  l::::l
    SSS::::::::SS  o::::o     o::::oc::::::c     ccccccc i::::i     aaaaaaa:::::a  l::::l
       SSSSSS::::S o::::o     o::::oc:::::c              i::::i   aa::::::::::::a  l::::l
            S:::::So::::o     o::::oc:::::c              i::::i  a::::aaaa::::::a  l::::l
            S:::::So::::o     o::::oc::::::c     ccccccc i::::i a::::a    a:::::a  l::::l
SSSSSSS     S:::::So:::::ooooo:::::oc:::::::cccccc:::::ci::::::ia::::a    a:::::a l::::::l
S::::::SSSSSS:::::So:::::::::::::::o c:::::::::::::::::ci::::::ia:::::aaaa::::::a l::::::l
S:::::::::::::::SS  oo:::::::::::oo   cc:::::::::::::::ci::::::i a::::::::::aa:::al::::::l
 SSSSSSSSSSSSSSS      ooooooooooo       cccccccccccccccciiiiiiii  aaaaaaaaaa  aaaallllllll
>>> Social V2""")
print(Style.RESET_ALL)
print("[*] starting @ {} /{}/".format(vakits, vakitT))
print()
print("[!] The information provided here may not be correct, it is still under development!")
print("[!] Enter the name or nickname of the person whose Social Media accounts you want to search")
isim = input(" > ")
time.sleep(1)
print()

List = []


 # instagram
social1 = ("https://instagram.com/"+isim)
url1 = social1
r = requests.get(url1)
status = r.status_code
if status == 200:
    List.append(url1)
    print("[{}+{}] {}Instagram:{} {}".format(green,
              temizle, green2, temizle2, url1))
    print()

    # facebook
social2 = ("https://facebook.com/"+isim)
url2 = social2
r = requests.get(url2)
status = r.status_code
if status == 200:
    List.append(url2)
    print("[{}+{}] {}Facebook:{} {}".format(green,
              temizle, green2, temizle2, url2))
    print()

    # pinterest
social3 = ("https://pinterest.com/"+isim)
url3 = social3
r = requests.get(url3)
status = r.status_code
if status == 200:
    List.append(url3)
    print("[{}+{}] {}Pinterest:{} {}".format(green,
              temizle, green2, temizle2, url3))
    print()

    # tiktok
social4 = ("https://www.tiktok.com/@"+isim)
url4 = social4
r = requests.get(url4)
status = r.status_code
if status == 200:
    List.append(url4)
    print("[{}+{}] {}Tiktok:{} {}".format(green,
              temizle, green2, temizle2, url4))
    print()

    # nine9gag
social5 = ("https://9gag.com/u/"+isim)
url5 = social5
r = requests.get(url5)
status = r.status_code
if status == 200:
    List.append(url5)
    print("[{}+{}] {}9gag:{} {}".format(green,
              temizle, green2, temizle2, url5))
    print()

    # blogspot
social6 = ("https://"+isim+".blogspot.com/")
url6 = social6
r = requests.get(url6)
status = r.status_code
if status == 200:
    List.append(url6)
    print("[{}+{}] {}Blogspot:{} {}".format(green,
              temizle, green2, temizle2, url6))
    print()

    # buzfeed
social7 = ("https://buzzfeed.com/"+isim)
url7 = social7
r = requests.get(url7)
status = r.status_code
if status == 200:
    List.append(url7)
    print("[{}+{}] {}BuzzFeed:{} {}".format(green,
              temizle, green2, temizle2, url7))
    print()

    # patreon
social8 = ("https://patreon.com/u/"+isim)
url8 = social8
r = requests.get(url8)
status = r.status_code
if status == 200:
    List.append(url8)
    print("[{}+{}] {}Patreon:{} {}".format(green,
              temizle, green2, temizle2, url8))
    print()

    # producthunt
social9 = ("https://producthunt.com/@"+isim)
url9 = social9
r = requests.get(url9)
status = r.status_code
if status == 200:
    List.append(url9)
    print("[{}+{}] {}ProductHunt:{} {}".format(green,
              temizle, green2, temizle2, url9))
    print()

    # quizlet
social10 = ("https://quizlet.com/"+isim)
url10 = social10
r = requests.get(url10)
status = r.status_code
if status == 200:
    List.append(url10)
    print("[{}+{}] {}Quizlet:{} {}".format(green,
              temizle, green2, temizle2, url10))
    print()

    # slideshare
social11 = ("https://slideshare.net/"+isim)
url11 = social11
r = requests.get(url11)
status = r.status_code
if status == 200:
    List.append(url11)
    print("[{}+{}] {}SlideShare:{} {}".format(green,
              temizle, green2, temizle2, url11))
    print()

    # wordpress
social12 = ("https://"+isim+".wordpress.com")
url12 = social12
r = requests.get(url12)
status = r.status_code
if status == 200:
    List.append(url12)
    print("[{}+{}] {}WordPress:{} {}".format(green,
              temizle, green2, temizle2, url12))
    print()

    # youtube
social13 = ("https://youtube.com/"+isim)
url13 = social13
r = requests.get(url13)
status = r.status_code
if status == 200:
    List.append(url13)
    print("[{}+{}] {}Youtube:{} {}".format(green,
              temizle, green2, temizle2, url13))
    print()

    # steam
social14 = ("https://steamcommunity.com/id/"+isim)
url14 = social14
r = requests.get(url14)
status = r.status_code
if status == 200:
    List.append(url14)
    print("[{}+{}] {}Steam:{} {}".format(green,
              temizle, green2, temizle2, url14))
    print()

    # steamid
social15 = ("https://steamid.uk/profile/"+isim)
url15 = social15
r = requests.get(url15)
status = r.status_code
if status == 200:
    List.append(url15)
    print("[{}+{}] {}Steamid:{} {}".format(green,
              temizle, green2, temizle2, url15))
    print()

    # twitch
social16 = ("https://twitch.tv/"+isim)
url16 = social16
r = requests.get(url16)
status = r.status_code
if status == 200:
    List.append(url16)
    print("[{}+{}] {}Twitch:{} {}".format(green,
              temizle, green2, temizle2, url16))
    print()

    # twitter
social17 = ("https://mobile.twitter.com/"+isim)
url17 = social17
r = requests.get(url17)
status = r.status_code
if status == 200:
    List.append(url17)
    print("[{}+{}] {}Twitter:{} {}".format(green,
              temizle, green2, temizle2, url17))
    print()

    # virüstotal
social18 = ("https://virustotal.com/ui/users/"+isim+"/trusted_users")
url18 = social18
r = requests.get(url18)
status = r.status_code
if status == 200:
    List.append(url18)
    print("[{}+{}] {}VirüsTotal:{} {}".format(green,
              temizle, green2, temizle2, url18))
    print()


    # Not Defterine Kayıt

print(" >> Not defterine kayıt oluşturulsunmu ?")
sorgu = input("-> ")

if sorgu.lower() == "e" or sorgu.lower() == "evet":
    with open("social.txt", "w", encoding='utf-8') as f:
        for url in List:
            f.write(url)
            f.write("\n")  
    print(" Kayıt klasörüne eklendi")


  




print()
input(" >> Devam etmek için enter tuşuna basın...")
