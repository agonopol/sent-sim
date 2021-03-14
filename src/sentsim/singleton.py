
class singleton:
    def __init__(self, cls):
        self._cls = cls

    def instance(self, **kwargs):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls(**kwargs)
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)