class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        # - float conversion trims digits before
        # - avg incorrect, incorrect condition
        # avg = (max(salary)+ min(salary))//2
        # print(f"{avg=}, {max(salary)}, {min(salary)}")
        # return avg
        # mins = min(salary)
        # maxs = max(salary)
        # salary.pop(salary.index(mins))
        # salary.pop(salary.index(maxs))
        # sums = sum(salary)
        # avg = sums/len(salary)-2
        # return float(avg)
        return ((sum(salary) - max(salary) - min(salary)) * 1.0) / (len(salary) - 2)


if __name__ == "__main__":
    assert Solution().average([4000, 3000, 1000, 2000]) == 2500.00000
    assert Solution().average([1000, 2000, 3000]) == 2000.00000
    assert Solution().average([8000, 9000, 2000, 3000, 6000, 1000]) == 4750.00000
