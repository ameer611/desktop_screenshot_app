﻿# Simple Screenshot App

## Overview
This is a lightweight Python application that allows you to take screenshots quickly using a simple graphical user interface (GUI). The app uses PyAutoGUI to capture screenshots and Tkinter to create the interface.

## Features
- Capture full screen screenshots with a single click
- Automatically save screenshots with a timestamp filename
- Simple, intuitive interface
- Ability to quit the application easily

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.12
- PyAutoGUI
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/screenshot-app.git
cd screenshot-app
```

2. Install required dependencies:
```bash
pip install pyautogui
```

3. Create a screenshots directory in the project folder:
```bash
mkdir screenshots
```

## Usage

Run the application:
```bash
python screenshot_app.py
```

### Interface
- **Take Screenshot**: Click the "Take Screenshot" button to capture the entire screen
- **Quit**: Click the "Quit" button to close the application

## How It Works
- When you click "Take Screenshot", the app:
  - Generates a unique timestamp-based filename
  - Saves the screenshot in the `screenshots` directory
  - Immediately displays the captured screenshot

## Configuration
- To change the screenshot save location, modify the `title` variable in the `screenshot_the_display()` function
- Uncomment and modify the alternative file path if needed

## Dependencies
- PyAutoGUI: Screen capture and manipulation
- Tkinter: Creating the graphical user interface

## Notes
- Ensure you have write permissions in the screenshots directory
- The app captures the entire screen at the moment of clicking the button

## License
[Insert your license here - e.g., MIT, Apache, etc.]

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Author
[Mukhammad Usmonov]
