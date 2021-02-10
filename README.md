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

## Lecture 02 - Uncertainty
Nessa aula foi apresentado a noção de incerteza (*uncertainty*) no contexto de IA. Quando se trata de Inteligência Artificial, geralmente existe incerteza sobre as informações que o algoritmo está lidando. Em situações como essa, inferências são feitas com base em **probabilidade**. Por exemplo, no contexto de um robô que tem sensores e está explorando um ambiente, talvez ele não saiba exatamente onde está ou o que está ao redor, mas ele tem acesso a alguns dados que o permitem realizar inferências com alguma probabilidade.

A partir disso, entra-se no tópico de probabilidade. Probabilidade se resume a ideia de mundos possíveis (*possible worlds*), por exemplo, quando se joga um dado existem 6 mundos possíveis. Ademais, foram abordados conceitos e regras fundamentais no campo da probabilidade: probabilidade não-condicional (*unconditional probability*), probabilidade condicional (*conditional probability*), variável aleatória (*random variable*), independência de variável (*variable independence*), distribuição de probabilidade (*probability distribution*), regra de Bayes (*Bayes' rule*), probabilidade conjunta (*joint probability*), negação (*negation*), inclusão-exclusão (*inclusion-exclusion*), marginalização (*marginalization*), condicionamento (*conditioning*) e inferência (*inference*).

Trazendo essas noções para o contexto computacional, a estrutura de dados rede Bayesian (*Bayesian network*) foi explorada como uma forma de representação de modelos probabilístico. Trata-se de um grafo direcionado onde cada nó representa uma variável, uma aresta do nó *x* para o nó *y* representa que *x* é pai de *y*. Cada nó tem uma distribuição de probabilidade. Além disso, foi mostrado que, fazendo uso da rede Bayesian, é possível aplicar o método de inferência por enumeração (*inference by enumeration*) a fim de realizar inferências de probabilidade. Em relação à performance, a inferência por enumeração demonstra-se pobre, então um método otimizado denominado *sampling* também foi apresentado. 

Para concluir, foi abordado a noção de probabilidades variando em função do tempo. Afim de modelar essa ideia, foram apresentados os conceitos: suposição Markov (*Markov assumption*), cadeia de Markov (*Markov chain*), modelo oculto de Markov (*hidden Markov model*) e a suposição Markov sobre sensores (*sensor Markov assumption*).

### Projects
O site da *Harvard University* disponibilizou dois projetos que abordam o tema explorado nesse aula, as soluções dos projetos se encontram na pasta *Lecture 02 - Uncertainty* desse repositório. O primeiro projeto é uma implementação de uma versão do método de ranqueamento de páginas usado pelo Google denomidado "*PageRank*" que toma como parâmetro um corpus de páginas e ranquea as probabilidade de um internauta acessar cada página em função das ligações que elas têm entre si. O segundo projeto é uma implementação de um método para calcular a probabilidade da prole de um casal herdar o gene GJB2 sob condição de mutação (a mutação desse gene é responsável por causar problemas de audição). O cálculo foi realizado a partir da dstribuição de probabilidade conjunta das varáveis envolvidas no problema.
