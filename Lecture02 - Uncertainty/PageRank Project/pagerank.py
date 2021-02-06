# Andrew Enrique Oliveira
# Ciência da Computação - Universidade Federal de Itajubá (2017 - )
# 05/01/2021
#
# Os conteúdos das funções transition_model, sample_pagerank e iterate_pagerank foram implementados por mim

import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    
    number_of_pages = len(corpus[page])
    damping_probability = damping_factor/number_of_pages
    additional_probability = (1 - damping_factor)/(1 + number_of_pages)
    probability = damping_probability + additional_probability
    probability_dict = {page: additional_probability}

    for page_ in corpus[page]:
        probability_dict[page_] = probability

    return probability_dict

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values a    print(corpus[page])re
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    track = {}
    for page_ in corpus.keys():
        # O exercício estabelece que, se uma página não faz ligação com ninguém,
        # deve-se considerar que ela faz ligação com todas as páginas
        if len(corpus[page_]) == 0:
            corpus[page_] = {page for page in corpus.keys()}

        track[page_] = 0

    page = random.choice(list(corpus.items()))[0]
    track[page] += 1

    for i in range(n - 1):
        # Retorna um critério de peso de seleção para cada página
        probability_dict = transition_model(corpus, page, damping_factor)
        # Escolhe uma página pseudo-aleatóriamente a partir de um critério de peso
        page = random.choices(list(probability_dict.keys()), weights=list(probability_dict.values()), k=1)[0]
        track[page] += 1

    # Retorna um dicionário com as probabilidades de acesso a cada página
    # a partir da quantidade de vezes que elas foram selecionadas 
    return {key: value/n for key, value in track.items()}


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    rank = {}
    former_rank = {}
    page_links = set()

    for page_ in corpus.keys():
        # O exercício estabelece que, se uma página não faz ligação com ninguém,
        # deve-se considerar que ela faz ligação com todas as páginas
        if len(corpus[page_]) == 0:
            corpus[page_] = {page for page in corpus.keys()}
        
        # Inicialmente, todas as páginas tem probabilidade igual
        rank[page_] = 1/len(corpus.keys())

    while True:
        stop_condition = 0
        former_rank = rank.copy()
        aux = {}

        for page in corpus.keys():
            # Busca pelos links que levam a página atual
            for super_page in corpus.keys():
                if page in corpus[super_page]:
                    page_links.add(super_page)

            # Cálculo da probabilidade
            first_condition = (1 - damping_factor)/len(corpus.keys())
            second_condition = damping_factor * sum(rank[super_page]/len(corpus[super_page]) for super_page in page_links)
            rank[page] = first_condition + second_condition

            page_links = set()
                
        for page in rank.keys():
            # Normalização
            aux[page] = rank[page]/sum(value for value in rank.values())
            
            # Verificação de distância entre o ranqueamento anterior e o atual
            if abs(former_rank[page] - aux[page]) < 0.001:
                stop_condition += 1
        
        rank = aux.copy()

        if stop_condition == len(corpus.keys()):
            break

    return rank

if __name__ == "__main__":
    main()
