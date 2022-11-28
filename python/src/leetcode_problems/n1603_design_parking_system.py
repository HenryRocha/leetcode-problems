class ParkingSystem:
    sizes: int = 3
    total_slots: dict[int, int] = dict()
    available_slots: dict[int, int] = dict()

    def __init__(self, big: int, medium: int, small: int):
        self.total_slots[1] = big
        self.total_slots[2] = medium
        self.total_slots[3] = small

        for i in range(1, self.sizes + 1):
            self.available_slots[i] = self.total_slots[i]

    def addCar(self, carType: int) -> bool:
        if self.available_slots[carType] > 0:
            self.available_slots[carType] -= 1
            return True

        return False
