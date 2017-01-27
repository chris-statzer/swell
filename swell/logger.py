
import logging

COLORS = {
    'DEBUG': 4,
    'ERROR': 1,
    'INFO': 7,
    'WARNING': 3}


class ColoredFormatter(logging.Formatter):
    def __init__(self, msg, datefmt=None, use_color=True):
        super(ColoredFormatter, self).__init__(msg, datefmt)
        self.use_color = use_color

    def format(self, record):
        level = record.levelname
        if self.use_color and level in COLORS:
            spacing = " " * (9 - len(level))
            level_color = "\x1B[1;%dm%s%s\x1B[0m" % (30 + COLORS[level],
                                                     spacing, level)
            record.levelname = level_color
        return logging.Formatter.format(self, record)


formatter = ColoredFormatter(
            (u"\x1B[1;33m[%(levelname)-20s\x1B[1;33m]\x1B[1;32m %(name)s\x1B[0m %(asctime)s "
             u"\x1B[1;37m%(message)s\x1B[0m"),
            u"%H:%M:%S")

# logging.basicConfig(level=logging.DEBUG)

console = logging.StreamHandler()
console.setFormatter(formatter)


def get_logger(name):
    new_log = logging.getLogger(name)
    new_log.addHandler(console)
    new_log.setLevel(logging.INFO)
    return new_log
