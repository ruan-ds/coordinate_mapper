class ToolManager:

    def __init__(self, default_tool=None):
        self.current_tool = default_tool


    def set_tool(self, tool):
        self.current_tool = tool


    def mouse_press(self, canvas, event):

        if self.current_tool:
            self.current_tool.mouse_press(
                canvas,
                event
            )