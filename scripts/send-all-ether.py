from brownie import *

def main(source, destination, price):
	fee = price * 21000
	value = source.balance() - fee
	tx = source.transfer(destination, value, gas_limit=21000, gas_price=price)