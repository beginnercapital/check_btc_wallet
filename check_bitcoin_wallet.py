import requests
import json
from datetime import datetime, timezone, timedelta

def check_bitcoin_wallet(address):
    # API endpoints
    balance_url = f"https://blockchain.info/balance?active={address}"
    txs_url = f"https://blockchain.info/rawaddr/{address}"

    try:
        # Get balance
        balance_response = requests.get(balance_url)
        balance_data = balance_response.json()
        balance = balance_data[address]['final_balance'] / 100000000  # Convert satoshis to BTC

        # Get transactions
        txs_response = requests.get(txs_url)
        txs_data = txs_response.json()
        
        # Print wallet information
        print(f"Wallet Address: {address}")
        print(f"Balance: {balance:.8f} BTC")
        print(f"Total Transactions: {txs_data['n_tx']}")
        
        # Print recent transactions
        print("\n5 Most Recent Transactions:")
        for tx in txs_data['txs'][:5]:  # Display the 5 most recent transactions
            tx_hash = tx['hash']
            tx_time = datetime.fromtimestamp(tx['time'], timezone.utc)  # UTC Time
            tx_time_est = tx_time.astimezone(timezone(timedelta(hours=-5)))  # Convert to EST
            tx_amount = sum(output['value'] for output in tx['out']) / 100000000  # Convert satoshis to BTC
            print(f"Hash: {tx_hash}")
            # print(f'Time (UTC): {tx_time.strftime("%Y-%m-%d %H:%M:%S %Z")}')
            print(f'Time (EST): {tx_time_est.strftime("%Y-%m-%d %H:%M:%S %Z")}')
            print(f"Amount: {tx_amount:.8f} BTC")
            print("---")
    
        return txs_data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except json.JSONDecodeError:
        print("Error: Unable to parse API response")
