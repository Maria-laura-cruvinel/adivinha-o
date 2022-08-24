from forex_python.converter import CurrencyRates

C = CurrencyRates()

vl = float(input("\nQual o valor em Dolar você deseja converter para real?\n"))

r = round(C.convert("USD", "BRL", vl), 2)

print(f"${vl} = R${r}")
