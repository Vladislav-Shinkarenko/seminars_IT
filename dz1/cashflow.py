import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import argparse as arg
#импорт библиотек

parser = arg.ArgumentParser()
parser.add_argument("a", type=str, help="месяц")
parser.add_argument("b", type=str, help="год")
args = parser.parse_args()
#испульзуем argparse, вводим переменные

def inp(a,b):
    dataset = pd.read_excel(f"C:\\Users\\Mi\\Desktop\\python\\2_semestr\\dz1\\outcome_{a}.{b}.xlsx")
    
    #print(dataset)

    dataset['Дата'] = [int(x.split()[0]) for x in dataset['Дата']]

    return dataset

#функция создает dataset

f = True
try:
    dataset = inp(args.a, args.b)
except FileNotFoundError:
    print('raise ValueError("Incorrect month number")')
    f = False
#создание исключения 
    
#колxозное завершение выполнения кода в случае ошибки =)    
if f == True:
    def axShow(month, year):

        fig, ax = plt.subplots(constrained_layout = True)

        sns.lineplot(
            data = dataset,
            x = 'Дата',
            y = 'Сумма',
            hue = 'Категория',
            ax = ax
        )
        ax.legend()

        plt.title(f'Расходы {month}.{year}')

        plt.show()
        
        fig, ax = plt.subplots(constrained_layout=True)

        sns.barplot(
            data = dataset,
            y= 'Категория',
            x= 'Сумма',
            orient = 'h',
            estimator = 'sum',
            errorbar=None,
            ax=ax
        )
        
        plt.title(f'Расходы {month}.{year}')
        
        plt.show()  

    axShow(args.a, args.b)
#фунция графиков
