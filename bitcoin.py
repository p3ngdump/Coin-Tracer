import requests
import logger
from datetime import datetime

bit_explorer = "https://blockchain.info/rawaddr/"

class BtcHunter:
    def __init__(self, wallet_address):
        self.logger = logger.Logger("bithunter")
        self.wallet_address = wallet_address

    def crawl(self):
        if(self.wallet_address is None):
            self.logger.error("Error: wallet address is None")
            return
        elif(self.wallet_address == ""):
            self.logger.error("Error: wallet address is empty")
            return

        if("0x" in self.wallet_address):
            self.wallet_address = self.wallet_address[2:]

        bit_explorer_send = f"{bit_explorer}{self.wallet_address}"

        res = requests.get(bit_explorer_send)
        if(res.status_code == 200):
            contents = res.json()
        else:
            self.logger.error(f"Error: bit_explorer error! {res.status_code}")
            return

        return contents

    def runner(self):
        contents = self.crawl()
        if(contents is None):
            return

        if("error" in contents):
            self.logger.error(f"Error: bit_explorer error! {contents['error']}")
            return

        for tx in contents["txs"]:
            self.logger.info(f"time: {datetime.fromtimestamp(tx['time'])} from: {tx['inputs'][0]['prev_out']['addr']}, to: {tx['out'][0]['addr']}, value: {tx['out'][0]['value']}")

if __name__ == "__main__":
    bithunter = BtcHunter("<wallet_address>")
    bithunter.runner()