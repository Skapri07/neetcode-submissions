class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create an empty dictionary, where key is nums and value is count.
        # loop through nums and if num appears then increase the value if seen otherwise just assign one.
        # Create an arrays for output.
            # Go in the max k, and then add key to list, and keep doing until k reaches 0.

        sara = {}
        sagar = []
        for num in nums:
            if num in sara:
                sara[num] += 1
            else:
                sara[num] = 1
        while(k != 0 and sara):
            max_key = max(sara, key = sara.get)
            sagar.append(max_key)
            del sara[max_key]
            k -= 1
        return sagar