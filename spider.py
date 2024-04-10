import requests
from bs4 import BeautifulSoup
import re

# Define your target keyword(s)
target_keywords = ["your_keyword"]

url = "your_website_url"  # Replace with your desired URL

# Download the webpage content
response = requests.get(url)

# Check if download was successful
if response.status_code == 200:
  # Parse the HTML content
  soup = BeautifulSoup(response.text, 'html.parser')

  # Extract all paragraph elements
  paragraphs = soup.find_all('p')

  # Loop through each paragraph
  for paragraph in paragraphs:
    # Extract text content from the paragraph
    paragraph_text = paragraph.get_text()

    # Check if any target keyword is present
    for keyword in target_keywords:
      if re.search(keyword, paragraph_text, flags=re.IGNORECASE):  # Search ignoring case
        # Keyword found! Extract details
        print(f"Found keyword: {keyword} in paragraph:")
        print(paragraph_text)  # Print the paragraph containing the keyword
        print(f"Page URL: {response.url}")  # Print the URL of the current page
      
else:
  print(f"Error downloading the webpage: {response.status_code}")

