# Visualizing Routes on Google Maps Using gmplot

This Python program uses the `gmplot` library to visualize routes on Google Maps. It reads coordinates from a CSV file and plots them as markers on a Google Map.

## How It Works

1. The program initializes a Google Map plotter with a specified starting location and zoom level.
2. It reads latitude and longitude coordinates from a CSV file (`route.csv`).
3. It places a yellow marker at the first coordinate, blue markers for subsequent coordinates, and a red marker at the final coordinate.
4. The map is then saved as an HTML file (`myhtml.html`), which can be opened in a web browser to view the plotted route.

## Usage

1. Ensure you have the `gmplot` library installed. You can install it using pip:
   pip install gmplot
2. Prepare a CSV file (`route.csv`) with latitude and longitude coordinates in each row.
3. Run the program. The resulting map will be saved as an HTML file (`myhtml.html`).

## Example

![Screenshot 2025-02-19 125935](https://github.com/user-attachments/assets/368f24a1-0bc6-4942-8a6a-77a895db8102)
