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
