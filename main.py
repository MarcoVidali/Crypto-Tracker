# Importings
import os
from rich import print
import cryptocompare



# Variables
cryptos_names = ["Bitcoin (BTC)", "Ethereum (ETH)", "Cardano (ADA)", "Tether (USDT)", "BinanceCoin (BNB)", "XRP (XRP)", "Solana (SOL)", "USDCoin (USDC)", "Polkadot (DOT)", "Dogecoin (DOGE)", "Avalanche (AVAX)", "Uniswap (UNI)", "Terra (LUNA)", "BinanceUSD (BUSD)", "Chainlink (LINK)", "Litecoin (LTC)", "Algorand (ALGO)", "BitcoinCash (BCH)", "WrappedBitcoin (WBTC)", "Cosmos (ATOM)"]



def main():   # Main function
    # Main loop
    while True:
        clearConsole()    # Clearing console

        # Printing each crypto name
        for crypto_name in cryptos_names:   # Looping each crypto name
            print(f"{blue(cryptos_names.index(crypto_name) + 1)}{blue(')')} {blue(crypto_name)}")   # Printing crypto name

        # Getting crypto to track
        crypto_to_track = ""
        while not crypto_to_track.strip():
            print(f"{white('Crypto to track: ')}", end = "")
            crypto_to_track = input()

        # Showing crypto price
        clearConsole()   # Clearing console

        # Variables
        last_price = 0

        while True:

            # Printing crypto price
            try:
                crypto_name = cryptos_names[int(crypto_to_track) - 1]   # Getting crypto to track index
                crypto_acronymum = crypto_name.split(' ')[1].replace('(', '').replace(')', '')   # Getting crypto acronymum
                crypto_price = cryptocompare.get_price(crypto_acronymum)[crypto_acronymum]['EUR']   # Getting crypto price

                # Printing crypto price
                if crypto_price >= float(last_price):   # Checking if crypto price is higher than last price
                    print(f"{green('€')}{green(crypto_price)}")   # Printing green crypto price
                    last_price = crypto_price   # Updating last price
                else:
                    print(f"{red('€')}{red(crypto_price)}")   # Printing red crypto price
                    last_price = crypto_price   # Updating last price
            except KeyboardInterrupt:
                main()   # Returning to main


def clearConsole():
    command = 'clear'   # Creating command
    if os.name in ('nt', 'dos'):   # Checking if os is NT or DOS based
        command = 'cls'   # Changing command
    os.system(command)   # Executing command

def blue(string):   # Making blue string
    return f"[bold blue]{string}[/bold blue]"   # Returning blue string

def white(string):   # Making white string
    return f"[bold white]{string}[/bold white]"   # Returning white string

def green(string):   # Making green string
    return f"[bold green]{string}[/bold green]"   # Returning green string

def red(string):   # Making red string
    return f"[bold red]{string}[/bold red]"   # Returning red string 



# Starting program
if __name__ == "__main__":
    main()