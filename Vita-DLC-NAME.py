#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Rouryi on 4/12.
import requests
from bs4 import BeautifulSoup
import re
import os

# アクセスするURL
base = "https://store.playstation.com/ja-jp/grid/JP0507-PCSG00418_00-0000000000000000/1?relationship=add-ons"
# DLする場所
# C:\Users\MYNAME\Downloadなら
# path = os.path.expanduser('~\Download')
path = 'DLC'


def get_dlc(url, game_id):
    res = requests.get(url, allow_redirects=False)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'lxml')

        elems = soup.find_all(href=re.compile("/ja-jp/product/"))

        dlc = []
        for e in elems:
            temp = e.get('href')[35:]
            if temp not in dlc:
                print(temp)
                dlc.append(temp)
                os.makedirs(path + "\\" + game_id + "\\addcont\\" + temp)
                # print(path + "\\" + game_id + "\\addcont\\" + temp)
    else:
        return -1


def main():
    game_id = base[48:57]
    print(game_id)
    for i in range(1):
        url = base[:-22] + str(i) + "?relationship=add-ons"
        # print(url)
        if get_dlc(url, game_id) == -1:
            break


if __name__ == '__main__':
    main()
