# CS50AI
Repositório para manter as atividades realizadas no curso "CS50AI - Introduction to Artificial Intelligence with Python" distribuído pela *Harvard University*. 

# Table of Contents
- [Dependencies](#dependencies)
- [Lecture 00 - Search](#lecture-00---search)
    * [Projects](#projects)
- [Lecture 01 - Knowledge](#lecture-01---knowledge)
    * [Projects](#projects-1)
- [Lecture 02 - Uncertainty](#lecture-02---uncertainty)
    * [Projects](#projects-2)
- [Lecture 03 - Optimization](#lecture-03---optimization)
    * [Local Search](#local-search)
    * [Linear Programming](#linear-programming)
    * [Constraint Satisfaction Problems](#constraint-satisfaction-problems)
    * [Projects](#projects-3)
- [Lecture 04 - Learning](#lecture-04---learning)
    * [Supervised Learning](#supervised-learning)
        + [Classification](#classification)
        + [Linear Regression](#linear-regression)
        + [Evaluation Hypotheses](#evaluation-hypotheses)
    * [Reinforcement Learning](#reinforcement-learning)
        + [Markov Decision Process](#markov-decision-process)
        + [Q-Learning](#q-Learning)
    * [Unsupervised Learning](#unsupervised-learning)
        + [Clustering](#clustering)
    * [Projects](#projects-4)

### Dependencies 
#### TicTacToe Project (Lecture 00), Minesweeper Project (Lecture 01)
[pygame](https://github.com/pygame/)

#### Shopping Project (Lecture 04)
[scikit-learn](https://github.com/scikit-learn/)

## Lecture 00 - Search
Nessa aula foram apresentados conceitos introdutórios de Inteligência Artificial no campo da busca. "Busca" (*search*) no contexto de IA é o problema de tentar descobrir o que fazer quando se existe um tipo de situação em que o computador se encontra e algum tipo de ambiente em que um **agente** está inserido. E se almeja que, de alguma forma, esse agente seja capaz de encontrar uma solução para o problema. Esse problema pode aparecer em diversos formatos. Exemplos são: Jogo do 15 e tentar achar o caminho certo através de um labirinto ou dois lugares geográficos.

Também foram abordados e definidos algumas terminologias relacionadas a esse campo: agente (*agent*), estado (*state*), estado inicial (*inital state*), ações (*actions*), modelo de transição (*transition model*), espaço de estados (*state space*), teste de objetivo (*goal test*), custo do caminho (*path cost*) e nó (*node*).

Além disso, foram apresentados definições e implementações de algoritmos de busca, são eles: *depth-first search*, *breadth-first search*, *uninformed search*, *informed search*, *greedy best-first search* e *A\* search*. Também foi explorado a noção de *adversarial search* e alguns algoritmos relacionados a esse tipo de cenário, como: *minimax*, *alpha-beta pruning* e *depth-limited minimax*.

### Projects 
O site da *Harvard University* disponibilizou dois projetos que abordam o tema explorado nesse aula, as soluções dos projetos se encontram na pasta *Lecture 00 - Search* desse repositório.

O primeiro projeto é uma implementação do jogo *Six Degrees of Kevin Bacon* utilizando *breadth-first search* para realizar as buscas.

O segundo é uma implementação do jogo da velha utilizando *minimax* como inteligência artificial adversária.

## Lecture 01 - Knowledge
Nessa aula foi apresentado a noção de conhecimento (*knowledge*) no contexto de IA. O tipo de inteligência artificial que opera com uma base de conhecimento é a *knowledge-based agent*. Porém, o foco principal da aula foi a noção de Lógica Proposicional (*Propositional Logic*), um método de lógica usado, nesse cenário, para representar o conhecimento de uma máquina e a sua capacidade de fazer inferências a partir desse conhecimento.

Foi abordado os conceitos mais básicos da Lógica Proposicional: símbolos proposicionais (*propositional symbols*), conectivos lógicos (*logical connective*), modelo (*model*), base de conhecimento (*knowledge base*), vinculação (*entailment*) e inferência (*inference*).

Além disso, duas formas de derivar as conclusões lógicas a partir da ideia de vinculação foram exploradas. Uma delas fazendo uso do conceito de "verificação de modelos" (*model checking*), onde todas as possibilidades de modelo são exploradas e se busca uma situação onde a base de conhecimento é verdadeira e a sentença também é verdadeira, dessa forma inferindo a vinculação; e a outra utilizando o método "forma normal conjuntiva" (*conjunctive normal form*), onde se faz uso das leis de De Morgan e o princípio da resolução (*resolution*) para se obter uma sentença lógica que seja um conjunção de disjunções e a partir disso, utilizando prova por absurdo, derivar uma senteça específica que possibilita inferir a qualidade da situação.

Por fim, foi apresentado superficialmente o método de Lógica de Primeira Ordem (*First-Order Logic*). Nesse método, existem dois tipos de símbolos: *constant symbols* que representam objetos e *predicate symbols* que representam relações ou funções. Essas funções recebem um argumento e o avalia, por exemplo, como verdadeiro ou falso. Todos os conectivos lógicos da Lógica Proposicional são válidos nesse método. A Lógica de Primeira Ordem também é composta pelo conceito de quantificadores (*quantifiers*). Existe dois tipos principais de quantificação, a quantificação universal (*universal quantifiers*) e a quantificação existencial (*existential quantification*).

### Projects
O site da *Harvard University* disponibilizou dois projetos que abordam o tema explorado nesse aula, as soluções dos projetos se encontram na pasta *Lecture 01 - Knowledge* desse repositório.

O primeiro projeto é uma implementação do puzzle *Knights and Knaves* utilizando uma biblioteca de Lógica Proposicional disponibilizada.

O segundo é uma implementação do jogo campo minado, uma IA foi implementada para tomar a decisão mais correta possível a partir de uma base de conhecimento e operações lógicas.

## Lecture 02 - Uncertainty
Nessa aula foi apresentado a noção de incerteza (*uncertainty*) no contexto de IA. Quando se trata de Inteligência Artificial, geralmente existe incerteza sobre as informações que o algoritmo está lidando. Em situações como essa, inferências são feitas com base em **probabilidade**. Por exemplo, no contexto de um robô que tem sensores e está explorando um ambiente, talvez ele não saiba exatamente onde está ou o que está ao redor, mas ele tem acesso a alguns dados que o permitem realizar inferências com alguma probabilidade.

A partir disso, entra-se no tópico de probabilidade. Probabilidade se resume a ideia de mundos possíveis (*possible worlds*), por exemplo, quando se joga um dado existem 6 mundos possíveis. Ademais, foram abordados conceitos e regras fundamentais no campo da probabilidade: probabilidade não-condicional (*unconditional probability*), probabilidade condicional (*conditional probability*), variável aleatória (*random variable*), independência de variável (*variable independence*), distribuição de probabilidade (*probability distribution*), regra de Bayes (*Bayes' rule*), probabilidade conjunta (*joint probability*), negação (*negation*), inclusão-exclusão (*inclusion-exclusion*), marginalização (*marginalization*), condicionamento (*conditioning*) e inferência (*inference*).

Trazendo essas noções para o contexto computacional, a estrutura de dados rede Bayesian (*Bayesian network*) foi explorada como uma forma de representação de modelos probabilístico. Trata-se de um grafo direcionado onde cada nó representa uma variável, uma aresta do nó *x* para o nó *y* representa que *x* é pai de *y*. Cada nó tem uma distribuição de probabilidade. Além disso, foi mostrado que, fazendo uso da rede Bayesian, é possível aplicar o método de inferência por enumeração (*inference by enumeration*) a fim de realizar inferências de probabilidade. Em relação à performance, a inferência por enumeração demonstra-se pobre, então um método otimizado denominado *sampling* também foi apresentado. 

Para concluir, foi abordado a noção de probabilidades variando em função do tempo. A fim de modelar essa ideia, foram apresentados os conceitos: suposição Markov (*Markov assumption*), cadeia de Markov (*Markov chain*), modelo oculto de Markov (*hidden Markov model*) e a suposição Markov sobre sensores (*sensor Markov assumption*).

### Projects
O site da *Harvard University* disponibilizou dois projetos que abordam o tema explorado nesse aula, as soluções dos projetos se encontram na pasta *Lecture 02 - Uncertainty* desse repositório.

O primeiro projeto é uma implementação de uma versão do método de ranqueamento de páginas usado pelo Google denomidado "*PageRank*" que toma como parâmetro um corpus de páginas e ranquea as probabilidades de um internauta acessar cada página em função das ligações que elas têm entre si.

O segundo projeto é uma implementação de um método para calcular a probabilidade da prole de um casal herdar o gene GJB2 sob condição de mutação (a mutação desse gene é responsável por causar problemas de audição). O cálculo foi realizado a partir da dstribuição de probabilidade conjunta das variáveis envolvidas no problema.

## Lecture 03 - Optimization
Nessa aula foi apresentado a noção de otimização (*optimization*) no contexto de IA. Otimização é a escolha da melhor opção dado um conjunto de opções. A fim de explorar essa noção, foram abordadas **três categorias de problemas** que exigem algoritmos específicos para solução.

### Local Search
Algoritmo de busca que, geralemente, utiliza apenas um nó e realiza a busca movendo-se para nós vizinhos. Busca local é especialmente útil quando o escopo do problema não é o caminho (*path*), mas sim a solução.

Ainda nesse contexto, foi abordado o conceito de *state-space landscape*, que represeta um estado particular que um cenário poderia estar, e expressa características como: máximo global (*global maximum*), minímo global (*global minimum*), função objetivo (*objective function) e função de custo (*cost function*). Além disso, um exemplo apresentado de algoritmo de busca local foi o *hill climbing* e suas variantes (*steepest-ascent*, *stochastic*, *first-choice*, *random-restart* e *local beam search*) que são utéis dependendo da situação. O *hill climbing* expressa o problema da possibilidade de não se encontrar o máximo/mínimo global, que pode ser contornados pelo algoritmo *simulated anneling*, que simula o processo de um sistema de alta temperatura, onde coisas estão se movendo aleatoriamente, mas com o passar do tempo ocorre uma diminuição na temperatura e eventualmente se chega em uma solução.

### Linear Programming
Programação linear geralmente aparece no contexto de resolução para alguma função matemática. É uma família de problemas que apresenta uma situação do seguinte tipo:

Minimizar uma função de custo
<p align="center"><img src="http://www.sciweavers.org/download/Tex2Img_1613154101.png"></p>
Com limitações da forma
<p align="center"><img src="http://www.sciweavers.org/download/Tex2Img_1613154145.png"></p>
E com restrições para cada variável do tipo
<p align="center"><img src="http://www.sciweavers.org/download/Tex2Img_1613134174.png"></p>
Existem vários tipos de algoritmos para solucionar problemas dessa categoria, dois exemplos são *simplex* e *interior-point*.

### Constraint Satisfaction Problems
A ideia básica dos problemas da satisfação de restrições é uma situação onde se tem um número de variáveis que terão algum valor atribuido. Então, é necessário descobrir quais valores atribuir para essas variáveis, porém essas variáveis estão sujeitas a restrições particulares que irão limitar quais valores podem ser atribuidos a elas. Essa noção pode ser expressa da seguinte maneira:

Conjunto de variáveis
<p align="center"><img src="http://www.sciweavers.org/download/Tex2Img_1613135599.png"></p>
Conjunto de domínios para cada variável
<p align="center"><img src="http://www.sciweavers.org/download/Tex2Img_1613135591.png"></p>
E conjunto de restrições
<p align="center"><img src="http://www.sciweavers.org/download/Tex2Img_1613135659.png"></p>
Sudoku é um exemplo de problema da satisfação de restrições.

Foi mostrado que uma possibilidade de estruturar um *CSP* é utilizando grafo (*constraint graph*), onde os vértices representam as variáveis e as arestas representam restrições de domínio entre as variáveis. 

Além disso, foram apresentados conceitos de consistência de variável (*node consistency* e *arc consistency*) e classificações de restrições (*hard constraints*, *soft constraints*, *unary constraint* e *binary constraint*).
O algoritmo de busca que é geralmente utilizado quando se trata de problemas de satisfação de restrições é o *backtracking search* que, de forma aprimorada, utiliza outro algoritmo chamado *AC3* para manter consistência de arco (*arc consistency*) ao longo do processo.

### Projects
O site da *Harvard University* disponibilizou um projeto que aborda o tema explorado nesse aula, a solução do projeto se encontra na pasta *Lecture 03 - Optimization* desse repositório. Esse projeto é uma implementação do algoritmo *backtracking search* para solucionar jogos de palavras cruzadas (palavras cruzadas é um problema da categoria de satisfação de restrições).

## Lecture 04 - Learning
A aula 04 iniciou a introdução do conceito de **Machine Learning**. O que caracteriza o conceito de *Machine Learning* é a ideia de **não** fornecer instruções explícitas ao computador em como desempenhar uma tarefa, mas apenas acesso a informações no formato de dados ou padrões, e deixar o computador descobrir por conta própria os padrões e entender os dados a fim de realizar a tarefa. Essa aula teve como objetivo explorar os algoritmos mais fundamentais relacionados a esse campo da IA. Foram apresentadas três métodos de aprendizagem de máquina. 

### Supervised Learning
Dado um conjunto de entrada-saída, com saídas classificadas com rótulos (*labels*), a máquina aprende uma função para mapear entradas à saídas. As tarefas (*tasks*), algoritmos e conceitos relacionados a esse método explorados foram:

#### Classification
Tarefa de aprendizagem supervisionada que consiste em aprender uma função que mepeia uma unidade de observação a uma categoria discreta.
    
* *Nearest-neighbor classification*
    
     Algoritmo que, dado uma entrada, escolhe a classe da unidade de observação mais próxima à entrada.
      
* *K-nearest-neighbor classification*
    
     Algoritmo que, dado uma entrada, escolhe a classe mais comum das k unidades de observação mais próximas à entrada. Esse algoritmo é adequado para uma grande variedade de diferentes tipos de problemas de classificação.
         
* *Hard threshold (step function) and Soft threshold (sigmoid funtion)*
    
     <p align="center"><img src="https://miro.medium.com/max/1278/1*Q55RIBsXLfSdzYOeltcuGw.png" alt="(Falha no carregamento da imagem)"></p>
     A vantagem da função sigmoid, é que ela permite uma saída em número real que potencialmente reflete uma probabilidade de uma unidade de observação pertencer a determinada categoria.   
    
#### Linear Regression

```
Weight vector W: (w0, w1, w2)
Input vector X: (1, x1, x2)
W * X : w0 + w1x1 + w2x2
hW(X) = 1 if W * X >= 0
        0 otherwise
```
    
* *Regression*
 
     Tarefa de aprendizagem supervisionada que consiste em aprender uma função que mapeia uma unidade de observação de entrada a um valor contínuo - um número real.
    
* *Perceptron learning rule*
  
     Dado unidade de observação (X, y), atualiza cada peso de acordo com:
<p align="center"><img src="http://www.sciweavers.org/download/Tex2Img_1613480411.png" alt="(Falha no carregamento da imagem) ( ADICIONAR FÓRMULA )"></p>
        
* *Support vector machine*
  
     São construídos para tentar encontrar o *maximum margin separator*.
  
* *Maximum margin separator*
  
     Limite que maximiza a distância entre qualquer uma das unidades de observação.
        
#### Evaluation Hypotheses
* *Loss function*
  
     Função que expressa o quão pobre é a performance de uma hipótese.
        
* *0-1 loss function*
 
     ```
     L(actual, predicted) =
          0 if actual = predicted
          1 otherwise
     ```
        
* *L1 loss function*
  
     ```
     L(actual, predicted) = |actual - predicted|
     ```

     Essa situação mostra o quão distante estão o valor atual e o previsto. Adequado para regressão. Se existem diversos ponto discrepantes e não é necessário modelá-los, então a função L1 é adequada.
        
* *L2 loss function*

     ```
     L(actual, predicted) = (actual - predicted)²
     ```
     Se é necessário minimizar o erro em muitos pontos discrepantes, então a função L2 é adequada.
     
* *Overfitting*

     Um modelo que é muito adequado a um conjunto particular de dados, portanto não é generalizado. ENtão é muito provável que não seja útil com dados futuros. O objetivo é que o modelo seja generalizado o suficiente para modelar dados que ainda não conhece.
        
     <p align="center"><img src="https://miro.medium.com/max/1125/1*_7OPgojau8hkiPUiHoGK_w.png"></p>
        
     Uma solução para esse problema é penalizar a complexidade da hipótese. Dessa forma, temos,
        
     <p align="center"><img src="http://www.sciweavers.org/download/Tex2Img_1613484489.png"></p>
        
     Se λ é grande, então existe uma penalização maior da complexidade da hipótese, caso contrário, existe uma penalização menor.
        
* *Regularization*

     Penalizar hipóteses que são complexas para favorecer hipóteses mais simples e generalizadas. 
     
* *Holdout cross-validation*

     Dividir os dados em um conjunto e treinamento e um conjunto de teste, de forma que o aprendizado da máquina aconteça com o conjuntos de treinamento e a avaliação no conjunto de teste. Uma das desvantagens dessa abordagem é que existe uma grande quantidade de dados que não estão sendo usados para treinamento, consequentemente não é possível obter um modelo potencialmente melhor.
     
* *K-fold cross-validation*

     Dividir os dados em k conjuntos e experimentar k vezes, usando cada conjunto como um conjunto de teste apenas uma vez, e usando os dados restantes como conjuntos de treinamento. 
 
### Reinforcement Learning
Aprendizagem por reforço consiste na experiência adquirida. Será dado a um agente um conjunto de recompensas (*rewards*) ou punições (*punishments*) na forma de valores numéricos, e baseado nisso, ele aprende quais ações tomar no futuro.

<p align="center"><img src="https://www.kdnuggets.com/images/reinforcement-learning-fig1-700.jpg"></p>

#### Markov Decision Process

* Modelo para tomada de decisões, representa estados, ações e recompensas
* Conjunto de estados S
* Conjunto de ações ACTIONS(s)
* Modelo de transição P(s' | s, a) 
* Função recompensa R(s, a, s')
    
#### Q-Learning

* Método para aprender uma função Q(s, a), que estima o valor de realizar a ação **a** no estado **s**
* Começa com Q(s, a) = 0 ∀ s, a
* Quando se toma uma ação e recebe uma recompensa
    - Estima o valor de Q(s, a) baseado na atual recompensa e recompensas futuras esperadas.
    - Atualiza Q(s, a) para levar em consideração velhos e novos valores estimados.
* Toda vez que se toma uma ação **a** no estado **s** e se observa uma recompensa **r**, obtem-se o valor de Q(s, a) da seguinte forma:

<p align="center"><img src="http://www.sciweavers.org/download/Tex2Img_1613475908.png"></p>

* Onde α é a taxa de aprendizagem (*learning rate*) e γ é o fator de desconto (*discount factor*)
* *Greedy decision-making*

     Quando no estado **s**, escolher a ação **a** com maior Q(s, a) 
     
* *Explore vs. exploit*

    - *Exploitation* basicamente é o método de decisão onde a IA utiliza o conhecimento que já têm.
    - *Exploration* é sobre explorar outras ações fora do escopo do conhecimento, porque talvez, mesmo sem saber sobre essas ações, uma delas pode levar a recompensas mais rapidamente ou maior quantidade de recompensas no futuro.
    
* *ε-greedy*

    - Com probabilidade ε, escolhe um decisão aleatória.
    - Com probabilidade 1 - ε, escolhe a decisão melhor estimada.
    
* *Function approximation*
        
     No contexto de aprendizagem de máquina, aproxima Q(s, a), geralmente com uma função que combina várias características, ao invés de armazenar um valor para cada par de estado-ação.
        
### Unsupervised Learning
Dado uma entrada sem qualquer rótulo ou *feedback* adicional, aprende padrões.

#### Clustering

Organizar um conjunto de objetos em grupos de forma que objetos similares tendem a ser do mesmo grupo.
    
* Algumas aplicações
    - Pesquisa genética
    - Segmentação de imagens
    - Pesquisa de mercado
    - Geração de imagens medicinais
    - Análise de redes sociais   
* *K-means clustering*
    
Algoritmo para agrupar dados baseado em na prático de repetidamente associar unidades de observações a grupos e atualizar os centros desses grupos (*cluster's centers*).

### Projects
O site da *Harvard University* disponibilizou dois projetos que abordam o tema explorado nesse aula, as soluções dos projetos se encontram na pasta *Lecture 04 - Learning* desse repositório.

O primeiro projeto consiste em utilizar as funções da biblioteca **scikit-learn** a fim de implementar o método de ***K-nearest-neighbor classification*** presente na aprendizagem supervisionada. O cenário em questão é um site de e-commerce, onde os dados de entrada consistem em um conjunto de informações dos usuários em uma visita ao site e os rótulos (*labels*) são um indicativo (True ou False) de que se, na visita, os usuários finalizaram uma compra ou não. Dado isso, o objetivo do algortimo é, após o treinamento (nesse caso, com 60% dos dados), realizar inferências em realção a intenção dos usuários.

O segundo projeto consiste em treinar uma IA para jogar Nim utilizando o método de ***Q-Learning*** presente na aprendizagem por reforço, implementando do zero fazendo uso da equação para obtenção do valor ótimo de Q(s, a) descrita na seção anterior. A IA é treinada dez mil vezes jogando contra si própria antes de jogar contra um humano.
