from PyQt5 import QtGui, QtWidgets, QtCore

from matplotlib.figure import Figure
from matplotlib.text import Text
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas



class MathTextLabel(QtWidgets.QWidget):
    def __init__(self, mathText, parent=None, **kwargs):
        QtWidgets.QWidget.__init__(self, parent, **kwargs)

        l = QtWidgets.QVBoxLayout(self)
        l.setContentsMargins(0, 0, 0, 0)

        r, g, b, a = self.palette().window().color().getRgbF()

        self._figure = Figure(edgecolor=(r, g, b), facecolor=(r, g, b))
        self._canvas = FigureCanvas(self._figure)
        l.addWidget(self._canvas)

        self._figure.clear()
        text = self._figure.suptitle(
            mathText,
            x=0.0,
            y=0.85,
            horizontalalignment='left',
            verticalalignment='top',
            size=16)  # set font size
        self._canvas.draw()

        (x0, y0), (x1, y1) = text.get_window_extent().get_points()
        w = x1 - x0
        h = y1 - y0

        self._figure.set_size_inches(w / 80, h / 80)
        self.setFixedSize(w, h)

    def updateText(self, mathText):
        text = self._figure.suptitle(
            mathText,
            x=0.0,
            y=0.85,
            horizontalalignment='left',
            verticalalignment='top',
            size=16)  # set font size
        self._canvas.draw()

        (x0, y0), (x1, y1) = text.get_window_extent().get_points()
        w = x1 - x0
        h = y1 - y0
        self._figure.set_size_inches(w / 80, h / 80)
        self.setFixedSize(w, h)


if __name__ == '__main__':
    from sys import argv, exit


    class Widget(QtWidgets.QWidget):
        def __init__(self, parent=None, **kwargs):
            QtWidgets.QWidget.__init__(self, parent, **kwargs)
            self.setFixedSize(400, 200)
            l = QtWidgets.QVBoxLayout(self)
            l.addWidget(QtWidgets.QLabel("<h1>Discrete Fourier Transform</h1>"))

            mathText = r'$X_k = \sum_{n=0}^{N-1} x_n . e^{\frac{-i2\pi kn}{N}} making this longer testing to make this longer than before$'
            l.addWidget(MathTextLabel(mathText, self),
                        alignment=QtCore.Qt.AlignHCenter)

    a = QtWidgets.QApplication(argv)
    w = Widget()
    w.show()
    w.raise_()
    exit(a.exec_())