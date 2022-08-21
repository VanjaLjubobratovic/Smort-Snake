import matplotlib.pyplot as plt
from IPython import display
from contextlib import contextmanager
import sys, os

plt.ion()


@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

def plot(scores, mean_scores, x_label, y_label, y_min):
    with suppress_stdout():
        display.clear_output(wait=True)
        display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=y_min)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.pause(.1)
    plt.savefig('graph.png')