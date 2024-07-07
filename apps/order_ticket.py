import random

class TrainTicketSystem:
    def __init__(self) -> None:
        # Daftar kelas dengan kapasitas dan biaya tiket
        self.classes = {
            'economy': {'capacity': 25, 'cost': 20},
            'business': {'capacity': 30, 'cost': 30},
            'exclusive': {'capacity': 35, 'cost': 40}
        }
        
        # Daftar rute perjalanan kereta beserta deskripsi
        self.routes = {
            'minstowe': 'Cowstone -> Freeham -> Donningpool -> Old Mere',
            'old mere': 'Minstowe -> Cowstone -> Freeham -> Donningpool -> Old Mere'
        }
        
        # Durasi perjalanan untuk setiap rute dalam jam
        self.trip_durations = {
            'minstowe': 10,  # Durasi perjalanan dari Minstowe ke Old Mere adalah 10 jam
            'old mere': 10   # Durasi perjalanan dari Old Mere ke Minstowe adalah 10 jam
        }

        # Tarif per jam dalam dollar
        self.rate_per_hour = 15

    def start(self):
        while True:
            print("Pastikan Anda telah memeriksa rute sebelum memesan tiket.")
            destination = self.get_route()

            print(f"Ini adalah rute dari {destination['from']} ke {destination['to']}:")
            print(self.routes[destination['to'].lower()])
            print(f"Durasi perjalanan: {self.trip_durations[destination['to'].lower()]} jam")

            chosen_class = self.get_class()

            print("Silakan masukkan data Anda:")
            name = input("Nama: ")
            departure_date = input("Tanggal keberangkatan (DD/MM/YYYY): ")
            departure_time = input("Waktu keberangkatan (HH:MM): ")
            train_number = self.generate_train_number()
            platform_number = random.randint(1, 10)
            seat_number = random.randint(1, 50)

            print("Apakah Anda yakin dengan semua data di atas? (Ya/Tidak): ")
            confirmation = input().lower()
            if confirmation == 'ya':
                self.print_ticket(destination, name, departure_date, departure_time, chosen_class, train_number, platform_number, seat_number)

            print("Ingin memesan tiket lagi? (Ya/Tidak): ")
            another_ticket_choice = input().lower()
            if another_ticket_choice == 'tidak':
                break

    def get_route(self):
        from_location = input("Ke mana tujuan Anda?\nDari: ").strip().title()
        to_location = input("Ke: ").strip().title()
        return {'from': from_location, 'to': to_location}

    def get_class(self):
        print("Pastikan Anda telah memeriksa barang bawaan Anda sebelum memilih kelas.")
        while True:
            chosen_class = input("Pilih kelas (Economy, Business, Exclusive): ").lower()
            if chosen_class in self.classes:
                return chosen_class
            print("Kelas tidak valid. Silakan pilih lagi.")

    def generate_train_number(self):
        number = random.randint(100, 999)
        letter = chr(random.randint(65, 90))  # Generate random uppercase letter
        return f"{number}-{letter}"

    def print_ticket(self, destination, name, departure_date, departure_time, chosen_class, train_number, platform_number, seat_number):
        duration_hours = self.trip_durations[destination['to'].lower()]
        total_cost = self.calculate_cost(chosen_class, duration_hours)

        arrival_date, arrival_time = self.calculate_arrival(departure_date, departure_time, duration_hours)

        print("\n+----------------------------+")
        print("|        TIKET KERETA         |")
        print("+----------------------------+")
        print(f"| ASAL         | {destination['from'].upper():<18} |")
        print("|--------------+------------------|")
        print(f"| TANGGAL      | {departure_date:<18} |")
        print(f"| WAKTU        | {departure_time:<18} |")
        print(f"| NOMOR KERETA | {train_number:<18} |")
        print(f"| KELAS        | {chosen_class.upper():<18} |")
        print(f"| PERON        | {platform_number:<18} |")
        print(f"| NOMOR KURSI  | {seat_number:<18} |")
        print("|--------------+------------------|")
        print(f"| TUJUAN       | {destination['to'].upper():<18} |")
        print("|--------------+------------------|")
        print(f"| TANGGAL      | {arrival_date:<18} |")
        print(f"| WAKTU        | {arrival_time:<18} |")
        print("|--------------+------------------|")
        print(f"| NAMA PENUMPANG | {name.upper():<14} |")
        print("+----------------------------+")
        print(f"Total biaya: ${total_cost}")
        print()

    def calculate_cost(self, chosen_class, duration_hours):
        base_cost = self.classes[chosen_class]['cost']
        total_cost = base_cost + (self.rate_per_hour * duration_hours)
        return total_cost

    def calculate_arrival(self, departure_date, departure_time, duration_hours):
        # Menghitung waktu kedatangan berdasarkan waktu keberangkatan dan durasi perjalanan
        departure_time_hours, departure_time_minutes = map(int, departure_time.split(':'))
        arrival_time_hours = (departure_time_hours + duration_hours) % 24
        arrival_date = departure_date  # Dalam implementasi nyata, ini akan disesuaikan untuk perjalanan multi-hari.
        arrival_time = f"{arrival_time_hours:02d}:{departure_time_minutes:02d}"
        return arrival_date, arrival_time

if __name__ == "__main__":
    TrainTicketSystem().start()
