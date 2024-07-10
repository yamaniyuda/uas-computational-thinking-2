from tabulate import tabulate
from apps.apps import Apps
from fractions import Fraction
from data.train import TRAINT_CLASESS

class ViewTrain:
    def __init__(self) -> None:
        self.classes = TRAINT_CLASESS
    
    

    def show_ui(self):
        headers = ["Class", "Max Capacity (kg)", "Cost ($)"]
        table = []
        for class_name, details in self.classes.items():
            table.append([class_name.capitalize(), details['capacity'], details['cost']])
        print(tabulate(table, headers, tablefmt="heavy_outline"))

        self.__recommend_items()



    def __recommend_items(self):
        print("We can help you choose to bring, do you want try ?")
        
        if input('Yes/No: ').strip().lower() == 'yes':
            class_train = input("Choose class: ")
            print('Give you item priority scale from 1 (very important) to 5 (not important)')

            if self.classes.get(class_train) is None:
                print('clases does\'n exist')
                input()
                return Apps.VIEW_TRAIN
            
            many_items = int(input("How many things you want to bring? "))
            bring_items = []
            
            for i in range(1, many_items + 1):
                name = input(f"Item-{i}\t\t: ")
                weight = int(input("Weight\t\t: "))
                priority = int(input("Priority(1-5)\t: "))
                bring_items.append(( name, weight, priority ))
                print()
            
            devided = input("Can you item be devided into parts? (yes/no) : ").strip().lower()
            if devided == 'yes': item_result = self.__get_item_bring_devided(bring_items, class_train)
            else: item_result = self.__get_item_bring(bring_items, class_train)

            if item_result is False: return None

            if (input('Try another class(yes/no): ').strip().lower() == 'yes'):
                return Apps.VIEW_TRAIN
                

        return None



    def __get_item_bring(self, items: list, classes: dict):
        class_choose = self.classes.get(classes)
        total_capacity = class_choose.get('capacity')
        current_capacity = 0
        select_items = []

        items.sort(key=lambda x: (x[2], x[1]))
        for item in items:
            if current_capacity + item[1] <= total_capacity:
                select_items.append(item[0])
                current_capacity += item[1]
            else:
                break
        select_items.reverse()

        if current_capacity < total_capacity: print('You can carry all of your items')
        else: self.__print_item_bring(select_items, current_capacity)

        return True
        


    def __get_item_bring_devided(self, items: list, classes: dict):
        class_choose = self.classes.get(classes)
        total_capacity = class_choose.get('capacity')
        current_capacity = 0
        select_items = []

        items.sort(key=lambda x: (-(x[1] / x[2]), x[2]))
        print(items)
        for item in items:
            if current_capacity + item[1] <= total_capacity:
                select_items.append(f'{item[0]} (whole)')
                current_capacity += item[1]
            else:
                fraction = Fraction(total_capacity - current_capacity, item[1])
                select_items.append(f'{item[0]} ({fraction.numerator}/{fraction.denominator})')
                current_capacity += item[1] * fraction.numerator / fraction.denominator
                break

        if current_capacity < total_capacity: print('You can carry all of your items')
        else: self.__print_item_bring(select_items, current_capacity)
        
        return True
    


    def __print_item_bring(self, items: list, total_weight: int):
        print('We recomended you to bring:')
        for i in range(1, len(items) + 1):
            print(f'{i}. {items[i - 1]}')
        print(f'With total weight: {total_weight} kg')
        print('You can use our recomendation or choose another class to carry more')