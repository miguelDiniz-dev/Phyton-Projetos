print("Escolha a operação:")
print("1- soma (+)")
print("2- subtração (-)")
print("3- multiplicação (*)")
print("4- divisão (/)")
operacao = input("Digite o número da operação (1,2,3,4):")
valor1 = float(input("Digite o primeiro número:"))
valor2 = float(input("Digite o segundo número:"))
if operacao == '1':
    resultado = valor1 + valor2
    print("primeiro número inserido + segundo número inserido =", resultado)
elif operacao == '2':
    resultado = valor1 - valor2
    print("primeiro valor inserido - segundo valor inserido =", resultado)
elif operacao == '3':
    resultado = valor1 * valor2
    print("primeiro número inserido * segundo número inserido =", resultado)
elif operacao == '4':
    resultado = valor1 / valor2
    print("primeiro valor inserido / segundo valor inserido =", resultado)
else:
    print("Operação inválida, escolha uma operação válida.")
