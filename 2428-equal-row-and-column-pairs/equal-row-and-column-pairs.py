class Solution(object):
  def equalPairs(self,grid):
    n = len(grid)
    count = 0
    
    row_map = {}
    for row in grid:
        row_tuple = tuple(row) 
        row_map[row_tuple] = row_map.get(row_tuple, 0) + 1
 
    for col in range(n):
        col_tuple = tuple(grid[row][col] for row in range(n))
        if col_tuple in row_map:
            count += row_map[col_tuple] 
    return count
