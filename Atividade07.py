def completo():
	nome_todo= input("Digite o seu nome completo por favor: ")
	primeiro_nome, sobrenomeuser=nome_todo.split()
	nome_completinho= nome_todo.upper()
	nome_completinho_em_minusculo= nome_todo.lower()

	tamanho_nome_completo= len(nome_todo)

	print(" O seu nome completo em letras maiuculas é: " , nome_completinho)
	print(" O seu nome todo em letras minúsculas é: " , nome_completinho_em_minusculo)
	print(" O seu nome todo é " , tamanho_nome_completo)
	return completo
completo()