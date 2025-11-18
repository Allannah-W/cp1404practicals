from silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Test", 100, 2)

    taxi.start_fare()
    taxi.drive(18)

    print(taxi)

    fare = taxi.get_fare()
    print(f"Fare: ${fare:.2f}")


main()
