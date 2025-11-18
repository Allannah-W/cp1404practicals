from unreliable_car import UnreliableCar


def main():
    """Test car over many attempts to see effects of reliability
    on the likelihood of driving"""
    unreliable_vehicle = UnreliableCar("30%", 1000, 30)
    reliable_vehicle = UnreliableCar("80%", 1000, 80)

    unreliable_successes = 0
    reliable_successes = 0

    attempts = 100
    test_distance = 10

    # 30% reliable car
    for i in range(attempts):
        distance = unreliable_vehicle.drive(test_distance)
        if distance > 0:
            unreliable_successes += 1
    print(f"30% reliability vehicle - successful tests: {unreliable_successes}")

    # 80% reliable car
    for i in range(attempts):
        distance = reliable_vehicle.drive(test_distance)
        if distance > 0:
            reliable_successes += 1
    print(f"80% reliability vehicle - successful tests: {reliable_successes}")


main()

