# Quran Viewer

Quran Viewer is a simple Python-based graphical application that allows users to explore, navigate, and interact with the Quran. The app provides features like verse navigation, chapter translation, search, bookmarking, and random verse display, using data fetched from an open-source Quran JSON repository.

## Features

- **View Quranic Chapters and Verses:**
  Navigate through chapters and verses of the Quran seamlessly.

- **Search for Verses:**
  Search for verses containing specific keywords.

- **Bookmark Verses:**
  Save your favorite verses and revisit them anytime.

- **Random Verse Display:**
  Discover random verses for inspiration or study.

- **View Translations:**
  Display chapter translations for better understanding.

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

## How to Use

1. **Navigation:**
   Use the `<< Previous Chapter`, `Next Chapter >>`, `<< Previous Verse`, and `Next Verse >>` buttons to navigate.

2. **Search:**
   Click `Search Verse`, enter a keyword, and view the results.

3. **Bookmarking:**
   Click `Bookmark Verse` to save the current verse.

4. **View Bookmarks:**
   Click `View Bookmarks` to see your saved verses.

5. **Random Verse:**
   Click `Random Verse` to display a random chapter and verse.

6. **Translations:**
   Click `View Translation` to display the translation of the current chapter.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## Acknowledgments

Special thanks to [risan/quran-json](https://github.com/risan/quran-json) for providing the Quran data in JSON format.
