print("Olá seja bem vindos, insira as informações abaixo.")
nome= input("Digite seu nome: ")
peso= float(input("informe seu peso: "))
altura= float(input("informe sua altura: "))

imc= peso/(altura **2)

print(f"Olá {nome}, seu imc é de {imc:.2f} ")

if imc < 18.5:
    print("Seu IMC indica que você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Seu IMC indica que seu peso está normal.")
elif 25 <= imc < 29.9:
    print("Seu IMC indica que você está com sobrepeso.")
elif 30 <= imc < 34.9:
    print("Seu IMC indica que você está com obesidade grau 1.")
elif 35 <= imc < 39.9:
    print("Seu IMC indica que você está com obesidade grau 2.")
else:
    print("Seu IMC indica que você está com obesidade grau 3 (obesidade mórbida).")