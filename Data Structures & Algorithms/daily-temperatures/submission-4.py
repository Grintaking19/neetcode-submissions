class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        max_temp = temperatures[-1]
        for i in range(n-1, -1, -1):
            t = temperatures[i]
            if t >= max_temp: max_temp = t
            else:
                i_next = i + 1
                while temperatures[i_next] <= t: i_next += ans[i_next]
                ans[i] = i_next - i
        return ans