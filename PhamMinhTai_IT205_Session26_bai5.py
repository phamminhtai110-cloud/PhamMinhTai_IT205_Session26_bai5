from abc import ABC, abstractmethod


class Companion(ABC):
    def __init__(self, name, level=1, **kwargs):
        self.name = name
        self.level = level
        super().__init__()

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Chỉ có thể lai tạo 2 sinh vật cùng loài!")

        if isinstance(self, Pet) and not isinstance(self, Dragon):
            return Pet(
                f"{self.name} {other.name}",
                self.bonus_atk + other.bonus_atk,
                self.level + 1
            )

        if isinstance(self, Mount) and not isinstance(self, Dragon):
            return Mount(
                f"{self.name} {other.name}",
                self.bonus_speed + other.bonus_speed,
                self.level + 1
            )

        return Dragon(
            f"{self.name} {other.name}",
            self.bonus_atk + other.bonus_atk,
            self.bonus_speed + other.bonus_speed,
            self.level + 1
        )

    @abstractmethod
    def unleash_skill(self):
        pass


class Pet(Companion):
    def __init__(self, name, bonus_atk, level=1, **kwargs):
        self.bonus_atk = bonus_atk
        super().__init__(name=name, level=level, **kwargs)

    def unleash_skill(self):
        print(
            f">> {self.name}: "
            f"Tấn công kẻ thù, gây {self.bonus_atk} sát thương!"
        )


class Mount(Companion):
    def __init__(self, name, bonus_speed, level=1, **kwargs):
        self.bonus_speed = bonus_speed
        super().__init__(name=name, level=level, **kwargs)

    def unleash_skill(self):
        print(
            f">> {self.name}: "
            f"Tăng tốc độ di chuyển thêm {self.bonus_speed} điểm!"
        )


class Dragon(Pet, Mount):
    def __init__(
        self,
        name,
        bonus_atk,
        bonus_speed,
        level=1
    ):
        super().__init__(
            name=name,
            level=level,
            bonus_atk=bonus_atk,
            bonus_speed=bonus_speed
        )

    def unleash_skill(self):
        print(f">> {self.name} thị uy:")
        print(
            f"   - Tấn công kẻ thù, gây {self.bonus_atk} sát thương!"
        )
        print(
            f"   - Tăng tốc độ di chuyển thêm {self.bonus_speed} điểm!"
        )


if __name__ == "__main__":

    try:
        c = Companion("Test")
    except TypeError as e:
        print("ABC Trap:", e)

    p1 = Pet("Sói Trắng", 50)
    p2 = Pet("Sói Đen", 60)

    p3 = p1 + p2

    print(
        f"\n{p3.name} | "
        f"Level {p3.level} | "
        f"Atk {p3.bonus_atk}"
    )

    m1 = Mount("Ngựa", 10)

    try:
        test = p1 + m1
    except TypeError as e:
        print("\nOperator Trap:", e)

    try:
        test = p1 + 10
    except TypeError as e:
        print("Operator Trap:", e)

    d1 = Dragon(
        "Rồng Lửa",
        bonus_atk=500,
        bonus_speed=200
    )

    print(
        f"\n{d1.name} | "
        f"Atk {d1.bonus_atk} | "
        f"Speed {d1.bonus_speed}"
    )

    equipped = [p3, m1, d1]

    print("\n=== XUẤT CHIẾN ===")

    for companion in equipped:
        companion.unleash_skill()