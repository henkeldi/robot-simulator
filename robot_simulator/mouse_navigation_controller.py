import glfw
import numpy as np


def _handle_drag_event(camera, from_sceen, to_screen):
    pass


class MouseNavigationController(object):

    def __init__(self, window, camera):
        self._camera = camera
        self._window = window.window
        glfw.set_cursor_pos_callback(self._window, self._cursor_pos_callback)
        glfw.set_mouse_button_callback(self._window,
                                       self._mouse_button_callback)
        self._cursor_pos = np.array([0, 0])
        self._dragging = False
        self._draggin_start_pos = np.array([0, 0])

    def _cursor_pos_callback(self, window, xpos, ypos):
        self._cursor_pos[:] = (xpos, ypos)
        if self._dragging:
            _handle_drag_event(camera, self._draggin_start_pos,
                               self._cursor_pos)

    def _mouse_button_callback(self, window, button, action, mods):
        if button == glfw.MOUSE_BUTTON_RIGHT and action == glfw.PRESS:
            self._dragging = True
            self._draggin_start_pos[:] = self._cursor_pos
        elif button == glfw.MOUSE_BUTTON_RIGHT and action == glfw.RELEASE:
            self._dragging = False
