import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class dataviz:
    def __init__(self,path):
        self.path = path
        try:
            self.data = pd.read_excel(path)
            print(self.data.head())
        except Exception as e:
            print(e)

    def headers(self):
        return self.data.columns

    def his(self,header):
        self.data[header].value_counts().plot.bar(figsize=(15,7), colormap='Dark2', fontsize=13, yticks=np.arange(0, 19, 2))
        plt.xlabel(header)
        plt.ylabel('Number of Items')
        plt.title('Bar Chart showing the Number of Items in each Category value')
        path=os.path.join("static","1.png")
        plt.savefig(path)
