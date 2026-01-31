import logging
from enum import StrEnum
import time
import requests
from PySide6.QtCore import QThread, Signal

logger = logging.getLogger(__name__)

SERVER_URL = "http://localhost:8000/"
ADMIN_URL = "http://localhost:8000/admin/"


class ConnectionStatus(StrEnum):
    CONNECTED = "Connected"
    NOT_CONNECTED = "Not Connected"
    TRY_CONNECTING = "Try Connecting..."
    CONNECTING = "Connecting ..."


class CheckConnection(QThread):
    connected = Signal(ConnectionStatus)

    @staticmethod
    def check_server():
        """Check if backend is running."""
        try:
            response = requests.get(SERVER_URL, timeout=5)
            return response.status_code < 500
        except requests.RequestException as e:
            logger.error(f"Backend check failed: {e!s}")
            return False

    def run(self) -> None:
        logger.info("Connection monitoring thread started running")
        while self.isRunning():
            logger.debug("Checking backend connection")
            if not self.check_server():
                self.connected.emit(ConnectionStatus.TRY_CONNECTING)
                time.sleep(3)
                self.connected.emit(ConnectionStatus.CONNECTING)
                time.sleep(0.5)
                if self.check_server():
                    self.connected.emit(ConnectionStatus.CONNECTED)
                else:
                    self.connected.emit(ConnectionStatus.NOT_CONNECTED)
            else:
                self.connected.emit(ConnectionStatus.CONNECTED)

            time.sleep(5)
