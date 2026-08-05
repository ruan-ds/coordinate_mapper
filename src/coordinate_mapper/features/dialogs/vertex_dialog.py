from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSpinBox,
    QPushButton,
    QSlider,
)


class VertexDialog(QDialog):

    def __init__(
        self,
        parent=None
    ):

        super().__init__(parent)

        self.setWindowTitle(
            "Configurar vértices"
        )

        self.setup_ui()


    def setup_ui(self):

        layout = QVBoxLayout()


        # quantidade de pontos

        count_layout = QHBoxLayout()

        count_label = QLabel(
            "Quantidade de pontos:"
        )

        self.count = QSpinBox()

        self.count.setMinimum(1)
        self.count.setValue(5)


        count_layout.addWidget(
            count_label
        )

        count_layout.addWidget(
            self.count
        )


        # densidade

        density_layout = QHBoxLayout()

        density_label = QLabel(
            "Densidade:"
        )


        self.density_value = QLabel(
            "100%"
        )


        self.density = QSlider(
            Qt.Horizontal
        )

        self.density.setMinimum(
            0
        )

        self.density.setMaximum(
            100
        )

        self.density.setValue(
            100
        )


        self.density.valueChanged.connect(
            self.update_density_label
        )


        density_layout.addWidget(
            density_label
        )

        density_layout.addWidget(
            self.density
        )

        density_layout.addWidget(
            self.density_value
        )


        # botão

        button = QPushButton(
            "Gerar"
        )

        button.clicked.connect(
            self.accept
        )


        layout.addLayout(
            count_layout
        )

        layout.addLayout(
            density_layout
        )

        layout.addWidget(
            button
        )


        self.setLayout(
            layout
        )


        self.count.setFocus()
        self.count.selectAll()


    def update_density_label(
        self,
        value
    ):

        self.density_value.setText(
            f"{value}%"
        )


    def get_values(self):

        return {
            "count": self.count.value(),
            "percentage": self.density.value()
        }