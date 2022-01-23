import os
from rich import print
import cryptocompare
import datetime
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta



crypto_names = ["Bitcoin (BTC)", "Ethereum (ETH)", "Cardano (ADA)", "Tether (USDT)", "BinanceCoin (BNB)", "XRP (XRP)", "Solana (SOL)", "USDCoin (USDC)", "Polkadot (DOT)", "Dogecoin (DOGE)", "Avalanche (AVAX)", "Uniswap (UNI)", "Terra (LUNA)", "BinanceUSD (BUSD)", "Chainlink (LINK)", "Litecoin (LTC)", "Algorand (ALGO)", "BitcoinCash (BCH)", "WrappedBitcoin (WBTC)", "Cosmos (ATOM)"]
sections = ["Current price tracker", "Historical price checker", "Average price checker"]



def main():
    while True:
        clear_console()

        print(f"{green('Crypto Tracker')}\n")

        # Printing sections
        current_index = 1
        for section in sections:
            print(f"{blue(str(current_index) + ') ' + section)}")
            current_index += 1

        try:
            # Getting section
            print(f"\n{white('Section: ')}", end="")
            section = input()

            # Checking if section is valid
            if not section.strip():
                main()
            try:
                int(section)
            except:
                main()
            section = int(section)
            if section <= 0 or section > len(sections):
                main()

            # Going to section
            if section == 1:
                price()
            elif section == 2:
                historical()
            elif section == 3:
                average()
        except:
            clear_console()
            quit()

def price():
    while True:
        clear_console()

        print(f"{green(sections[0])}\n")

        # Printing cryptos names
        current_index = 1
        for crypto_name in crypto_names:
            print(f"{blue(str(current_index) + ') ' + crypto_name)}")
            current_index += 1

        try:
            # Getting crypto to track
            print(f"\n{white('Crypto to track: ')}", end="")
            crypto_to_track = input()

            # Checking if crypto is valid
            if not crypto_to_track.split():
                price()
            try:
                int(crypto_to_track)
            except:
                price()
            crypto_to_track = int(crypto_to_track)
            if crypto_to_track <= 0 or crypto_to_track > len(crypto_names):
                price()

            # Showing crypto price
            try:
                clear_console()
                last_price = 0.0
                while True:
                    crypto_name = crypto_names[crypto_to_track - 1]
                    crypto_acronymum = crypto_name.split(" ")[1].replace("(", "").replace(")", "")
                    crypto_price = cryptocompare.get_price(crypto_acronymum)[crypto_acronymum]["EUR"]

                    # Checking if price is lower/higher of last price
                    if crypto_price >= last_price:
                        print(f"{green('€' + str(crypto_price))}")
                        last_price = crypto_price   # Updating last price
                    else:
                        print(f"{red('€' + str(crypto_price))}")
                        last_price = crypto_price   # Updating last price
            except:
                price()
        except:
            main()

def historical():
    while True:
        clear_console()

        print(f"{green(sections[1])}\n")

        # Printing cryptos names
        current_index = 1
        for crypto_name in crypto_names:
            print(f"{blue(str(current_index) + ') ' + crypto_name)}")
            current_index += 1

        try:
            # Getting crypto to check historical price
            print(f"\n{white('Crypto to check historical price: ')}", end = "")
            crypto_to_historical = input()

            # Checking crypto to check historical price
            if not crypto_to_historical.strip():
                historical()
            try:
                int(crypto_to_historical)
            except:
                historical()
            crypto_to_historical = int(crypto_to_historical)
            if crypto_to_historical <= 0 or crypto_to_historical > len(crypto_names):
                historical()

            # Getting date
            print(f"{white('Date (dd/mm/yy): ')}", end="")
            date = input()

            # Checking date
            try:
                day, month, year = date.split("/")
            except:
                historical()
            try:
                int(day)
                int(month)
                int(year)
            except:
                historical()
            day, month, year = int(day), int(month), int(year)
            try:
                datetime.datetime(year, month, day)
            except:
                historical()

            clear_console()

            try:
                # Showing historical price
                crypto_name = crypto_names[crypto_to_historical - 1].split(" ")[0]
                crypto_acronymum = crypto_names[crypto_to_historical - 1].split(" ")[1].replace("(", "").replace(")", "")
                crypto_price = cryptocompare.get_historical_price(crypto_acronymum, "EUR", datetime.datetime(year, month, day))[crypto_acronymum]['EUR']
                print(blue(f"{crypto_name} price at {date}: €{crypto_price}"))

                # Blocking user
                while True:
                    input()
            except:
                historical()
        except:
            main()

