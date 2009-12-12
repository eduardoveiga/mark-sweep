# -*- coding: utf8 -*-
import sys
disco = []
tabela = []
memoria = []
tabelaraiz = {}
N = 256
tab = 0
porcentagem = None
def inicializa_memoria ( memoria ):
	for i in Range ( 0, N ):
		memoria.append( None )	
def inicializa_tabela ( tabela ):
	for i in Range ( 0, N ):
		tabela.append( None )
	return tabela
def Range ( ini, fim, passo = 1 ):
	lista = []
	i = ini
	while ( i < fim ):
		lista.append( i )
		i = i + passo
	return lista
	



#funcao que recebe uma lista de linhas de um arquivo e faz a leitura dessas linhas

def leArq(linhasArq):
	
	ler = 0
	
	for i in linhasArq:
		if ler == 1:
			
			k=filtro(i)
			executa(k)
			printciclo()
			
		else:
			if i.find("bytecodes") != -1:
				ler = 1
		
#fim leArq

def filtro( i ):		
	tuplaPart = None
	tuplatemp = None
	obT = None
	obN = None
	dadosClasse = None
	camposDestino = None
	camposOrigem = None
	listaGeral = []
	
	
	
	tuplaPart = i.partition(' = ')
	#se tiver () , temos que procurar os dados do objeto ex: obj() : temos que achar os campos, tipos e tamanho de 'obj'
	#feito isso, temos que retornar os campos de destino junto com esse dados
	if tuplaPart[2].find('(') != -1:
		obT = tuplaPart[2].partition('(')
		obN = obT[0]
		#agora obN esta com o nome do objeto
		#vamos coletar na lista t todos os dados da classe obN
		dadosClasse = retDadosClasse( obN )
		camposDestino = tuplaPart[0].rsplit('.')
		#print "teste destino: ",camposDestino 
		listaGeral.append(camposDestino)
		listaGeral.append(camposOrigem)
		listaGeral.append(dadosClasse)
		
	else: # se nao tem () se trata de uma atribuicao	
		camposDestino = tuplaPart[0].rsplit('.')
		
		tuplatemp = tuplaPart[2].partition(';')
		camposOrigem=tuplatemp[0].rsplit('.')
		listaGeral.append(camposDestino)
		listaGeral.append(camposOrigem)
		listaGeral.append(dadosClasse)
		
	return listaGeral
	
	
#fim filtro

#vai separar os nomes dos campos do destino
def trataDest(t0):
	dest = []
	tup = None
	if t0.find('.') != -1:	# se tem ponto!
		tup = t0.partition('.')
		dest.append(tup[0])
		while tup[2].find('.') != -1:	#se tem ponto em tup2
		
			if tup[2].find('.') != -1:	#se tem ponto em tup2
				tup = tup[2].partition('.')
				dest.append(tup[0])
		
		dest.append(tup[2])	
	else: # se argumento e simples
		return t0
	return dest
#fim trataDest


#vai separar os nomes dos campos da origem
def trataOrig(t2):
	orig = []
	tup = None
	if t2.find('.') != -1:	# se tem ponto!
		tup = t2.partition('.')
		orig.append(tup[0])
		while tup[2].find('.') != -1:	#se tem ponto em tup2
		
			if tup[2].find('.') != -1:	#se tem ponto em tup2
				tup = tup[2].partition('.')
				orig.append(tup[0])
		
		orig.append(tup[2])	
	else: # se argumento e simples
		return t2
	#print "ORIGENS",orig
	return orig
#fim trataOrig
	
#end filtro
	
#------------------------	
# funcao que retorna uma lista com os dados de uma classe, [ lista campos , tipo campos , tamanho classe ]
# argumentos: nome da classe que se deseja alocar
# acoes: essa funcao abre o arquivo onde se encontra o header do codigo e procura os dados da classe procurada

def retDadosClasse( nomeClasse ):
	f = open( 'arquivo.txt', 'r' )
	linhas = f.readlines()
	achou = 0
	tup = None
	str = None
	str2 = None
	tuplaPartCampos = None
	tuplaPartTipos = None
	tuplaPartTamanho = None
	listaCampos = None
	listaTipos = None
	varTamanho = 0
	listaGeral = []
	okCampos = 0
	okTipos = 0
	okTamanho = 0

	
	for i in linhas:
		if i.find('bytecodes') == -1: # enquanto nao chegamos na linha em que comeca as atribuicoes
			if achou == 0:
				if i.find('classe') != -1:  # se achou classe!
					tup = i.partition(' : ')
					
					if nomeClasse.find(tup[2].strip()) != -1: # se achou o nome mandado como argumento
					#if tup[2].find(nomeClasse) != -1: # se achou o nome mandado como argumento
						achou = 1
					
			else: # se ja achou
				if i.find('campos') != -1:
					tuplaPartCampos = i.partition(' : ')

					listaCampos = tuplaPartCampos[2].rsplit(',')

					okCampos = 1
					
					
				if i.find('tipos') != -1:
					tuplaPartTipos = i.partition(' : ')
					listaTipos = tuplaPartTipos[2].rsplit(',')
					okTipos = 1
					
					
				if i.find('tamanho') != -1:
					tuplaPartTamanho = i.partition(':')
					varTamanho = tuplaPartTamanho[2].rstrip()
					
					varintTamanho=int(varTamanho)
					okTamanho = 1
					
				if okCampos == 1 and okTipos == 1 and okTamanho == 1:
					listaGeral.append(nomeClasse)
					listaGeral.append(listaCampos)
					listaGeral.append(listaTipos)
					listaGeral.append(varintTamanho)
					#print listaGeral
					return listaGeral
		
		else:	return -1 #caso em que nao eh encontrado		
	
	return -1 #caso em que nao eh encontrado

					
