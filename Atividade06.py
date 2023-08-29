def sobrenome():
	usuario= input("Digite seu primeiro nome, por favor:")
	espaco_maiusculo= usuario.upper().replace(" ", " ")
	sobrenome= input("Digite seu sobrenome, por gentileza: ")
	sobrenome_minusculo_espaco= sobrenome.lower().replace(" ", " ")
	print(" O seu primeiro Nome é: " , espaco_maiusculo , " e seu sobrenome é: " , sobrenome_minusculo_espaco )
	return sobrenome
sobrenome()