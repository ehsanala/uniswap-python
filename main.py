import os
from uniswap import Uniswap
from web3.middleware.cache import construct_simple_cache_middleware

# Load secrets from Replit's environment variables
private_key = os.getenv(
    "6d1665385f6765c01ade1228d5e04f30a750bc2f43909e4390aad912050fa16e")
wallet_address = os.getenv("0x745C88bc93de2e0723e8fc8be99B6fa930df6a75")

# Initialize Uniswap client
uniswap = Uniswap(address=wallet_address, private_key=private_key, version=3)

from web3 import Web3

# Convert to checksummed addresses
eth_address = Web3.toChecksumAddress(
    "0xC02aaa39b223FE8D0A0E5C4F27eAD9083C756Cc2")
usdc_address = Web3.toChecksumAddress(
    "0xA0b86991C6218B36c1D19D4a2e9Eb0cE3606eB48")

# Specify the fee tier (3000 for 0.3% in most cases)
fee_tier = 3000  # Adjust this based on the pair's liquidity pool

# Fetch price of 1 ETH in USDC
eth_in_usdc = uniswap.get_price_input(eth_address,
                                      usdc_address,
                                      1 * 10**18,
                                      fee=fee_tier)  # 1 ETH in wei
print(f"1 ETH = {eth_in_usdc / 10**6} USDC")
