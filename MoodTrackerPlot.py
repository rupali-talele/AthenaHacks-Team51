import io
import random
from flask import Flask, Response
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
app = Flask(__name__)

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

def create_figure():
    fig = Figure()
    ax = fig.add_subplot(1, 1, 1)
    xs = range(31)
    ys = [random.randint(-5, 5) for x in xs]
    ys = moving_average(ys, 4)
    ax.plot(xs[:28], ys)
    ax.set_title('Mood Tracker Feburary 2021')
    ax.set_xlabel('Day')
    ax.set_ylabel('overall mood (pos/neg thinking)')
    ax.set_xticks(np.arange(28))
    ax.set_xticklabels(np.arange(1,29))
    ax.grid(True)
    return fig


app.run()
