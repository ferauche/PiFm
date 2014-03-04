!#\usr\python
### Author: Thiago Ferauche
### 03/03/2014

import PiFm

op=0

while(op!=3):
	print("Selecione uma opção")
	print("[1] Star Wars")
	print("[2] Risadas")
	print("[3] Sair")
	op=int(input("Entre com sua opção..: "))

	if op==1:
		print("\n Tocando Star Wars...")
		PiFm.play_sound("sound.wav")
	elif op==2:
		print("\n Risadas... ")
		PiFm.play_sound("risada1.wav")
		PiFm.play_sound("risada2.wav")
		PiFm.play_sound("evil.wav")

print("Fim")
