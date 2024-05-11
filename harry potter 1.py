import requests
from bs4 import BeautifulSoup
import pandas as pd

# The URL of the website
url = "https://tomfeltonandmore.tripod.com/home/id9.html"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find all paragraphs with class "MsoNormal"
paragraphs = soup.find_all("p", class_="MsoNormal")

# Initialize lists to store dialogue and speaker
dialogues = []
speaker = None

# Loop through each paragraph
for paragraph in paragraphs:
    text = paragraph.get_text().strip()

    # Check if the paragraph contains dialogue
    if ":" in text:
        # Split the text into speaker and dialogue
        speaker, dialogue = text.split(":", 1)
        speaker = speaker.strip()  # Remove leading/trailing whitespaces

        # Append dialogue and speaker to the lists
        dialogues.append({"Speaker": speaker, "Dialogue": dialogue.strip()})

# Create a DataFrame from the dialogues and speakers
df = pd.DataFrame(dialogues)
print(df)
# Save the DataFrame to a CSV file
df.to_csv("dialogues.csv", index=False)

print("Harry Potter 1 d.csv'")
