from tabulate import tabulate

class ViewTrain:
    def __init__(self) -> None:
        self.classes = {
            'economy': {'capacity': 25, 'cost': 20},
            'business': {'capacity': 30, 'cost': 30},
            'exclusive': {'capacity': 35, 'cost': 40}
        }
        self.items = []
    
    def start(self):
        while True:
            print("We can help you choose what to bring, do you want to try? (Yes/No)")
            try_choice = input().lower()
            if try_choice == 'no':
                break

            self.display_classes()

            chosen_class = self.get_class()
            self.get_items()
            self.recommend_items(chosen_class)
            
            print("Try another class(Yes/No): ")
            another_class_choice = input().lower()
            if another_class_choice == 'no':
                break
            self.items.clear()

    def get_class(self):
        chosen_class = input("Choose class: ").lower()
        if chosen_class not in self.classes:
            print("Invalid class selected. Please choose again.")
            return self.get_class()
        return chosen_class

    def get_items(self):
        num_items = int(input("How many things you want to bring?: "))
        for i in range(num_items):
            print(f"Item-{i+1}:")
            name = input("Name: ")
            weight = int(input("Weight(kg): "))
            priority = int(input("Priority(1-5): "))
            self.items.append({'name': name, 'weight': weight, 'priority': priority})

    def recommend_items(self, chosen_class):
        capacity = self.classes[chosen_class]['capacity']
        self.items.sort(key=lambda x: x['priority'])

        total_weight = 0
        recommended_items = []
        
        for item in self.items:
            if total_weight + item['weight'] <= capacity:
                recommended_items.append(item)
                total_weight += item['weight']
        
        print("We recommend you to bring:")
        for item in recommended_items:
            print(f"{item['name']}")
        print(f"With total weight: {total_weight} kg")
        print("You can use our recommendation or choose another class to carry more")

    def display_classes(self):
        headers = ["Class", "Max Capacity (kg)", "Cost ($)"]
        table = []
        for class_name, details in self.classes.items():
            table.append([class_name.capitalize(), details['capacity'], details['cost']])
        print(tabulate(table, headers, tablefmt="grid"))

if __name__ == "__main__":
    Vr = ViewTrain()
    Vr.start()
    Vr.get_class()
    Vr.get_items()
    Vr.recommend_items()
    Vr.display_classes()