#fim achaTamanho				
#---------------------




#---------------------
#programa principal
#---------------------
	

	
	

def Varredura ():	
	
	for pos,item in enumerate(tabela):
	
		if type(memoria[pos])==list:
	
			if memoria[pos][3]==False:
	
				for i in Range(pos,pos+memoria[pos][2]):
	
					tabela[i]=None
	
def garbage_collector ():
	gc = tabelaraiz.values()	
	for ob in gc:		
		percorre(ob)
		
	Varredura()
def percorre(x):
	

	
	
	#print memoria[x]
	if memoria[x][3]==False:
		
		memoria[x][3]=True
		for atr in memoria[x][1]:
			if atr != None:
				y=memoria[x+atr[1]]
				if y!=None:
				
					percorre (y)
	
		
	
				
def aloca(ID,ini,n):
	global tab	
	global porcentagem
	fim=ini+n		
	for i in Range (ini,fim):
		tabela[i] = True		
		tab = tab + 1
	memoria[ini]=ID
	
def gerarcabecalho(op):
	deslocamento=1
	classe=op[2][0]
	tamanho=op[2][3]
	listatrs=[]
	atrdesloc=0

	
	for i,atributo in enumerate(op[2][1]):
		tipo=op[2][2][i]
		
		if tipo=="ptr" or tipo=="ptr\n":
			atrdesloc=deslocamento
			deslocamento=deslocamento+1

		
		elif tipo=="int" or tipo=="int\n":
			
			atrdesloc=deslocamento
			deslocamento=deslocamento+4

		listatr=[atributo,atrdesloc]
		listatrs.append(listatr)
	
	list=[classe,listatrs,tamanho,False]
	return list
		
		
	
		
def executa (op):
	
	if op[2] !=None:
		
		alocado=calcula_espaco(op)					
		
		if(alocado==False):
			print "nao foi possivel alocar"
	else:
		referencias(op)		
def calcula_espaco(op):
	pos_cont=0
	#
	
	for indice,item in enumerate(tabela):
		
		if ( item == None and pos_cont<=op[2][3] ):
			pos_cont = pos_cont + 1	
		elif(item==True and pos_cont<=op[2][3]):
			pos_cont=0
		else:
			if ( pos_cont-1 == op[2][3] ): #Acho espaço na tabela para fazer a alocação
				ini = (indice-2) - ( op[2][3]-1)	
			
				ID=gerarcabecalho(op)	

				aloca (ID,ini,op[2][3])
				Ref=referencias(op,ini)
			
				return True
	return False	
def referencias(op,end=None):
	

	if end!=None:
		n=len(op[0])
	
		if(n==1):
		
			tabelaraiz[op[0][0]]=end
		else:
			calcula_pos_objeto(op,op[0][n-2],op[0][n-1],end)
	else:
		
		n=len(op[0])
		n2=len(op[1])
		endorig=calcula_pos(op[1],op[1][n2-1],n2,"origem")
		enddest=calcula_pos(op[0],op[0][n-1],n,"destino")
		
		if(n==1):
			
			tabelaraiz[op[0][0]]=endorig
			
		else:
			memoria[enddest]=endorig
			
def calcula_pos_objeto(op,objname,atrname,end):
	#print tabelaraiz[op[0][0]]
	
	atual=tabelaraiz[op[0][0]]
	
	for var in op[0]:
		#if (var != op[0][0]):
		for i,atualatr in enumerate(memoria[atual][1]):
				#if atualatr==op[0][i+1]
			if atualatr[0]==var:
				ponteirodes=memoria[atual][1][i][1]
				atual=memoria[atual+ponteirodes]
		if var==objname:
			endatr=calcula_pos_atributo(atual,atrname)
			insere_ponteiro(endatr,end)
			#printmemoria()
			return None
		
		
		
	#endatr=calcula_pos_atributo(objpos,atr)
	#memoria[endatr]

