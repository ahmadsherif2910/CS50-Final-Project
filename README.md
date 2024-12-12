# Quran Viewer

#### Video Demo: https://youtu.be/C0Fk-J1WmAs

#### Description:
Quran Viewer is an interactive Python-based application designed to provide a comprehensive yet user-friendly interface for exploring the Quran. This application caters to both casual readers and serious students of the Quran by offering features such as chapter navigation, verse search, bookmarking, and translation viewing. The project aims to bridge accessibility and functionality, allowing users to delve into the Quran's text and its contextual meaning effortlessly.

One of the standout features of Quran Viewer is its simplicity and ease of use. Users can navigate through the Quran chapter by chapter and verse by verse with intuitive controls. For those seeking specific content, the search functionality enables keyword-based exploration, delivering results with clear references to chapters and verses. Additionally, the ability to bookmark verses allows users to save and revisit their favorite parts of the Quran with ease. For inspiration or curiosity, the app's random verse generator provides a unique way to discover new passages.

Understanding the Quran's message is crucial, and to facilitate this, the application includes translations for each chapter. These translations provide users with a deeper understanding of the text, making it more accessible to non-Arabic speakers. The application's design focuses on both functionality and inclusivity, ensuring it serves a diverse audience effectively.

## Disclaimer
I used AI after i finished writing the code to help me align text and name variables better

## Features

- **View Quranic Chapters and Verses:**
  Navigate seamlessly through the Quran, with clear labels displaying the current chapter and verse.

- **Search for Verses:**
  Quickly find verses containing specific keywords, with results presented alongside chapter and verse details.

- **Bookmark Verses:**
  Save your favorite verses for future reference using the bookmarking system.

- **Random Verse Display:**
  Discover new passages with the random verse generator.

- **View Translations:**
  Each chapter's translation provides contextual understanding of the Quran's message.

## Project Files and Their Purpose

### `quran_viewer.py`
This main script encapsulates all application logic and serves as the core of the project. Key functionalities include:

1. **Data Retrieval:**
   - Fetches Quranic text and chapter metadata from open-source JSON files hosted online.
   - Utilizes Python's `urllib` and `json` libraries for seamless integration of external data.

2. **User Interface:**
   - Built using the `tkinter` library to ensure a lightweight and responsive graphical interface.
   - Implements buttons, labels, and additional windows for intuitive user interaction.

3. **Core Features:**
   - Navigation controls for chapters and verses.
   - Search functionality for retrieving verses based on keywords.
   - Bookmark management for saving and revisiting favorite passages.
   - Random verse selection, offering a new way to engage with the text.

### Data Files

- **`quran.json`**:
  Contains the Quranic text organized by chapters and verses.

- **`chapters.json`**:
  Provides metadata for each chapter, including names and translations.

These files are sourced dynamically from the [risan/quran-json](https://github.com/risan/quran-json) repository, ensuring accuracy and reliability.

## Design Choices and Considerations

1. **GUI Framework Selection:**
   `tkinter` was chosen for its simplicity and out-of-the-box availability in Python. While other frameworks like PyQt or Kivy offer advanced features, `tkinter` provided the right balance of functionality and ease of use for this project.

2. **Data Source:**
   Using the `risan/quran-json` repository ensured the project remained lightweight while offering comprehensive and accurate Quranic data. This choice eliminated the need for a local database, reducing complexity.

3. **Feature Prioritization:**
   The features were selected based on their relevance to users. For instance, the random verse generator and search functionality cater to both casual and scholarly users, enhancing the application's versatility.

4. **Scalability:**
   The modular design of the code allows for future enhancements, such as adding multilingual translations or advanced search filters.

5. **User Experience:**
   The navigation and interaction design emphasize simplicity, ensuring the application is accessible to users of all technical backgrounds.

## How to Use

1. **Navigation:**
   - Use the `<< Previous Chapter`, `Next Chapter >>`, `<< Previous Verse`, and `Next Verse >>` buttons to explore the Quran.

2. **Search:**
   - Click `Search Verse`, enter a keyword, and view matching verses with chapter and verse references.

3. **Bookmarking:**
   - Click `Bookmark Verse` to save a verse. View all saved bookmarks via the `View Bookmarks` button.

4. **Random Verse:**
   - Click `Random Verse` to display a randomly selected chapter and verse.

5. **Translations:**
   - Click `View Translation` to see the translation of the current chapter.

## Requirements

- Python 3.x
- `tkinter` (included with Python)
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

## Acknowledgments

Special thanks to [risan/quran-json](https://github.com/risan/quran-json) for providing the Quran data in JSON format.


