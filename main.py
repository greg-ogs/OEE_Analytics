import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from SQL_server import SQLServer


class ReadData:  # Create a class
    def __init__(self, para):  # Create a start method
        self.data = None  # Create a data variable
        print(para)

    def import_from_csv(self):  # First method
        self.data = pd.read_csv("Compilado.csv", encoding='latin1')  # set var data
        return self.data  # return data


class Plots:
    def __init__(self):
        reader = ReadData(para=79)  # Instanciando la clase
        # reader_1 = ReadData()  # new instance
        self.data = reader.import_from_csv()  # READ database (csv)
        # data2 = reader_1.import_from_csv()
        # print("number 1")
        # print("number 2")
        # print(data2)
        print(self.data.columns)  # Print colum name
        print(self.data.head())

    def histogram(self):
        plt.figure(figsize=(10, 5), facecolor="white", edgecolor="black")  # Figure configuration
        # plt.title('Histogram') displot cant use plt title
        # sns.set_style('whitegrid')
        sns.set_style('darkgrid')  # Set background color and grid
        sns.displot(self.data, x='tela', hue='tela',
                    palette='inferno')  # Create graphics using limit bal column,
        # Use hue to add another colum to histogram
        # Use palette for color palette
        plt.show()

    def unique_data(self):
        plt.figure(figsize=(15, 7.5), facecolor="#E1E4E3", edgecolor="white")  # Figure configuration
        plt.title('Tela mas usada en cada maquina')
        sns.set_style('darkgrid')  # Set background color and grid
        sns.countplot(x='Maquina', data=self.data, hue='tela', palette='inferno_r')
        # Plot using unique data, shows every option in a column, can use hue and palette
        plt.show()

    def dispersion_plot(self):
        # plt.figure(figsize=(15, 7.5), facecolor="#E1E4E3", edgecolor="white")  # Figure configuration
        # plt.title('Dispersion plot')
        # The function catplot cant use plt figure and title
        sns.set_style('darkgrid')  # Set background color and grid
        sns.catplot(x='MARRIAGE', y='LIMIT_BAL', data=self.data, hue='DEFAULT',
                    dodge=True)  # Dispersion plot, dodge is used to separate
        plt.show()

    def unique_dispersion(self):
        plt.figure(figsize=(15, 7.5), facecolor="#E1E4E3", edgecolor="white")  # Figure configuration
        plt.title('Unique dispersion data plot')
        sns.set_style('darkgrid')  # Set background color and grid
        sns.swarmplot(x='evento', y='tiempototal', data=self.data, palette='inferno_r')
        plt.show()

    def box_plot(self):
        plt.figure(figsize=(50, 25), facecolor="#E1E4E3", edgecolor="white")  # Figure configuration
        plt.title('Unique dispersion data plot using boxplot')
        sns.set_style('darkgrid')  # Set background color and grid
        sns.boxplot(x='EDUCATION', y='IU', data=self.data, palette='bone', hue='DEFAULT')
        plt.show()

    def violin_plot(self):
        plt.figure(figsize=(100, 10), facecolor="#E1E4E3", edgecolor="white")  # Figure configuration
        plt.title('Tiempo usado para cada evento')
        sns.set_style('darkgrid')  # Set background color and grid
        sns.violinplot(x='evento', y='tiempototal', data=self.data, palette='inferno')
        plt.show()


# plotting = Plots()  # Instance plot object
# plotting.histogram()
# plotting.unique_data()
# plotting.unique_dispersion()
# plotting.violin_plot()

server = SQLServer()
server.insert_data()
server.read_from_lite()
