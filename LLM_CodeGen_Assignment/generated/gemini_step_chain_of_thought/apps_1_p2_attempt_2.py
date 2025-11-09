from typing import List
# Gemini solution using step_chain_of_thought (Attempt 2/3)
# Dataset: Unknown
# Problem: APPS/1
# Difficulty: Hard

def shortest_path_with_obstacles(grid: List[List[int]], k: int) -> int:
    '''
    You are given a grid of size N x M where:
    - 0 represents an empty cell
    - 1 represents an obstacle
    - 2 represents the start position
    - 3 represents the end position
    
    You can move in 4 directions (up, down, left, right).
    However, you have a special ability: you can remove at most K obstacles during your journey.
    
    Find the shortest path from start to end, considering you can remove at most K obstacles.
    Return the minimum number of steps, or -1 if impossible.
    
    Parameters:
    - grid: 2D list representing the grid
    - k: maximum number of obstacles you can remove
    
    Example:
    grid = [[2, 1, 0, 0],
            [0, 1, 1, 0], 
            [0, 0, 1, 3]]
    k = 1
    
    Without removing obstacles: impossible
    With removing 1 obstacle: can reach in 5 steps
    '''

    rows, cols = len(grid), len(grid[0])

    # Find start and end positions
    start_row, start_col = -1, -1
    end_row, end_col = -1, -1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                start_row, start_col = r, c
            elif grid[r][c] == 3:
                end_row, end_col = r, c

    # State: (row, col, obstacles_removed)
    # We use a queue for BFS
    queue = collections.deque([(start_row, start_col, 0, 0)])  # (row, col, obstacles_removed, steps)

    # Visited set to avoid cycles and redundant computations.
    # The state includes the number of obstacles removed, as reaching the same cell
    # with fewer obstacles removed is always better.
    visited = set([(start_row, start_col, 0)])

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c, obstacles_removed, steps = queue.popleft()

        # If we reached the end
        if r == end_row and c == end_col:
            return steps

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check if the new position is within grid bounds
            if 0 <= nr < rows and 0 <= nc < cols:
                new_obstacles_removed = obstacles_removed

                # If it's an obstacle
                if grid[nr][nc] == 1:
                    new_obstacles_removed += 1

                # If we can still remove obstacles and haven't visited this state before
                if new_obstacles_removed <= k and (nr, nc, new_obstacles_removed) not in visited:
                    visited.add((nr, nc, new_obstacles_removed))
                    queue.append((nr, nc, new_obstacles_removed, steps + 1))

    # If the queue is empty and we haven't reached the end, it's impossible
    return -1