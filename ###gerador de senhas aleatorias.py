###gerador de senhas aleatorias
import random

letras= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros= "0123456789"
simbolos= "!$#&"
todos_caracteres= letras + numeros + simbolos

tamanho_senha= {12,16,20,24,28,32,36,40,44,48,52,56,60}
tamanho_senha= random.choice(list(tamanho_senha))

senha_aleatoria= "".join(random.sample(todos_caracteres, tamanho_senha))
print("Senha gerada:", senha_aleatoria, "com a quantidade de caracteres de:", tamanho_senha)