#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import random
import os
import timeit
import logging
from helper import *

def steepest_ascent(start_seq, log_name):
    """Implementation of steepest ascent algorithm
    for the travelling salesman problem.
    The hill climbing algorithm runs 10,000 iterations and
    restarts at every 2,000 iterations with a randomly chosen route.

    Parameters
    ----------
    start_seq : list
        A sequence of city which represent a initial route.

    Returns
    -------
    (int, list)
        The result of the algorithm which is the total distance for the 
        best sequence found along with the corresponding sequence.
    """
    pass

if __name__ == '__main__':
    # Reading txt file path from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str)
    args = parser.parse_args()
    file_path = os.path.join(os.getcwd(), args.filename)
    with open(file_path) as file:
        data = file.readlines()

    # Configure logging
    log_name = (args.filename).replace("data/", "steepest-ascent-")
    logging.basicConfig(filename='./results/log-{}'.format(log_name),
                        level=logging.INFO,
                        format='%(asctime)s\t\t%(message)s',
                        filemode='w')

    # Getting the list of cities and their coordinates
    list_of_cities = [i.strip().split(',') for i in data]
    city_names = [row[0] for row in list_of_cities[1:]]
    coordinates = [[row[1], row[2]] for row in list_of_cities[1:]]

    # Generating a random initial sequence
    number_of_cities = len(city_names)
    random_start_seq = random.sample(list_of_cities[1:], number_of_cities)

    # Calculating the least distance using simple hill climbing
    start_time = timeit.default_timer()
    least_distance, best_seq = steepest_ascent(random_start_seq, log_name)
    end_time = timeit.default_timer()

    logging.info("Results from Steepest ascent climbing:")
    logging.info("Best Sequence: {}".format(best_seq))
    logging.info("Least distance is {}".format(least_distance))
    logging.info("Time: {}".format(end_time - start_time))
