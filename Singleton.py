class Singleton:
    """
    A non-thread-safe helper class to make singleton classes(scrapper, in this case)
    """

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        try:
            return self._decorated
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self, *args, **kwargs):
        raise TypeError('Singletons must be accessed through Instance()')

    def __instancecheck(self, inst):
        return isinstance(inst, self._decorated)