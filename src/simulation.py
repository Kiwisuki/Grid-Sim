from typing import List, Optional, Tuple

import numpy as np

from config.constants import STATES


class Person:
    """Person class to represent a person in the simulation."""

    def __init__(self, state: int, x: int, y: int):
        """Args:
        state: State of the person.
        x: X coordinate of the person.
        y: Y coordinate of the person.
        """
        self.state = state
        self.x = x
        self.y = y
        self.next_state = state
        self.sick_days = 0

    def _is_sick_neighbour(self, grid):
        if self.x > 0 and grid[self.x - 1, self.y].state == STATES['Infected']:
            return True
        if (
            self.x < grid.shape[0] - 1
            and grid[self.x + 1, self.y].state == STATES['Infected']
        ):
            return True
        if self.y > 0 and grid[self.x, self.y - 1].state == STATES['Infected']:
            return True
        if (
            self.y < grid.shape[1] - 1
            and grid[self.x, self.y + 1].state == STATES['Infected']
        ):
            return True
        return False

    def infect(self, inf_rate: float, grid: np.ndarray):
        """Infects a person if a sick neighbour is present."""
        if (
            self._is_sick_neighbour(grid)
            and np.random.random() < inf_rate
            and self.state == STATES['Susceptible']
        ):
            self.next_state = STATES['Infected']

    def recover(self, rec_rate: float):
        """Recovers a person if the person is infected."""
        if self.state == STATES['Infected'] and np.random.random() < rec_rate:
            self.next_state = STATES['Recovered']

    def kill(self, mort_rate: float):
        """Kills a person if the person is infected."""
        if (
            self.state == STATES['Infected']
            and self.next_state == STATES['Infected']
            and np.random.random() < mort_rate
        ):
            self.next_state = STATES['Deceased']

    def update(self):
        """Updates the state of the person."""
        if self.state != STATES['Empty']:
            self.state = self.next_state


class Population:
    """Population class to represent the population in the simulation."""

    def __init__(
        self,
        grid_size: int,
        initial_infected: Optional[int] = None,
        coords: Optional[List[Tuple[int, int]]] = None,
    ):
        """Args:
        grid_size: Size of the grid.
        initial_infected: Number of initial infected people.
        coords: Coordinates of initial infected people.
        """
        self.grid_size = grid_size

        if coords:
            self.initial_infected = len(coords)
        else:
            self.initial_infected = initial_infected  # type: ignore

        self.grid = self._create_grid(coords)

    def _create_grid(self, coords: Optional[List[Tuple[int, int]]] = None):
        grid = np.empty((self.grid_size, self.grid_size), dtype=Person)
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                grid[i, j] = Person(STATES['Susceptible'], i, j)

        if coords:
            for x, y in coords:
                grid[x, y] = Person(STATES['Infected'], x, y)
            return grid

        for _ in range(self.initial_infected):
            x = np.random.randint(0, self.grid_size)
            y = np.random.randint(0, self.grid_size)
            while grid[x, y].state == STATES['Empty']:
                x = np.random.randint(0, self.grid_size)
                y = np.random.randint(0, self.grid_size)
            grid[x, y] = Person(STATES['Infected'], x, y)

        return grid

    def count_states(self):
        """Counts the number of people in each state."""
        states = {k: 0 for k in STATES.values()}
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                states[self.grid[i, j].state] += 1
        result = {}
        for k, v in zip(STATES.keys(), states.values()):
            result[k] = v
        del result['Empty']
        return result

    def update(self, inf_rate: float, rec_rate: float, mort_rate: float):
        """Updates the state of the population."""
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.grid[i, j].infect(inf_rate, self.grid)
                self.grid[i, j].recover(rec_rate)
                self.grid[i, j].kill(mort_rate)
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.grid[i, j].update()

    def get_matrix(self):
        """Returns the grid as a matrix."""
        matrix = np.zeros((self.grid_size, self.grid_size))
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                matrix[i, j] = self.grid[i, j].state
        return np.array(matrix)

    def isolate_subpopulations(self):
        """Isolates the subpopulations."""
        for i in range(self.grid_size):
            self.grid[i, self.grid_size // 3].state = STATES['Empty']
            self.grid[self.grid_size // 3, i].state = STATES['Empty']

            self.grid[i, 2 * self.grid_size // 3].state = STATES['Empty']
            self.grid[2 * self.grid_size // 3, i].state = STATES['Empty']
