"""Tests that the mouse navigation work properly."""

from __future__ import division
from __future__ import print_function

import unittest

from camera import Camera
from mouse_navigation_controller import _handle_drag_event


class TestMouseNavigationTransform(unittest.TestCase):

    def test_dragging(self):
        camera = Camera()
        camera.viewport[:] = (0, 0, 200, 100)
        camera.ortho(200, 100, -1, 1)
        _handle_drag_event(camera, 0, 10)
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
