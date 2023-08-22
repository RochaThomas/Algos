# morning algos
# neetcode walls and gates

import collections
from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms):
        ROWS, COLS = len(rooms), len(rooms[0])
        q = collections.deque()
        visited = set()

        distance = 0

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        def addRoom(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or rooms[r][c] == -1:
                return
            q.append([r, c])
            visited.add((r, c))

        while q:
            r, c = q.popleft()
            rooms[r][c] = distance
            addRoom(r + 1, c)
            addRoom(r - 1, c)
            addRoom(r, c + 1)
            addRoom(r, c - 1)
            distance += 1



