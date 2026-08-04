from PySide6.QtWidgets import QFileDialog

from coordinate_mapper.features.project.storage import save_project


class CanvasProjectMixin:

    def save_project(self):

        if not self.image_path:
            return

        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar projeto",
            "points.json",
            "JSON (*.json)",
        )

        if not filename:
            return

        project = {
            "image": {
                "path": self.image_path,
                "width": self.image_width,
                "height": self.image_height,
            },
            "points": [
                point.to_dict()
                for point in self.annotation.get_points()
            ],
        }

        save_project(project, filename)