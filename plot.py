import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the datasets
df1 = pd.read_csv('dataset1.csv', sep='|')
df2 = pd.read_csv('dataset2.csv', sep='|')
df3 = pd.read_csv('dataset3.csv', sep='|')
df4 = pd.read_csv('dataset4.csv', sep='|')

# Add a column to each dataset indicating its source
df1['source'] = 'dataset1'
df2['source'] = 'dataset2'
df3['source'] = 'dataset3'
df4['source'] = 'dataset4'

# Concatenate the datasets
df = pd.concat([df1, df2, df3, df4], ignore_index=True)

# Vectorize the text using Tf-idf
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(df['text'].values)

# Reduce the dimensionality of the vectors using PCA
pca = PCA(n_components=3)
pca_result = pca.fit_transform(vectors.toarray())
df['pca_0'] = pca_result[:, 0]
df['pca_1'] = pca_result[:, 1]
df['pca_2'] = pca_result[:, 2]

# Plot each dataset independently
sources = ['dataset1', 'dataset2', 'dataset3', 'dataset4']
for source in sources:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    data = df[df['source'] == source]
    ax.scatter(data['pca_0'], data['pca_1'], data['pca_2'])
    for i, text in enumerate(data['text']):
        ax.text(data['pca_0'].iloc[i], data['pca_1'].iloc[i], data['pca_2'].iloc[i], text)
    ax.set_title(source)
    plt.show()

# Plot all datasets together
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for source in sources:
    data = df[df['source'] == source]
    ax.scatter(data['pca_0'], data['pca_1'], data['pca_2'])
ax.set_title('All Datasets')
plt.show()
