# This project is licensed under the MIT License - see the LICENSE file for details.
import sys

from PySide6.QtWidgets import QApplication  # pylint: disable = no-name-in-module
from GUI import MainWindow


def main():
    """
    TaskFlow entry point.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
