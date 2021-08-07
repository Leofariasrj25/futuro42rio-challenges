# Desafio 2 - calculadora simples

# Conversor de criptomoedas.

# cotações com base no dia 23/07/2021
usd_brl = 5.18
btc_brl = 168450.000

def from_brl_to_usd(brl):
    return round((brl / usd_brl), 2)

def from_brl_to_btc(brl):
    return round((brl / btc_brl), 8)

def convert_input_brl():
    return float(input(">R$").replace(",", "."))

def main(): 
    print("Bem vindo a conversora de moedas tabajara 3000")
    print("Digite:")
    print("usd para converter de real para dólar")
    print("btc para converter de real para bitcoin")
    currency = input('>')

    if currency == 'usd':
        print("Coversão de real em dólar")
        
        brl = convert_input_brl()
        brl_usd = from_brl_to_usd(brl)
        print(f"R${brl} equivale a ${brl_usd}")

    elif currency == "btc":
        print("Conversão de real em bitcoin")

        brl = convert_input_brl()
        brl_btc = from_brl_to_btc(brl)
        print(f"R${brl} equivale a {brl_btc}btc")

    
    else:
        print("por favor, digite uma moeda válida.")
        exit(0)



main()
