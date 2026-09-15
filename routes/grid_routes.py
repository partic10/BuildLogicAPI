"""
Grid Routes - API endpoints for grid operations
REST endpoints for managing the 16x16 grid panel
"""

from flask import Blueprint, request, jsonify, current_app

grid_bp = Blueprint('grid', __name__)

@grid_bp.route('', methods=['GET'])
def get_grid():
    """Get current grid state"""
    grid_data = current_app.grid_manager.get_grid()
    stats = current_app.grid_manager.get_stats()
    
    return jsonify({
        'status': 'success',
        'grid': grid_data,
        'stats': stats
    }), 200

@grid_bp.route('/cell/<int:x>/<int:y>', methods=['GET'])
def get_cell(x, y):
    """Get value of a specific cell"""
    value = current_app.grid_manager.get_cell(x, y)
    
    if value == -1:
        return jsonify({
            'status': 'error',
            'message': f'Invalid coordinates: ({x}, {y})'
        }), 400
    
    return jsonify({
        'status': 'success',
        'x': x,
        'y': y,
        'value': value
    }), 200

@grid_bp.route('/cell/<int:x>/<int:y>', methods=['POST'])
def set_cell(x, y):
    """Set a cell value"""
    data = request.get_json()
    
    if not data or 'value' not in data:
        return jsonify({
            'status': 'error',
            'message': 'Missing "value" in request body'
        }), 400
    
    success = current_app.grid_manager.set_cell(x, y, data['value'])
    
    if not success:
        return jsonify({
            'status': 'error',
            'message': f'Invalid coordinates: ({x}, {y})'
        }), 400
    
    return jsonify({
        'status': 'success',
        'message': f'Cell ({x}, {y}) set to {data["value"]}',
        'x': x,
        'y': y,
        'value': current_app.grid_manager.get_cell(x, y)
    }), 200

@grid_bp.route('/cell/<int:x>/<int:y>/toggle', methods=['POST'])
def toggle_cell(x, y):
    """Toggle a cell between 0 and 1"""
    success = current_app.grid_manager.toggle_cell(x, y)
    
    if not success:
        return jsonify({
            'status': 'error',
            'message': f'Invalid coordinates: ({x}, {y})'
        }), 400
    
    new_value = current_app.grid_manager.get_cell(x, y)
    
    return jsonify({
        'status': 'success',
        'message': f'Cell ({x}, {y}) toggled to {new_value}',
        'x': x,
        'y': y,
        'value': new_value
    }), 200

@grid_bp.route('/row/<int:row>', methods=['GET'])
def get_row(row):
    """Get entire row"""
    grid = current_app.grid_manager.get_grid()
    
    if row < 0 or row >= len(grid):
        return jsonify({
            'status': 'error',
            'message': f'Invalid row: {row}'
        }), 400
    
    return jsonify({
        'status': 'success',
        'row': row,
        'values': grid[row]
    }), 200

@grid_bp.route('/row/<int:row>', methods=['POST'])
def set_row(row):
    """Set entire row"""
    data = request.get_json()
    
    if not data or 'values' not in data:
        return jsonify({
            'status': 'error',
            'message': 'Missing "values" in request body'
        }), 400
    
    success = current_app.grid_manager.set_row(row, data['values'])
    
    if not success:
        return jsonify({
            'status': 'error',
            'message': f'Invalid row or values length'
        }), 400
    
    return jsonify({
        'status': 'success',
        'message': f'Row {row} updated',
        'row': row
    }), 200

@grid_bp.route('/column/<int:col>', methods=['GET'])
def get_column(col):
    """Get entire column"""
    grid = current_app.grid_manager.get_grid()
    
    if col < 0 or col >= len(grid[0]):
        return jsonify({
            'status': 'error',
            'message': f'Invalid column: {col}'
        }), 400
    
    column_values = [row[col] for row in grid]
    
    return jsonify({
        'status': 'success',
        'column': col,
        'values': column_values
    }), 200

@grid_bp.route('/reset', methods=['POST'])
def reset_grid():
    """Reset entire grid to zeros"""
    current_app.grid_manager.reset()
    
    return jsonify({
        'status': 'success',
        'message': 'Grid reset to all zeros',
        'grid': current_app.grid_manager.get_grid()
    }), 200

@grid_bp.route('/fill', methods=['POST'])
def fill_area():
    """Fill a rectangular area"""
    data = request.get_json()
    
    required_fields = ['x1', 'y1', 'x2', 'y2', 'value']
    if not data or not all(field in data for field in required_fields):
        return jsonify({
            'status': 'error',
            'message': f'Missing required fields: {required_fields}'
        }), 400
    
    success = current_app.grid_manager.fill_area(
        data['x1'], data['y1'],
        data['x2'], data['y2'],
        data['value']
    )
    
    if not success:
        return jsonify({
            'status': 'error',
            'message': 'Invalid coordinates for fill operation'
        }), 400
    
    return jsonify({
        'status': 'success',
        'message': 'Area filled successfully'
    }), 200

@grid_bp.route('/stats', methods=['GET'])
def get_stats():
    """Get grid statistics"""
    stats = current_app.grid_manager.get_stats()
    
    return jsonify({
        'status': 'success',
        'stats': stats
    }), 200

@grid_bp.route('/export', methods=['GET'])
def export_grid():
    """Export grid as JSON"""
    data = current_app.grid_manager.export_json()
    
    return jsonify({
        'status': 'success',
        'data': data
    }), 200

@grid_bp.route('/import', methods=['POST'])
def import_grid():
    """Import grid from JSON"""
    data = request.get_json()
    
    if not data:
        return jsonify({
            'status': 'error',
            'message': 'Missing request body'
        }), 400
    
    success = current_app.grid_manager.import_json(data)
    
    if not success:
        return jsonify({
            'status': 'error',
            'message': 'Invalid grid data format'
        }), 400
    
    return jsonify({
        'status': 'success',
        'message': 'Grid imported successfully',
        'grid': current_app.grid_manager.get_grid()
    }), 200

@grid_bp.route('/history', methods=['GET'])
def get_history():
    """Get operation history"""
    history = current_app.grid_manager.get_history()
    
    return jsonify({
        'status': 'success',
        'history_length': len(history),
        'history': history[-20:]  # Last 20 operations
    }), 200

@grid_bp.route('/history/clear', methods=['POST'])
def clear_history():
    """Clear operation history"""
    current_app.grid_manager.clear_history()
    
    return jsonify({
        'status': 'success',
        'message': 'History cleared'
    }), 200
