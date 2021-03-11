import os
import requests
from bs4 import BeautifulSoup

CURRENT_DIR = os.getcwd()

def get_rastet_net():
    url= 'https://kallxo.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    notif_table = soup.find("div", {"class": "notification_bar__info"})
    infos = notif_table.find_all('h4')
    


    kallxo = []
    for info in infos:
        net = info.split(' ')[-1].replace(",", "").replace("\n", "").text
        kallxo.append(int(net))
    return kallxo

    



# def get_rastet_net():
#     """
#     Qitu i lexojme rastet nga kallxo.com
#     return: liste [infektuar, sheruar, vdekur] prej internetit
#     """


# def read_rastet():
#     """
#     Qitu i lexojme rastet paraprake ne file
#     return: liste [infektuar, sheruar, vdekur]
#     """
#     f = open(CURRENT_DIR + '\\web\\info.txt', 'r')
#     lines = f.readlines()
#     f.close()
#     stats = []
#     for line in lines:
#         shifra = line.split(' ')[-1].replace(",", "").replace("\n", "")  
#         stats.append(int(shifra))
#     return stats



# def send_notification():
#     print("Nese ka raste te reja dergo notification")







