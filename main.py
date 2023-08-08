import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams

from SQL_server import SQLServer


class ReadData:  # Create a class
    def __init__(self):  # Create a start method
        self.data = None  # Create a data variable

    def import_from_csv(self):  # First method
        self.data = pd.read_csv("Compilado.csv", encoding='latin1')  # set var data
        return self.data  # return data


class Plots:
    def __init__(self):
        reader = ReadData()  # Instanciando la clase
        # reader_1 = ReadData()  # new instance
        self.data = reader.import_from_csv()  # READ database (csv)
        # data2 = reader_1.import_from_csv()
        # print("number 1")
        # print("number 2")
        # print(data2)
        print(self.data.columns)  # Print colum name
        print(self.data.head())

    def histogram(self):
        # sns.set_style('whitegrid')
        sns.set_style('darkgrid')  # Set background color and grid
        sns.displot(self.data, x='supervisor', col="tipoevento" )  # Create graphics using limit bal column,
        # Use hue to add another colum to histogram
        # Use palette for color palette
        # plt.xticks(rotation=25)
        plt.show()

    def unique_dispersion(self):
        plt.figure(figsize=(5, 2.5), facecolor="#E1E4E3", edgecolor="white")  # Figure configuration
        plt.title('Metros producidos por maquina semana 31')
        sns.set_style('darkgrid')  # Set background color and grid
        sns.swarmplot(x='maquina', y='metros', data=self.data, palette='inferno_r', hue="folio")
        plt.show()


plotting = Plots()  # Instance plot object
plotting.histogram()
plotting.unique_dispersion()


# server = SQLServer()
# server.insert_data()
# rows = server.read_from_lite()
