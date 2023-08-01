import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class ReadData:  # Create a class
    def __init__(self, para):  # Create a start method
        self.data = None  # Create a data variable
        print(para)

    def import_from_csv(self):  # First method
        self.data = pd.read_csv("credit_card.csv")  # set var data
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

    def new_var(self):
        self.data['IU'] = self.data['BILL_AMT'] / self.data['LIMIT_BAL']
        print(self.data.head(10))  # First 10 rows in python  console
        # ages = self.data.AGE.nunique()
        # print(ages)
        bins = [20, 30, 40, 50, 100] # Cut in multiple ranges and put in a new column
        colum_titles = ['20-30', '30-40', '40-50', '50+']
        self.data['AGE_RANGE'] = pd.cut(self.data['AGE'], bins, labels=colum_titles)
        print(self.data.columns)  # Print colum name
        plt.figure(figsize=(40, 25), facecolor="#E1E4E3", edgecolor="white")  # Figure configuration
        plt.title('Unique dispersion data plot using boxplot about age and limit')
        sns.set_style('darkgrid')  # Set background color and grid
        sns.boxplot(x='AGE_RANGE', y='LIMIT_BAL', data=self.data, palette='bone', hue='DEFAULT')
        plt.show()

    def histogram(self):
        plt.figure(figsize=(10, 5), facecolor="white", edgecolor="black")  # Figure configuration
        # plt.title('Histogram') displot cant use plt title
        # sns.set_style('whitegrid')
        sns.set_style('darkgrid')  # Set background color and grid
        sns.displot(self.data, x='LIMIT_BAL', hue='EDUCATION',
                    palette='inferno')  # Create graphics using limit bal column,
        # Use hue to add another colum to histogram
        # Use palette for color palette
        plt.show()

    def histogram_subplot(self):
        plt.figure(figsize=(10, 5), facecolor="white", edgecolor="black")  # Figure configuration
        # plt.title('Histogram') displot cant use plt title
        # sns.set_style('whitegrid')
        sns.set_style('darkgrid')  # Set background color and grid
        sns.displot(self.data, x='LIMIT_BAL', col='EDUCATION', kind='kde', hue='AGE_RANGE',
                    palette='inferno')  # Create graphics using limit bal column,
        # Use hue to add another colum to histogram,
        # Use col to add another plot to histogram and kind for density,
        # Use palette for color palette
        plt.show()

    def unique_data(self):
        plt.figure(figsize=(10, 5), facecolor="#E1E4E3", edgecolor="white")  # Figure configuration
        plt.title('Unique data plot')
        sns.set_style('darkgrid')  # Set background color and grid
        sns.countplot(x='CHECKING_ACCOUNT', data=self.data, hue='DEFAULT', palette='inferno_r')
        # Plot using unique data, shows every option in a column, can use hue and palette

    def dispersion_plot(self):
        # plt.figure(figsize=(10, 5), facecolor="#E1E4E3", edgecolor="white")  # Figure configuration
        # plt.title('Dispersion plot')
        # The function catplot cant use plt figure and title
        sns.set_style('darkgrid')  # Set background color and grid
        sns.catplot(x='MARRIAGE', y='LIMIT_BAL', data=self.data, hue='DEFAULT',
                    dodge=True)  # Dispersion plot, dodge is used to separate
        plt.show()

    def unique_dispersion(self):
        plt.figure(figsize=(50, 25), facecolor="#E1E4E3", edgecolor="white")  # Figure configuration
        plt.title('Unique dispersion data plot')
        sns.set_style('darkgrid')  # Set background color and grid
        sns.swarmplot(x='EDUCATION', y='IU', data=self.data, palette='inferno_r')
        plt.show()

    def box_plot(self):
        plt.figure(figsize=(50, 25), facecolor="#E1E4E3", edgecolor="white")  # Figure configuration
        plt.title('Unique dispersion data plot using boxplot')
        sns.set_style('darkgrid')  # Set background color and grid
        sns.boxplot(x='EDUCATION', y='IU', data=self.data, palette='bone', hue='DEFAULT')
        plt.show()

    def violin_plot(self):
        plt.figure(figsize=(50, 25), facecolor="#E1E4E3", edgecolor="white")  # Figure configuration
        plt.title('Unique dispersion data plot using boxplot')
        sns.set_style('darkgrid')  # Set background color and grid
        sns.violinplot(x='EDUCATION', y='IU', data=self.data, palette='inferno', hue='DEFAULT')
        plt.show()


plotting = Plots()  # Instance plot object
plotting.new_var()
plotting.histogram()
plotting.histogram_subplot()
plotting.unique_data()
plotting.dispersion_plot()
plotting.unique_dispersion()
plotting.box_plot()
plotting.violin_plot()