import gif
import pandas as pd

from config.constants import (
    COORDS,
    GRID_SIZE,
    INFECTION_RATE,
    INITIAL_INFECTED,
    RECOVERY_RATE,
    SIM_DAYS,
)
from src.animation import plot_comparison
from src.simulation import Population


def run_simulation():
    pop_a = Population(GRID_SIZE, INITIAL_INFECTED, coords=COORDS)
    pop_b = Population(GRID_SIZE, INITIAL_INFECTED, coords=COORDS)
    pop_b.isolate_subpopulations()

    grids_a = [pop_a.get_matrix()]
    ts_a = [pop_a.count_states()]

    grids_b = [pop_b.get_matrix()]
    ts_b = [pop_b.count_states()]

    size_a = (
        pop_a.count_states()['Susceptible']
        + pop_a.count_states()['Infected']
        + pop_a.count_states()['Recovered']
    )
    size_b = (
        pop_b.count_states()['Susceptible']
        + pop_b.count_states()['Infected']
        + pop_b.count_states()['Recovered']
    )

    frames = []

    for _ in range(SIM_DAYS):
        print('Day ' + str(_ + 1), end='\r')

        pop_a.update(INFECTION_RATE, RECOVERY_RATE, 0)
        grids_a.append(pop_a.get_matrix())
        ts_a.append(pop_a.count_states())

        pop_b.update(INFECTION_RATE, RECOVERY_RATE, 0)
        grids_b.append(pop_b.get_matrix())
        ts_b.append(pop_b.count_states())

        ts_a_plot = pd.DataFrame(ts_a)['Infected'] / size_a * 100
        ts_b_plot = pd.DataFrame(ts_b)['Infected'] / size_b * 100

        grid_a = grids_a[-1]
        grid_b = grids_b[-1]

        frames.append(plot_comparison(grid_a, ts_a_plot, grid_b, ts_b_plot))

    gif.save(frames, 'output/comparison.gif', duration=100)


if __name__ == '__main__':
    run_simulation()
