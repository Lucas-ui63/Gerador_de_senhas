# Calculadora de preço teto simples (Seguindo a fórmula bazin)

class Calculadora:
    def __init__(self):
        self.dividendos = 0
        self.dy = 0
        pass

    def calcular_teto(self, valor_acao, dividend_yild):
        dividend = dividend_yild / 100
        return valor_acao / dividend
calc = Calculadora()
tetos = {}
while True:
    try:
        ticker = input("Digite o nome do ativo (ex PETR4): ")
        valor_div = float(input("-- Dica: Utilize o valor médio dos dividendos pagos nos últimos 5 anos.-- \n Digite o valor do dividendo (em R$): ").replace(",", "."))
        dividend_yild = float(input("-- Dica: Utilize o DY médio dos ultimos 5 anos.-- \n Digite o dividend yild que espera receber (em %): ").replace(",", "."))
        teto = calc.calcular_teto(valor_div, dividend_yild)
        tetos[ticker] = teto
        print(f"Preço teto: R$ {teto:.2f}")
        print(f"Margem segura: R$ {teto * (1 - 0.20):.2f}")
    except ValueError:
        print("Por favor, digite um valor numérico.")
    exit = input("Deseja fechar a calculadora? (s/n): ")
    if exit == "s":
        break
    
for ticker, preco in tetos.items():
    print(f"Preço teto de {ticker}: R$ {preco:.2f}")