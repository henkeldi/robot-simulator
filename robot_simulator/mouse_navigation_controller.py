import glfw
import numpy as np


class MouseNavigationController(object):

    def __init__(self, camera):
        self._camera = camera
        self._cursor_pos = np.array([0, 0])
        self._dragging = False
        self._dragging_start_pos = np.array([0, 0])

    def _cursor_pos_callback(self, window, xpos, ypos):
        self._cursor_pos[:] = (xpos, ypos)
        if self._dragging:
            self._handle_drag_event(self._dragging_start_pos, self._cursor_pos)

    def _mouse_button_callback(self, window, button, action, mods):
        if button == glfw.MOUSE_BUTTON_RIGHT and action == glfw.PRESS:
            self._dragging = True
            self._dragging_start_pos[:] = self._cursor_pos
        elif button == glfw.MOUSE_BUTTON_RIGHT and action == glfw.RELEASE:
            if self._dragging:
                self._handle_drag_end_event(self._dragging_start_pos, self._cursor_pos)
                self._dragging = False

    def _handle_drag_event(self, from_screen, to_screen):
        pass

    def _handle_drag_end_event(self, from_screen, to_screen):
        pass
