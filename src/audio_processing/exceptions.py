class AudioLoadError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'AudioLoaderError, {self.message}'
        else:
            return 'AudioLoaderError has been raised'
        
class UnsupportedFormatError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'UnsupportedFormatError, {self.message}'
        else:
            return 'UnsupportedFormatError has been raised'
        
class AudioTooLongError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'AudioTooLongError, {self.message}'
        else:
            return 'AudioTooLongError has been raised'
        