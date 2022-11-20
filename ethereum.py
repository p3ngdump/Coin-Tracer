import requests
import logger
from datetime import datetime

etherscan = "https://api.etherscan.io/api"

etherscan_API_KEY = "<API_KEY>"

class EthHunter:
    def __init__(self, wallet_address):
        self.logger = logger.Logger("ethhunter")
        self.wallet_address = wallet_address
        self.startblock = 0
        self.endblock = 99999999
        self.page = 10
        self.offset = 10
        self.sort = "asc"

    def crawl(self):
        if(self.wallet_address is None):
            self.logger.error("Error: wallet address is None")
            return
        elif(self.wallet_address == ""):
            self.logger.error("Error: wallet address is empty")
            return

        if("0x" not in self.wallet_address):
            self.wallet_address = "0x" + self.wallet_address

        etherscan_send = f"{etherscan}?module=account&action=txlistinternal&address={self.wallet_address}&startblock={self.startblock}&endblock={self.endblock}&page={self.page}&offset={self.offset}&sort={self.sort}&apikey={etherscan_API_KEY}"

        res = requests.get(etherscan_send)
        if(res.status_code == 200):
            contents = res.json()
        else:
            self.logger.error(f"Error: etherscan error! {res.status_code}")
            return

        return contents

    def runner(self):
        contents = self.crawl()
        if(contents is None):
            return

        if(contents["status"] == "0"):
            self.logger.error(f"Error: etherscan error! {contents['message']}")
            return

        for tx in contents["result"]:
            self.logger.info(f"time: {datetime.fromtimestamp(int(tx['timeStamp']))} from: {tx['from']}, to: {tx['to']}, value: {tx['value']}")

if __name__ == "__main__":
    ethhunter = EthHunter("<wallet_address>")
    ethhunter.runner()