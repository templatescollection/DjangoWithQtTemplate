import logging
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from frontend.main_windows import CheckConnection, ConnectionStatus
from ui import main_windows

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        logger.info("MainWindow initialized")
        self.ui = main_windows.Ui_MainWindow()
        try:
            self.ui.setupUi(self)
            logger.info("UI setup done")
        except Exception as e:
            logger.error(f"UI setup error: {e}")
            raise

        self.check_connection_thread = CheckConnection()
        self.check_connection_thread.connected.connect(self.show_connection)
        self.check_connection_thread.start()
        logger.info("Connection monitoring thread started")

    def show_connection(self, connected: ConnectionStatus):
        self.statusBar().showMessage(str(connected))
        logger.info(f"Connection status: {connected}")


def main():
    # Basic logging configuration
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stderr)],
    )

    app = QApplication(sys.argv)
    logger.info("QApplication created")

    # Apply qt-material style
    try:
        from qt_material import apply_stylesheet

        apply_stylesheet(app, theme="dark_teal.xml")
        logger.info("Applied qt-material dark_teal theme")
    except ImportError:
        logger.warning("qt-material not available, using default theme")

    main_window = MainWindow()
    main_window.setWindowTitle("Frontend")
    main_window.show()
    logger.info("MainWindow shown")

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
