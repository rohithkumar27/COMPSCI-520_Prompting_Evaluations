# Gemini solution using chain_of_thought (Attempt 1/3)
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

    rows = len(grid)
    cols = len(grid[0])

    start_row, start_col = -1, -1
    end_row, end_col = -1, -1

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                start_row, start_col = r, c
            elif grid[r][c] == 3:
                end_row, end_col = r, c

    # State: (row, col, obstacles_removed)
    # We use a set to keep track of visited states to avoid cycles and redundant computations.
    # A state is defined by (row, col, obstacles_removed) because reaching the same cell
    # with a different number of obstacles removed might lead to a shorter path later.
    visited = set()

    # Queue for BFS: (row, col, obstacles_removed, steps)
    queue = deque([(start_row, start_col, 0, 0)])
    visited.add((start_row, start_col, 0))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c, obstacles_removed, steps = queue.popleft()

        if r == end_row and c == end_col:
            return steps

        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc

            # Check if the new position is within the grid boundaries
            if 0 <= new_r < rows and 0 <= new_c < cols:
                new_obstacles_removed = obstacles_removed

                # If it's an obstacle, increment the count of obstacles removed
                if grid[new_r][new_c] == 1:
                    new_obstacles_removed += 1

                # Check if we can still remove obstacles and if this state has not been visited
                if new_obstacles_removed <= k:
                    if (new_r, new_c, new_obstacles_removed) not in visited:
                        visited.add((new_r, new_c, new_obstacles_removed))
                        queue.append((new_r, new_c, new_obstacles_removed, steps + 1))

    # If the queue becomes empty and we haven't reached the end, it's impossible
    return -1