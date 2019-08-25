#!/usr/bin/env python3
import glfw
from OpenGL.GL import *
import numpy as np

from camera import Camera
from controller import Controller
from mouse_navigation_controller import MouseNavigationController

from gl_camera import GlCamera
from gl_scene import GlScene
from window import Window


def main():
    if not glfw.init():
        return
    window = Window(800, int(800*9/16))

    s = 50
    vertices = np.array([[-s, -s, -s, s, s, -s, s, s]],
                        dtype=np.float32)

    camera = Camera()
    Controller(window, camera)
    mouse_controller = MouseNavigationController(camera)
    window.set_cursor_pos_callback(mouse_controller._cursor_pos_callback)
    window.set_mouse_button_callback(mouse_controller._mouse_button_callback)
    gl_camera = GlCamera(camera)
    gl_scene = GlScene(vertices)

    while not window.should_close():
        gl_camera.update()
        gl_scene.update()
        window.update()

    glfw.terminate()


if __name__ == '__main__':
    main()
