#!/bin/env python3
import glfw


class Controller(object):

    def __init__(self, window, camera):
        self._camera = camera
        self._window = window.window
        glfw.set_window_size_callback(self._window, self._window_size_callback)
        glfw.set_key_callback(self._window, self._key_ballback)
        glfw.set_scroll_callback(self._window, self._scroll_callback)
        width, height = glfw.get_window_size(self._window)
        self._window_size_callback(self._window, width, height)

    def _window_size_callback(self, window, width, height):
        self._camera.viewport[:] = (0, 0, width, height)
        self._camera.ortho(width, height, -1, 1)

    def _key_ballback(self, window, key, scancode, action, mods):
        if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(window, True)

    def _scroll_callback(self, window, xoffset, yoffset):
        print(xoffset, yoffset)
