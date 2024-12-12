from urllib.request import urlopen
import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

## Disclaimer
# I used AI after i finished writing the code to help me align text and name variables better

# Function to fetch JSON data from a URL
def getJsonFromUrl(url):
    response = urlopen(url)
    data_json = json.loads(response.read())
    return data_json

# URLs for Quran data and chapters
quran_url = "https://raw.githubusercontent.com/risan/quran-json/main/data/quran.json"
chapters_url = "https://raw.githubusercontent.com/risan/quran-json/main/data/chapters/en.json"
Quran = getJsonFromUrl(quran_url)
Chapters = getJsonFromUrl(chapters_url)

# Initialize main app
app = tk.Tk()
app.title("Quran Viewer")
app.geometry("800x600")
app.configure(bg="#f5f5f5")  # Light background color

selection = {"chapter": 1, "verse": 1}
bookmarks = []

def displaySelection():
    ayalabel["text"] = Quran[str(selection["chapter"])][selection["verse"] - 1]["text"]
    suralabel["text"] = f"Chapter: {Chapters[selection['chapter'] - 1]['name']}"
    numlabel["text"] = f"Verse: {selection['verse']}"

def displayTranslation():
    translation_window = tk.Toplevel(app)
    translation_window.title("Chapter Translation")
    translation_window.geometry("400x300")

    chapter = Chapters[selection["chapter"] - 1]
    tk.Label(translation_window, text=f"Chapter: {chapter['name']}", font=("Helvetica", 14, "bold")).pack(pady=10)
    tk.Label(translation_window, text=f"Translation: {chapter['translation']}", wraplength=350).pack(pady=5)

def displayprevaya():
    ayanextbtn["state"] = "normal"
    if selection["verse"] > 1:
        selection["verse"] -= 1
        displaySelection()
    else:
        ayaprevbtn["state"] = "disabled"

def displaynextaya():
    ayaprevbtn["state"] = "normal"
    if selection["verse"] < Chapters[selection["chapter"] - 1]["total_verses"]:
        selection["verse"] += 1
        displaySelection()
    else:
        ayanextbtn["state"] = "disabled"

def displayprevsura():
    suraprev["state"] = "normal"
    if selection["chapter"] > 1:
        selection["chapter"] -= 1
        selection["verse"] = 1
        ayaprevbtn["state"] = "normal"
        ayanextbtn["state"] = "normal"
        displaySelection()
    else:
        suraprev["state"] = "disabled"

def displaynextsura():
    suranext["state"] = "normal"
    if selection["chapter"] < len(Chapters):
        selection["chapter"] += 1
        selection["verse"] = 1
        suraprev["state"] = "normal"
        ayaprevbtn["state"] = "normal"
        ayanextbtn["state"] = "normal"
        displaySelection()
    else:
        suranext["state"] = "disabled"

def searchVerse():
    search_window = tk.Toplevel(app)
    search_window.title("Search Verse")
    search_window.geometry("400x300")

    tk.Label(search_window, text="Enter Keyword:").pack(pady=10)
    keyword_entry = tk.Entry(search_window)
    keyword_entry.pack(pady=5)

    result_label = tk.Label(search_window, text="", wraplength=350)
    result_label.pack(pady=10)

    def performSearch():
        keyword = keyword_entry.get().lower()
        results = []
        for chapter_id, verses in Quran.items():
            for verse in verses:
                if keyword in verse["text"].lower():
                    chapter_name = Chapters[int(chapter_id) - 1]["name"]
                    results.append(f"{chapter_name} ({verse['verse']}): {verse['text']}")
        if results:
            result_label.config(text="\n\n".join(results[:5]) + ("\n\n...more" if len(results) > 5 else ""))
        else:
            result_label.config(text="No results found.")

    search_btn = ttk.Button(search_window, text="Search", command=performSearch)
    search_btn.pack(pady=10)

def addBookmark():
    bookmark = (selection["chapter"], selection["verse"])
    if bookmark not in bookmarks:
        bookmarks.append(bookmark)
        messagebox.showinfo("Bookmark Added", f"Bookmarked Chapter {bookmark[0]}, Verse {bookmark[1]}.")
    else:
        messagebox.showinfo("Already Bookmarked", "This verse is already bookmarked.")

def viewBookmarks():
    bookmarks_window = tk.Toplevel(app)
    bookmarks_window.title("Bookmarks")
    bookmarks_window.geometry("400x300")

    if bookmarks:
        for chapter, verse in bookmarks:
            chapter_name = Chapters[chapter - 1]["name"]
            tk.Label(bookmarks_window, text=f"{chapter_name} (Verse {verse})").pack()
    else:
        tk.Label(bookmarks_window, text="No bookmarks available.").pack()

def displayRandomVerse():
    random_chapter = random.randint(1, len(Chapters))
    random_verse = random.randint(1, Chapters[random_chapter - 1]["total_verses"])
    selection["chapter"] = random_chapter
    selection["verse"] = random_verse
    displaySelection()

# Labels for display
suralabel = ttk.Label(app, text=Chapters[0]["name"], font=("Helvetica", 14, "bold"), background="#f5f5f5")
suralabel.pack(pady=(10, 5))

ayalabel = ttk.Label(
    app, text=Quran[str(selection["chapter"])][0]["text"], wraplength=750, font=("Helvetica", 12), background="#f5f5f5")
ayalabel.pack(pady=10)

numlabel = ttk.Label(app, text=f"Verse: {Quran[str(selection['chapter'])][0]['verse']}", font=("Helvetica", 10), background="#f5f5f5")
numlabel.pack(pady=(5, 15))

# Navigation buttons
nav_frame = ttk.Frame(app)
nav_frame.pack(pady=10)

suranext = ttk.Button(nav_frame, text="Next Chapter >>", command=displaynextsura)
suranext.grid(row=0, column=2, padx=5)

suraprev = ttk.Button(nav_frame, text="<< Previous Chapter", command=displayprevsura)
suraprev.grid(row=0, column=0, padx=5)

verse_frame = ttk.Frame(app)
verse_frame.pack(pady=10)

ayanextbtn = ttk.Button(verse_frame, text="Next Verse >>", command=displaynextaya)
ayanextbtn.grid(row=0, column=2, padx=5)

ayaprevbtn = ttk.Button(verse_frame, text="<< Previous Verse", command=displayprevaya)
ayaprevbtn.grid(row=0, column=0, padx=5)

# Additional Features
extras_frame = ttk.Frame(app)
extras_frame.pack(pady=10)

search_btn = ttk.Button(extras_frame, text="Search Verse", command=searchVerse)
search_btn.grid(row=0, column=0, padx=5)

bookmark_btn = ttk.Button(extras_frame, text="Bookmark Verse", command=addBookmark)
bookmark_btn.grid(row=0, column=1, padx=5)

view_bookmarks_btn = ttk.Button(extras_frame, text="View Bookmarks", command=viewBookmarks)
view_bookmarks_btn.grid(row=0, column=2, padx=5)

random_verse_btn = ttk.Button(extras_frame, text="Random Verse", command=displayRandomVerse)
random_verse_btn.grid(row=0, column=3, padx=5)

translation_btn = ttk.Button(extras_frame, text="View Translation", command=displayTranslation)
translation_btn.grid(row=0, column=4, padx=5)

app.mainloop()
