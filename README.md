# CS50AI
Repositório para manter resumo das anotações e atividades realizadas no curso "CS50AI - Introduction to Artificial Intelligence with Python" distribuído pela *Harvard University*. 

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
        + [Q-Learning](#q-learning)
    * [Unsupervised Learning](#unsupervised-learning)
        + [Clustering](#clustering)
    * [Projects](#projects-4)
- [Lecture 05 - Neural Networks](#lecture-05---neural-networks)
    * [Neural Network - Structure and Features](#neural-network---structure-and-features)
        + [Activation Function](#activation-function)
        + [Gradient Descent](#gradient-descent)
        + [Multiple Outputs Neural Network](#multiple-outputs-neural-network)
        + [Limitations](#limitations)
    * [Multilayer Neural Network](#multilayer-neural-network)
        + [Backpropagation](#backpropagation)
        + [Deep Neural Networks](#deep-neural-networks)
        + [Overfitting](#overfitting)
    * [Computer Vision](#computer-vision)
        + [Image Convulation](#image-convulation)
        + [Pooling](#pooling)
        + [Convolutional Neural Network](#convolutional-neural-network)
    * [Recurrent Neural Network](#recurrent-neural-network)
    * [Projects](#projects-5)
        
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
O site da *Harvard University* disponibilizou dois projetos que abordam o tema explorado nesse aula, as soluções dos projetos se encontram na pasta *Lecture01 - Knowledge* desse repositório.

O primeiro projeto é uma implementação do puzzle *Knights and Knaves* utilizando uma biblioteca de Lógica Proposicional disponibilizada.

O segundo é uma implementação do jogo campo minado, uma IA foi implementada para tomar a decisão mais correta possível a partir de uma base de conhecimento e operações lógicas.

## Lecture 02 - Uncertainty
Nessa aula foi apresentado a noção de incerteza (*uncertainty*) no contexto de IA. Quando se trata de Inteligência Artificial, geralmente existe incerteza sobre as informações que o algoritmo está lidando. Em situações como essa, inferências são feitas com base em **probabilidade**. Por exemplo, no contexto de um robô que tem sensores e está explorando um ambiente, talvez ele não saiba exatamente onde está ou o que está ao redor, mas ele tem acesso a alguns dados que o permitem realizar inferências com alguma probabilidade.

A partir disso, entra-se no tópico de probabilidade. Probabilidade se resume a ideia de mundos possíveis (*possible worlds*), por exemplo, quando se joga um dado existem 6 mundos possíveis. Ademais, foram abordados conceitos e regras fundamentais no campo da probabilidade: probabilidade não-condicional (*unconditional probability*), probabilidade condicional (*conditional probability*), variável aleatória (*random variable*), independência de variável (*variable independence*), distribuição de probabilidade (*probability distribution*), regra de Bayes (*Bayes' rule*), probabilidade conjunta (*joint probability*), negação (*negation*), inclusão-exclusão (*inclusion-exclusion*), marginalização (*marginalization*), condicionamento (*conditioning*) e inferência (*inference*).

Trazendo essas noções para o contexto computacional, a estrutura de dados rede Bayesian (*Bayesian network*) foi explorada como uma forma de representação de modelos probabilístico. Trata-se de um grafo direcionado onde cada nó representa uma variável, uma aresta do nó *x* para o nó *y* representa que *x* é pai de *y*. Cada nó tem uma distribuição de probabilidade. Além disso, foi mostrado que, fazendo uso da rede Bayesian, é possível aplicar o método de inferência por enumeração (*inference by enumeration*) a fim de realizar inferências de probabilidade. Em relação à performance, a inferência por enumeração demonstra-se pobre, então um método otimizado denominado *sampling* também foi apresentado. 

Para concluir, foi abordado a noção de probabilidades variando em função do tempo. A fim de modelar essa ideia, foram apresentados os conceitos: suposição Markov (*Markov assumption*), cadeia de Markov (*Markov chain*), modelo oculto de Markov (*hidden Markov model*) e a suposição Markov sobre sensores (*sensor Markov assumption*).

### Projects
O site da *Harvard University* disponibilizou dois projetos que abordam o tema explorado nesse aula, as soluções dos projetos se encontram na pasta *Lecture02 - Uncertainty* desse repositório.

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
O site da *Harvard University* disponibilizou um projeto que aborda o tema explorado nesse aula, a solução do projeto se encontra na pasta *Lecture03 - Optimization* desse repositório. Esse projeto é uma implementação do algoritmo *backtracking search* para solucionar jogos de palavras cruzadas (palavras cruzadas é um problema da categoria de satisfação de restrições).

## Lecture 04 - Learning
A aula 04 iniciou a introdução do conceito de ***Machine Learning***. O que caracteriza o conceito de *Machine Learning* é a ideia de **não** fornecer instruções explícitas ao computador em como desempenhar uma tarefa, mas apenas acesso a informações no formato de dados ou padrões, e deixar o computador descobrir por conta própria os padrões e entender os dados a fim de realizar a tarefa. Essa aula teve como objetivo explorar os algoritmos mais fundamentais relacionados a esse campo da IA. Foram apresentadas três métodos de aprendizagem de máquina. 

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

     Um modelo que é muito adequado a um conjunto particular de dados, portanto não é generalizado. Então é muito provável que não seja útil com dados futuros. O objetivo é que o modelo seja generalizado o suficiente para modelar dados que ainda não conhece.
        
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

<p align="center"><img src="https://user-images.githubusercontent.com/29299799/108392184-37134980-71f1-11eb-9673-1d19048f2683.png"></p>

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
O site da *Harvard University* disponibilizou dois projetos que abordam o tema explorado nesse aula, as soluções dos projetos se encontram na pasta *Lecture04 - Learning* desse repositório.

O primeiro projeto consiste em utilizar as funções da biblioteca **scikit-learn** a fim de implementar o método de ***K-nearest-neighbor classification*** presente na aprendizagem supervisionada. O cenário em questão é um site de e-commerce, onde os dados de entrada consistem em um conjunto de informações dos usuários em uma visita ao site e os rótulos (*labels*) são um indicativo (True ou False) de que se, na visita, os usuários finalizaram uma compra ou não. Dado isso, o objetivo do algortimo é, após o treinamento (nesse caso, com 60% dos dados), realizar inferências em realção a intenção dos usuários.

O segundo projeto consiste em treinar uma IA para jogar Nim utilizando o método de ***Q-Learning*** presente na aprendizagem por reforço, implementando fazendo uso da equação para obtenção do valor ótimo de Q(s, a) descrita na seção anterior. A IA é treinada dez mil vezes jogando contra si própria antes de jogar contra um humano.


## Lecture 05 - Neural Networks
Nessa aula foi introduzido o conceito de Rede Neural Artificial (***Artificial Neural Network***). Uma Rede Neural Artificial é um modelo matemático inspirado na rede neural biológica. Tem a característica de modelar uma função matemática a partir de entradas para saídas baseado em sua estrutura e parâmetros. Além disso, ela permite **aprendizagem** dos parâmetros baseado no conjunto de dados em seu domínio. A aula apresentou os conceitos e os tipos de redes neurais mais fundamentais relacionados a esse campo da inteligência artificial.

### Neural Network - Structure and Features
Foi apresentado uma representação básica de uma estrutura de rede neural (**perceptron**) a fim de abordar os conceitos de variáveis, unidades (ou neurônios ou nós) de entrada e saída, peso (*weight)*, viés (*bias*) e suas relações.

<p align="center"><img src="https://user-images.githubusercontent.com/29299799/108361155-e1c74000-71d0-11eb-83a2-108ca262832e.png"></p>

Onde a primeira coluna (com duas unidades) - a camada de entrada (*input layer*) - está ligada a uma unidade que representa a camada de saída (*output layer*). Além disso, *x* são variáveis de entrada, *w (1 e 2)* são pesos, *w* (0) é viés e *g* é uma função de **combinação linear**.

A rede neural irá aprender quais valores de *w0*, *w1* e *w2* são os mais apropriados. A saída da função *g* será a entrada de uma função de ativação (***activation function***), e a saída dessa segunda função representa o resultado.

#### Activation Function
A função de ativação de um nó define a saída desse nó, é uma tranformação não linear, portanto tem como entrada a saída da função *g*.
Foram retomadas as **step function** e **sigmoid function** [abordadas em sessões anteriores](#classification) e foi apresentada a função **ReLU** como exemplos de funções de ativação.

A função ReLU é definida da seguinte forma: 

<p align="center"><img src="http://www.sciweavers.org/download/Tex2Img_1613655428.png"></p>

#### Gradient Descent
O método do gradiente é implementado a fim de minimizar a perda (*loss*) quando se treina uma rede neural. Esse método é um campo do Cálculo e pode ser entendido como uma espécie de declive (*slope*). Representa a direção em que a função de perda (*loss function*) está se movendo dado um ponto e irá determinar quais valores os pesos devem assumir a fim de minimizar a quantidade de perda.

De forma geral e sem aprofundamento na matemática, a ideia do método do gradiente nesse contexto, pode ser formulada da seguinte maneira:
- Inicia-se com escolhas aleatórias de pesos
- Repetir:
    * Calcular o gradiente baseado em todos as unidades de observação (i.e., direção que irá proporcionar a diminuição da perda)
    * Atualizar os pesos de acordo com o gradiente

O custo computacional quando se considera todos as unidades de observação é grade. Portanto, existem alternativas a essa abordagem:
- *stochastic gradient descent*: escolhe apenas uma unidade de observação de cada vez e calcula o gradiente. Essa abordagem provavelmente gera resultados menos precisos.
- *mini-batch gradient descent*: divide o conjunto de dados em pequenos grupos, podendo haver decisões do tamanho de cada um dos grupos. Em contraste com a abordagem *stochastic*, espera-se resultados mais precisos.

#### Multiple Outputs Neural Network
As rede neurais também podem ter múltiplas saídas. E, baseado nos cálculos realizados com as variáveis de entrada e os pesos, um valor associado com cada nó de saída que podem representar, por exemplo, uma probabilidade. Por exemplo:

<p align="center"><img src="https://user-images.githubusercontent.com/29299799/108399407-d720a100-71f8-11eb-99fe-ea8409485d5a.png"></p>

A rede neural acima é um exemplo de [aprendizagem supervisionada](#supervised-learning) (i.e, os dados são rotulados). Também é possível aplicar a ideia de rede neural de múltiplas saídas utilizando o método de [aprendizagem por reforço](#reinforcement-learning). Isso é atingido quando se considera cada variável de entrada como uma informação sobre o estado atual em que o agente se encontra, e as informações de saída poderiam ser cada uma, por exemplo, diferentes ações que o agente poderia escolher performar.
A fim de treinar a rede neural do exemplo, em específico, é possível pensar na situação como quatro redes neurais separadas, então se aplica o treinemento em cada um delas separadamente.

#### Limitations
É importante pensar sobre as limitações nesse tipo de abordagem em que se tem uma combinação linear de variáveis de entrada e pesos e se passa o resultado a uma função de ativação.

Acontece que, quando se realiza uma classificação binária, **só é possível prever dados que são separáveis linearmente (*linear separable*)**, porque se utiliza uma combinação linear para definir um limite de decisão (*decision boundary*). Na seguinte situação é possível estabelecer um limite que separa os pontos laranjas dos azuis.

<p align="center"><img src="https://user-images.githubusercontent.com/29299799/108399429-db4cbe80-71f8-11eb-942d-39b178173667.png"></p>
   
Porém, um perceptron realizando uma classificação binária não seria capaz de lidar com uma situação onde nenhuma linha reta é capaz de separar os dados, como na situação a seguir:
 
<p align="center"><img src="https://user-images.githubusercontent.com/29299799/108399443-e0117280-71f8-11eb-8dcf-45e0411ec8d4.png"></p>

Esse é um caso que requer um limite de decisão mais complexo. Dados do mundo real, em geral, não são separáveis linearmente.

### Multilayer Neural Network
A solução proposta para superar as limitações descritas anteriomente foi a ideia de redes neurais multicamadas. Uma rede neural é uma rede neural multicamadas se satisfazer os seguintes critérios: possuir uma camada de entrada, uma camada de saída e pelo menos uma camada escondida (**hidden layer**).

Cada uma das unidades escondidas (**hidden units**) irão calcular um valor de saída (*activation*) baseado na combinação linear de todos os valores de saída da camada anterior. E após calcular os valores de todas as unidades, o processo é repetido para a camada posterior. Segue um exemplo de estrutura de redes neurais multicamadas:

<p align="center"><img src="https://user-images.githubusercontent.com/29299799/108439742-9e042300-7230-11eb-8dd0-0d62f0768086.png">
   
A vantagem de uma rede neural multicamadas é que ela possibilita a modelagem de funções mais complexas. Ao invés de aprender apenas um limite de decisão, cada uma das unidade escondidas podem aprender um limite de decisão diferente, e esses resultados podem ser combinados para produzir uma saída final.

#### Backpropagation
Nessa abordagem não é possível ter conhecimento de quais valores os nós das camadas escondidas devem assumir, portanto, para treinar esse modelo, é preciso considerar a perda no valor de saída. Então, baseado nos pesos que conectam ao nó de saída - se um desses pesos é maior que o outro - é possível calcular uma estimativa do quanto a perda na saída foi devido a alguma parte específica da camada escondida. Isto é, pode-se aplicar uma retropropagação (**backpropagation**) na rede neural com o valor da perda e levantar uma conjectura de quais são os erros de cada um dos nós nas camadas escondidas baseando-se nesse valor.

Sem entrar em detalhes matemáticos, o algoritmo de retropropagação pode ser definido da seguinte forma:
- Inicia-se com escolhas aleatórias de pesos
- Repetir:
    * Calcular a perda para a camada de saída
    * Para cada camada, começando com a camada de saída, e movendo-se para dentro em direção as camadas escondidas iniciais:
        + Propagar a perda para a camada anterior: dado o valor de perda, descobrir qual a perda deve ser para a camada anterior baseado nos valores dos pesos
        + Atualizar os pesos

**O algoritmo de retropropagação é o algoritmo que torna possível a funcionalidade e treinamento das redes neurais multicamadas.**

#### Deep Neural Networks
As redes neurais profundas são redes neurais com diversas camadas escondidas. Isso permite modelar funções ainda mais sofisticadas: cada camada escondida calcula um aspecto diferente da função que posteriormente são combinados em um função complexa.

#### Overfitting
[Overfitting](#evaluation-hypotheses) também aparece no contexto de redes neurais. Uma estratégia  popular para lidar com essa situação é a ideia de ***dropout***.

* Dropout: temporariamente remover unidades da rede neural - selecionadas aleatóriamente - para previnir extrema dependência dessas unidades.
   
### Computer Vision
Método computacional para analisar e entender imagens digitais.

Uma situação em que se está lidando com uma imagem muito grande traz problemas. Primeiro, significa uma entrada muito grande para a rede neural. Segundo, significa que todos os detalhes de cada pixel da imagem estão sendo levados em consideração, quando na realidade apenas as características de certas regiões são relevantes. 

Existem procedimentos para reduzir o tamanho e considerar apenas as características relevantes de uma imagem no contexto de visão computacional e rede neural.

#### Image Convulation
O método de *image convulation* consiste em aplicar um filtro (em forma de matriz) em pixels de uma imagem para detecção de características desses pixels em relação a seus vizinhos, como por exemplo, detecção de curvas. A seguir um exemplo de *image convulation*:

<p align="center"><img src="https://user-images.githubusercontent.com/29299799/108516924-8adf6a80-72a5-11eb-8da8-baf8b8c46f85.png"></p>

#### Pooling
Pooling é o método de reduzir o tamanho da entrada considerando amostras de regiões específicas da imagem de entrada. Uma aborgadem famosa de pooling é o ***max-pooling***, que consiste em escolher o maior valor em determinada região, por exemplo:

<p align="center"><img src="https://user-images.githubusercontent.com/29299799/108516930-8dda5b00-72a5-11eb-86d8-6b3a9c8f8440.png"></p>

#### Convolutional Neural Network
Tipo de rede neural que usa os métodos de convolução e *pooling*, em geral para analisar imagens. O processo em que a imagem é submetida antes de ser utilizada como entrada para a rede neural é representado da seguinte forma:

<p align="center"><img src="https://user-images.githubusercontent.com/29299799/108505177-bf4b2a80-7295-11eb-87aa-b14d41d88871.png"></p>

### Recurrent Neural Network
Os tipo de rede neurais descritos nas sessões anteriores fazem parte da categoria de ***feed-forward neural network*** (i.e., rede neural que tem conexões apenas em uma direção). Nessa sessão será explorada a categoria de ***recurrent neural network***, que pode ser definida como o grupo de redes neurais que geram saídas que são usadas como entradas para si própria em situações futuras.

* Diagrama feed-forward neural network

<p align="center"><img src="https://user-images.githubusercontent.com/29299799/108505137-b65a5900-7295-11eb-99ec-bd9bcc56fa7a.png"></p>

* Diagrama recurrent neural network

<p align="center"><img src="https://user-images.githubusercontent.com/29299799/108505163-bb1f0d00-7295-11eb-80bb-582c38cdfb49.png"></p>

Na abordagem das redes neurais tradicional apenas existe a definição de pesos, então não ocorre o armazenamento de qualquer informação sobre entradas a fim de ser reutilizadas para iterações futuras. **Redes neurais recorrentes são particularmente úteis quando se trata de um sequência de dados**.

Com essa nova abordagem é possível treinar uma rede neural para descrever uma imagem, como faz o *CaptionBot* da Microsoft. Esse tipo de cenário não é possível para as *feed-forward neural network*, porque nesse caso existe um número fixo de entrada e um número fixo de saída, então é impossível esse tipo de rede neural receber uma imagem como entrada e produzir uma descrição de texto complexa de suas características. Texto é uma sequência de palavras - na abordagem tradicional é possível imaginar uma saída de uma palavra, porém uma sequência de palavras é muito mais desafiador, porque dependendo da imagem podem existir diferentes tipos de tamanhos de saída.

A solução desse problema pode ser alcançada utilizando as *recurrent neural network*, porque elas podem alimentar-se como entrada suas saídas. Isso permite um relacionamento de 1 para N (*one-to-many relationship*) em relação a entrada e saídas. Na abordagem tradicional se tem uma relação de 1 para 1 (*one-to-one relationship*).

Existem diferentes tipos de algoritmos para *recurrent neural network*, um dos mais populares é o *long short-term memory* (*LSTM*).

### Projects
O site da *Harvard University* disponibilizou um projeto que abordam o tema explorado nesse aula, a solução do projeto se encontra na pasta *Lecture05 - Neural Networks* desse repositório.

O projeto consiste em treinar uma **Rede Neural Convolucional** para classificar centenas de imagens de placas de trânsito em 43 categorias. A leitura e o redimensionamento das imagens foi realizado utilizando a biblioteca **OpenCV**, que, dado uma imagem, a converte para um `numpy.ndarray`. A biblioteca utilizada para construir a rede neural foi a **TensorFlow** com a API **Keras**. A divisão dos dados em dados de treino e dados de teste foi realizada utilizando a função `train_test_split` da biblioteca **scikit-learn**.

A estrutura da rede neural consiste em duas camadas de convolução e max-pooling, uma camada densa de entrada com um dropout com taxa de 0.5 e outra camada densa de saída com ativação *softmax*. A média de acurácia com os dados de teste é 96%.
