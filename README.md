#Gerenciador de Memória
##Autores
[Rafaelo Pinheiro](mailto:rafaelo.pinheiro1988@gmail.com)

[Eduardo Veiga](mailto:kluwe@softwarelivre.org)

[Harlan Maas Martins](mailto:hmaas00@hotmail.com)

[Eliezer Flores](mailto:eliezersflores@gmail.com)



#Introdução 
* Implementação de um simulador de gerência dinâmica de memória
* Utilização da linguagem de programação python
* Projeto desenvolvido com base no algoritmo Mark-and-Sweep

#Arquivo .mypyc 
* Contém bytecodes de alocações de memória de um programa
* Contém informações essenciais sobre as classes de um programa
* O Mark Sweep irá ler este arquivo para realizar as operações de alocação 

#Processo 

* Busca seqüencial de  uma instrução no no arquivo .mypyc
* Instrução é decodificada para definir qual  operação será feita(alocação, operação será feita(alocação, referenciação) 
* Decodificação das instruções (referencia dos objetos)
* Execução da operação de alocação(caso seja essa a operação a ser feita)
* Ajuste das referências. 


[Mais informações](https://github.com/eduardoveiga/mark-sweep/blob/master/mark%20sweep.pdf)