[![Build Status](https://github.com/RafaelRoj8/CS_3300_Grp10_Project/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/RafaelRoj8/CS_3300_Grp10_Project/actions)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Packaged with PyInstaller](https://img.shields.io/badge/Packaged_with-PyInstaller-orange.svg)](https://pyinstaller.org/)


# PriceSnipr  
*Multi‑store price tracker & notifier*

**PriceSnipr** helps you search product prices across Amazon, Walmart, Best Buy, eBay, and more—set watch alerts, translate listings, view history, and toggle dark mode, all from a single executable. This Python program, called PriceSnipr, is a desktop application built with Tkinterthat lets users search for products using Google Shopping via the SerpAPI. Users can filter results by store, sort by price or popularity, and translate product info into other languages. The app displays search results with images, prices, and store names, and users can click images to open product links. It also includes a watchlist feature where users can set price alerts; when a product drops below the target price, a desktop notification is triggered and logged in the history. The app supports light/dark themes, remembers user data between sessions using a JSON file, and uses Google Translate, PIL, and Plyer for translation, image handling, and notifications.

---

##  Key Features

- **Multi‑Store Search**  
  Query dozens of merchants via SerpAPI.

- **Watchlist & Desktop Alerts**  
  “☆” a product, set a target price, and get notified when it drops.

- **Dark Mode & Themes**  
  Easy toggle between light and dark for day/night use.

- **Language Translation**  
  Translate product info on the fly (EN ↔ ES, FR, DE, ZH) using `googletrans`.

- **Standalone Packaging**  
  One‑click Windows `.exe` built with PyInstaller—you don’t need Python installed.

---

##  Using the Pre‑built Executable

Unzip **PriceSnipr.zip** (contains `PriceSnipr.exe`, `watchlist.json`, `PriceSnipr_Logo.png`).

Double‑click **PriceSnipr.exe** to launch.

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
- Use pytest to add unit tests for:

- Price parsing logic ("$1,234.56" → 1234.56)

- Sort/filter functions

- Watchlist persistence

  pytest tests/


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
- Team 10: Rafael Rojero, Dylan Lareno
- Advisor: Dr. Armin Moin | TA: Himon Thakur

---

# 📜 License
This project is licensed under the MIT License.



