# Quran Viewer

#### Video Demo: <URL HERE>

#### Description:
Quran Viewer is a Python-based graphical application designed to provide an interactive way to explore and engage with the Quran. The application leverages open-source JSON data to present the Quran's text, chapter translations, and other features. This project aims to make Quranic study more accessible through intuitive navigation, powerful search capabilities, and user-friendly design.

## Features

- **View Quranic Chapters and Verses:**
  Navigate through the Quran chapter by chapter and verse by verse, with clear and organized labels displaying the current chapter and verse.

- **Search for Verses:**
  A search feature allows users to find verses containing specific keywords, providing results with chapter and verse references.

- **Bookmark Verses:**
  Users can save their favorite verses for quick access later, with an easy-to-use bookmarking system.

- **Random Verse Display:**
  For inspiration or curiosity, the app can display a random verse from the Quran.

- **View Translations:**
  Each chapter includes a translation summary to aid understanding.

## Project Files and Their Purpose

### `quran_viewer.py`
This is the main Python script containing the application logic. It uses the following key components:

1. **Data Retrieval:**
   - Fetches Quranic data and chapter information from open-source JSON files hosted online.
   - Parses JSON data to provide structured information for display and search.

2. **User Interface:**
   - Built using the `tkinter` library.
   - Provides buttons, labels, and additional windows for features like search, bookmarks, and translations.

3. **Features Implementation:**
   - Navigation controls for chapters and verses.
   - Search functionality with keyword matching across verses.
   - Bookmark management for saving and viewing favorite verses.
   - Random verse selection using Python's `random` module.

4. **Event Handling:**
   - Implements click events for all buttons to update the display or open new windows for additional functionality.

### Data Files
- **`quran.json`**:
  Contains the Quranic text, organized by chapters and verses.

- **`chapters.json`**:
  Provides metadata about each chapter, including names and translations.

These files are fetched dynamically from [risan/quran-json](https://github.com/risan/quran-json), ensuring up-to-date and reliable content.

## Design Choices and Considerations

1. **Why `tkinter` for GUI?**
   - `tkinter` is a standard Python library, meaning no additional installations are required.
   - It provides sufficient functionality for a simple and clean user interface.

2. **JSON Data Source:**
   - The decision to use an open-source Quran JSON repository ensures the app remains lightweight and avoids the need for a local database.

3. **Modular Design:**
   - Features like searching, bookmarking, and random verse display are encapsulated in their respective functions for maintainability and scalability.

4. **Versatility of Use:**
   - Features like random verse display and keyword search were added to cater to a broader audience, including casual readers and serious students.

5. **Simplified Navigation:**
   - The use of buttons for navigation ensures that the app is easy to use, even for individuals unfamiliar with technical software.

## How to Use

1. **Navigation:**
   - Use the `<< Previous Chapter`, `Next Chapter >>`, `<< Previous Verse`, and `Next Verse >>` buttons to move through the Quran.

2. **Search:**
   - Click `Search Verse`, enter a keyword, and view a list of matching verses.

3. **Bookmarking:**
   - Click `Bookmark Verse` to save the current verse. View saved bookmarks via the `View Bookmarks` button.

4. **Random Verse:**
   - Click `Random Verse` to display a random chapter and verse.

5. **Translations:**
   - Click `View Translation` to see the translation of the current chapter.

## Requirements

- Python 3.x
- `tkinter` (usually included with Python)
- `urllib`
- `json`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/quran-viewer.git
   cd quran-viewer
   ```

2. Run the application:

   ```bash
   python quran_viewer.py
   ```

## Data Sources

The app uses the following open-source JSON files:

- Quran data: [quran.json](https://raw.githubusercontent.com/risan/quran-json/main/data/quran.json)
- Chapter data: [chapters.json](https://raw.githubusercontent.com/risan/quran-json/main/data/chapters/en.json)

## Screenshots

_Add screenshots of the application interface here._

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## Acknowledgments

Special thanks to [risan/quran-json](https://github.com/risan/quran-json) for providing the Quran data in JSON format.

