from email.mime import message

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
)

from coordinate_mapper.app.widgets.toast import Toast
from coordinate_mapper.features.canvas.canvas import Canvas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Coordinate Mapper")
        self.setMinimumSize(1000, 700)

        self.canvas = Canvas()
        self.canvas = Canvas()
        self.toast = Toast(self)

        self.canvas.tools.on_tool_changed = self.show_toast

        self.setup_ui()

    def setup_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        top_layout = QHBoxLayout()

        self.load_button = QPushButton("Carregar imagem")
        self.load_button.clicked.connect(self.load_image)

        self.save_button = QPushButton("Salvar projeto")
        self.save_button.clicked.connect(self.canvas.save_project)

        help_label = QLabel("?")

        help_label.setStyleSheet("""
            QLabel {
                border: 1px solid gray;
                border-radius: 10px;
                padding: 0px 5px;
                font-weight: bold;
            }
        """)

        help_label.setToolTip(
    "Ferramentas:\n"
    "Ctrl+M: Alterna modo movimentação\n"
    "\n"
    "Pontos:\n"
    "Clique esquerdo: Insere ponto\n"
    "Clique direito sobre ponto: Menu de ações\n"
    "\n"
    "Projeto:\n"
    "Ctrl+S: Salvar projeto\n"
    "Ctrl+Z: Remover última inserção"
)

        top_layout.addWidget(self.load_button)
        top_layout.addWidget(self.save_button)
        top_layout.addStretch()
        top_layout.addWidget(help_label)

        layout.addLayout(top_layout)
        layout.addWidget(self.canvas)

    def load_image(self):

        filename, _ = QFileDialog.getOpenFileName(
            self, "Abrir imagem", "", "Imagens (*.png *.jpg *.jpeg *.bmp)"
        )

        if filename:
            self.canvas.load_image(filename)

    def show_toast(self, message):
        self.toast.show_message(message)
