import logging

from common.proj_paths import *


class CustomFileHandler(logging.FileHandler):
    """
    Taken from: https://stackoverflow.com/a/9408509
    Allows config to specify local file path
    """

    def __init__(self, mode='w'):
        log_file = proj_dir / (proj_dir.stem + '.log')
        super(CustomFileHandler, self).__init__(log_file, mode)


class CustomFormatter(logging.Formatter):
    """
    https://stackoverflow.com/a/7004565
    Custom formatter, overrides funcName with value of name_override if it exists
    """

    def format(self, record):
        if hasattr(record, 'name_override'):
            record.funcName = record.name_override
        return super(CustomFormatter, self).format(record)
