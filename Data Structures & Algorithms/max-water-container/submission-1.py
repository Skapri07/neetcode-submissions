class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = []
        i = 0
        j = len(heights) - 1
        while(j > i):
            width = j - i
            minimum = min(heights[i], heights[j])
            num = width * minimum
            result.append(num)
            if(heights[i] > heights[j]):
                j = j - 1
            else:
                i += 1
        return max(result)