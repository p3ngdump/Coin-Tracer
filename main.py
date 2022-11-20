from ethereum import EthHunter
from bitcoin import BtcHunter
from monero import MoneroHunter
from logger import Logger

def main():
    logger = Logger("main")
    coin_type = input("Select coin type:\n1. Ethereum\n2. Bitcoin\n3. Monero")

    if(coin_type == "1"):
        wallet_address = input("Input wallet address: ")
        ethhunter = EthHunter(wallet_address)
        ethhunter.runner()
    elif(coin_type == "2"):
        wallet_address = input("Input wallet address: ")
        bithunter = BtcHunter(wallet_address)
        bithunter.runner()
    elif(coin_type == "3"):
        wallet_address = input("Input wallet address: ")
        monerohunter = MoneroHunter(wallet_address)
        monerohunter.runner()
    else:
        logger.error("Error: Invalid coin type")

if __name__ == "__main__":
    main()