from os import close, getcwd
import platform
import requests
from bs4 import BeautifulSoup
import datetime


data_sot = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")


CURRENT_DIR = getcwd()
URL = "https://kallxo.com/"

if platform.system() == 'Linux':
    sep = '/'
else:
    sep = '\\'


def get_rastet_net():
    """Qitu i lexojme rastet nga kallxo.com
    #return: liste [infektuar, sheruar, vdekur] prej internetit"""
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    notif_table = soup.find("div", {"class": "notification_bar__info"})
    infos = notif_table.find_all('h4')
    kallxo = []
    for info in infos:
        info = info.text.replace('.', '')
        net = info.split(' ')[-1].replace(",", "").replace("\n", "")
        kallxo.append(int(net))
    return kallxo


def write_rastet(lista_rasteve):
    text_file = open("info.txt", "a")
    text_file.write('\n')
    text_file.write('---------------------------- \n')
    text_file.write("Data: " + data_sot + "\n")
    text_file.write(" Te Infektuar: " + str(lista_rasteve[0])+ "\n")
    text_file.write(" Te Sheruar: " + str(lista_rasteve[1]) + "\n")
    text_file.write(" Te Vdekur: " + str(lista_rasteve[2]))
    text_file.close()



def read_rastet():
    """"Qitu i lexojme rastet paraprake ne file
        #return: liste [infektuar, sheruar, vdekur]"""

    f = open(CURRENT_DIR + sep + 'info.txt', 'r') # koment
    lines = f.readlines()
    lines = lines[::-1]
    lines = lines[0:3]
    f.close()
    stats = []
    for line in lines:
        shifra = line.split(' ')[-1].replace(",", "").replace("\n", "")
        stats.append(int(shifra))
    return stats[::-1]


def send_notification():
    # Detyre me dergu notification ne PC
    print("Nese ka raste te reja dergo notification")


if __name__ == '__main__':
    rastet_net = get_rastet_net()
    rastet_file = read_rastet()
    
    for i in range(3):
        if rastet_file[i] != rastet_net[i]:
            write_rastet(rastet_net)
            send_notification()
            break
    else:
        print('Nuk kemi update.')
    




