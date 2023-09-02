from banco import obterConta

def consultarSaldo(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        print(f'Saldo: {cliente["saldo"]}')
    else:
        print('Conta não existe')

# if __name__ == "__main__":
#     consultarSaldo(2)
#     print(banco)