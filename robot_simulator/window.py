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
        self.window = glfw.create_window(W, H, "Hello World",
                                         None, None)

        if not self.window:
            glfw.terminate()
            return

        center_pos(self.window, 0, W, H)

        glfw.make_context_current(self.window)

    def should_close(self):
        return glfw.window_should_close(self.window)

    def update(self):
        glfw.swap_buffers(self.window)
        glfw.poll_events()
