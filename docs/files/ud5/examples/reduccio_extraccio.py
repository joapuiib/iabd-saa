import pandas as pd
# --8<-- [start:import_pca]
from sklearn.decomposition import PCA
# --8<-- [end:import_pca]
# --8<-- [start:import_lda]
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
# --8<-- [end:import_lda]
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from sklearn.metrics import accuracy_score

wine = datasets.load_wine()

X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
print("Original shape:", X_train.shape)

def train_test_model(name, X_train, X_test, y_train, y_test):
    model_knn = KNeighborsClassifier(n_neighbors=5, weights='uniform')
    model_knn.fit(X_train, y_train)

    y_pred_rf = model_knn.predict(X_test)
    print(name, model_knn.__class__.__name__, float("{0:.4f}".format(accuracy_score(y_test, y_pred_rf))))

n_components = 2

# --8<-- [start:pca]
pca = PCA(n_components=n_components)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)
print(f"PCA shape:", X_train_pca.shape)
# --8<-- [end:pca]
train_test_model("PCA", X_train_pca, X_test_pca, y_train, y_test)

# --8<-- [start:lda]
lda = LDA(n_components=n_components)
X_train_lda = lda.fit_transform(X_train, y_train)
X_test_lda = lda.transform(X_test)
print(f"LDA shape:", X_train_lda.shape)
# --8<-- [end:lda]
train_test_model("LDA", X_train_lda, X_test_lda, y_train, y_test)
