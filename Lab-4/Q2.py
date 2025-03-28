class TargetSum:
    def __init__(self, numbers: list[int], target: int):
        self.numbers = numbers
        self.target = target

    def compute_indices(self) -> tuple[int, int]:
        for i in range(len(self.numbers)):
            delta = self.target - self.numbers[i]

            if delta in self.numbers:
                return i, self.numbers.index(delta)

        return -1, -1
