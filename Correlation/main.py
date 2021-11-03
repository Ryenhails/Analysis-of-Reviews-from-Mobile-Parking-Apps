from functions import General
import pandas


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    df = General.readFile('./data/indicators/', 'compound')

    df = df.dropna()

    General.correlationMatrix(df.iloc[:, 2:7])  # removing index column
