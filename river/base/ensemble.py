class EnsembleMixin:
    """An ensemble is a model which is composed of a list of models.

    Parameters
    ----------
    models

    """

    def __init__(self, models):
        self.models = list(models)

    def __len__(self):
        return len(self.models)

    def __iter__(self):
        return iter(self.models)

    def __getitem__(self, index):
        return self.models[index]
