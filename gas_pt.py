from web3 import Web3, HTTPProvider
import statistics

x = 'x'
web3 = Web3(HTTPProvider("https://dawn-distinguished-sound.ethereum-goerli.discover.quiknode.pro/bd15ae9cf37d801f052837a2bfe6b330752fd949/"))
pending_transactions = web3.provider.make_request("parity_pendingTransactions", [])
gas_prices = []
gases = []
for tx in pending_transactions:
	gas_prices.append(int(tx, 16))
	gases.append(int(tx,16))
gmean = statistics.mean(gas_prices)
gmedian = statistics.mean(gas_prices)
