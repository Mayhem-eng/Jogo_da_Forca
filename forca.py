from corpo import *
from time import sleep
from random import choice
import json
import os

números = [x for x in range(0, 10)]

def jogar():
	if len(números) == 0:
		return print("ACABOU O JOGO")
	palavra_acertadas = []
	letras_erradas = []
	erros = 0
	chances = 6

	with open("dicas.json", "r") as file:
		get = json.loads(file.read())

		escolhido = choice(números)

		palavra_secreta = str(get[escolhido]['palavra'])
		
	for index in range(len(palavra_secreta)):
		palavra_acertadas.insert(index, '_')
	
	cabecalho()

	print(palavra_acertadas)
	print()

	while True:
		sleep(0.5)
		print()
		print(f"DICA: {get[escolhido]['dica']}")

		chute = input("Chute: ").upper()
		print()

		if chute.upper() == palavra_secreta.upper():
			ganhou()
			break

		if chute in palavra_secreta.upper():
			if not chute in palavra_acertadas:
				print(f"TEM A LETRA [ {chute.upper()} ] NA PALAVRA SECRETA")
		
			for index, palavra in enumerate(palavra_secreta):
				if palavra.upper() == chute.upper():
					palavra_acertadas[index] = chute

		else:
			erros += 1
			chances-= 1
			corpo(erros, chances)
			if not chute in letras_erradas:
				letras_erradas.append(chute)
	
		if not erros == 6:
			print(f"PALAVRA: {palavra_acertadas}")

		if erros == 6:
			perdeu(palavra_secreta)
			break

		if not '_' in palavra_acertadas:
			ganhou()
			break

		print()
		print(f"Caracteres tentados: {letras_erradas}")

	números.remove(escolhido)

if __name__ == '__main__':
	while True:
		os.system('cls')
		jogar()
		print()
		jogar_dnv = input("Jogar denovo? [S/N] ").upper()
		if jogar_dnv  != 'S' or len(números) == 0:
			break
