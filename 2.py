class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, price, available_seats):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.price = price
        self.available_seats = available_seats

class Ticket:
    def __init__(self, flight, passenger_name):
        self.flight = flight
        self.passenger_name = passenger_name

def display_available_flights(flights):
    print("Available Flights:")
    for flight in flights:
        print(f"{flight.flight_number}: {flight.origin} to {flight.destination} - {flight.departure_time}, Seats: {flight.available_seats}, Price: {flight.price}$")

def book_ticket(flight, passenger_name):
    if flight.available_seats > 0:
        flight.available_seats -= 1
        ticket = Ticket(flight, passenger_name)
        print(f"Ticket booked successfully for {passenger_name} on flight {flight.flight_number}.")
        return ticket
    else:
        print("Sorry, no available seats for this flight.")
        return None

def main():
    # Sample flights
    flight1 = Flight("F123", "City A", "City B", "12:00 PM", 150, 10)
    flight2 = Flight("F456", "City B", "City C", "02:30 PM", 200, 5)
    flights = [flight1, flight2]

    while True:
        print("\nAir Ticket Booking System")
        print("1. Display Available Flights")
        print("2. Book a Ticket")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            display_available_flights(flights)
        elif choice == "2":
            display_available_flights(flights)
            flight_number = input("Enter the flight number you want to book: ")
            passenger_name = input("Enter your name: ")

            selected_flight = next((flight for flight in flights if flight.flight_number == flight_number), None)
            if selected_flight:
                booked_ticket = book_ticket(selected_flight, passenger_name)
                if booked_ticket:
                    print(f"Total Price: {booked_ticket.flight.price}$")
        elif choice == "3":
            print("Thank you for using the Air Ticket Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
