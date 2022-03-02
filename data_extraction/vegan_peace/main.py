import requests
from bs4 import BeautifulSoup

def process_text(text_data):
    stripped_string = text_data.split(":")[0].strip()
    capitalized_string =  stripped_string.upper() if not stripped_string[0].islower() else None
    return capitalized_string

if __name__ == "__main__":
    url = "https://www.veganpeace.com/ingredients/ingredients.htm"
    requests.get
    # Get raw html content
    html_content = requests.get(url).text

    # Parse html content
    soup = BeautifulSoup(html_content, "html.parser")

    # Get all the ingredients from font tag

    font_data = soup.find_all("font")


    data = []
    for font in font_data:
        processed = process_text(font.text)
        print(processed)
        if processed:
            data.append(processed)
            