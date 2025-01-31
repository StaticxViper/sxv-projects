# Script must be executed via .venv (virtual environment) to avoid conflicts with other packages


#pylint: disable=missing-docstring
#pylint: disable=unspecified-encoding
#pylint: disable=line-too-long
#pylint: disable=wrong-import-position
#pylint: disable=import-error
#pylint: disable=no-else-return
import os
from flask import Flask, request, jsonify
import openai
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Flask app
app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape_property():
    """Get property address from POST request"""
    address = request.json.get('address', timeout=10)
    if not address:
        return jsonify({"error": "No address provided"}), 400

    # Example scraping logic (modify based on your real scraping needs)
    zillow_url = f"https://www.zillow.com/homes/{address.replace(' ', '-')}_rb/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(zillow_url, headers=headers, timeout=10)

    if response.status_code == 200:
        # Parse the Zillow page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Example: Extract the property price (you will need to modify this selector)
        price = soup.find('span', class_='ds-value').text if soup.find('span', class_='ds-value') else 'N/A'

        # Call OpenAI to get more insights (you can customize the prompt)
        prompt = f"Provide an analysis of this property: {address}. Price: {price}"
        openai_response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )

        insights = openai_response.choices[0].text.strip()

        # Return the property data and insights
        return jsonify({
            "address": address,
            "price": price,
            "insights": insights
        })
    else:
        return jsonify({"error": "Failed to scrape Zillow"}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
