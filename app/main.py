class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None
    ) -> None:
        self.weight = weight
        self.name = name
        self.coords = [0, 0] if coords is None else coords

    def go_forward(self, num: int = 1) -> None:
        self.coords[1] += num

    def go_back(self, num: int = 1) -> None:
        self.coords[1] -= num

    def go_right(self, num: int = 1) -> None:
        self.coords[0] += num

    def go_left(self, num: int = 1) -> None:
        self.coords[0] -= num

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.coords = [0, 0, 0] if coords is None else coords

    def go_up(self, num: int = 1) -> None:
        self.coords[2] += num

    def go_down(self, num: int = 1) -> None:
        self.coords[2] -= num


class DeliveryDrone(FlyingRobot):
    def __init__(
            self,
            name: str,
            weight: int,
            max_load_weight: int,
            current_load: bool | int,
            coords: list = None
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load
        self.coords = [0, 0, 0] if coords is None else coords

    def hook_load(self, cargo: Cargo) -> None:
        if not self.current_load and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
