
# Imports
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


topologies = [
    "Solo",
    "Star",
    "Ring",
    # "Fully Connected",
]

dataset = "CIFAR-10"
sampling_algos = [
    "DSGD",
    "DRR",
]

exp_dir = "/home/ubuntu/Desktop/topology-in-decentralized-learning/experiments"
base_path = f"{exp_dir}/epoch100"
output_path = f"{exp_dir}/epoch100/figures"

learning_rates = [
    0.001, 0.005, 0.01, 0.05, 0.1, 0.5
]
losses = [
    ("Solo", "DSGD", [1.204, 0.921, 1.025, 2.051, 2.308, 2.304]), 
    ("Star", "DSGD", [1.053, 0.617, 0.566, 0.687, 2.306, 2.303]), # the last two diverges
    ("Ring", "DSGD", [0.927, 0.484, 0.458, 0.418, 0.432, 2.304]),
    ("Fully Connected", "DSGD", [0.845, 0.502, 0.483, 0.503, 0.444, 2.303]),
    ("Solo", "DRR", [1.206, 0.928, 0.974, 2.159, 2.315, 2.303]), # the last three diverges
    ("Star", "DRR", [1.047, 0.589, 0.536, 0.661, 2.018, 2.303]), # the last two diverges
    ("Ring", "DRR", [0.922, 0.474, 0.440, 0.456, 0.423, 2.306]),
    ("Fully Connected", "DRR", [0.845, 0.500, 0.529, 0.490, 0.445, 2.303]),

]


def plot_loss():
    for algo_idx, sampling_algo in enumerate(sampling_algos):
        # plot loss vs learning rate
        # plot diff topologies on same plot
        fig = plt.figure()
        plt.clf()
        ax = fig.add_subplot(111)
        ax.set_xlabel("Learning Rate")
        ax.set_ylabel("Loss")
        ax.set_title("Loss vs Learning Rate for {}".format(sampling_algo))
        ax.set_xscale("log")
        # ax.set_yscale("log")
        # ax.set_xlim([0.001, 0.1])
        # ax.set_ylim([0.1, 10])
        ax.xaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
        ax.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
        plt.xticks(learning_rates)

        ax.grid(True)

        for topo_idx, topology in enumerate(topologies):
            ax.plot(learning_rates, losses[algo_idx * len(topologies) + topo_idx][2], label=topology)
            ax.legend()

        plt.savefig(os.path.join(output_path, "{}_loss.png".format(sampling_algo)))
        plt.close()

plot_loss()
            

