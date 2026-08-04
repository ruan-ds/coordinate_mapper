from coordinate_mapper.features.tools.point import PointTool
from coordinate_mapper.features.tools.select import SelectTool


class ToolManager:

    def __init__(self, on_tool_changed=None):

        self.on_tool_changed = on_tool_changed

        self.point_tool = PointTool()
        self.select_tool = SelectTool()

        self.current_tool = self.point_tool


    def toggle_move(self):

        if self.current_tool == self.select_tool:

            self.current_tool = self.point_tool

            message = "Modo movimentação desativado"

        else:

            self.current_tool = self.select_tool

            message = "Modo movimentação ativado"


        if self.on_tool_changed:
            self.on_tool_changed(message)

    def mouse_press(self, canvas, event):

        self.current_tool.mouse_press(
            canvas,
            event
        )


    def mouse_move(self, canvas, event):

        self.current_tool.mouse_move(
            canvas,
            event
        )


    def mouse_release(self, canvas, event):

        self.current_tool.mouse_release(
            canvas,
            event
        )