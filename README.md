# Text Vectorization and Plotting in 3 Dimensions
This project is aimed at vectorizing text data from multiple sources and plotting the resulting vectors in 3 dimensions. The purpose of this analysis is to help visualize the relationships between the text data and identify patterns and similarities between the different datasets.

## Requirements
The following packages are required to run the code in this project:

NumPy
Pandas
Matplotlib
Scikit-learn

You can install these packages using pip install numpy pandas matplotlib scikit-learn.

## Data Sources
This project uses 4 datasets of random text data, stored in the files dataset1.csv, dataset2.csv, dataset3.csv, and dataset4.csv. These datasets are generated using the code provided in the previous section. The data in each dataset consists of 50 rows of text, randomly selected from a predefined list of texts related to eBay's help pages.

## Analysis
The text data from each dataset is vectorized using the TfidfVectorizer from the scikit-learn library. The resulting vectors are then plotted in 3 dimensions using the Matplotlib library. The plot allows us to visualize the relationships between the text data and identify patterns and similarities between the different datasets. Additionally, the encoded text is shown at each point in the plot, providing a visual representation of the text data.

## Conclusion
Visualizing text data in 3 dimensions can be a useful tool for identifying patterns and similarities between different datasets. In this project, we used TfidfVectorizer from the scikit-learn library to vectorize the text data and Matplotlib to plot the resulting vectors in 3 dimensions. The resulting plot provides a visual representation of the relationships between the text data and allows us to identify patterns and similarities between the different datasets.
