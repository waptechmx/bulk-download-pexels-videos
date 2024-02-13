# Bulk Downloads Videos Script in Python

This Python script allows you to download videos from Pexels based on a specific query. It utilizes the Pexels API to search for and download high-quality videos automatically.

## Requirements

Before running this script, make sure you have Python installed on your system. You can download it from [Python.org](https://www.python.org/) and install it following the instructions provided on its official website.

## Usage

1. Make sure you have a Pexels API key. You can obtain one by registering at [Pexels](https://www.pexels.com/api/new/).
2. Copy and paste the code into a Python file.
3. Replace `PEXELS_API_KEY` with your own API key.
4. Modify the parameters `query`, `page`, `per_page`, `size`, and `orientation` according to your preferences.
5. Run the script.

## Modify

```python
PEXELS_API_KEY = 'YOUR_API_KEY'
query = 'sad'
page = 1
per_page = 1
size= 'large'
orientation='portrait'

```

## Código

Make sure to replace YOUR_API_KEY with your own Pexels API key.
You can modify the search parameters (query, page, per_page, size, orientation) according to your needs.
This script will download the first video that matches the query in mp4 format in the same directory where the script is located.
If you want to download more videos, adjust the per_page and page parameters accordingly.