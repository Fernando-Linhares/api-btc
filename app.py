from flask import Flask, Response, request
from actions import *

app = Flask(__name__)

@app.route('/')
def index():
    return {"data": show_wallets()}

@app.route('/key')
def key():
    return {"data": {"passphrase": get_passphrases()}}

@app.route('/wallet', methods = ['POST'])
def makewallet():
    p = request.form['passphrase']
    n = request.form['walletname']
    return create_wallet(n, p), 201

@app.route('/wallet/<id>')
def findwallet(id):
    w = find_wallet(id)

    if w is not None:
        return { "data": w }

    return {"error":"not found"} , 404

@app.route('/wallet/<id>', methods = ['DELETE'])
def wallet(id):
    w = find_wallet(id)

    if w is not None:
        return {"data": f"wallet deleted {delete_wallet(w)}"}, 201

    return {"error": "not found"} , 404

@app.route('/wallet/access', methods=['POST'])
def login():
    return {'data' : access_wallet(request.form['walletname'], request.form['passphrase'])}, 200

@app.route('/wallet/<id>/qrcode')
def qrcodegenerate(id):
    return generate_qrcode(id), 200

if __name__ == '__main__':
    app.run(debug=True)
