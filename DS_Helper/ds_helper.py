import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import classification_report,confusion_matrix
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

class svm:
    def eval_metric(model, X_train, y_train, X_test, y_test):
        """SVM model için metrik bilgilerini verir.

        Args:
            model (_type_): _description_
            X_train (_type_): _description_
            y_train (_type_): _description_
            X_test (_type_): _description_
            y_test (_type_): _description_
        """
        y_train_pred = model.predict(X_train)
        y_pred = model.predict(X_test)
        
        print("Test_Set")
        print(confusion_matrix(y_test, y_pred))
        print(classification_report(y_test, y_pred))
        print()
        print("Train_Set")
        print(confusion_matrix(y_train, y_train_pred))
        print(classification_report(y_train, y_train_pred))

    def plot_svm_decision_boundary_with_errors(X, y):
        """SVM model için sonuç grafiği çizer

        Args:
            X (_type_): _description_
            y (_type_): _description_
        """
        # Örnek veriyi oluşturma ve bazı noktaları yanlış sınıflandırmayı sağlama
        X, y = make_blobs(n_samples=300, centers=2, random_state=42, cluster_std=1.0)
        y[::10] = 1 - y[::10]  # Her 10. örneğin sınıfını değiştirerek yanlış sınıflandırma sağlama

        # Veriyi eğitim ve test setlerine ayırma
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # SVM modelini oluşturma ve eğitme
        model = SVC(kernel='linear', C=1.0)
        model.fit(X_train, y_train)

        # Grafiği oluşturma
        plt.figure(figsize=(10, 6))

        # Eğitim verisini çizdirme
        plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='bwr', s=30, edgecolors='k', label='Train')
        plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='coolwarm', s=30, edgecolors='k', label='Test')

        # Support vectorleri çizdirme
        plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=100, facecolors='none', edgecolors='k', label='Support Vectors')

        # Decision boundary ve marginleri çizdirme
        ax = plt.gca()
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        # Decision boundary için meshgrid oluşturma
        xx = np.linspace(xlim[0], xlim[1], 30)
        yy = np.linspace(ylim[0], ylim[1], 30)
        YY, XX = np.meshgrid(yy, xx)
        xy = np.vstack([XX.ravel(), YY.ravel()]).T
        Z = model.decision_function(xy).reshape(XX.shape)

        # Decision boundary ve marginleri çizdirme
        ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])

        # Yanlış sınıflandırılmış noktaları belirleme ve çizdirme
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)

        misclassified_train = (y_train != y_train_pred)
        misclassified_test = (y_test != y_test_pred)

        plt.scatter(X_train[misclassified_train, 0], X_train[misclassified_train, 1], facecolors='none', edgecolors='r', s=100, label='Misclassified Train')
        plt.scatter(X_test[misclassified_test, 0], X_test[misclassified_test, 1], facecolors='none', edgecolors='y', s=100, label='Misclassified Test')

        # Grafiği gösterme
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.title('SVM Decision Boundary with Misclassified Points')
        plt.legend()
        plt.show()