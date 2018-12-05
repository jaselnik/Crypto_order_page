from data_ import BitmexDataHandler
from app.models import ClientModel

import logging
import redis
import time

NAMESPACE = "run_ws"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename=f'{NAMESPACE}.log')
logger = logging.getLogger(__name__)

r = redis.StrictRedis(host='localhost',charset="utf-8", port=6379, db=0)


def main():
    endpoint = "wss://testnet.bitmex.com/realtime"
    symbols = ["XBTUSD"]
    subs = ["margin"]
    clients = ClientModel.query.filter_by(visible=True).filter(ClientModel.email != 'autherror@email').all()
    wst = {}
    for client in clients:
        wst[client] = BitmexDataHandler(None, symbols, endpoint, subs, api=client.apiKey, secret=client.secret)
    while True:
        time.sleep(5)


if __name__ == '__main__':
    main()
