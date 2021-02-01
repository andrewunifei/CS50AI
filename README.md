# CS50AI
Repositório para manter as atividades realizadas no curso "CS50AI - Introduction to Artificial Intelligence with Python" distribuído pela *Harvard University*. 

### Dependencies 
Alguns projetos necessitam da dependência [pygame](https://github.com/pygame/). Para instalação, digite a seguinte linha de código na pasta dos arquivos do projeto que necessita da dependência: `pip3 install -r requirements.txt`

## Lecture 00 - Search
Nessa aula foram apresentados conceitos introdutórios de Inteligência Artificial no campo da busca. "Busca" (*search*) no contexto de IA é o problema de tentar descobrir o que fazer quando se existe um tipo de situação em que o computador se encontra e algum tipo de ambiente em que um **agente** está inserido. E se almeja que, de alguma forma, esse agente seja capaz de encontrar uma solução para o problema. Esse problema pode aparecer em diversos formatos. Exemplos são: Jogo do 15 e tentar achar o caminho certo através de um labirinto ou dois lugares geográficos.

Também foram abordados e definidos algumas terminologias relacionadas a esse campo: agente (*agent*), estado (*state*), estado inicial (*inital state*), ações (*actions*), modelo de transição (*transition model*), espaço de estados (*state space*), teste de objetivo (*goal test*), custo do caminho (*path cost*) e nó (*node*).

Além disso, foram apresentados definições e implementações de algoritmos de busca, são eles: *depth-first search*, *breadth-first search*, *uninformed search*, *informed search*, *greedy best-first search* e *A\* search*. Também foi explorado a noção de *adversarial search* e alguns algoritmos relacionados a esse tipo de cenário, como: *minimax*, *alpha-beta pruning* e *depth-limited minimax*.

### Projects
O site da *Harvard University* disponibilizou dois projetos que abordam o tema explorado nesse aula, as soluções dos projetos se encontram na pasta *Lecture 00 - Search* desse repositório. O primeiro projeto é uma implementação do jogo *Six Degrees of Kevin Bacon* utilizando *breadth-first search* para realizar as buscas. O segundo é uma implementação do jogo da velha utilizando *minimax* como inteligência artificial adversária.

## Lecture 01 - Knowledge
Nessa aula foi apresentado a noção de conhecimento (*knowledge*) no contexto de IA. O tipo de inteligência artificial que opera com uma base de conhecimento é a *knowledge-based agent*. Porém, o foco principal da aula foi a noção de Lógica Proposicional (*Propositional Logic*), um método de lógica usado, nesse cenário, para representar o conhecimento de uma máquina e a sua capacidade de fazer inferências a partir desse conhecimento.

Foi abordado os conceitos mais básicos da Lógica Proposicional: símbolos proposicionais (*propositional symbols*), conectivos lógicos (*logical connective*), modelo (*model*), base de conhecimento (*knowledge base*), vinculação( *entailment*) e inferência (*inference*).

Além disso, duas formas de derivar as conclusões lógicas a partir da ideia de vinculação foram exploradas. Uma delas fazendo uso do conceito de "verificação de modelos" (*model checking*), onde todas as possibilidades de modelo são exploradas e se busca uma situação onde a base de conhecimento é verdadeira e a sentença também é verdadeira, dessa forma inferindo a vinculação; e a outra utilizando o método "forma normal conjuntiva" (*conjunctive normal form*), onde se faz uso das leis de De Morgan e o princípio da resolução (*resolution*) para se obter uma sentença lógica que seja um conjunção de disjunções e a partir disso, utilizando prova por absurdo, derivar uma senteça específica que possibilita inferir a qualidade da situação.

Por fim, foi apresentado superficialmente o método de Lógica de Primeira Ordem (*First-Order Logic*). Nesse método, existem dois tipos de símbolos: *constant symbols* que representam objetos e *predicate symbols* que representam relações ou funções. Essas funções recebem um argumento e o avalia, por exemplo, como verdadeiro ou falso. Todos os conectivos lógicos da Lógica Proposicional são válidos nesse método. A Lógica de Primeira Ordem também é composta pelo conceito de quantificadores (*quantifiers*). Existe dois tipos principais de quantificação, a quantificação universal (*universal quantifiers*) e a quantificação existencial (*existential quantification*).

### Projects
O site da *Harvard University* disponibilizou dois projetos que abordam o tema explorado nesse aula, as soluções dos projetos se encontram na pasta *Lecture 01 - Knowledge* desse repositório. O primeiro projeto é uma implementação do puzzle *Knights and Knaves* utilizando uma biblioteca de Lógica Proposicional disponibilizada. O segundo é uma implementação do jogo campo minado: uma IA foi implementada para tomar a decisão mais correta possível a partir de uma base de conhecimento e operações lógicas.
