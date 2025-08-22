from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split


def train_ada_boost(X, target, estimators=3, random_seed=0):
    X_train, X_test, y_train, y_test = train_test_split(
        X, target, random_state=random_seed
    )
    model = AdaBoostClassifier(n_estimators=estimators, random_state=random_seed)
    model.fit(X_train, y_train)
    return (model, X_test, y_test)
