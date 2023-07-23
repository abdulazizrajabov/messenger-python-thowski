import sys
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit

class ClientGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.chat_box = QTextEdit()
        self.message_input = QLineEdit()
        self.send_button = QPushButton("Send")

        layout = QVBoxLayout()
        layout.addWidget(self.chat_box)
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.message_input)
        h_layout.addWidget(self.send_button)
        layout.addLayout(h_layout)

        self.setLayout(layout)

        self.send_button.clicked.connect(self.send_message)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('SERVER_IP_ADDRESS', SERVER_PORT))  # Replace with actual server IP and port

    def send_message(self):
        message = self.message_input.text()
        self.client_socket.send(message.encode('utf-8'))
        self.message_input.clear()

    def receive_messages(self):
        while True:
            message = self.client_socket.recv(1024).decode('utf-8')
            self.chat_box.append(message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = ClientGUI()
    client.show()

    sys.exit(app.exec_())
