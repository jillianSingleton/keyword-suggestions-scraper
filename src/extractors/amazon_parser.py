thonimport requests
from bs4 import BeautifulSoup

class AmazonParser:
    def __init__(self, keyword):
        self.keyword = keyword
        self.url = f"https://www.amazon.com/s?k={keyword}"

    def get_suggestions(self, max_results):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        suggestions = []

        for suggestion in soup.find_all("span", class_="a-text-normal"):
            if len(suggestions) >= max_results:
                break
            suggestions.append(suggestion.get_text().strip())

        return suggestions