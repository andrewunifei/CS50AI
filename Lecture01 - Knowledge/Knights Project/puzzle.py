# Andrew Enrique Oliveira
# Ciência da Computação - Universidade Federal de Itajubá (2017 - )
# 31/01/2021
#
# Os conteúdos das variáveis knowledge0, knowledge1, knowledge2 e knowledge3 foram implementados por mim

from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Implementação do Puzzle 0
    #
    # AKnight -> ¬AKnave ∧               # Se A é cavaleiro, então não é valete
    # AKnave -> ¬AKnight ∧               # Se A é valete, então não é cavaleiro
    #
    # (AKnight ∧ AKnave) -> AKnight ∧    # Se A é tanto cavaleiro quando valete, então A é cavaleiro por dizer a verdade
    # ¬(AKnight ∧ AKnave) -> AKnave      # Se A não é tanto cavaleiro quando valete, então A é valete por mentir
    #
    # A é valete

    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),

    Implication(And(AKnight, AKnave), AKnight),
    Implication(Not(And(AKnight, AKnave)), AKnave)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Implementação do Puzzle 1
    #
    # AKnight -> ¬AKnave ∧               # Se A é cavaleiro, então não é valete
    # AKnave -> ¬AKnight ∧               # Se A é valete, então não é cavaleiro 
    # BKnight -> ¬BKnave ∧               # Se B é cavaleiro, então não é valete
    # BKnave -> ¬BKnight ∧               # Se B é valete, então não é cavaleiro
    #
    # (AKnave ∧ BKnave) -> AKnight  ∧    # Se ambos são valetes, então A é cavaleiro por dizer a verdade
    # ¬(AKnave ∧ BKnave) -> AKnight ∧    # Se ambos não são valetes, então A é valete por mentir
    # (AKnave ∧ BKnave) -> AKnight  ∧    # Se ambos são valetes, então B é valete
    # ¬(AKnave ∧ BKnave) -> AKnight      # Se ambos não são valetes, então A é está mentindo e B é cavaleiro
    #
    # A é valete e B é cavaleiro

    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight)),

    Implication(And(AKnave, BKnave), AKnight),
    Implication(Not(And(AKnave, BKnave)), AKnave),
    Implication(And(AKnave, BKnave), BKnave),
    Implication(Not(And(AKnave, BKnave)), BKnight)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Implementação do Puzzle 2
    # 
    # AKnight -> ¬AKnave ∧                                       # Se A é cavaleiro, então não é valete
    # AKnave -> ¬AKnight ∧                                       # Se A é valete, então não é cavaleiro 
    # BKnight -> ¬BKnave ∧                                       # Se B é cavaleiro, então não é valete
    # BKnave -> ¬BKnight ∧                                       # Se B é valete, então não é cavaleiro
    #
    # ((Aknave ∧ Bknave) ∨ (AKnight ∧ Bknight)) -> AKnight  ∧    # Se ambos são do mesmo tipo, A é cavaleiro por dizer a verdade
    # ¬((Aknave ∧ Bknave) ∨ (AKnight ∧ Bknight)) -> AKnave  ∧    # Se ambos não são do mesmo tipo, A é valete por mentir
    # ((Aknave ∧ Bknave) ∨ (AKnight ∧ Bknight)) -> AKnave   ∧    # Se ambos são do mesmo tipo, B é valete por mentir
    # ¬((Aknave ∧ Bknave) ∨ (AKnight ∧ Bknight)) -> AKnight      # Se ambos não são do mesmo tipo, B é cavaleiro por dizer a verdade
    #
    # A é valete e B é cavaleiro

    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight)),

    Implication(Or(
            And(AKnave, BKnave),
            And(AKnight, BKnight)
        ),
        AKnight
    ),
    Implication(Not(Or(
            And(AKnave, BKnave),
            And(AKnight, BKnight)
        )),
        AKnave
    ),
    Implication(Or(
            And(AKnave, BKnave),
            And(AKnight, BKnight)
        ),
        BKnave
    ),
    Implication(Not(Or(
            And(AKnave, BKnave),
            And(AKnight, BKnight)
        )),
        BKnight
    ),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(   
    # Implementação do Puzzle 3
    # 
    # AKnight ∨ AKnave ∧                             # A é cavaleiro ou valete
    # BKnight ∨ BKnave ∧                             # B é cavaleiro ou valete
    # CKnight ∨ CKnave ∧                             # C é cavaleiro ou valete
    #
    # BKnight -> (AKnave ∧ (Aknave -> AKnight)) ∧    # Se B é um cavaleiro, então A disse que é um valete
    # BKnave -> ¬(AKnave ∧ (Aknave -> AKnight)) ∧    # Se B é um valete, então A não disse que é um valete
    # BKnave <-> CKnight ∧                           # C é um cavaleiro se, e somente se, B for um valete
    # CKnight <-> AKnight                            # A é um cavaleiro se, e somente se, C for um cavaleiro
    #
    # A é cavaleiro, B é valete e C é cavaleiro
    
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),

    Implication(BKnight, And(AKnave, Implication(AKnave, AKnight))),
    Implication(BKnave, Not(And(AKnave, Implication(AKnave, AKnight)))),
    Biconditional(CKnight, BKnave),
    Biconditional(AKnight, CKnight)
)


def main():
    # print(knowledge0.formula())
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
