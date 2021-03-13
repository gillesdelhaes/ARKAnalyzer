#!/usr/bin/python3
import sys
import os
import datetime
import requests

def DownloadARKFiles():
    '''
    Downloads csv files from ARK's website using the urls in ../conf/ARKURLS.txt\n
    Stores them in ../data prefixed with the date
    '''
    ARKURLsFile = open("../conf/ARKURLs.txt")
    for line in ARKURLsFile:
        downloadedFilename = f'{datetime.datetime.now():%Y-%m-%d}_{line.split("/")[-1][:-1]}'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        r = requests.get(line.strip('\n'),headers=headers).content.decode()
        open(f'../data/{downloadedFilename}', 'w').write(r)

if __name__ == '__main__':
    DownloadARKFiles()