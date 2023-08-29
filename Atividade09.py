def remover_vogais(texto):
    vogais = "aeiouAEIOU"
    texto_com_falta_de_vogais = ""

    for letra in texto:
        if letra not in vogais:
            texto_com_falta_de_vogais += letra

    return texto_com_falta_de_vogais


    texto = input("Digite um texto: ")
    texto_sem_vogais = remover_vogais(texto)
    print("Texto sem vogais:", texto_com_falta_de_vogais)
