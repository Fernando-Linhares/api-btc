# Wallet Bitcoin

  ### OVERVIEW

Backend implementation of bitcoin wallet, for make service of wallet bitcoin.

### Usage
Install flask
	
	pip install flask
Install Bitcoinloib
		
	pip install bitcoinlib
			
Run App
	
	python app.py

### Requests and Responses

List Wallets
| Method | Uri | Body |
|  --------  |  -------  |  ------- |
| GET | ```http://localhost:5000/``` | none |
####
| Response | 200 |
| ------ | ---- |

```json
{
	"data": [
		{
			"id": 2,
			"main_key_id": 7,
			"name": "mywallet",
			"network": "bitcoin",
			"owner": "",
			"parent_id": null,
			"purpose": 44,
			"scheme": "bip32"
		}]
	}
```
------------

Generate Private Key
| Method | Uri | Body |
|  --------  |  -------  |  ------- |
| GET | ```http://localhost:5000/key``` | none |
####
| Response | 200 |
| ------ | ---- |

```json
{
	"data": {
		"passphrase": "scorpion mimic truly ...."
	}
}
```
------------

Create an Wallet
| Method | Uri | Body |
|  --------  |  -------  |  ------- |
| POST | ```http://localhost:5000/wallet``` | Form |
####

Body Request
| Form Field| Value|
|  --------  |  -------  |
| ```passphrase``` | ```scorpion mimic truly ....``` |
| ```walletname``` | ```mywallet``` |

####
| Response | 201 |
| ------ | ---- |

```json
{
	"wallet": {
		"address": "123asda123asd...",
		"balance": 0.0,
		"key": {
			"key_public": "123123asd....",
			"type": "bip32"
		},
		"name": "mywallet",
		"network": "bitcoin",
		"owner": "",
		"purpose": 44,
		"scheme": "bip32",
		"transactions": []
	}
}
```
------------
Access an Wallet
| Method | Uri | Body |
|  --------  |  -------  |  ------- |
| POST | ```http://localhost:5000/wallet/access``` | Form |
####

Body Request
| Form Field| Value|
|  --------  |  -------  |
| ```passphrase``` | ```scorpion mimic truly ....``` |
| ```walletname``` | ```mywallet``` |

####
| Response | 201 |
| ------ | ---- |

```json
{
	"wallet": {
		"address": "123asda123asd...",
		"balance": 0.0,
		"key": {
			"key_public": "123123asd....",
			"type": "bip32"
		},
		"name": "mywallet",
		"network": "bitcoin",
		"owner": "",
		"purpose": 44,
		"scheme": "bip32",
		"transactions": []
	}
}
```

------------

Show Wallet

| Method | Uri | Body |
|  --------  |  -------  |  ------- |
| GET | ```http://localhost:5000/wallet/2``` | none |
####
| Response | 200 |
| ------ | ---- |

```json
{
	"wallet": {
		"address": "123asda123asd...",
		"balance": 0.0,
		"key": {
			"key_public": "123123asd....",
			"type": "bip32"
		},
		"name": "mywallet",
		"network": "bitcoin",
		"owner": "",
		"purpose": 44,
		"scheme": "bip32",
		"transactions": []
	}
}
```
-----
Delete Wallet

| Method | Uri | Body |
|  --------  |  -------  |  ------- |
| DELETE | ```http://localhost:5000/wallet/1``` | none |
####
| Response | 201 |
| ------ | ---- |

```json
{
	"data": "wallet deleted mywallet"
}
```

-----
Delete Wallet

| Method | Uri | Body |
|  --------  |  -------  |  ------- |
| DELETE | ```http://localhost:5000/wallet/1/qrcode``` | none |
####
| Response | 200 |
| ------ | ---- |

```json
{
	"qrcode": "https://chart.googleapis.com/chart?chs=250x250&cht=qr&chl=1Cj5R...."
}
```

-----
Transaction Send

| Method | Uri | Body |
|  --------  |  -------  |  ------- |
| POST | ```http://localhost:5000/transaction``` | Form |

####
Body Request
| Form Field | Value |
|  --------  |  -------  |
| ```address``` | ```asdasdasdasdasdasd ....``` |
| ```wallet``` | ```[id or name]``` |
| ```value``` | ```0.0031``` |
| ```network``` | ```bitcoin``` |

####
| Response | 201 |
| ------ | ---- |

```json
	{
		"block_hash": null,
		"block_height": 837850,
		"coinbase": false,
		"confirmations": 458,
		"date": "Fri, 05 Apr 2024 15:57:57 GMT",
		"fee": 6000,
		"fee_per_kb": 5976,
		"flag": null,
		"input_total": 360912654,
		"inputs": [
			...
		]
		...
	}
```

Transaction Info
| Method | Uri | Body |
|  --------  |  -------  |  ------- |
| GET | ```http://localhost:5000/transaction/<id>/info``` | none |
####
| Response | 200 |
| ------ | ---- |

```json
	{
		"block_hash": null,
		"block_height": 837850,
		"coinbase": false,
		"confirmations": 458,
		"date": "Fri, 05 Apr 2024 15:57:57 GMT",
		"fee": 6000,
		"fee_per_kb": 5976,
		"flag": null,
		"input_total": 360912654,
		"inputs": [
			...
		]
		...
	}
```
------------

### Dependencies
[Python 3.10](https://docs.python.org/3.10/)
 [Flask 3.0](https://flask.palletsprojects.com/en/3.0.x/)
 [Bitcoinlib 6.12](https://bitcoinlib.readthedocs.io/en/latest/index.html)

