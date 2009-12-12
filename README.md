#Gerenciador de Mem�ria
##Autores
[Rafaelo Pinheiro](mailto:rafaelo.pinheiro1988@gmail.com)

[Eduardo Veiga](mailto:kluwe@softwarelivre.org)

[Harlan Maas Martins](mailto:hmaas00@hotmail.com)

[Eliezer Flores](mailto:eliezersflores@gmail.com)



#Introdu��o 
* Implementa��o de um simulador de ger�ncia din�mica de mem�ria
* Utiliza��o da linguagem de programa��o python
* Projeto desenvolvido com base no algoritmo Mark-and-Sweep

#Arquivo .mypyc 
* Cont�m bytecodes de aloca��es de mem�ria de um programa
* Cont�m informa��es essenciais sobre as classes de um programa
* O Mark Sweep ir� ler este arquivo para realizar as opera��es de aloca��o 

#Processo 

* Busca seq�encial de  uma instru��o no no arquivo .mypyc
* Instru��o � decodificada para definir qual  opera��o ser� feita(aloca��o, opera��o ser� feita(aloca��o, referencia��o) 
* Decodifica��o das instru��es (referencia dos objetos)
* Execu��o da opera��o de aloca��o(caso seja essa a opera��o a ser feita)
* Ajuste das refer�ncias. 


[Mais informa��es](https://github.com/eduardoveiga/mark-sweep/blob/master/mark%20sweep.pdf)