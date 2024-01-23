import argparse
import logging

import gif
import pandas as pd
from alive_progress import alive_bar

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

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


def run_simulation(gen_gif: bool = False):
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

    if gen_gif:
        frames = []

    logging.info('Simulating days...')
    with alive_bar(SIM_DAYS) as bar:
        for _ in range(SIM_DAYS):
            bar()
            pop_a.update(INFECTION_RATE, RECOVERY_RATE, 0)
            grids_a.append(pop_a.get_matrix())
            ts_a.append(pop_a.count_states())

            pop_b.update(INFECTION_RATE, RECOVERY_RATE, 0)
            grids_b.append(pop_b.get_matrix())
            ts_b.append(pop_b.count_states())

            if gen_gif:
                ts_a_plot = pd.DataFrame(ts_a)['Infected'] / size_a * 100
                ts_b_plot = pd.DataFrame(ts_b)['Infected'] / size_b * 100

                grid_a = grids_a[-1]
                grid_b = grids_b[-1]

                frames.append(plot_comparison(grid_a, ts_a_plot, grid_b, ts_b_plot))

    if gen_gif:
        logging.info('Generating GIF...')
        gif.save(frames, 'output/comparison.gif', duration=100)

    return grids_a, ts_a, grids_b, ts_b


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-g',
        '--gif',
        help='Generate a GIF of the simulation.',
        action='store_true',
    )
    args = parser.parse_args()
    logging.info('Running simulation...')
    logging.info('Generating GIF: ' + str(args.gif))

    run_simulation(args.gif)
    logging.info('Simulation complete.')
