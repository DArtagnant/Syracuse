from syracuse_num import SyracuseNum
from syracuse_graphs import app_syracuse

import matplotlib.pyplot as plt


def super_syracuse(num_max):

    vols = []
    alts = []

    for num in range(1, num_max+1):
        s = SyracuseNum(num)
        vols.append(s.vol)
        alts.append(s.alt)

    fig = plt.figure()

    ax1 = plt.subplot(231)
    ax1.plot(range(len(alts)), alts)
    ax1.set_title("altitude en fonction du nombre")

    ax2 = plt.subplot(234)
    ax2.plot(range(len(vols)), vols)
    ax2.set_title("vol en fonction du nombre")

    ax2 = plt.subplot(1, 3, (2, 3))
    update = app_syracuse(1, fig, ax2, show=False)
    ax2.set_title("Syracuse pour n = 1")

    def onclick(event):

        """
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
            ('double' if event.dblclick else 'single', event.button,
            event.x, event.y, event.xdata, event.ydata))
        """
        if (not event.dblclick) and event.button == 3:
            update(round(event.xdata))

    cid = fig.canvas.mpl_connect('button_press_event', onclick)

    plt.show()

if __name__ == "__main__":
    super_syracuse(100)