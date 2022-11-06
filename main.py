from flask import Flask, render_template, request
from web3 import Web3, HTTPProvider
import gas_pt

app = Flask(__name__)

@app.route('/')
def index():

    web3 = Web3(HTTPProvider("https://dawn-distinguished-sound.ethereum-goerli.discover.quiknode.pro/bd15ae9cf37d801f052837a2bfe6b330752fd949/"))
    estimate = web3.eth.estimateGas({'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601', 'from': '0x6E0d01A76C3Cf4288372a29124A26D4353EE51BE', 'value': 145})
    #print("Gas estimate is: ", estimate)
    return render_template('home.html', variable = estimate, mean = gas_pt.gmean, median = gas_pt.gmedian)

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html',form_data = form_data)


if __name__ == '__main__':
    app.run(debug=True)
