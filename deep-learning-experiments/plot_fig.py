
# Imports
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


topologies = [
    "Star",
    "Ring",
    "Fully Connected",
]

dataset = "CIFAR-10"
sampling_algos = [
    "DSGD",
    "DRR",
]

base_path = "/home/ubuntu/Desktop/experiments/lr_speedup"
output_path = "/home/ubuntu/Desktop/experiments/lr_speedup/figures"

learning_rates = [
    0.001, 0.005, 0.01, 0.05,
]
losses = [
    ("Star", "DSGD", [1.817,  1.350, 1.243, 1.506]),
    ("Ring", "DSGD", [1.757, 1.022, 0.813, 0.656]),
    ("Fully Connected", "DSGD", [1.703, 0.845, 0.628, 0.426]),
    ("Star", "DRR", [1.831, 1.369, 1.257, 1.523]),
    ("Ring", "DRR", [1.755, 1.032, 0.815, 0.640]),
    ("Fully Connected", "DRR", [1.703, 0.846, 0.616, 0.432]),

]


def plot_loss():
    for algo_idx, sampling_algo in enumerate(sampling_algos):
        # plot loss vs learning rate
        # plot diff topologies on same plot
        fig = plt.figure()
        plt.clf()
        ax = fig.add_subplot(111)
        ax.set_xlabel("Loss")
        ax.set_ylabel("Learning Rate")
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
            

