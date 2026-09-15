# Build Logic API - Comprehensive Documentation

## Table of Contents
1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Grid Operations](#grid-operations)
4. [Logic Gates](#logic-gates)
5. [Examples](#examples)
6. [API Reference](#api-reference)

## Installation

### Prerequisites
- Windows 10 or higher
- Python 3.9+
- pip (Python package manager)

### Setup Steps

```bash
# Clone the repository
git clone https://github.com/partic10/BuildLogicAPI.git
cd BuildLogicAPI

# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py
```

The API will start on `http://localhost:5000`

## Quick Start

### Starting the Server

```bash
python main.py
```

Expected output:
```
==================================================
Build Logic API - Windows Edition
==================================================
Starting server on http://127.0.0.1:5000
Grid Size: 16x16
==================================================
```

### Testing the API

Using curl:
```bash
# Health check
curl http://localhost:5000/health

# Get grid
curl http://localhost:5000/grid

# Set a cell
curl -X POST http://localhost:5000/grid/cell/5/5 \
  -H "Content-Type: application/json" \
  -d '{"value": 1}'
```

## Grid Operations

### Get Current Grid

```
GET /grid
```

Response:
```json
{
  "status": "success",
  "grid": [
    [0, 0, 0, ..., 0],
    [0, 0, 0, ..., 0],
    ...
  ],
  "stats": {
    "size": 16,
    "total_cells": 256,
    "active_cells": 0,
    "inactive_cells": 256,
    "activation_rate": 0.0,
    "history_length": 0
  }
}
```

### Set Cell Value

```
POST /grid/cell/<x>/<y>
Content-Type: application/json

{
  "value": 1
}
```

Example:
```bash
curl -X POST http://localhost:5000/grid/cell/5/5 \
  -H "Content-Type: application/json" \
  -d '{"value": 1}'
```

### Get Cell Value

```
GET /grid/cell/<x>/<y>
```

### Toggle Cell

```
POST /grid/cell/<x>/<y>/toggle
```

Toggles between 0 and 1.

### Get Row

```
GET /grid/row/<row_number>
```

### Set Row

```
POST /grid/row/<row_number>
Content-Type: application/json

{
  "values": [0, 1, 0, 1, ...]
}
```

### Fill Area

```
POST /grid/fill
Content-Type: application/json

{
  "x1": 0,
  "y1": 0,
  "x2": 5,
  "y2": 5,
  "value": 1
}
```

### Reset Grid

```
POST /grid/reset
```

Clears all cells to 0.

### Grid Statistics

```
GET /grid/stats
```

Returns activation rate and cell counts.

### Export/Import Grid

**Export:**
```
GET /grid/export
```

**Import:**
```
POST /grid/import
Content-Type: application/json

{
  "grid": [
    [0, 1, 0, ...],
    [1, 0, 1, ...],
    ...
  ]
}
```

## Logic Gates

### AND Gate

```
POST /logic/and
Content-Type: application/json

{
  "inputs": [1, 1]
}
```

Returns: `{"output": 1}`

### OR Gate

```
POST /logic/or
Content-Type: application/json

{
  "inputs": [1, 0]
}
```

Returns: `{"output": 1}`

### NOT Gate

```
POST /logic/not
Content-Type: application/json

{
  "input": 1
}
```

Returns: `{"output": 0}`

### XOR Gate

```
POST /logic/xor
Content-Type: application/json

{
  "inputs": [1, 0]
}
```

Returns: `{"output": 1}`

### NAND Gate

```
POST /logic/nand
Content-Type: application/json

{
  "inputs": [1, 1]
}
```

Returns: `{"output": 0}`

### NOR Gate

```
POST /logic/nor
Content-Type: application/json

{
  "inputs": [0, 0]
}
```

Returns: `{"output": 1}`

### XNOR Gate

```
POST /logic/xnor
Content-Type: application/json

{
  "inputs": [1, 1]
}
```

Returns: `{"output": 1}`

### Buffer Gate

```
POST /logic/buffer
Content-Type: application/json

{
  "input": 1
}
```

Returns: `{"output": 1}`

### Truth Tables

Get a truth table for any logic operation:

```
GET /logic/truth-table/AND?inputs=2
GET /logic/truth-table/OR?inputs=2
GET /logic/truth-table/XOR?inputs=2
```

## Examples

### Python Client Example

```python
from examples.client import BuildLogicClient

# Initialize client
client = BuildLogicClient('http://localhost:5000')

# Get grid state
grid = client.get_grid()
print(f"Active cells: {grid['stats']['active_cells']}")

# Set cells
client.set_cell(0, 0, 1)
client.set_cell(1, 1, 1)

# Logic operations
result_and = client.and_gate([1, 1])
print(f"AND(1, 1) = {result_and['output']}")

result_or = client.or_gate([1, 0])
print(f"OR(1, 0) = {result_or['output']}")

# Fill area
client.fill_area(0, 0, 5, 5, 1)

# Get statistics
stats = client.get_stats()
print(f"Grid stats: {stats['stats']}")
```

### Bash Example with curl

```bash
# Set multiple cells
curl -X POST http://localhost:5000/grid/cell/0/0 \
  -H "Content-Type: application/json" \
  -d '{"value": 1}'

curl -X POST http://localhost:5000/grid/cell/1/1 \
  -H "Content-Type: application/json" \
  -d '{"value": 1}'

# Test AND gate
curl -X POST http://localhost:5000/logic/and \
  -H "Content-Type: application/json" \
  -d '{"inputs": [1, 1]}'

# Get truth table
curl http://localhost:5000/logic/truth-table/AND?inputs=2
```

## API Reference

### System Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/health` | Health check |
| GET | `/version` | API version |
| GET | `/info` | API information |
| GET | `/endpoints` | List all endpoints |

### Grid Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/grid` | Get grid state |
| GET | `/grid/cell/<x>/<y>` | Get cell value |
| POST | `/grid/cell/<x>/<y>` | Set cell value |
| POST | `/grid/cell/<x>/<y>/toggle` | Toggle cell |
| GET | `/grid/row/<row>` | Get row |
| POST | `/grid/row/<row>` | Set row |
| GET | `/grid/column/<col>` | Get column |
| POST | `/grid/reset` | Reset grid |
| POST | `/grid/fill` | Fill area |
| GET | `/grid/stats` | Get statistics |
| GET | `/grid/export` | Export grid |
| POST | `/grid/import` | Import grid |
| GET | `/grid/history` | Get history |
| POST | `/grid/history/clear` | Clear history |

### Logic Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/logic/and` | AND gate |
| POST | `/logic/or` | OR gate |
| POST | `/logic/not` | NOT gate |
| POST | `/logic/xor` | XOR gate |
| POST | `/logic/nand` | NAND gate |
| POST | `/logic/nor` | NOR gate |
| POST | `/logic/xnor` | XNOR gate |
| POST | `/logic/buffer` | Buffer gate |
| GET | `/logic/truth-table/<op>` | Truth table |
| POST | `/logic/analyze` | Analyze operation |

## Response Format

All responses follow a standard format:

### Success Response
```json
{
  "status": "success",
  "data": {...}
}
```

### Error Response
```json
{
  "status": "error",
  "message": "Error description"
}
```

## Grid Coordinates

- Grid is 16x16 (0-15 for both x and y)
- Origin (0, 0) is at the top-left
- Cell values: 0 (OFF) or 1 (ON)

## Troubleshooting

### Port Already in Use

If port 5000 is already in use:

```bash
# On Windows, find the process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace PID with actual process ID)
taskkill /PID <PID> /F
```

### Import Error

Ensure all dependencies are installed:

```bash
pip install -r requirements.txt
```

### Connection Refused

Make sure the server is running:

```bash
python main.py
```

Check if the server started successfully on `http://localhost:5000`
