def cadastro():
    print("=== Cadastro do Jogador ===")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    print(f"\nBem-vindo(a), {nome}! Vamos começar o quiz!\n")
    return nome

def quiz():
    perguntas = [
        {
            "pergunta": "Qual o menor país do mundo?",
            "opcoes": ["a) Vaticano", "b) Brasil", "c) Rússia", "d) Italia"],
            "resposta": "a"
        },
        {
            "pergunta": "Qual o maior páis do mundo?'?",
            "opcoes": ["a) EUA", "b) China", "c) Rússia", "d) Índia"],
            "resposta": "c"
        },
