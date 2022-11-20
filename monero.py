import requests
import logger
from datetime import datetime

class MoneroHunter:
    def __init__(self, wallet_address):
        self.logger = logger.Logger("monerohunter")
        self.wallet_address = wallet_address

    def crawl(self):
        if(self.wallet_address is None):
            self.logger.error("Error: wallet address is None")
            return
        elif(self.wallet_address == ""):
            self.logger.error("Error: wallet address is empty")
            return

        monero_explorer = f"https://xmrchain.net/api/account/{self.wallet_address}"

        res = requests.get(monero_explorer)
        if(res.status_code == 200):
            contents = res.json()
        else:
            self.logger.error(f"Error: monero_explorer error! {res.status_code}")
            return

        return contents

    def runner(self):
        contents = self.crawl()
        if(contents is None):
            return

        if("error" in contents):
            self.logger.error(f"Error: monero_explorer error! {contents['error']}")
            return

        for tx in contents["data"]["txs"]:
            self.logger.info(f"time: {datetime.fromtimestamp(tx['timestamp'])} from: {tx['inputs'][0]['address']}, to: {tx['outputs'][0]['address']}, value: {tx['outputs'][0]['amount']}")

if __name__ == "__main__":
    monerohunter = MoneroHunter("<wallet_address>")
    monerohunter.runner()