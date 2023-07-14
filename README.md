# URL-Classifier

<h2 style="font-size: larger;">Description</h2>

This GitHub repository contains code and datasets for a project that focuses on classifying URLs based on their attack type. The project utilizes the UNB dataset, obtained from the UNB website, as well as a dataset obtained from Kaggle. Several classifiers, including Random Forest, Decision Tree, Fully Connected Neural Network (FCNN), and 3 Ensemble Model, were implemented and evaluated on both the UNB and Kaggle datasets.


<h2 style="font-size: larger;">Dataset</h2>
The repository includes the following dataset folders:

**unb-dataset**: This folder contains URL datasets from the UNB website. The datasets are organized based on multiple attack types, allowing for binary and multi-class classification tasks.

**kaggle-dataset**: This folder contains the URL dataset obtained from Kaggle.

<h2 style="font-size: larger;">Preprocessing Folder</h2>

The repository includes a preprocessing folder, which contains the following .ipynb files:

**feature-extraction.ipynb**: This file demonstrates the code for extracting relevant features from the URL datasets. It covers techniques such as parsing URL components, analyzing domain-related features, and extracting textual features.

**normalization.ipynb**: This file showcases the code for normalizing the extracted features. It covers techniques such as scaling, encoding categorical variables, and handling missing data.

<h2 style="font-size: larger;">Classifier Folders</h2> 

The repository includes separate folders for each classifier, containing the corresponding .py files. These folders are as follows:

**random-forest**: This folder contains the Random Forest classifier's .py file, showcasing the code used to train and evaluate the classifier.

**decision-tree:** This folder contains the Decision Tree classifier's .py file, demonstrating the code used to train and evaluate the classifier on all the datasets. 

**fcnn**: This folder contains the Fully Connected Neural Network (FCNN) classifier's .py file. 

**ensemble:** This folder contains the Heterogeneous Ensemble Model's .py file, illustrating the code used to train and evaluate the model all the datasets.

**homogeneous ensemble:** This folder contains  .py files , illustrating the code used to train and evaluate the model on the UNB binary, UNB multiclass, and Kaggle datasets using ensemble model using decision tree, and another ensemble model using fully connected neural network.

<h2 style="font-size: larger;">Usage</h2>

You can access the relevant code files for each classifier in their respective folders. The .py files provide a step-by-step implementation of the classifiers, including data preprocessing, training, and evaluation.

To reproduce the results, you can execute the code in your preferred Jupyter Notebook environment, ensuring that the required dependencies are installed.


