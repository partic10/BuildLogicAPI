"""
Build Logic API - Python Client Example
Example client for interacting with the Build Logic API
"""

import requests
import json
from typing import List, Dict

class BuildLogicClient:
    """Client for Build Logic API"""
    
    def __init__(self, base_url: str = 'http://localhost:5000'):
        """Initialize client with base URL"""
        self.base_url = base_url
    
    # Grid Operations
    def get_grid(self) -> Dict:
        """Get current grid state"""
        response = requests.get(f'{self.base_url}/grid')
        return response.json()
    
    def set_cell(self, x: int, y: int, value: int) -> Dict:
        """Set a cell value"""
        response = requests.post(
            f'{self.base_url}/grid/cell/{x}/{y}',
            json={'value': value}
        )
        return response.json()
    
    def get_cell(self, x: int, y: int) -> Dict:
        """Get a cell value"""
        response = requests.get(f'{self.base_url}/grid/cell/{x}/{y}')
        return response.json()
    
    def toggle_cell(self, x: int, y: int) -> Dict:
        """Toggle a cell"""
        response = requests.post(f'{self.base_url}/grid/cell/{x}/{y}/toggle')
        return response.json()
    
    def reset_grid(self) -> Dict:
        """Reset entire grid"""
        response = requests.post(f'{self.base_url}/grid/reset')
        return response.json()
    
    def fill_area(self, x1: int, y1: int, x2: int, y2: int, value: int) -> Dict:
        """Fill a rectangular area"""
        response = requests.post(
            f'{self.base_url}/grid/fill',
            json={'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2, 'value': value}
        )
        return response.json()
    
    def get_stats(self) -> Dict:
        """Get grid statistics"""
        response = requests.get(f'{self.base_url}/grid/stats')
        return response.json()
    
    # Logic Operations
    def and_gate(self, inputs: List[int]) -> Dict:
        """AND gate operation"""
        response = requests.post(
            f'{self.base_url}/logic/and',
            json={'inputs': inputs}
        )
        return response.json()
    
    def or_gate(self, inputs: List[int]) -> Dict:
        """OR gate operation"""
        response = requests.post(
            f'{self.base_url}/logic/or',
            json={'inputs': inputs}
        )
        return response.json()
    
    def not_gate(self, input_val: int) -> Dict:
        """NOT gate operation"""
        response = requests.post(
            f'{self.base_url}/logic/not',
            json={'input': input_val}
        )
        return response.json()
    
    def xor_gate(self, inputs: List[int]) -> Dict:
        """XOR gate operation"""
        response = requests.post(
            f'{self.base_url}/logic/xor',
            json={'inputs': inputs}
        )
        return response.json()


if __name__ == '__main__':
    # Example usage
    client = BuildLogicClient()
    
    print('Building Logic API - Client Example')
    print('=' * 40)
    
    # Test health
    print('\nTesting API Health...')
    health = requests.get('http://localhost:5000/health').json()
    print(f'Status: {health["status"]}')
    
    # Get grid
    print('\nGetting Grid State...')
    grid = client.get_grid()
    print(f'Grid size: 16x16')
    print(f'Active cells: {grid["stats"]["active_cells"]}')
    
    # Set a cell
    print('\nSetting cell (5, 5) to 1...')
    result = client.set_cell(5, 5, 1)
    print(f'Result: {result["message"]}')
    
    # Test logic gates
    print('\nTesting Logic Gates...')
    and_result = client.and_gate([1, 1])
    print(f'AND(1, 1) = {and_result["output"]}')
    
    or_result = client.or_gate([0, 1])
    print(f'OR(0, 1) = {or_result["output"]}')
    
    xor_result = client.xor_gate([1, 0])
    print(f'XOR(1, 0) = {xor_result["output"]}')
