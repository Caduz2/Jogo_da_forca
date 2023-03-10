import os

# Lista de palavras
palavras = ["banana", "maçã", "pera", "laranja", "abacaxi"]

# Escolhe uma palavra aleatória da lista
palavra_secreta = palavras[int(input("Escolha o número da palavra secreta (0-4):"))]

# Variáveis
letras_acertadas = ["_" for letra in palavra_secreta]
letras_erradas = []

# Desenho do boneco
desenho = ["""
   _________
  |         |
  |         |
  |         
  |         
  |
__|__
""",
"""
   _________
  |         |
  |         |
  |         O
  |         
  |
__|__
""",
"""
   _________
  |         |
  |         |
  |         O
  |         |
  |
__|__
""",
"""
   _________
  |         |
  |         |
  |         O
  |        /|
  |
__|__
""",
"""
   _________
  |         |
  |         |
  |         O
  |        /|\\
  |
__|__
""",
"""
   _________
  |         |
  |         |
  |         O
  |        /|\\
  |        /
__|__
""",
"""
   _________
  |         |
  |         |
  |         O
  |        /|\\
  |        / \\
__|__
"""]

# Loop do jogo
while "_" in letras_acertadas and len(letras_erradas) < 6:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(desenho[len(letras_erradas)])
    print("Palavra: " + " ".join(letras_acertadas))
    print("Letras erradas: " + " ".join(letras_erradas))
    letra = input("Adivinhe uma letra: ").lower()
    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_acertadas[i] = letra
    else:
        letras_erradas.append(letra)

# Verifica se o jogador ganhou ou perdeu
os.system('cls' if os.name == 'nt' else 'clear')
print(desenho[len(letras_erradas)])
if "_" not in letras_acertadas:
    print("Parabéns! Você acertou a palavra secreta.")
else:
   print("Você foi enforcado!")
