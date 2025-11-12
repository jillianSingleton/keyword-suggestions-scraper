thonimport json
import time
from extractors.google_parser import GoogleParser
from extractors.amazon_parser import AmazonParser
from extractors.youtube_parser import YouTubeParser
from outputs.json_exporter import JSONExporter

class KeywordSuggestionsScraper:
    def __init__(self, keywords, max_results=10):
        self.keywords = keywords
        self.max_results = max_results
        self.exporter = JSONExporter()

    def run(self):
        results = []
        for keyword in self.keywords:
            google_suggestions = GoogleParser(keyword).get_suggestions(self.max_results)
            amazon_suggestions = AmazonParser(keyword).get_suggestions(self.max_results)
            youtube_suggestions = YouTubeParser(keyword).get_suggestions(self.max_results)

            results.append({
                "keyword": keyword,
                "platforms": {
                    "google": google_suggestions,
                    "amazon": amazon_suggestions,
                    "youtube": youtube_suggestions
                },
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())
            })

        self.exporter.export(results)

if __name__ == "__main__":
    keywords = ["SEO", "keyword research", "digital marketing"]
    scraper = KeywordSuggestionsScraper(keywords)
    scraper.run()