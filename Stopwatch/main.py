import sys
from PyQt5.QtWidgets import QApplication
from stopwatch import Stopwatch

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Stopwatch()
    ex.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication
from stopwatch import Stopwatch

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Stopwatch()
    ex.show()
    sys.exit(app.exec_())
