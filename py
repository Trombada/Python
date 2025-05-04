def cadastro():
    print("=== Cadastro do Jogador ===")
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    print(f"\nBem-vindo(a), {nome}! Vamos começar o quiz!\n")
    return nome

def quiz():
    perguntas = [
        {
            "pergunta": "Qual é a capital do Brasil?",
            "opcoes": ["a) São Paulo", "b) Brasília", "c) Rio de Janeiro", "d) Salvador"],
            "resposta": "b"
        },
        {
            "pergunta": "Quem escreveu 'Dom Casmurro'?",
            "opcoes": ["a) Machado de Assis", "b) José de Alencar", "c) Clarice Lispector", "d) Graciliano Ramos"],
            "resposta": "a"
        },
        {
            "pergunta": "Quanto é 9 x 7?",
            "opcoes": ["a) 63", "b) 56", "c) 72", "d) 64"],
            "resposta": "a"
        },
        {
            "pergunta": "Qual é o maior planeta do sistema solar?",
            "opcoes": ["a) Terra", "b) Júpiter", "c) Saturno", "d) Marte"],
            "resposta": "b"
        },
        {
            "pergunta": "Em que continente está localizado o Egito?",
            "opcoes": ["a) Europa", "b) América", "c) África", "d) Ásia"],
            "resposta": "c"
        }
    ]

    pontos = 0

    for i, pergunta in enumerate(perguntas):
        print(f"Pergunta {i+1}: {pergunta['pergunta']}")
        for opcao in pergunta['opcoes']:
            print(opcao)
        resposta = input("Sua resposta (a/b/c/d): ").lower()

        if resposta == pergunta['resposta']:
            print("✅ Resposta correta!\n")
            pontos += 1
        else:
            print(f"❌ Resposta errada! A resposta correta era: {pergunta['resposta']}\n")

    return pontos

def main():
    nome = cadastro()
    pontuacao = quiz()
    print(f"{nome}, você terminou o quiz com {pontuacao} de {5} pontos!")

if __name__ == "__main__":
    main()
