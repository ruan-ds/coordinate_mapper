import sys

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog
)

from canvas import Canvas


def main():

    app = QApplication(sys.argv)

    canvas = Canvas()

    image_path, _ = QFileDialog.getOpenFileName(
        None,
        "Abrir imagem",
        "",
        "Imagens (*.png *.jpg *.jpeg *.bmp)"
    )

    if not image_path:
        sys.exit(0)

    canvas.load_image(image_path)

    canvas.setWindowTitle("Coordinate Mapper")
    canvas.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()