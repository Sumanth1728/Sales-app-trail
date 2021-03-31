import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import random


class dataviz:
    def __init__(self,path):
        self.path = path
        try:
            type=path.rsplit('.', 1)[1].lower()
            print(type)
            print("------------------------")
            if(type=="xlsx"):
                self.data = pd.read_excel(path)
            elif(type=="csv"):
                self.data=pd.read_csv(path)

        except Exception as e:
            print(e)

    def headers(self):
        return self.data.columns

    def barchart(self,header):
        self.data[header].value_counts().plot.bar(figsize=(15,7), colormap='Dark2', fontsize=13, yticks=np.arange(0, 19, 2))
        plt.xlabel(header)
        plt.ylabel('Number of Items')
        plt.title('Bar Chart showing the Number of Items in each'+ header+'value')
        n = random.randint(0,10000)
        path=os.path.join("static",str(n)+".png")
        plt.savefig(path)
        return n

    def linechart(self,header):
        self.data[header].plot(kind='line', figsize=(15,7), color='blue', fontsize=13, linestyle='-.')
        plt.xlabel("Index")
        plt.ylabel(header)
        plt.title('Line chart showing the variation of' + header)
        n = random.randint(0,10000)
        path=os.path.join("static",str(n)+".png")
        plt.savefig(path)
        return n
    def areachart(self,header):
        self.data[header].plot(kind='area', figsize=(15,7), color='violet', fontsize=13)
        plt.xlabel("Index")
        plt.ylabel(header)
        plt.title('Line chart showing the variation of' + header)
        n = random.randint(0,10000)
        path=os.path.join("static",str(n)+".png")
        plt.savefig(path)
        return n
    def donutchart(self,header):
        space = np.ones(11)/10
        self.data[header].value_counts().plot(kind='pie', explode=space, fontsize=14, autopct='%3.1f%%', wedgeprops=dict(width=0.15), shadow=True, startangle=160, figsize=(10,10), cmap='inferno', legend=True)
        plt.ylabel(header)
        plt.title('Donut Plot showing the proportion of each'+header+' value')
        n = random.randint(0,10000)
        path=os.path.join("static",str(n)+".png")
        plt.savefig(path)
        return n
    def scatterplot(self,var1,var2):
        self.data.plot(kind='scatter', x=var1, y=var2, figsize=(10, 6), color='purple', grid=False)
        plt.title('Scatter plot showing the variation of'+var2+' with '+var1)
        n = random.randint(0,10000)
        path=os.path.join("static",str(n)+".png")
        plt.savefig(path)
        return n

    def hexplot(self,var1,var2):
        self.data.plot(kind='hexbin', x=var1, y=var2, figsize=(15, 7), gridsize=25, fontsize=13, colormap='Reds')
        plt.title('Hex plot showing the variation of'+var2+' with '+var1)
        n = random.randint(0,10000)
        path=os.path.join("static",str(n)+".png")
        plt.savefig(path)
        return n



    def DataCat(self,header):
        return self.data[header][10]
