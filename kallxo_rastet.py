from os import getcwd
import platform
from win10toast import ToastNotifier
import requests
from bs4 import BeautifulSoup
import datetime
import time

data_sot = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

CURRENT_DIR = getcwd()
URL = "https://www.koha.net/tag/covid-19/"


def get_rastet_net():
    """Qitu i lexojme rastet nga koha.com return: liste [infektuar, sheruar, vdekur] prej internetit"""
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    body = soup.find('body')
    notif_table = body.find("div", {"class": "row clear top_home mgb-30 pb-3 with-border hidden-xs"}).text
    infos = notif_table.split('|')[-3:]
    koha = []
    for info in infos:
        info = info.strip().split(' ')
        info = info[1].split('\n')[0]
        koha.append(int(info))
    return koha


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
    """"Qitu i lexojme rastet paraprake ne file  return: liste [infektuar, sheruar, vdekur]"""
    f = open(CURRENT_DIR + '\\info.txt', 'r') # koment
    lines = f.readlines()
    lines = lines[::-1]
    lines = lines[0:3]
    f.close()
    stats = []
    for line in lines:
        shifra = line.split(' ')[-1].replace(",", "").replace("\n", "")
        stats.append(int(shifra))
    return stats[::-1]


def send_notification(mesazhi): 
    toast = ToastNotifier()
    toast.show_toast(title="Koha - Covid 19", msg=mesazhi, duration=7)


def msg_notification(lista_rasteve):
    return "Te infektuar " + str(lista_rasteve[0]) + ". Te sheruar " + str(lista_rasteve[1]) + ". Te vdekur " + str(lista_rasteve[2])

if __name__ == '__main__':
    rastet_net = get_rastet_net()
    rastet_file = read_rastet()
    for i in range(3):
        if rastet_file[i] != rastet_net[i]:
            write_rastet(rastet_net)
            send_notification(msg_notification(read_rastet()))
            break
    else:
        print('No, Update.')
    