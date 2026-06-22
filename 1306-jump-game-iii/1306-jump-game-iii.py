class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        from collections import deque
        n = len(arr)
        queue = deque([start])
        visited = set([start])

        while queue:
            i = queue.popleft()

            if arr[i] == 0:
                return True

            for next_i in (i + arr[i], i - arr[i]):
                if 0 <= next_i < n and next_i not in visited:
                    visited.add(next_i)
                    queue.append(next_i)

        return False
        