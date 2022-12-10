from syracuse import SyracuseNum

import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

def app_syracuse(default_num, fig, ax, show=True):

    fig.subplots_adjust(bottom=0.2)

    graph, = SyracuseNum(default_num)._graph_plot(ax, lw=2)

    axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
    text_box = TextBox(axbox, "", textalignment="center")

    def update(new_num):
        num = int(new_num)
        s = SyracuseNum(num)
        graph.set_xdata(range(len(s)))
        graph.set_ydata(list(s))
        ax.relim()
        ax.autoscale_view()
        ax.set_title(f"Syracuse pour n = {new_num}")
        text_box.set_val(str(new_num))
        plt.draw()
    
    text_box.on_submit(update)
    text_box.set_val(repr(default_num))  # Trigger `submit` with the initial string.

    if show:
        plt.show()
    else:
        return update

if __name__ == "__main__":
    fig, ax = plt.subplots()
    app_syracuse(10, fig, ax)