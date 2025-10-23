# Enhanced Gemini solution using enhanced_gemini_chain_of_thought (Attempt 2/3)
# Dataset: Enhanced
# Problem: APPS/1
# Difficulty: Enhanced

from typing import List
from collections import deque

def shortest_path_with_obstacles(grid, k):
    rows = len(grid)
    cols = len(grid[0])
    
    # Find start and end positions
    start_row = start_col = end_row = end_col = -1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                start_row, start_col = r, c
            elif grid[r][c] == 3:
                end_row, end_col = r, c
    
    # BFS with state (row, col, obstacles_removed, steps)
    queue = deque([(start_row, start_col, 0, 0)])
    visited = set()
    visited.add((start_row, start_col, 0))
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        r, c, obstacles_removed, steps = queue.popleft()
        
        # Check if we reached the end
        if r == end_row and c == end_col:
            return steps
        
        # Try all 4 directions
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            
            # Check bounds
            if 0 <= new_r < rows and 0 <= new_c < cols:
                new_obstacles_removed = obstacles_removed
                
                # If it's an obstacle, increment count
                if grid[new_r][new_c] == 1:
                    new_obstacles_removed += 1
                
                # Check if we can still remove obstacles and haven't visited this state
                if new_obstacles_removed <= k:
                    state = (new_r, new_c, new_obstacles_removed)
                    if state not in visited:
                        visited.add(state)
                        queue.append((new_r, new_c, new_obstacles_removed, steps + 1))
    
    return -1