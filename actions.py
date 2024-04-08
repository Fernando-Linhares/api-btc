from bitcoinlib.wallets import Wallet, wallet_create_or_open, wallets_list, wallet_delete_if_exists, HDKey
from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.services.services import Service

def show_wallets():
    return wallets_list()

def create_wallet(walletname, passphrase):
    w = Wallet.create(walletname, password=passphrase)
    return show_wallet_info(w)

def find_wallet(walletid):
    w = Wallet(walletid)
    return show_wallet_info(w)

def show_wallet_info(w: Wallet):
    keys = w.get_key().as_dict()

    return {
        "wallet": {
            "address": keys['address'],
            "name": w.name,
            "owner": w.owner,
            "scheme": w.scheme,
            "purpose": w.purpose,
            "balance": w.balance(),
            "network": keys['network'],
            "key": {
                'type': keys['key_type'],
                'key_public': keys['key_public']
            },
            "transactions": w.transactions()
        },
    }

def get_passphrases():
    m = Mnemonic()
    return m.generate(strength=256, add_checksum=True)

def delete_wallet(w):
    wallet_delete_if_exists(w['wallet']['name'], force=True)
    return w['wallet']['name']

def access_wallet(walletname, passphrase):
    w = wallet_create_or_open(walletname, passphrase)
    return show_wallet_info(w)

def make_transaction(id, address, value):
    w = Wallet(id)
    t = w.send_to(address, value)
    return t.as_dict()

def generate_qrcode(walletid):
    w = Wallet(walletid)
    return {"qrcode": f"https://chart.googleapis.com/chart?chs=250x250&cht=qr&chl={w.get_key().address}"}

def gettransactioninfo(id, n):
    service = Service(network=n)
    t = service.gettransaction(id)
    return t.as_dict()
