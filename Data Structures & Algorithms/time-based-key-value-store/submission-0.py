class TimeMap:

    def __init__(self):
        self.ds = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ds[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        array = self.ds[key]
        res = ""
        for val, t in array:
            if t <= timestamp:
                res = val
            else:
                break
        return res