from tabulate import tabulate

class ViewTrain:
    def __init__(self) -> None:
        self.classes = {
            'economy': {'capacity': 25, 'cost': 20},
            'business': {'capacity': 30, 'cost': 30},
            'exclusive': {'capacity': 35, 'cost': 40}
        }
        self.items = []
    
    

    def show_ui(self):
        headers = ["Class", "Max Capacity (kg)", "Cost ($)"]
        table = []
        for class_name, details in self.classes.items():
            table.append([class_name.capitalize(), details['capacity'], details['cost']])
        print(tabulate(table, headers, tablefmt="heavy_outline"))
        self.recommend_items()



    def recommend_items(self):
        print("We can help you choose to bring, do you want try ?")
        
        if input('Yes/No: ').strip().lower() == 'yes':
            class_train = input("Choose class: ")
            print('Give you item priority scale from 1 (very important) to 5 (not important)')
            
            many_items = int(input("How many things you want to bring? "))
            bring_items = []
            
            for i in range(1, many_items + 1):
                name = input(f"Item-{i}\t\t: ")
                weight = input("Weight\t\t: ")
                priority = int(input("Priority(1-5)\t"))
                bring_items.append(( name, weight, priority ))
            
            devided = input("Can you item be devided into parts? (yes/no) :").strip().upper()
            if devided == 'yes': self.get_item_bring_devided(bring_items, class_train)
            else: self.get_item_bring(bring_items, class_train)
                

        return None


    def get_item_bring(self, items, classes):
        class_choose = self.classes.get(classes)
        total_capacity = class_choose.get('capacity')
        K = [[0 for _ in range(total_capacity + 1)] 
             for _ in range(len(items) + 1)]

        for i in range(len(items) + 1):
            for j in range(total_capacity + 1):
                if i == 0 or j == 0:
                    K[i][j] = 0
                elif items[1] <= total_capacity:
                    K[i][j] = min(items[i-1][2] + K[i-1][j-items[i-1][1]], K[i-1][j])
                else:
                    K[i][j] = K[i - 1][j]
        print(K[len(items)][total_capacity])


    def get_item_bring_devided(self, items, classes):
        pass