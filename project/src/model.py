"""Model training and inference."""

from sklearn.ensemble import RandomForestClassifier


class Model:
    def __init__(self):
        self.clf = RandomForestClassifier()

    def train(self, X, y):
        self.clf.fit(X, y)

    def predict(self, X):
        return self.clf.predict(X)
