import numpy as np


class CellularAutomationModel:
    grid_width = 40
    grid_height = 40

    def __init__(self):
        self.grid = self._randomised_grid()

    def evolve(self):
        """
        Evolve the current grid state using Conway's Game of Life algorithm.

        :returns
            dict: A dictionary representation of the state of cells in the grid

        """
        base_grid = self.grid.copy()
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                cell_state = base_grid[x, y]
                n_neighbours = self._calculate_alive_neighbours(x, y, cell_state, grid=base_grid)
                self.grid[x, y] = self._next_cell_state(cell_state, n_neighbours)

        return self._json_formatted_grid()

    def toggle_cell_state(self, x, y):
        """
        Reverses the cell state for a particular cell coordinate.
        """
        self.grid[x][y] = 0 if self.grid[x][y] == 1 else 1

    def reset_grid(self):
        """
        Resets the grid array to a random state.

        :returns
            dict: A dictionary representation of the state of cells in the grid
        """
        self.grid = self._randomised_grid()

        return self._json_formatted_grid()

    def _calculate_alive_neighbours(self, x, y, cell_state, grid):
        """
        Returns the number of alive nearest neighbours.
        """
        surrounding_arr = self._surrounding_arr(x, y, grid)
        n_alive = sum(sum(surrounding_arr))

        return n_alive - cell_state

    def _json_formatted_grid(self):
        """
        Returns a python dictionary which represents the current state of the cells in the grid.
        key: An integer that represents a single cell based on the coordinate position.
        value: The cell state <0 or 1> to represent whether a cell is dead or alive.
        """
        json_grid = {}

        for x in range(self.grid_width):
            for y in range(self.grid_height):
                cell_id = int(x + y*self.grid_width)
                json_grid[cell_id] = int(self.grid[x, y])

        return json_grid

    def _randomised_grid(self):
        """
        Returns a 2d array with values of randomly assigned values of 0 or 1.
        """
        return np.random.randint(2, size=(self.grid_height, self.grid_width))

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
    def _next_cell_state(cell_state, n_neighbours):
        """
        Returns the new cell state 0 (dead) or 1 (alive). New state is determined using the current cell state
        and number of alive neighbours based on the rules in Conway's Game of Life.
        """
        if (cell_state == 1 and (n_neighbours not in range(2, 4))) or (cell_state == 0 and n_neighbours != 3):
            return 0
        return 1
