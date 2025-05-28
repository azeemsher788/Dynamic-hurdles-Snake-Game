# Snake Game

A classic Snake game implemented in Python using the Turtle graphics library.

## Prerequisites

- Python 3.x
- Tkinter (Python's standard GUI package)
- Pandas library

## Installation

### Automatic Setup

#### For Linux/macOS:

1. Open a terminal in this directory
2. Make the setup script executable:
   ```bash
   chmod +x setup.sh
   ```
3. Run the setup script:
   ```bash
   ./setup.sh
   ```

#### For Windows:

1. Open Command Prompt in this directory
2. Run the setup script:
   ```cmd
   setup.bat
   ```

### Manual Setup

If the automatic setup doesn't work for you, follow these steps:

1. Install tkinter (system dependency):
   - **Debian/Ubuntu**: `sudo apt-get install python3-tk`
   - **Fedora**: `sudo dnf install python3-tkinter`
   - **macOS** (with Homebrew): `brew install python-tk`
   - **Windows**: Tkinter is included with the standard Python installation. If it's missing, reinstall Python and make sure to check the option to install tcl/tk and IDLE during installation.

2. Install Python package dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

To start the game, run:

```bash
python main.py
```

## Game Controls

- **Up Arrow**: Move the snake up
- **Down Arrow**: Move the snake down
- **Left Arrow**: Move the snake left
- **Right Arrow**: Move the snake right
- **P**: Pause the game
- **B**: Toggle boundaries

## Troubleshooting

If you encounter the error:
```
ModuleNotFoundError: No module named 'tkinter'
ImportError: No module named 'tkinter', please install the python3-tk package
```

Follow the installation instructions above to install the tkinter package for your operating system.

For other issues, refer to the main project README.md file or open an issue on the project repository.