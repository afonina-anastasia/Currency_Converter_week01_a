if __name__ == "__main__":
    USD_TO_YUAN = 6.74
    YUAN_TO_USD = 0.15
    print(f'Enter number "1" to convert dollars to Yuan or number "2" to convert Yuan to dollars: ')

    while True:
        try:
            number = int(input("Number: "))
            amount = float(input("Please enter an amount for the conversion: "))
            if number == 1:
                print(f'Date: 04.02.2023\n'
                      f'currency exchange rate: 6.74')
                print(f'{amount} USD in CNY = {(float(amount) * USD_TO_YUAN):.2f} CNY')

                break

            elif number == 2:
                print(f'Date: 04.02.2023\n'
                      f'currency exchange rate: 0.15')
                print(f'{amount} CNY in USD = {(float(amount) * YUAN_TO_USD):.2f} USD')
                break
            elif number > 2:
                print(f'bbTry again. Enter the numbers "1" or "2 ')

            else:
                number = int(input("bbNumber: "))
                amount = float(input("Please enter an amount for the conversion: "))

        except:
            print(f'Try again. Enter the numbers "1" or "2 ')







