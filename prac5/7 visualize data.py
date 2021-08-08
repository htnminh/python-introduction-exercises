import numpy as np
import pandas as pd
import sklearn.model_selection
import matplotlib.pyplot as plt

class DataPreprocessing():
    def __init__(self):
        # Auto initialize necessary attributes of the object
        self.dataframe = None
        self.X = None
        self.y = None
        
    def read_from_csv(self):
        # Read data from .csv file into the dataframe and display the first 5 rows
        df = pd.read_csv('real_estate.csv', index_col='No')
        self.dataframe = df
        #print(df.head)
        #print(df.iloc[0][1])

    def set_attributes_and_output(self):
        # Set X and y to data attributes and output from the dataframe
        
        ##################
        # YOUR CODE HERE #
        ##################

        #print(self.dataframe)
        self.X = self.dataframe.values[:, :-1]
        self.y = self.dataframe.values[:, -1]
    

    def visualize_data(self):
        # Visualize relation between each attribute and output
        columns_plot = np.array(self.dataframe.columns)[:-1].reshape(3, -1)
        fig, ax = plt.subplots(3, 2, figsize=(10,8), sharey=True)
        fig.suptitle('Correlation between each attribute and the house price of unit area')

        for i in range(3):
            for j in range(2):
                ax[i,j].scatter(self.X[:,i*2 + j], self.y, s=10, color="bgrcmy"[i*2+j])
                ax[i,j].set_xlabel(columns_plot[i, j].split(' ', 1)[1].title())

        fig.tight_layout()   
        fig.add_subplot(111, frameon=False)
        plt.tick_params(labelcolor='none', which='both', top=False, bottom=False, left=False, right=False)
        plt.ylabel(self.dataframe.columns[-1].split(' ', 1)[1].title())
        plt.show()

dp = DataPreprocessing()
dp.read_from_csv()
dp.set_attributes_and_output()

print(dp.dataframe)
dp.visualize_data()
