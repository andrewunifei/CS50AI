# Andrew Enrique Oliveira
# Ciência da Computação - Universidade Federal de Itajubá (2017 - )
# 12/02/2021
#
# Os conteúdos das funções 
# enforce_node_consistency, revise, ac3, assignment_complete, consistent, order_domain_values, elect_unassigned_variable e backtrack
# foram implementados por mim

import sys
import queue
from crossword import *

class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for variable in self.domains.copy():
            for word in self.domains[variable].copy():
                if len(word) != variable.length:
                    self.domains[variable].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revised = False
        overlap = self.crossword.overlaps[x, y]
        new_domain = set()

        if overlap:
            x_letter, y_letter = overlap
            for word_x in self.domains[x].copy():
                for word_y in self.domains[y]:
                    if word_x[x_letter] == word_y[y_letter]:
                        new_domain.add(word_x)
                        revised = True
        
            self.domains[x] = new_domain
        
        return revised

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        q = queue.SimpleQueue()

        if not arcs:
            overlaps = self.crossword.overlaps

            for key in overlaps:
                if overlaps[key] != None: q.put(key)
        else:
            for value in arcs:
                q.put(value)

        while not q.empty():
            (x, y) = q.get()

            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    return False
                for neighbor in self.crossword.neighbors(x):
                    if neighbor == y:
                        continue
                    q.put((neighbor, x))
        
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        if len(self.crossword.variables) == len(assignment):
            return True

        return False

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # Checa se os tamanhos estão certos
        for variable in assignment:
            if variable.length != len(assignment[variable]):
                return False

        # Checa se as palavras são diferentes
        if len(set(assignment[variable] for variable in assignment)) != len(assignment):
            return False
        
        # Checa se os vizinhos são consistentes
        overlaps = self.crossword.overlaps
        for variable_x in assignment:
            for variable_y in assignment:
                if variable_x == variable_y:
                    continue
                
                if overlaps[variable_x, variable_y] == None:
                    continue
                
                letter_x, letter_y = overlaps[variable_x, variable_y]
                if assignment[variable_x][letter_x] == assignment[variable_y][letter_y]:
                    continue
                else:
                    return False
        
        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        word_mapped = {}
        for word in self.domains[var]:
            word_mapped[word] = 0

        neighbors_vars = self.crossword.neighbors(var)
        neighbors_domains = list()
    
        for variable in neighbors_vars:
            if variable not in assignment:
               neighbors_domains.append(self.domains[variable])

        for set_ in neighbors_domains:
            for word in set_:
                if word in word_mapped:
                    word_mapped[word] += 1

        # Retorna uma lista com os valores de dominio com o menor poder de restrição até os com maior poder de restrição
        return list(dict((sorted(word_mapped.items(), key=lambda item: item[1]))))
                
        
    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        available_vars_domain = {}
        available_vars_neighbors = {}
        selected_vars = {}

        for variable in self.crossword.variables:
            if variable not in assignment:
                available_vars_domain[variable] = len(self.domains[variable])
                available_vars_neighbors[variable] = len(self.crossword.neighbors(variable))

        ordered_dict_domain = dict((sorted(available_vars_domain.items(), key=lambda item: item[1])))
        smallest_domain = next(iter(ordered_dict_domain))

        for key in ordered_dict_domain:
            if ordered_dict_domain[key] == ordered_dict_domain[smallest_domain]:
                selected_vars[key] = available_vars_neighbors[key]
            else:
                break

        if len(selected_vars) > 1:
            # Retorna variável com maior número de vizinhos
            return next(iter(dict((sorted(selected_vars.items(), key=lambda item: item[1], reverse=True)))))
        
        return smallest_domain

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment): return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            assignment[var] = value 
            if self.consistent(assignment):
                result = self.backtrack(assignment)
                if result != None: return result
            del assignment[var]
        return None

def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
