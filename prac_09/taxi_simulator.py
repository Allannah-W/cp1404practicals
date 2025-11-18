from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def display_menu():
    """Display menu."""
    print("q)uit, c)hoose taxi, d)rive")


def choose_taxi(taxis, current_taxi):
    """Display list of available taxis and let user pick."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

    taxi_choice = int(input("Choose taxi: "))
    if 0 <= taxi_choice < len(taxis):
        current_taxi = taxis[taxi_choice]
    else:
        print("Invalid taxi choice")

    return current_taxi


def drive_taxi(current_taxi, bill_to_date):
    """Get travel distance then show trip cost and update bill."""
    travel_distance = float(input("Drive how far? "))
    current_taxi.start_fare()
    current_taxi.drive(travel_distance)

    trip_cost = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
    bill_to_date += trip_cost

    return bill_to_date


def main():
    """Taxi simulator program."""
    current_taxi = None
    bill_to_date = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    display_menu()
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis, current_taxi)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                bill_to_date = drive_taxi(current_taxi, bill_to_date)
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        display_menu()
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

main()
