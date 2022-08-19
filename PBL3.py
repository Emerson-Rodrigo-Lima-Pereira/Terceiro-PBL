import os
import sys

#função para indexar Arquivos
def indexacao_arquivo(indice_invertido, raiz_indice_invertido):
	try:
		with open(raiz_indice_invertido, "w+") as indice:
			for linha in indice_invertido:
				indice.write(f"{linha}@°{indice_invertido[linha]}\n")
	except TypeError:	
		pass		
		
#função para ler o Arquivo e passá-lo para um dicionario
def extrair_dicionario(raiz_indice_invertido, indice_invertido):

    if os.path.isfile(raiz_indice_invertido):

        with open(raiz_indice_invertido, "r") as dic:
            for linha in dic.readlines():
                if linha != "\n":
                    chave, conteudo = linha.rstrip("\n").split("@°")
                    indice_invertido[chave] = eval(conteudo)
        return indice_invertido
    else:
        with open(raiz_indice_invertido, "w+") as dic:
            return indice_invertido

#função para criar o indice invertido
def inverted_index(raiz_arquivo, indice_invertido):

	#função para abrir o Arquivo e passá-lo para uma variável
	try:
		with open(raiz_arquivo, "r",encoding="utf8" ) as arquivo:
			arquivo = arquivo.read()
			arquivo = arquivo.split()
			dicionario = {}
			stopwords = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'é', 'com', 'não', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'à', 'seu', 'sua', 'ou', 'ser', 'quando', 'muito', 'há', 'nos', 'já', 'está', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'era', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'estão', 'você', 'tinha', 'foram', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 'minha', 'têm', 'numa', 'pelos', 'elas', 'havia', 'seja', 'qual', 'será', 'nós', 'tenho', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 'te', 'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos', 'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houverá', 'houveremos', 'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'era', 'éramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fôssemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'será', 'seremos', 'serão', 'seria', 'seríamos', 'seriam', 'tenho', 'tem', 'temos', 'tém', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam']

			#função para passar os termos do Arquivo que não são StopWords
			for palavra in arquivo:
				if palavra not in stopwords:
					palavra = palavra.lower().replace(":","").replace(",","").replace(".","").replace(";","").replace("!","").replace("?","").replace("(","").replace(")","").replace("[","").replace("]","").replace("{","").replace("}","").replace("“","").replace("”","")

					#função para adicionar a frequencia do termo
					if palavra != "":
						if palavra not in dicionario.keys():
							dicionario[palavra] = 1
						else:
							dicionario[palavra] +=1

			#função para adicionar o termo e a frequencia dele no indice invertido
			for palavra in dicionario:
				if palavra not in indice_invertido.keys():
					indice_invertido[palavra] = {raiz_arquivo:dicionario[palavra]}
				else:
					indice_invertido[palavra][raiz_arquivo] = dicionario[palavra]

		return indice_invertido
	except UnicodeDecodeError:
		print("Arquivo não compatível.")

#função para ordenar os Arquivos pela ordem de frequência dos termos
def ordenar(indice_invertido):

	lista = []

	for arquivo in indice_invertido:
		lista.append((arquivo,indice_invertido[arquivo]))
	#algoritmo de Bubble sort
	for i in range(len(lista)-1):
		for ii in range(len(lista)-i-1):
			if lista[ii][1] < lista[ii+1][1]:
				aux = lista[ii+1]
				lista[ii+1] = lista[ii]
				lista[ii] = aux

	return lista

#função para buscar Arquivos pelos termos
def buscar_item(lista, termo, indice_invertido):

	if termo in indice_invertido:
		print("------------------------------------------")
		print("O termo {} foi encontrado no(s) Arquivo(s):".format(termo))
		print()

		for item in lista:
			print(item)
		print("------------------------------------------")

#função para remover um Arquivo do indice invertido
def remover(raiz_arquivo, indice_invertido):

	for arquivo in indice_invertido:
		if raiz_arquivo in indice_invertido[arquivo].keys():
			indice_invertido[arquivo].pop(raiz_arquivo)

	for item in indice_invertido.copy():
		if not indice_invertido[item]:
			indice_invertido.pop(item)

	return indice_invertido

#função para mostrar o indice invertido
def mostrar_indice(indice_invertido):

	print("----------------Indice Invertido---------------\n")

	for item in indice_invertido:
		print(item+" : ", end="")
		for chave in indice_invertido[item].keys():
			print("({} : {}) ".format(chave, indice_invertido[item][chave]), end="")
		print()
		print()
	print("-----------------------------------------------")

#função para mostrar um tutorial do funcionamento
def tutorial():

	print("-----------------------------------------------------Funcionamento----------------------------------------------------")
	print("Para o código funcionar os argumentos devem ser escritos na seguinte ordem:\n\nLinguagem: python;\nNome do Arquivo: emersonrodrigolimapereirapbl3.py;\nFunção: indexar, buscar, remover, mostrar_indice, ajuda ou atualizar;\nEndereço do Arquivo: qualquer um.\n\nExemplo:\n\npython emersonrodrigolimapereirapbl3.py indexar C:/Users/55779/Pictures/emerson\n\nObservação:\n\nQuando a Função escolhida for a de buscar, mostrar_indice ou ajuda, não é necessário escrever o Endereço do Arquivo. Além disso, quando o Endereço do Arquivo ou diretório conter algum espaço, deixe-a entre aspas.")
	print("----------------------------------------------------------------------------------------------------------------------")


