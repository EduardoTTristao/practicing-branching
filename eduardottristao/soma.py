def soma_cumulativa(lista):
	lista_n = []
	soma = 0
	for x in lista:
		soma = soma + x
		lista_n.append(soma)
	return lista_n
