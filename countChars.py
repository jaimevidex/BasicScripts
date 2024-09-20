# Script para contar o número de caracteres em um arquivo de texto
def contar_caracteres(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            conteudo = file.read()
            num_caracteres = len(conteudo)
            print(f"O número de caracteres no ficheiro é: {num_caracteres}")
    except FileNotFoundError:
        print("O ficheiro não foi encontrado. Verifique o caminho e tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Insira o caminho do ficheiro abaixo
filepath = input("Insira o caminho completo do ficheiro: ")
contar_caracteres(filepath)