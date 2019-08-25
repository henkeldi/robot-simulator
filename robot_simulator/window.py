import glfw


def center_pos(window, monitor_id, W, H):
    # W, H: window dimensions
    mon = glfw.get_monitors()
    xpos = glfw.get_monitor_pos(mon[monitor_id])[0] + \
        glfw.get_video_mode(mon[monitor_id]).size[0]/2-W/2
    ypos = glfw.get_monitor_pos(mon[monitor_id])[1] + \
        glfw.get_video_mode(mon[monitor_id]).size[1]/2-H/2
    glfw.set_window_pos(window, int(xpos), int(ypos))


class Window(object):

    def __init__(self, W, H):
        self._window = glfw.create_window(W, H, "Hello World",
                                         None, None)

        if not self._window:
            glfw.terminate()
            return

        center_pos(self._window, 0, W, H)

        glfw.make_context_current(self._window)

    def set_cursor_pos_callback(self, cursor_pos_callback):
        glfw.set_cursor_pos_callback(self._window, cursor_pos_callback)

    def set_mouse_button_callback(self, mouse_button_callback):
        glfw.set_mouse_button_callback(self._window, mouse_button_callback)

    def set_window_size_callback(self, window_size_callback):
        glfw.set_window_size_callback(self._window, window_size_callback)

    def set_key_callback(self, key_ballback):
        glfw.set_key_callback(self._window, key_ballback)

    def set_scroll_callback(self, scroll_callback):
        glfw.set_scroll_callback(self._window, scroll_callback)

    def get_window_size(self):
        return glfw.get_window_size(self._window)

    def should_close(self):
        return glfw.window_should_close(self._window)

    def update(self):
        glfw.swap_buffers(self._window)
        glfw.poll_events()

