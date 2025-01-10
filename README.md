# FL Studio Rich Presence (FLRPC)

A Python program that integrates FL Studio with Discord Rich Presence, showing your current project, FL Studio version, and other session details in your Discord status.

## Features

- Displays the active FL Studio project name.
- Shows the FL Studio version in use.
- Updates Rich Presence dynamically as you switch projects.
- Automatically disconnects if FL Studio is closed.

## Requirements

- Python 3.6 or higher
- Required Python libraries:
  - `psutil`
  - `pygetwindow`
  - `pypresence`

Install dependencies using:
```bash
pip install psutil pygetwindow pypresence
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/odinong/FLRPC.git
   cd FLRPC
   ```

2. Run the program:
   ```bash
   python flrpc.py
   ```

5. Open FL Studio, and your Discord status will update with the project name and FL Studio version.

## How It Works

- The script uses `psutil` to detect the FL Studio process.
- `pygetwindow` extracts the window title to determine the project name and version.
- `pypresence` updates Discord Rich Presence with this information.

## Known Issues

- May not work if the FL Studio window title format changes.
- Ensure FL Studio is running before starting the script.

## Credits

- Developed by [@trix9x](https://github.com/odinong).

## License

This project is open-source under the MIT License.

