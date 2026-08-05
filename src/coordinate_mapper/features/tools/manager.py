from coordinate_mapper.features.tools.point import PointTool
from coordinate_mapper.features.tools.select import SelectTool
from coordinate_mapper.features.tools.vertex import VertexTool


class ToolManager:

    def __init__(self, on_tool_changed=None):

        self.on_tool_changed = on_tool_changed

        self.point_tool = PointTool()
        self.select_tool = SelectTool()
        self.vertex_tool = VertexTool()

        self.current_tool = self.point_tool

        self.canvas = None


    def toggle_move(self):

        if self.current_tool == self.select_tool:

            self.set_tool(
                self.point_tool
            )

            message = "Modo movimentação desativado"

        else:

            self.set_tool(
                self.select_tool
            )

            message = "Modo movimentação ativado"


        self.notify(
            message
        )


    def toggle_vertex(self):

        if self.current_tool == self.vertex_tool:

            self.set_tool(
                self.point_tool
            )

            message = "Modo vértice desativado"

        else:

            self.set_tool(
                self.vertex_tool
            )

            message = "Modo vértice ativado"


        self.notify(
            message
        )


    def set_tool(self, tool):

        if self.current_tool == tool:
            return


        if self.canvas:

            self.current_tool.reset(
                self.canvas
            )

        else:

            self.current_tool.reset()


        self.current_tool = tool



    def notify(self, message):

        if self.on_tool_changed:
            self.on_tool_changed(message)



    def mouse_press(self, canvas, event):
        self.canvas = canvas

        self.current_tool.mouse_press(
            canvas,
            event
        )


    def mouse_move(self, canvas, event):
        self.canvas = canvas

        self.current_tool.mouse_move(
            canvas,
            event
        )


    def mouse_release(self, canvas, event):
        self.canvas = canvas

        self.current_tool.mouse_release(
            canvas,
            event
        )