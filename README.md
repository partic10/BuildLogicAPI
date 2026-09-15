# Build Logic API

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Platform: Windows](https://img.shields.io/badge/platform-Windows-blue.svg)](WINDOWS_SETUP.md)

A Windows-based REST API for the **Build Logic** Roblox game by Tomtom4500. This API provides logic gate operations and comprehensive 16x16 grid panel management.

## 🎮 About Build Logic

Build Logic is an innovative Roblox sandbox game where players use logic gates and components to build digital circuits and automated systems. This API brings that functionality to Windows with a powerful REST interface.

## ✨ Features

- **🔌 Complete Logic Gates**: AND, OR, NOT, XOR, NAND, NOR, XNOR, Buffer
- **📊 16x16 Grid Panel**: Full grid state management and manipulation
- **🖥️ Windows Native**: Optimized for Windows 10+ with dedicated setup guide
- **⚡ Real-time Updates**: Live panel state synchronization
- **💾 Import/Export**: Save and load grid configurations
- **📜 Operation History**: Track all grid modifications
- **🧮 Truth Tables**: Generate logic operation truth tables
- **🔄 REST API**: Standard HTTP/JSON interface for easy integration

## 🚀 Quick Start

### Installation (Windows)

```bash
# Clone repository
git clone https://github.com/partic10/BuildLogicAPI.git
cd BuildLogicAPI

# Create virtual environment (recommended)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py
```

Server starts on `http://localhost:5000`

For detailed Windows setup, see [WINDOWS_SETUP.md](WINDOWS_SETUP.md)

### First API Call

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

## 📚 Documentation

- **[DOCUMENTATION.md](DOCUMENTATION.md)** - Complete API reference and usage guide
- **[WINDOWS_SETUP.md](WINDOWS_SETUP.md)** - Windows-specific installation and troubleshooting
- **[examples/README.md](examples/README.md)** - Code examples and usage patterns

## 🔌 API Endpoints

### Grid Operations
```
GET  /grid                      - Get grid state
POST /grid/cell/<x>/<y>         - Set cell value
GET  /grid/cell/<x>/<y>         - Get cell value
POST /grid/cell/<x>/<y>/toggle  - Toggle cell
POST /grid/reset                - Clear all cells
POST /grid/fill                 - Fill rectangular area
GET  /grid/stats                - Get statistics
GET  /grid/export               - Export as JSON
POST /grid/import               - Import from JSON
```

### Logic Gates
```
POST /logic/and                 - AND operation
POST /logic/or                  - OR operation
POST /logic/not                 - NOT operation
POST /logic/xor                 - XOR operation
POST /logic/nand                - NAND operation
POST /logic/nor                 - NOR operation
POST /logic/xnor                - XNOR operation
POST /logic/buffer              - Buffer operation
GET  /logic/truth-table/<op>    - Get truth table
```

### System
```
GET  /                          - Welcome
GET  /health                    - Health check
GET  /version                   - API version
GET  /endpoints                 - List endpoints
```

## 💻 Python Client Example

```python
from examples.client import BuildLogicClient

# Initialize
client = BuildLogicClient('http://localhost:5000')

# Grid operations
grid = client.get_grid()
client.set_cell(5, 5, 1)
client.fill_area(0, 0, 7, 7, 1)

# Logic gates
and_result = client.and_gate([1, 1])      # Output: 1
or_result = client.or_gate([1, 0])        # Output: 1
xor_result = client.xor_gate([1, 0])      # Output: 1

# Statistics
stats = client.get_stats()
print(f"Active cells: {stats['stats']['active_cells']}")
```

## 🎯 Grid Specification

- **Size**: 16x16 cells
- **Cell Values**: 0 (OFF) or 1 (ON)
- **Coordinates**: (0,0) at top-left to (15,15) at bottom-right
- **Storage**: In-memory with operation history

## 🛠️ Technical Stack

- **Framework**: Flask 2.3.2
- **Language**: Python 3.9+
- **Platform**: Windows 10+
- **API Style**: REST/JSON
- **Dependencies**: NumPy, Flask-CORS, python-dotenv

## 📋 Requirements

```
Flask==2.3.2
Flask-CORS==4.0.0
numpy==1.24.3
requests==2.31.0
python-dotenv==1.0.0
Werkzeug==2.3.6
```

## 🚨 Troubleshooting

### Port 5000 already in use
```powershell
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Import errors
```bash
pip install -r requirements.txt
```

### "python" not found
Ensure Python is installed and added to PATH. Download from [python.org](https://www.python.org/downloads/)

See [WINDOWS_SETUP.md](WINDOWS_SETUP.md) for more troubleshooting.

## 📦 Project Structure

```
BuildLogicAPI/
├── main.py                 # Entry point
├── app.py                  # Flask app factory
├── core/
│   ├── grid.py            # Grid manager
│   └── logic_gates.py      # Logic operations
├── routes/
│   ├── grid_routes.py      # Grid endpoints
│   ├── logic_routes.py     # Logic endpoints
│   └── system_routes.py    # System endpoints
├── examples/
│   ├── client.py           # Python client
│   └── README.md           # Examples guide
├── requirements.txt        # Dependencies
├── DOCUMENTATION.md        # Full API docs
├── WINDOWS_SETUP.md        # Setup guide
└── LICENSE                 # MIT License
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, fork the repository, and create pull requests.

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Credits

- **Tomtom4500** - Creator of Build Logic (Roblox game)
- Build Logic API - Windows REST API implementation

## 🔗 Links

- 🎮 [Play Build Logic on Roblox](https://www.roblox.com/games/9527099245/Build-Logic)
- 📚 [Full Documentation](DOCUMENTATION.md)
- 🖥️ [Windows Setup Guide](WINDOWS_SETUP.md)
- 💻 [Python Examples](examples/README.md)

---

**Made with ❤️ for the Build Logic community**

Have fun building! 🚀
