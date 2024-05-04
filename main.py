import random

def rock_paper_scissors():
  user = input("Escolha pedra, papel ou tesoura: ")
  computer = random.choice(['pedra', 'papel', 'tesoura'])
  print(f"Ryan Gosling escolheu {computer}")

  if user == computer:
    return "Empate AAAAAAAAAAAAAAH"

  elif (user == "pedra" and computer == "tesoura" or (user == "papel"    and computer == "pedra")) or (user == "tesoura" and computer == "papel"):
    return "Você Ganhou Baitola"
  else:
    return "Você perdeu Otário"

print(rock_paper_scissors())