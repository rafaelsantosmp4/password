import random
import string
import pyperclip

comprimento = int(input("Digite o comprimento da senha: "))

letras_maiusculas = string.ascii_uppercase
letras_minusculas = string.ascii_lowercase
numeros = string.digits
caracteres_especiais = string.punctuation

todos_caracteres = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais

senha = ''.join(random.choice(todos_caracteres) for _ in range(comprimento))

pyperclip.copy(senha)

print(f"Sua senha segura é: {senha}")
print("A senha foi copiada para a área de transferência.")