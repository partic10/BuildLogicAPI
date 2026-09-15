"""
System Routes - API endpoints for system operations
Health checks, version info, and general system endpoints
"""

from flask import Blueprint, jsonify, current_app

system_bp = Blueprint('system', __name__)

@system_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Build Logic API',
        'version': '1.0.0',
        'platform': 'Windows'
    }), 200

@system_bp.route('/version', methods=['GET'])
def get_version():
    """Get API version"""
    return jsonify({
        'version': '1.0.0',
        'name': 'Build Logic API',
        'description': 'Windows API for Build Logic Roblox game',
        'grid_size': current_app.config['GRID_SIZE']
    }), 200

@system_bp.route('/info', methods=['GET'])
def get_info():
    """Get API information"""
    return jsonify({
        'status': 'success',
        'service': 'Build Logic API',
        'version': '1.0.0',
        'description': 'API for Build Logic Roblox game with 16x16 grid panel support',
        'features': [
            'Logic gate operations (AND, OR, NOT, XOR, NAND, NOR, XNOR)',
            '16x16 grid management',
            'Real-time grid state updates',
            'Operation history tracking',
            'Grid import/export functionality'
        ],
        'endpoints': {
            'grid': '/grid',
            'logic': '/logic',
            'health': '/health'
        },
        'grid_size': current_app.config['GRID_SIZE']
    }), 200

@system_bp.route('/endpoints', methods=['GET'])
def list_endpoints():
    """List all available endpoints"""
    endpoints = {
        'system': {
            'GET /health': 'Health check',
            'GET /version': 'Get API version',
            'GET /info': 'Get API information',
            'GET /endpoints': 'List all endpoints'
        },
        'grid': {
            'GET /grid': 'Get current grid state',
            'POST /grid/cell/<x>/<y>': 'Set a cell value',
            'GET /grid/cell/<x>/<y>': 'Get a cell value',
            'POST /grid/cell/<x>/<y>/toggle': 'Toggle a cell',
            'GET /grid/row/<row>': 'Get entire row',
            'POST /grid/row/<row>': 'Set entire row',
            'GET /grid/column/<col>': 'Get entire column',
            'POST /grid/reset': 'Reset grid to zeros',
            'POST /grid/fill': 'Fill rectangular area',
            'GET /grid/stats': 'Get grid statistics',
            'GET /grid/export': 'Export grid as JSON',
            'POST /grid/import': 'Import grid from JSON',
            'GET /grid/history': 'Get operation history',
            'POST /grid/history/clear': 'Clear history'
        },
        'logic': {
            'POST /logic/and': 'AND gate operation',
            'POST /logic/or': 'OR gate operation',
            'POST /logic/not': 'NOT gate operation',
            'POST /logic/xor': 'XOR gate operation',
            'POST /logic/nand': 'NAND gate operation',
            'POST /logic/nor': 'NOR gate operation',
            'POST /logic/xnor': 'XNOR gate operation',
            'POST /logic/buffer': 'Buffer gate operation',
            'GET /logic/truth-table/<operation>': 'Get truth table',
            'POST /logic/analyze': 'Analyze any operation'
        }
    }
    
    return jsonify({
        'status': 'success',
        'endpoints': endpoints
    }), 200

@system_bp.route('/', methods=['GET'])
def root():
    """Root endpoint - welcome message"""
    return jsonify({
        'status': 'success',
        'message': 'Welcome to Build Logic API',
        'version': '1.0.0',
        'documentation': '/endpoints',
        'health': '/health'
    }), 200
