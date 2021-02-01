# Andrew Enrique Oliveira
# Ciência da Computação - Universidade Federal de Itajubá (2017 - )
# 31/01/2021
#
# Os conteúdos das funções known_mines, known_safes, mark_mine, mark_safe na classe Sentence,
# e o conteúdo da função add_knowledge na classe MinesweeperAI, foram implementados por mim

import itertools
import random

class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if self.count == len(self.cells) and self.count != 0:
            return self.cells
        
        return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if self.count == 0:
            return self.cells
        
        return set()  

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count =- 1
        
        return

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.remove(cell)
        
        return


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)
        
        return

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

        return

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        self.moves_made.add(cell)
        self.mark_safe(cell)

        # Adiciona uma nova sentença na base de conhecimento da IA
        adjacent_cells = set()
        i, j = cell

        ## Essas coordenadas são para auxiliar na busca pela células adjacentes à célula segura
        coordinates = ((-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1))

        for coordinate in coordinates:
            c_i = i + coordinate[0]
            c_j = j + coordinate[1]

            ## Checa se as novas coordenadas estão dentro do tabuleiro e for adas jogadas feitas
            if (c_i >= 0 and c_i < self.height) and (c_j >= 0 and c_j < self.width) and ((c_i, c_j) not in self.moves_made):
                adjacent_cells.add((i + coordinate[0], j + coordinate[1]))
        
        self.knowledge.append(Sentence(adjacent_cells, count))
        print(adjacent_cells)

        # 4
        temp = self.knowledge.copy()
        self.update()

        # 5
        while self.knowledge != temp:
            temp = self.knowledge
            self.update()
        return

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        if len(self.safes) != 0:
            for cell in self.safes:
                if cell not in self.moves_made:
                    return cell
        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """

        free = []
        for i in range(self.height):
            for j in range(self.width):
                cell = (i, j)
                if cell not in self.moves_made and cell not in self.mines:
                    free.append(cell)
        # BUG: if there are no free moves return None
        # fixed with below "if statement"
        if len(free) == 0:
            return None
        else:
            i = random.randrange(len(free))
            return free[i]

    def update(self):
        if len(self.mines) != 0:
            for mine in self.mines:
                self.mark_mine(mine)
        if len(self.safes) != 0:
            for safe in self.safes:
                self.mark_safe(safe)
        if len(self.knowledge) != 0:
            for sentence in self.knowledge:
                self.safes = self.safes.union(sentence.known_safes())
                self.mines = self.mines.union(sentence.known_mines())
        # do the subtraction thing
        temp_know = []
        if len(self.knowledge) > 1:
            for super_set in self.knowledge:
                for sub_set in self.knowledge:
                    if sub_set.cells.issubset(super_set.cells) and sub_set != super_set:
                        new_cells = super_set.cells - sub_set.cells
                        new_count = super_set.count - sub_set.count
                        new_sentence = Sentence(cells=new_cells, count=new_count)
                        temp_know.append(new_sentence)
            for temp_sent in temp_know:
                # BUG: do not add duplicates to knowledge
                # fixed with below "if statement"
                if temp_sent not in self.knowledge:
                    self.knowledge.append(temp_sent)