def calcula_pos_atributo(objpos,atrname):

	#n=len(obj[0][1])
	
	for i,atualatr in enumerate(memoria[objpos][1]):

		if atualatr[0]==atrname or atualatr[0]==atrname+"\n":
			
			atrdesloc=memoria[objpos][1][i][1]
			ponteiro=objpos+atrdesloc
			return ponteiro
	
		
def calcula_pos(pos,name,n,type):
	#print pos
	pont = 0
	if(n==1):
		if type=="destino":
			print""
		elif type=="origem":
			
			atualend=tabelaraiz[pos[0]]
		
			return atualend
	else:
		
		atualend=tabelaraiz[pos[0]]

		for var in pos:	
			for i,atualatr in enumerate(memoria[atualend][1]):
				if atualatr[0]==var or atualatr[0]==var+"\n":
					pont=memoria[atualend][1][i][1]
					
					#retorna o endereço do atributo 
				atualend=atualend+pont
				if var==name:
					if type=="destino":
						return atualend
						#retorna o conteúdo de um atributo	
					elif type=="origem":
						
						return memoria[atualend]
					

			
		
		
def insere_ponteiro(atrpos,end):
	#print "inserindo ponteiro"
	#print atrpos
	memoria[atrpos]=end	
		
		
	

def porcentagem_livre():
	cont=0
	for i in tabela:
		if i is None:
			cont = cont+1
	return (cont*100)/N
def porcentagem_ocupada():
	cont=0
	for i in tabela:
		if i is True:
			cont = cont+1
	return(cont*100)/N
def porcentagem_lixo():
	cont=0
	for i,item in enumerate(tabela):
		if item is False and memoria[i]!=None:
			cont=cont+1
	return(cont*100)/N
def printciclo():
	print "pos\tocupado\t\t\t\t\t\t\t\t\tmemória"
	for i,mempos in enumerate(memoria):
		#if type(mempos)==list:
		#	mempos = "ID"
		print i,"\t",tabela[i],"\t\t\t\t\t\t\t\t\t",mempos	
	print "memória livre: ",porcentagem_livre(),"% \t memória ocupada: ",porcentagem_ocupada()," % \t lixo: ",porcentagem_lixo(),"%"
		#print "memória livre: %s \t memória ocupada: %s \t lixo: %s \t"%porcentagem_livre()%porcentagem_ocupada%porcentagem_lixo
	raw_input()

inicializa_memoria(memoria)
inicializa_tabela(tabela)
linhas = file ( sys.argv[1], 'r' ).readlines()
leArq(linhas)
print tabelaraiz
garbage_collector()
for i,j in enumerate(tabela):
			if(j is True):
				print "tabela",i,j


	
for i,mempos in enumerate(memoria):
	if(mempos!=None):
		print i,mempos


	
'''op = 0
while (op != 3):
	print "Menu:"
	print '1. Chamada do Garbage Collector num determinado número de ciclos;'
	print '2. Chamada do Garbage Collector numa determinada porcentagem;'
	print '3. Sair do programa;'
	op = int ( raw_input ( 'Opção: ' ) )
	linhas = file ( 'arquivo.txt', 'r' ).readlines()
	if (op == 1):
		ciclos = int (raw_input( 'Informe o número de ciclos:' ) )	
		inicializa_memoria(memoria)
		inicializa_tabela(tabela)
		cont = 0
		for i in tabela:
			if cont < ciclos:
				print "cont<ciclos"
				leArq(linhas)
				cont = cont + 1
			else:
				garbage_collector()			
				cont = 0
				leArq(linhas)				
		for indice,i in enumerate(ref):
			print "referencias",i,'->',ref[i]	
		#for i,mempos in enumerate(memoria):
		#	if(mempos!=None):
		#		print i,mempos
		#for i,j in enumerate(tabela):
		#	if(j is True):
		#		print i,j
		#garbage_collector()
		#for i,j in enumerate(tabela):			
		#	print "tabela",i,j,"\t","memoria",i,memoria[i]
	elif (op == 2):		
		porcentagem = float (raw_input( 'Informe a porcentagem de endereços de memória alocada:' ) )	
		inicializa_memoria(memoria)
		inicializa_tabela(tabela)
		leArq(linhas)
		for indice,i in enumerate(ref):
			print "referencias",i,'->',ref[i]	
		for i,mempos in enumerate(memoria):
			if(mempos!=None):
				print i,mempos
		for i,j in enumerate(tabela):
			if(j is True):
				print "tabela",i,j
		
		garbage_collector()
		for i,mempos in enumerate(memoria):
			if(mempos!=None):
				print i,mempos
		for i,j in enumerate(tabela):			
			print "tabela",i,j,"\t","memoria",i,memoria[i]
	elif (op == 3):
		print 'Saindo do programa...'
		exit()
	else:
		print 'Você digitou a opção errada' '''
