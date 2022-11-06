from web3 import Web3, HTTPProvider
import statistics
web3 = Web3(HTTPProvider("https://dawn-distinguished-sound.ethereum-goerli.discover.quiknode.pro/bd15ae9cf37d801f052837a2bfe6b330752fd949/"))
pending_transactions = web3.provider.make_request("parity_pendingTransactions", [])
gas_prices = []
gases = []
for tx in pending_transactions["result"[:10]]:
	gas_prices.append(int((tx["gasPrice"]),16))
	gases.append(int((tx["gas"]),16))

print("Average:")
print("-"*80)
print("gasPrice: ", statistics.mean(gas_prices))
print(" ")
print("Median:")
print("-"*80)
print("gasPrice: ", statistics.median(gas_prices))