def main():

	#função para ler a linha de comando
	opcao = sys.argv
	dicionario_chaves = {}
	#função para aceitar só 3 Argumentos ou menos
	if len(opcao) <= 3 and len(opcao) != 1:

		#função para aceitar só Argumentos válidos
		if opcao[1] != "indexar" and opcao[1] != "buscar" and opcao[1] != "remover" and opcao[1] != "mostrar_indice" and opcao[1] != "ajuda" and opcao[1] != "atualizar":
			
			tutorial()
		#função para indentificar se tem só 3 Argumentos
		if len(opcao) == 3:	
			raiz_arquivo = opcao[2]

			#função para indentificar se o usuário quer buscar um termo
			if opcao[1] != "buscar":
				
				if os.path.isdir(raiz_arquivo) or os.path.isfile(raiz_arquivo):
					pass
				else:
					tutorial()
				

			indice_invertido = {}
			raiz_indice_invertido = 'indice_invertido.ddd'
			raiz_cache_chaves = "chaves_diretorios.ddd"
			indice_invertido = extrair_dicionario(raiz_indice_invertido, indice_invertido)
			dicionario_chaves = extrair_dicionario(raiz_cache_chaves, dicionario_chaves)
			#função para indentificar se o usuário quer indexar um Arquivo ou um Diretório
			if opcao[1] == "indexar":
				raiz_arquivo = opcao[2]
				if os.path.isdir(raiz_arquivo):
					for raiz, diretorios, arquivos in os.walk(raiz_arquivo):
						for chave in arquivos:
							raiz_arquivo = raiz+"/"+chave
							if raiz_arquivo[-4:] == ".txt":
								if raiz not in dicionario_chaves.keys():
									dicionario_chaves[raiz] = [raiz_arquivo]
								else:
									dicionario_chaves[raiz].append(raiz_arquivo)
								indexacao_arquivo(dicionario_chaves, raiz_cache_chaves)
								indice_invertido = inverted_index(raiz_arquivo, indice_invertido)
					indexacao_arquivo(indice_invertido, raiz_indice_invertido)

				elif os.path.isfile(raiz_arquivo):
					if raiz_arquivo[-4:] == ".txt":
						local = os.path.dirname(raiz_arquivo)
						if local not in dicionario_chaves.keys():
							dicionario_chaves[local] = [raiz_arquivo]
						else:
							dicionario_chaves[local].append(raiz_arquivo)
						indexacao_arquivo(dicionario_chaves, raiz_cache_chaves)
						indice_invertido = inverted_index(raiz_arquivo, indice_invertido)
					indexacao_arquivo(indice_invertido, raiz_indice_invertido)

			#função para indentificar se o usuário quer buscar por um termo
			elif opcao[1] == "buscar":
				termo = opcao[2]
				if termo in indice_invertido:
					lista = ordenar(indice_invertido[termo])
					buscar_item(lista, termo, indice_invertido)
				else:
					pass
			#função para indentificar se o usuário quer remover um Arquivo ou um Diretório
			elif opcao[1] == "remover":
				raiz_arquivo = opcao[2]
				if os.path.isdir(raiz_arquivo):
					for nome_arquivo in dicionario_chaves[raiz_arquivo]:
						remover(nome_arquivo, indice_invertido)

				else:
					if raiz_arquivo[-4:] == ".txt":
						indice_invertido = remover(raiz_arquivo, indice_invertido)
				indexacao_arquivo(indice_invertido, raiz_indice_invertido)

			#função para indentificar se o usuário quer atualizar o indice invertido
			elif opcao[1] == "atualizar":
				raiz_arquivo = opcao[2]
				if os.path.isdir(raiz_arquivo):
					for nome_arquivo in dicionario_chaves[raiz_arquivo]:
						indice_invertido = remover(nome_arquivo, indice_invertido)
					for raiz, diretorios, arquivos in os.walk(raiz_arquivo):
						for chave in arquivos:
							raiz_arquivo = raiz+"/"+chave
							if chave[-4:] == ".txt":
								if raiz not in dicionario_chaves.keys():
									dicionario_chaves[raiz] = [raiz_arquivo]
								else:
									dicionario_chaves[raiz].append(raiz_arquivo)
								indexacao_arquivo(dicionario_chaves, raiz_cache_chaves)	
									
								indice_invertido = inverted_index(raiz_arquivo, indice_invertido)
					indexacao_arquivo(indice_invertido, raiz_indice_invertido)

				elif os.path.isfile(raiz_arquivo):
					if raiz_arquivo[-4:] == ".txt":
						local = os.path.dirname(raiz_arquivo)
						if local not in dicionario_chaves.keys():
							dicionario_chaves[local] = [raiz_arquivo]
						else:
							dicionario_chaves[local].append(raiz_arquivo)
						indexacao_arquivo(dicionario_chaves, raiz_cache_chaves)
						indice_invertido = remover(raiz_arquivo, indice_invertido)
						indice_invertido = inverted_index(raiz_arquivo, indice_invertido)
					indexacao_arquivo(indice_invertido, raiz_indice_invertido)

		#função para indentificar se só tem 2 Argumentos
		elif len(opcao) == 2:
			indice_invertido = {}
			raiz_indice_invertido = 'indice_invertido.ddd'
			indice_invertido = extrair_dicionario(raiz_indice_invertido, indice_invertido)

			#função para indentificar se o usuário quer ver o indice invertido
			if opcao[1] == "mostrar_indice":
				mostrar_indice(indice_invertido)

			#função para indentificar se o usuário quer ajuda
			elif opcao[1] == "ajuda":
				tutorial()
	#função para mostrar o funcionamento do código caso tenha mais argumentos
	else:
		tutorial()

if __name__ == "__main__":
	main()