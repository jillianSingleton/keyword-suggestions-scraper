thonimport requests
from bs4 import BeautifulSoup

class YouTubeParser:
    def __init__(self, keyword):
        self.keyword = keyword
        self.url = f"https://www.youtube.com/results?search_query={keyword}"

    def get_suggestions(self, max_results):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        suggestions = []

        for suggestion in soup.find_all("a"):
            if len(suggestions) >= max_results:
                break
            suggestion_text = suggestion.get_text().strip()
            if suggestion_text:
                suggestions.append(suggestion_text)

        return suggestions