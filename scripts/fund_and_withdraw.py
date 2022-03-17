from brownie import FundMe, network
from scripts.helpful_scripts import (
    get_account,
)


def fund():
    print(len(FundMe))
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(fund_me.getPrice() / 10**18)
    print(fund_me.getConversionRate(1))
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
