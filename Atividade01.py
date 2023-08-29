def substitui_palavra(palavra):
	palavra_substituida= ""
	vogais= "AEIOUaeiou"
	for letra in palavra:
		if letra in vogais:
			palavra_substituida += "*"
	else:
		palavra_substituida += letra
		return palavra_substituida

palavra= input(" Digite uma palavra por favor ")
palavra_substituida = substitui_palavra(palavra)
print(" A palavra substituída é: ", palavra_substituida);
