import numpy as np


class GameOfLife:
    grid_width = 15
    grid_height = 15

    def __init__(self):
        self.grid = self.randomise_grid()

    def next_evolution(self):
        """
        Evolve the current grid state using Conway's Game of Life algorithm.
        """
        base_grid = self.grid.copy()
        for x in range(GameOfLife.grid_width):
            for y in range(GameOfLife.grid_height):
                cell_state = base_grid[x, y]
                n_neighbours = self._calculate_alive_neighbours(x, y, cell_state, grid=base_grid)
                self.grid[x, y] = self._next_cell_state(cell_state, n_neighbours)

        return self.grid

    def toggle_cell_state(self, x, y):
        """
        Reverses the cell state for a particular coordinate.
        """
        self.grid[x, y] = 0 if self.grid[x, y] == 1 else 1

    def _calculate_alive_neighbours(self, x, y, cell_state, grid):
        """
        Returns the number of alive nearest neighbours.
        """
        surrounding_arr = self._surrounding_arr(x, y, grid)
        n_alive = sum(sum(surrounding_arr))

        return n_alive - cell_state

    @staticmethod
    def _surrounding_arr(x, y, grid):
        """
        Returns an 2d array containing all the adjacent cells for a particular coordinate (radius = 1 cell).
        """
        if x != 0 and y != 0:
            return grid[x - 1:x + 2, y - 1:y + 2]
        elif x == 0:
            return grid[x:x + 2, y - 1:y + 2]
        elif y == 0:
            return grid[x - 1:x + 2, y:y + 2]
        else:
            return grid[x:x + 2, y:y + 2]

    @staticmethod
    def _next_cell_state(cell_state, n_alive):
        """
        Returns the new cell state 0 (dead) or 1 (alive). New state is determined using the current cell state
        and number of alive neighbours based on the rules in Conway's Game of Life.
        """
        n_neighbours = n_alive - cell_state
        if (cell_state == 1 and (n_neighbours not in range(2, 4))) or (cell_state == 0 and n_neighbours != 3):
            return 0
        return 1

    @staticmethod
    def randomise_grid():
        return np.random.randint(2, size=(GameOfLife.grid_height, GameOfLife.grid_width))
