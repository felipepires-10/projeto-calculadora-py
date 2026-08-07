def calcular():
    print("=== CALCULADORA EM PYTHON ===")

    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        print("\nEscolha a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            resultado = numero1 + numero2
            operador = "+"
        elif opcao == "2":
            resultado = numero1 - numero2
            operador = "-"
        elif opcao == "3":
            resultado = numero1 * numero2
            operador = "*"
        elif opcao == "4":
            if numero2 == 0:
                print("Erro: não é possível dividir por zero.")
                return
            resultado = numero1 / numero2
            operador = "/"
        else:
            print("Opção inválida.")
            return

        print(f"\nResultado: {numero1} {operador} {numero2} = {resultado}")

    except ValueError:
        print("Erro: digite apenas números válidos.")


if __name__ == "__main__":
    calcular()
