import random

class TrainTicketSystem:
    def __init__(self) -> None:
        self.classes = {
            'economy': {'capacity': 25, 'cost': 20},
            'business': {'capacity': 30, 'cost': 30},
            'exclusive': {'capacity': 35, 'cost': 40}
        }
        self.routes = {
            'minstowe': 'Cowstone -> Freeham -> Donningpool -> Old Mere',
            'old mere': 'Minstowe -> Cowstone -> Freeham -> Donningpool -> Old Mere'
        }
        self.trip_durations = {'minstowe': 15, 'old mere': 15}  # Durations in hours

    def start(self):
        while True:
            print("Make sure you already check your route before you order ticket")
            destination = self.get_route()

            print(f"Here is the route from {destination['from']} to {destination['to']}:")
            print(self.routes[destination['to'].lower()])
            print(f"Duration: {self.trip_durations[destination['to'].lower()]} hours")

            chosen_class = self.get_class()

            print("Please insert your data:")
            name = input("Name: ")
            departure_date = input("Departure date (DD/MM/YYYY): ")
            departure_time = input("Departure time (HH:MM): ")
            train_number = self.generate_train_number()
            platform_number = random.randint(1, 10)
            seat_number = random.randint(1, 50)

            print("Are you sure about all the data above? (Yes/No): ")
            confirmation = input().lower()
            if confirmation == 'yes':
                self.print_ticket(destination, name, departure_date, departure_time, chosen_class, train_number, platform_number, seat_number)

            print("Order another ticket? (Yes/No): ")
            another_ticket_choice = input().lower()
            if another_ticket_choice == 'no':
                break

    def get_route(self):
        from_location = input("Where do you want to go?\nFrom: ").strip().title()
        to_location = input("To: ").strip().title()
        return {'from': from_location, 'to': to_location}

    def get_class(self):
        print("Make sure you already check your belongings before choose the class")
        while True:
            chosen_class = input("Choose class (Economy, Business, Exclusive): ").lower()
            if chosen_class in self.classes:
                return chosen_class
            print("Invalid class. Please choose again.")

    def generate_train_number(self):
        number = random.randint(100, 999)
        letter = chr(random.randint(65, 90))  # A-Z
        return f"{number}-{letter}"

    def print_ticket(self, destination, name, departure_date, departure_time, chosen_class, train_number, platform_number, seat_number):
        total_cost = self.classes[chosen_class]['cost']
        duration_hours = self.trip_durations[destination['to'].lower()]
        arrival_date, arrival_time = self.calculate_arrival(departure_date, departure_time, duration_hours)

        print("\n+----------------------------+")
        print("|        TRAIN TICKET        |")
        print("+----------------------------+")
        print(f"| ORIGIN       | {destination['from'].upper():<18} |")
        print("|--------------+------------------|")
        print(f"| DATE         | {departure_date:<18} |")
        print(f"| TIME         | {departure_time:<18} |")
        print(f"| TRAIN#       | {train_number:<18} |")
        print(f"| CLASS        | {chosen_class.upper():<18} |")
        print(f"| PLATFORM     | {platform_number:<18} |")
        print(f"| SEAT         | {seat_number:<18} |")
        print("|--------------+------------------|")
        print(f"| DESTINATION  | {destination['to'].upper():<18} |")
        print("|--------------+------------------|")
        print(f"| DATE         | {arrival_date:<18} |")
        print(f"| TIME         | {arrival_time:<18} |")
        print("|--------------+------------------|")
        print(f"| PASSENGER NAME | {name.upper():<14} |")
        print("+----------------------------+")
        print(f"Total cost: ${total_cost}")
        print()

    def calculate_arrival(self, departure_date, departure_time, duration_hours):
        # For simplicity, this function will assume no date changes and handle time only.
        departure_time_hours, departure_time_minutes = map(int, departure_time.split(':'))
        arrival_time_hours = (departure_time_hours + duration_hours) % 24
        arrival_date = departure_date  # In a real implementation, this would be adjusted for multi-day trips.
        arrival_time = f"{arrival_time_hours:02d}:{departure_time_minutes:02d}"
        return arrival_date, arrival_time

if __name__ == "__main__":
    TrainTicketSystem().start()
