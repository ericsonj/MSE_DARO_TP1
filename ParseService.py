from Currency import Currency
from Currency import CurrencyParser
from Currency import CurrencyFactory
from ParserLine import ParserLine
from ParserLine import ParserException

import json
import socket
import time
import signal
import sys
import threading
import configparser

UDP_IP      =  "127.0.0.1"
UDP_PORT    = 10000

runing = True

def toJson(currencylist):
    jsonstr = "["
    listlen = len(currencylist)
    for i in range(listlen):
        c = currencylist[i]
        jsonstr += json.dumps({"id": c.iid, "value1": c.buyValue, "value2": c.saleValue, "name": c.name})
        if (i < listlen -1):
            jsonstr += ", "
    jsonstr += "]"
    return jsonstr

def app():

    try:

        config = configparser.ConfigParser()
        config.read('config.txt')
        options = config['PROPERTIES']
        filecsv = options['currency_file_csv']

        global runing
        while(runing):
            currencylist = CurrencyFactory.buildFromFile(filecsv)
            result = toJson(currencylist)
            print(result)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(bytes(result, "utf-8"), (UDP_IP, UDP_PORT))
            for _ in range(30):
                if runing == False:
                    break
                time.sleep(1)

        print("BYE")
    except Exception as e:
        print(str(e))

th = threading.Thread(target=app)

def handler(signum, frame):
    global runing
    runing = False
    print("Closing...")

signal.signal(signal.SIGINT, handler)

th.start()