import utils


def main():
    nome = input("Digite seu nome: ").strip()
    print(f'Olá, {nome}! Bem-vindo ao programa.')
    utils.hora_agora()

if __name__ == "__main__":
    main()
