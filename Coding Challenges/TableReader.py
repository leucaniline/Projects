import re
import requests
from bs4 import BeautifulSoup


def print_unicode_grid(google_doc_url: str) -> None:
    """
    Retrieve a Google Doc containing a table of (x, character, y) entries, reconstruct
    the grid structure, and display it as text in the terminal.

    Grid coordinate system (cartesian):
        - (0, 0) is the bottom-left corner
        - x increases from left to right
        - y increases from bottom to top
    """

    # Step 1 — make sure we have an HTML export URL
    url = google_doc_url

    # Try to find a Google Doc ID in the provided URL
    doc_id_match = re.search(r"https://docs\.google\.com/document/d/([^/]+)/", google_doc_url)

    # If we found an ID and the URL is not already an HTML export or published URL,
    # convert it into the HTML export form to parse.
    if doc_id_match and "export?format=html" not in google_doc_url and "/pub" not in google_doc_url:
        doc_id = doc_id_match.group(1)
        url = f"https://docs.google.com/document/d/{doc_id}/export?format=html"

    # Download the HTML and raise if the request failed
    response = requests.get(url)
    response.raise_for_status()
    html_text = response.text

    # Step 2 — parse the HTML and locate the table with the data
    soup = BeautifulSoup(html_text, "html.parser")
    tables = soup.find_all("table")
    if not tables:
        raise ValueError("No tables found in the document.")

    # Use the first table by default; callers may structure a table with headers
    # labelled 'x-coordinate', 'character' and 'y-coordinate' — if such a table
    # exists prefer it.
    chosen_table = tables[0]
    for table in tables:
        first_row = table.find("tr")
        if not first_row:
            continue
        headers = [c.get_text(strip=True).lower() for c in first_row.find_all(["td", "th"])]
        if len(headers) >= 3 and "x-coordinate" in headers[0] and "character" in headers[1] and "y-coordinate" in headers[2]:
            chosen_table = table
            break

    # Step 3 — read each data row and collect characters by (x, y) coordinate
    char_map = {}
    max_x = max_y = 0
    rows = chosen_table.find_all("tr")

    # Skip the header row and parse the remaining rows. Each row is expected
    # to contain at least three columns: x, character, y.
    for data_row in rows[1:]:
        cells = data_row.find_all(["td", "th"])
        if len(cells) < 3:
            # Not enough columns — ignore this row
            continue

        try:
            x_text = cells[0].get_text(strip=True)
            char_text = cells[1].get_text()
            y_text = cells[2].get_text(strip=True)

            # Convert coordinate strings into integers and normalise character
            x = int(x_text)
            y = int(y_text)
            char = char_text.strip("\n\r")
            # Treat an empty cell as a space so the grid prints correctly
            if char == "":
                char = " "
        except ValueError:
            # If parsing fails (e.g. non-integer coordinates), skip the row
            continue

        char_map[(x, y)] = char
        # Track bounds so we know how large the grid should be
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # Step 4 — construct a 2D grid. Note that the document's coordinate system
    # treats y=0 as the bottom row, but when printing we output from the top row
    # downwards, so we flip the y-axis when placing characters.
    width = max_x + 1
    height = max_y + 1

    # grid[row_index][col_index] where row_index 0 corresponds to the top row
    grid = [[" " for _ in range(width)] for _ in range(height)]

    for (x, y), char in char_map.items():
        row_index = max_y - y
        col_index = x
        grid[row_index][col_index] = char

    # Step 5 — print the grid row by row from the top down
    for row_index in range(height):
        print("".join(grid[row_index]))



# Funcion Usage:
print_unicode_grid("https://docs.google.com/document/d/e/2PACX-1vQiVT_Jj04V35C-YRzvoqyEYYzdXHcRyMUZCVQRYCu6gQJX7hbNhJ5eFCMuoX47cAsDW2ZBYppUQITr/pub")
