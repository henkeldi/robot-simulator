"""Class to represent a camera."""

from __future__ import division
from __future__ import print_function

import numpy as np


class Camera(object):

    def __init__(self):
        self._projection = np.eye(4, dtype=np.float32)
        self.view = np.eye(4, dtype=np.float32)
        self.viewport = np.array([0, 0, 0, 0], np.float32)
        self._height = 0
        self._width = 0
        self._near = 0
        self._far = 0
        self.clear_color = np.array([0.3, 0.3, 0.3, 1], np.float32)
        self.changed = True

    def ortho(self, width, height, near, far):
        self._width = width
        self._height = height
        self._near = near
        self._far = far
        self._projection[:] = self.transform('projection', 'ncd')
        self.changed = True

    def transform(self, parent, child):
        if parent == 'screen' and child == 'ncd':
            x0, y0, w, h = self.viewport
            return np.array([[2.0/w, 0, 0, -1.0],
                             [0, -2.0/h, 0, 1.0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 1]], np.float32)
        elif parent == 'ncd' and child == 'screen':
            x0, y0, w, h = self.viewport
            return np.array([[0.5*w, 0, 0, 0.5*w],
                             [0, -0.5*h, 0, 0.5*h],
                             [0, 0, 0, 0],
                             [0, 0, 0, 1]], np.float32)
        elif parent == 'viewport' and child == 'ncd':
            x0, y0, w, h = self.viewport
            return np.array([[2.0/w, 0, 0, -1.0-2.0/w*x0],
                             [0, 2.0/h, 0, -1.0-2.0/h*y0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 1]], np.float32)
        elif parent == 'ncd' and child == 'viewport':
            x0, y0, w, h = self.viewport
            return np.array([[0.5*w, 0, 0, x0+0.5*w],
                             [0, 0.5*h, 0, y0+0.5*h],
                             [0, 0, 0, 0],
                             [0, 0, 0, 1]], np.float32)
        elif parent == 'ncd' and child == 'projection':
            f, n = self._far, self._near
            w, h = self._width, self._height
            return np.array([[0.5*w, 0, 0, 0],
                             [0, 0.5*h, 0, 0],
                             [0, 0, 0.5*(f-n), 0.5*(f+n)],
                             [0, 0, 0, 1]], np.float32)
        elif parent == 'projection' and child == 'ncd':
            f, n = self._far, self._near
            w, h = self._width, self._height
            return np.array([[2.0/w, 0, 0, 0],
                             [0, 2.0/h, 0, 0],
                             [0, 0, 2.0/(f-n), (n+f)/(n-f)],
                             [0, 0, 0, 1]], np.float32)
        elif parent == 'view' and child == 'projection':
            return self.view
        elif parent == 'projection' and child == 'view':
            R = self.view[:3, :3]
            t = self.view[:3, 3]
            T = np.eye(4, dtype=np.float32)
            T[:3, :3] = R.T
            T[:3, 3] = -R.T.dot(t)
            return T
        elif parent == 'screen' and child == 'projection':
            return self.transform('projection', 'ncd')\
                .dot(self.transform('screen', 'ncd'))
        elif parent == 'projection' and child == 'screen':
            return self.transform('ncd', 'screen')\
                .dot(self.transform('projection', 'ncd'))
        elif parent == 'screen' and child == 'view':
            return self.transform('projection', 'view')\
                .dot(self.transform('ncd', 'projection'))\
                .dot(self.transform('screen', 'ncd'))
        else:
            raise ValueError("Unknown transform from {} to {}".format(
                parent, child))

    @property
    def projection(self):
        return self._projection

    @property
    def data(self):
        return np.hstack((self.projection.T.reshape(-1),
                          self.view.T.reshape(-1))).astype(np.float32)