def average():
    while True:
        clear_console()

        print(f"{green(sections[2])}\n")

        # Printing cryptos names
        current_index = 1
        for crypto_name in crypto_names:
            print(f"{blue(str(current_index) + ') ' + crypto_name)}")
            current_index += 1

        try:
            # Getting crypto to check average price
            print(f"\n{white('Crypto to check average price: ')}", end="")
            crypto_to_average = input()

            # Checking if crypto to check average is valid
            if not crypto_to_average.strip():
                average()
            try:
                int(crypto_to_average)
            except:
                average()
            crypto_to_average = int(crypto_to_average)
            if crypto_to_average <= 0 or crypto_to_average > len(crypto_names):
                average()

            # Getting since when to check average
            print(f"{white('Since the last (week/month/year): ')}", end="")
            since_last = input()
            since_last = since_last.lower()

            # Checking if since when to check average is valid
            if not since_last == "week" and not since_last == "month" and not since_last == "year":
                average()

            clear_console()

            try:
                # Showing average price
                if since_last == "week":
                    prices = []
                    days = []
                    percentage = 0

                    # Looping last 7 days
                    for day in range(7):
                        # Getting price that day ago
                        now = datetime.datetime.now()
                        day += 1
                        x_days_ago = now - datetime.timedelta(days = day)
                        crypto_name = crypto_names[crypto_to_average - 1].split(" ")[0]
                        crypto_acronymum = crypto_names[crypto_to_average - 1].split(" ")[1].replace("(", "").replace(")", "")
                        crypto_price = cryptocompare.get_historical_price(crypto_acronymum, "EUR",
                                x_days_ago)[crypto_acronymum]['EUR']

                        # Adding price to prices and day to days
                        prices.append(crypto_price)
                        days.append(f"{day}d")

                        # Printing percentage
                        percentage += 100 / 7
                        print(f"{blue(str(int(percentage)) + '%... ')}", end = "")

                    # Reversing prices and days
                    prices.reverse()
                    days.reverse()

                    # Plotting
                    plt.plot(days, prices)
                    plt.title("Crypto prices last week")
                    plt.show()

                if since_last == "month":
                    prices = []
                    weeks = []
                    percentage = 0

                    # Looping last 4 weeks
                    for week in range(4):
                        # Getting price that week ago
                        now = datetime.datetime.now()
                        week += 1
                        x_weeks_ago = now - datetime.timedelta(weeks = week)
                        crypto_name = crypto_names[crypto_to_average - 1].split(" ")[0]
                        crypto_acronymum = crypto_names[crypto_to_average - 1].split(" ")[1].replace("(", "").replace(")", "")
                        crypto_price = cryptocompare.get_historical_price(crypto_acronymum, "EUR",
                                x_weeks_ago)[crypto_acronymum]['EUR']

                        # Adding price to prices and week to weeks
                        prices.append(crypto_price)
                        weeks.append(f"{week}w")

                        # Printing percentage
                        percentage += 100 / 4
                        print(f"{blue(str(int(percentage)) + '%... ')}", end = "")

                    # Reversing prices and days
                    prices.reverse()
                    weeks.reverse()

                    # Plotting
                    plt.plot(weeks, prices)
                    plt.title("Crypto prices last month")
                    plt.show()

                if since_last == "year":
                    prices = []
                    months = []
                    percentage = 0

                    # Looping last 4 months
                    for month in range(12):
                        # Getting price that month ago
                        now = datetime.datetime.now()
                        month += 1
                        x_months_ago = now - relativedelta(months = month)
                        crypto_name = crypto_names[crypto_to_average - 1].split(" ")[0]
                        crypto_acronymum = crypto_names[crypto_to_average - 1].split(" ")[1].replace("(", "").replace(")", "")
                        crypto_price = cryptocompare.get_historical_price(crypto_acronymum, "EUR",
                                x_months_ago)[crypto_acronymum]['EUR']

                        # Adding price to prices
                        prices.append(crypto_price)
                        months.append(f"{month}m")

                        # Printing percentage
                        percentage += 100 / 12
                        print(f"{blue(str(int(percentage)) + '%... ')}", end = "")

                    # Reversing prices and months
                    prices.reverse()
                    months.reverse()

                    # Plotting
                    plt.plot(months, prices)
                    plt.title("Crypto prices last year")
                    plt.show()

                    # blocking user
                    while True:
                        input()
            except:
                average()
        except:
                main()



def clear_console():
    command = "clear"
    if os.name in ("nt", "dos"):   # Changing command
        command = "cls"
    os.system(command)   # Executing command

def green(string):
    return f"[bold green]{string}[/bold green]"

def blue(string):
    return f"[bold blue]{string}[/bold blue]"

def white(string):
    return f"[bold white]{string}[/bold white]"

def red(string):
    return f"[bold red]{string}[/bold red]"



if __name__ == "__main__":
    main()