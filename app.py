from flask import Flask, Response, request
from actions import *
import asyncio

app = Flask(__name__)

@app.route('/')
async def index():
    return {"data": show_wallets()}

@app.route('/key')
async def key():
    return {"data": {"passphrase": get_passphrases()}}

@app.route('/wallet', methods = ['POST'])
async def makewallet():
    p = request.form['passphrase']
    n = request.form['walletname']
    return create_wallet(n, p), 201

@app.route('/wallet/<id>')
async def findwallet(id):
    w = find_wallet(id)

    if w is not None:
        return { "data": w }

    return {"error":"not found"} , 404

@app.route('/wallet/<id>', methods = ['DELETE'])
async def wallet(id):
    w = find_wallet(id)

    if w is not None:
        return {"data": f"wallet deleted {delete_wallet(w)}"}, 201

    return {"error": "not found"} , 404

@app.route('/wallet/access', methods=['POST'])
async def login():
    return {'data' : access_wallet(request.form['walletname'], request.form['passphrase'])}, 200

@app.route('/wallet/<id>/qrcode')
async def qrcodegenerate(id):
    return generate_qrcode(id), 200

@app.route('/transaction/<id>/<network>/info')
async def transactioninfo(id, network):
    return gettransactioninfo(id, network)

@app.route('/transaction', methods=['POST'])
async def transactionsend():
    addr = request.form['address']
    val = request.form['value']
    net = request.form['network']
    w = request.form['wallet']

    wallet = Wallet(w)
    t = val.send_to(address, val, network=net)

    return t.as_dict() , 201

if __name__ == '__main__':
    app.run(debug=True)
