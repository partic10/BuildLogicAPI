"""
Grid Manager - 16x16 Panel Logic
Manages the state and operations of the 16x16 grid panel
"""

import numpy as np
from typing import List, Dict, Tuple

class GridManager:
    """Manages 16x16 grid state and operations"""
    
    def __init__(self, size: int = 16):
        """Initialize grid with given size"""
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)
        self.history = []
        
    def get_grid(self) -> List[List[int]]:
        """Get current grid state as list"""
        return self.grid.tolist()
    
    def set_cell(self, x: int, y: int, value: int) -> bool:
        """Set a single cell value"""
        if not self._is_valid_coord(x, y):
            return False
        
        old_value = self.grid[x, y]
        self.grid[x, y] = 1 if value else 0
        
        # Record history
        self.history.append({
            'action': 'set_cell',
            'x': x,
            'y': y,
            'old_value': old_value,
            'new_value': self.grid[x, y]
        })
        
        return True
    
    def get_cell(self, x: int, y: int) -> int:
        """Get value of a single cell"""
        if not self._is_valid_coord(x, y):
            return -1
        return int(self.grid[x, y])
    
    def set_row(self, row: int, values: List[int]) -> bool:
        """Set an entire row"""
        if row < 0 or row >= self.size or len(values) != self.size:
            return False
        
        self.grid[row, :] = [1 if v else 0 for v in values]
        self.history.append({
            'action': 'set_row',
            'row': row,
            'values': values
        })
        return True
    
    def set_column(self, col: int, values: List[int]) -> bool:
        """Set an entire column"""
        if col < 0 or col >= self.size or len(values) != self.size:
            return False
        
        self.grid[:, col] = [1 if v else 0 for v in values]
        self.history.append({
            'action': 'set_column',
            'col': col,
            'values': values
        })
        return True
    
    def reset(self) -> None:
        """Reset entire grid to zeros"""
        self.grid = np.zeros((self.size, self.size), dtype=int)
        self.history.append({'action': 'reset'})
    
    def clear_history(self) -> None:
        """Clear operation history"""
        self.history = []
    
    def get_history(self) -> List[Dict]:
        """Get operation history"""
        return self.history
    
    def get_stats(self) -> Dict:
        """Get grid statistics"""
        total_cells = self.size * self.size
        active_cells = int(np.sum(self.grid))
        inactive_cells = total_cells - active_cells
        
        return {
            'size': self.size,
            'total_cells': total_cells,
            'active_cells': active_cells,
            'inactive_cells': inactive_cells,
            'activation_rate': active_cells / total_cells,
            'history_length': len(self.history)
        }
    
    def export_json(self) -> Dict:
        """Export grid as JSON"""
        return {
            'grid': self.get_grid(),
            'stats': self.get_stats(),
            'history': self.history[-10:]  # Last 10 operations
        }
    
    def import_json(self, data: Dict) -> bool:
        """Import grid from JSON"""
        if 'grid' not in data or len(data['grid']) != self.size:
            return False
        
        for row_idx, row in enumerate(data['grid']):
            if len(row) != self.size:
                return False
            self.set_row(row_idx, row)
        
        return True
    
    def _is_valid_coord(self, x: int, y: int) -> bool:
        """Check if coordinates are valid"""
        return 0 <= x < self.size and 0 <= y < self.size
    
    def fill_area(self, x1: int, y1: int, x2: int, y2: int, value: int) -> bool:
        """Fill a rectangular area with a value"""
        if not (self._is_valid_coord(x1, y1) and self._is_valid_coord(x2, y2)):
            return False
        
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)
        
        self.grid[min_x:max_x+1, min_y:max_y+1] = 1 if value else 0
        
        self.history.append({
            'action': 'fill_area',
            'x1': x1, 'y1': y1,
            'x2': x2, 'y2': y2,
            'value': value
        })
        
        return True
    
    def toggle_cell(self, x: int, y: int) -> bool:
        """Toggle a cell between 0 and 1"""
        if not self._is_valid_coord(x, y):
            return False
        
        self.grid[x, y] = 1 - self.grid[x, y]
        
        self.history.append({
            'action': 'toggle_cell',
            'x': x,
            'y': y,
            'new_value': int(self.grid[x, y])
        })
        
        return True
