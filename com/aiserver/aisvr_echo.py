#!/usr/bin/python

import requests
import commands
import logging
import time

aisvr_url = 'http://127.0.0.1:11380/deepwise/echo'
logging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt = '%a, %d %b %Y %H:%M:%S',
                    filename = '/root/aisvr_check.log',
                    filemode = 'a')


def aisvr_echo(aisvr_url):
    try:
        response = requests.get(aisvr_url, timeout = 2)
        # print(response)
        if response.status_code == 200:
            aisvr_echo_json = response.json()
            # result is {"code":0,"data":"echo return"}
            if aisvr_echo_json['code'] == 0 and aisvr_echo_json['data'] == "echo return":
                logging.info('aisvr is ok!')
                pass
            else:
                aisvr_restart()
    except Exception as E:
        logging.error(E)
        aisvr_restart()


def aisvr_restart():
    logging.info('aisvr is down! reboot now!')
    status, result = commands.getstatusoutput('service aisvr restart')
    if status == 0:
        logging.info('aisvr restart done!')
    else:
        logging.error('aisvr restart error!%s' % result)


if __name__ == "__main__":
    aisvr_echo(aisvr_url)
