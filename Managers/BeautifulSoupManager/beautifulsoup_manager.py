import requests
from bs4 import BeautifulSoup
import hashlib
import time

class BeautifulSoupManager:
  
    def __init__(self):
        self.monitored_sites = {}

    def fetch_html(self, url):
        """Fetches the HTML content of a given URL."""
        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_html(self, html):
        """Parses HTML content using BeautifulSoup."""
        return BeautifulSoup(html, 'html.parser')

    def scrape_website(self, url, element_selector):
        """Scrapes the website for a specific HTML element based on the selector."""
        html = self.fetch_html(url)
        if html:
            soup = self.parse_html(html)
            elements = soup.select(element_selector)
            return [element.get_text(strip=True) for element in elements]
        return []

    def monitor_website(self, url, check_interval=60):
        """Monitors a website for changes in its content."""
        if url in self.monitored_sites:
            print(f"Already monitoring {url}")
            return

        def get_site_hash():
            html = self.fetch_html(url)
            if html:
                return hashlib.md5(html.encode('utf-8')).hexdigest()
            return None

        initial_hash = get_site_hash()
        if initial_hash is None:
            print(f"Failed to fetch initial content for {url}")
            return

        self.monitored_sites[url] = initial_hash
        print(f"Started monitoring {url}")

        try:
            while True:
                time.sleep(check_interval)
                current_hash = get_site_hash()
                if current_hash and current_hash != self.monitored_sites[url]:
                    print(f"Change detected on {url}!")
                    self.monitored_sites[url] = current_hash
                else:
                    print(f"No changes detected on {url}.")
        except KeyboardInterrupt:
            print(f"Stopped monitoring {url}")
            del self.monitored_sites[url]

# Example Usage
if __name__ == "__main__":
    manager = BeautifulSoupManager()

    test_url = "https://staticxviper.github.io/sxv-projects/test_beautifulsoup_page.html"
    url = "https://staticxviper.github.io/sxv-projects/blog_investing.html"

    selector = "h1" 
    print("Scraped content:", manager.scrape_website(url, selector))

    selector = "p"  
    print("Scraped content:", manager.scrape_website(url, selector))

    
    #monitor_url = "https://example.com"
    #manager.monitor_website(monitor_url, check_interval=10)
