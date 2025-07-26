[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Packaged with PyInstaller](https://img.shields.io/badge/Packaged_with-PyInstaller-orange.svg)](https://pyinstaller.org/)


# PriceSnipr  
*Multi‑store price tracker & notifier*

**PriceSnipr** helps you search product prices across Amazon, Walmart, Best Buy, eBay, and more—set watch alerts, translate listings, view history, and toggle dark mode, all from a single executable. This Python program, called PriceSnipr, is a desktop application built with Tkinterthat lets users search for products using Google Shopping via the SerpAPI. Users can filter results by store, sort by price or popularity, and translate product info into other languages. The app displays search results with images, prices, and store names, and users can click images to open product links. It also includes a watchlist feature where users can set price alerts; when a product drops below the target price, a desktop notification is triggered and logged in the history. The app supports light/dark themes, remembers user data between sessions using a JSON file, and uses Google Translate, PIL, and Plyer for translation, image handling, and notifications.

---

## Key Features

- **Multi‑Store Search**  
  Search products across Amazon, Walmart, Best Buy, Target, GameStop, and more using SerpAPI.

- **Watchlist & Desktop Alerts**  
  Add items to a watchlist, set a price target, and get a desktop notification when the current price meets your criteria.

- **Language Translation**  
  Translate product descriptions into Spanish, French, German, or Chinese using `googletrans`.

- **Dark Mode Toggle**  
  Instantly switch between light and dark UI themes.

- **Persistent Storage**  
  Automatically saves watchlist and alert history to a local JSON file.

- **Image Previews and Clickable Links**  
  Product thumbnails open product pages in the browser.

- **Standalone Executable**  
  Includes support for packaging into a `.exe` file for Windows users without Python.

---

## Using the Pre-Built Executable (Windows)

1. Download and unzip `PriceSnipr.zip`, which contains:
   - `PriceSnipr.exe`
   - `watchlist.json`
   - `PriceSnipr_Logo.png`

2. Double-click `PriceSnipr.exe` to launch the app.

No Python installation required.

---

## How to Run from Source

### Method 1: Run in PyCharm

1. Open the project in PyCharm.
2. Run the `PriceSnipr.py` script.
3. The GUI should appear.

### Method 2: Run from Terminal (Python 3.12+ Required)

1. Open terminal or command prompt.
2. Navigate to the project directory:
      ```bash
   cd path/to/PriceSnipr

# Install dependencies:
  ```bash
pip install -r requirements.txt

# Run the script: 
     ```bash
python PriceSnipr.py

---

##  Usage Examples

**Basic Search**  
1. Enter **Nintendo Switch** in the **Product Name** field.  
2. Select **All** stores.  
3. Sort by **Lowest Price**.  
4. Click **Search**.

**Set a Watch Alert**  
1. Click the **☆** next to a product listing.  
2. Enter your target price (e.g. `$299.00`).  
3. Receive a desktop notification when price ≤ target.

**View & Manage History**  
- Switch to the **Watchlist** tab.  
- See current watches and past alerts.  
- Click **Remove Selected** or **Clear History** to manage entries.

**Dark Mode**  
Click the **Dark Mode** button to switch themes instantly.

---
#  Testing
- Run all tests (via pytest)
   ```bash
   pytest test/
   
- Test coverage includes:

- Price parsing logic (e.g. "$1,234.56" → 1234.56)

- Watchlist loading and persistence

- Notification logic

- Sorting filters



---

# python -m PyInstaller \
  --onefile \
  --windowed \
  --icon=PriceSnipr_Logo.ico \
  --add-data "watchlist.json;." \

##  Project Structure

--PriceSnipr.py \
--requirements.txt \
--watchlist.json \
--PriceSnipr_Logo.png \
--PriceSnipr_Logo.ico \
--dist/                 ← packaged EXE + assets \
-- build/                ← PyInstaller build artifacts \
-- README.md


  ---

  #  Team & Credits
  
- CS 3300‑001 Summer 2025
- Team 10: Rafael Rojero
- Advisor: Dr. Armin Moin | TA: Himon Thakur

---

# License
This project is licensed under the MIT License.

You are free to use, copy, modify, and distribute this software with attribution.



