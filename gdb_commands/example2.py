import gdb


class CallerIs(gdb.Function):
    """Return True if the calling function's name is equal to a string.
This function takes one or two arguments.
The first argument is the name of a function; if the calling function's
name is equal to this argument, this function returns True.
The optional second argument tells this function how many stack frames
to traverse to find the calling function.  The default is 1."""

    def __init__(self):
        super(CallerIs, self).__init__("caller_is")

    def invoke(self, name, nframes=1):
        frame = gdb.get_current_frame()
        while nframes > 0:
            frame = frame.get_prev()
            nframes = nframes - 1
        return frame.get_name() == name.string()

CallerIs()