from brownie import AgidiToken
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(26000, "ether")


def main():
    account = get_account()
    agidi_token = AgidiToken.deploy(initial_supply, {"from": account})
    print(agidi_token.name())
