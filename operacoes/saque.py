from banco import obterConta

def sacar(conta: int, valor: float) -> None:
    cliente = obterConta(conta)
    if cliente:
        if cliente['saldo'] >= valor:
            cliente['saldo'] -= valor

            print('Saque realizado com sucesso!')
        else:
            print('Saldo insuficiente!')
    else:
        print('Cliente não encontrado!')


# if __name__ == "__main__":
#     sacar(1, 159.99)
#     print(banco)