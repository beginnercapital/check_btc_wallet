# check_btc_wallet
Pull balance and transaction history of any Bitcoin wallet

# Example Usage
-  Satoshi Nakamoto's "genesis address" which received the first 50 BTC mined from the genesis block of Bitcoin on January 3, 2009
`wallet_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"`
`txs_data1 = check_bitcoin_wallet(wallet_address)`
>> Wallet Address: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
>> Balance: 100.25855669 BTC
>> Total Transactions: 40374
>> 
>> 5 Most Recent Transactions:
>> Hash: efa987c8a64e528bd3091802f45434f3c7df81f66ee48e9a046da890d64654d6
>> Time (EST): 2024-11-12 20:27:26 UTC-05:00
>> Amount: 0.00000600 BTC
>> ...

- The address `1HLoD9E4SDFFPDiYfNYnkBLQ85Y51J3Zb1` was used to send the first Bitcoin transaction to Hal Finney on January 12, 2009
`wallet_address = "1HLoD9E4SDFFPDiYfNYnkBLQ85Y51J3Zb1"`
`check_bitcoin_wallet(wallet_address)`
>> Wallet Address: 1HLoD9E4SDFFPDiYfNYnkBLQ85Y51J3Zb1
>> Balance: 50.07868795 BTC
>> Total Transactions: 47
>> ...
