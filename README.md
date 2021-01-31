# CS50AI
Repositório para manter as atividades realizadas no curso "CS50AI - Introduction to Artificial Intelligence with Python" distribuído pela *Harvard University*. 

## Lecture 00 - Search
Nessa aula foram apresentados conceitos introdutórios de Inteligência Artificial no campo da busca. "Busca" (*search*) no contexto de IA é o problema de tentar descobrir o que fazer quando se existe um tipo de situação em que o computador se encontra e algum tipo de ambiente em que um **agente** está inserido. E se almeja que, de alguma forma, esse agente seja capaz de encontrar uma solução para o problema. Esse problema pode aparecer em diversos formatos. Exemplos são: Jogo do 15 e tentar achar o caminho certo através de um labirinto ou dois lugares geográficos.

Também foram abordados e definidos algumas terminologias relacionadas a esse campo: agente (*agent*), estado (*state*), estado inicial (*inital state*), ações (*actions*), modelo de transição (*transition model*), espaço de estados (*state space*), teste de objetivo (*goal test*), custo do caminho (*path cost*) e nó (*node*).

Além disso, foram apresentados definições e implementações de algoritmos de busca, são eles: *depth-first search*, *breadth-first search*, *uninformed search*, *informed search*, *greedy best-first search* e *A\* search*. Também foi explorado a noção de *adversarial search* e alguns algoritmos relacionados a esse tipo de cenário, como: *minimax*, *alpha-beta pruning* e *depth-limited minimax*.

### Projects
O site da *Harvard University* disponibilizou dois projetos que abordam o tema explorado nesse aula, as soluções dos projetos se encontram na pasta *Lecture 00 - Search* desse repositório. O primeiro projeto é uma implementação do jogo *Six Degrees of Kevin Bacon* utilizando *breadth-first search* para realizar as buscas. O segundo é uma implementação do jogo da velha utilizando *minimax* como inteligência artificial adversária.
