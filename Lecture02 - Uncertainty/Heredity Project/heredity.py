# Andrew Enrique Oliveira
# Ciência da Computação - Universidade Federal de Itajubá (2017 - )
# 06/01/2021
#
# Os conteúdos das funções joint_probability, update e normalize foram implementados por mim

import csv
import itertools
import sys
import math

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}

def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")

def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data

def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]

def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    result = 1

    for person in people:
        have = person in have_trait
        
        if person in one_gene:
            person_genes = 1
        elif person in two_genes:
            person_genes = 2
        else:
            person_genes = 0

        if people[person]['mother'] == None:
            result *= PROBS["gene"][person_genes]

        else:
            does_get = []
            doesnt_get = []
            parents = ['mother', 'father']

            for i, parent in enumerate(parents):
                if people[person][parent] in one_gene:
                    # Metada da chance de herdar o gene.
                    # 0.5 - PROBS["mutation"] de herdar,
                    # porém o outro gene também tem uma probabilidade de mutação, portanto,
                    # 0.5 - PROBS["mutation"] + PROBS["mutation"],
                    # logo a probabilidade de mutação é cancelada

                    does_get.append(0.5)

                elif people[person][parent] in two_genes:
                    does_get.append(1 - PROBS["mutation"])

                else:
                    does_get.append(PROBS["mutation"])

                doesnt_get.append(1 - does_get[i])
            
            if person_genes == 1:
                # Em termos de probabilidade, vamos considerar:
                # as vezes que o filho não herda da mãe (doesnt_get[0]) qual a probabilidade dele herdar do pai (does_get[1]).
                # Somado a isso, temos:
                # as vezes que o filho não herda do pai (doesnt_get[1]) qual a probabilidade dele herdar da mãe (does_get[0])

                result *= doesnt_get[0] * does_get[1] + doesnt_get[1] * does_get[0]

            elif person_genes == 2:
                # Em termos de probabilidade, vamos considerar:
                # a probabilidade do filho herdar o gene da mãe (does_get[0]) E
                # a probabilidade do filho herdar o gene do pai (does_get[1])
                
                result *= does_get[0] * does_get[1]

            else:
                # Em termos de probabilidade, vamos considerar:
                # a probabilidade do filho não herdar o gene da mãe (doesnt_get[0]) E
                # a probabilidade do filho não herdar o gene do pai (doesnt_get[1]) 

                result *= doesnt_get[0] * doesnt_get[1]
            
        result *= PROBS["trait"][person_genes][have]
            
    return result
            
def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities:
        if person in one_gene:
            person_gene = 1
        elif person in two_genes:
            person_gene = 2
        else:
            person_gene = 0
        
        have = True if person in have_trait else False

        probabilities[person]['trait'][have] += p
        probabilities[person]['gene'][person_gene] += p

def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    new_value = dict()

    for person in probabilities:
        for group in probabilities[person]:
            for key in probabilities[person][group]:
                new_value[key] = probabilities[person][group][key]/sum(value for value in probabilities[person][group].values())

            probabilities[person][group] = new_value.copy()
            new_value = {}

if __name__ == "__main__":
    main()
