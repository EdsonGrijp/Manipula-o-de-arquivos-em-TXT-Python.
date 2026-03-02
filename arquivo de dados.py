# Criando e gravando dados em um arquivo (considerando que o arquivo SAIDA.txt
# não exista no caminho atural).

#novo_arquivo = open('C:/PythonSAIDA.txt', 'w')
#novo_arquivo.write('Aula de manipulação de arquivos em python')
#novo_arquivo.write('Escrevendo dados em um arquivo')
#novo_arquivo.write('\nCriando uma nova linha')
#novo_arquivo.close()

#============================================================
#Adicionando novas linhas num arquivo existente
#novo_arquivo = open('C:/PythonSAIDA.txt', 'a')
#novo_arquivo.write('\n Incluindo uma nova linha')
#novo_arquivo.close()
#================================================================
#Lendo dados de um arquivo linha a linha
#arquivo = open('C:/PythonSAIDA.txt', 'r')
#or linha in arquivo:
#    print(linha)

#arquivo.close()

#===============================================================
#Lendo dados do arquivo por inteiro e não linta por linha
#arquivo = open('C:/PythonSAIDA.txt', 'r')
#conteudo = arquivo.read()#lendo o conteudo do arquivo como uma String
#print('Conteúdo - método read()...')
#print(conteudo)
#print(type(conteudo))

#=================================================
#Gravando uma lista em um arquivo
# Lista com os nomes (já com quebra de linha)
lista = ['\nJoão', '\nMaria', '\nJoaquim']

# Abre o arquivo para adicionar (append)
arquivo = open('C:/PythonSAIDA.txt', 'a')

# Escreve cada item da lista manualmente (mais seguro)
for nome in lista:
    arquivo.write(nome)

# Fecha o arquivo
arquivo.close()

print("Pronto! Verifique o arquivo.")



