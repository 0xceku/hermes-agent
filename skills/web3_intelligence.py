import requests

def get_eth_balance(wallet_address):
    """Fetches the current ETH balance of a given EVM wallet address."""
    # Using public RPC/API for demonstration
    url = f"https://api.blockcypher.com/v1/eth/main/addrs/{wallet_address}/balance"
    try:
        response = requests.get(url)
        data = response.json()
        balance = data.get('balance', 0) / (10**18)
        return f"Wallet {wallet_address} has a balance of {balance:.4f} ETH."
    except Exception as e:
        return f"Error fetching balance: {str(e)}"

def get_gas_price():
    """Fetches the current Ethereum network gas price."""
    url = "https://api.etherscan.io/api?module=gastracker&action=gasoracle"
    try:
        response = requests.get(url)
        data = response.json()
        safe_gas = data['result']['SafeGasPrice']
        fast_gas = data['result']['FastGasPrice']
        return f"Current ETH Gas Prices -> Safe: {safe_gas} Gwei, Fast: {fast_gas} Gwei."
    except Exception as e:
        return f"Error fetching gas price: {str(e)}"

# Register the tools for Hermes
WEB3_TOOLS = [
    {
        "name": "web3_get_balance",
        "description": "Get the ETH balance of a specific EVM wallet address.",
        "function": get_eth_balance
    },
    {
        "name": "web3_get_gas",
        "description": "Check current Ethereum gas prices before making transactions.",
        "function": get_gas_price
    }
]
