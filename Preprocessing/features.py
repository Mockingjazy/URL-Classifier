# -*- coding: utf-8 -*-
"""features_benign.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H0SwTt97rWre5sYFKphwGB8RH5yZpRX3
"""

from google.colab import files
uploaded = files.upload()

!pip install spellchecker

pip install pyspellchecker

import pandas as pd
import re
import requests
from urllib.parse import urlparse
from spellchecker import SpellChecker
df = pd.read_csv('dtanew (3).csv')  # Replace 'your_dataset.csv' with your actual dataset file name/path

from spellchecker import SpellChecker

# Initialize the spell checker
spell_checker = SpellChecker()

def is_spelling_correct(word):
    # Check if the word is in the dictionary
    return word in spell_checker

# Example usage
word = "google"
if is_spelling_correct(word):
    print(f"The word '{word}' is spelled correctly.")
else:
    print(f"The word '{word}' is misspelled.")

from urllib.parse import urlparse
import pandas as pd
import re


def extract_features(url):
    features = {}

    # URL Length
    features['URLLength'] = len(url)

    # URL Depth
    features['URLDepth'] = url.count('/')

    # Https
    features['Https'] = 1 if re.search('https://', url) else 0

    # Prefix/Suffix
    features['PrefixSuffix'] = 1 if '-' in url else 0

    # Have client, admin, server, login
    features['HaveClient'] = 1 if 'client' in url else 0
    features['HaveAdmin'] = 1 if 'admin' in url else 0
    features['HaveServer'] = 1 if 'server' in url else 0
    features['HaveLogin'] = 1 if 'login' in url else 0

    # Presence of file extensions
    file_extensions = ['.php', '.html', '.info', '.txt', '.js', '.exe']
    for ext in file_extensions:
        features['Has' + ext.replace('.', '')] = 1 if ext in url else 0

    # Num of periods
    features['NumPeriods'] = url.count('.')

    # Num encoded char
    features['NumEncodedChar'] = len(re.findall(r'%[0-9A-Fa-f]{2}', url))

    # Num of parameters
    features['NumParameters'] = len(re.findall(r'[\?&][^&=]+=[^&=]+', url))

    # Num of digits
    features['NumDigits'] = sum(c.isdigit() for c in url)

    # Num of spec char
    features['NumSpecChar'] = len(re.findall(r'[^\w\s]', url))

    # Tempting words
    tempting_words = ['money', 'free', 'Paypal', 'banking', 'password', 'verify', 'account']
    features['TemptingWords'] = sum(1 for word in tempting_words if word in url.lower())

    # Image
    features['Image'] = 1 if 'image' in url else 0

    # Login or upload
    features['LoginOrUpload'] = 1 if 'login' in url or 'upload' in url else 0

    # Spelling check for each word in the domain
    matches = re.findall(r'^(?:https?://)?([\w.-]+)', url)
    if matches:
        domain = matches[0]
        domain_words = domain.split('.')
        misspelled_count = 0
        for word in domain_words:
            if not is_spelling_correct(word):
                misspelled_count += 1
        features['SpellingErrorInDomain'] = misspelled_count
    else:
        features['SpellingErrorInDomain'] = 0

    # Raw word count
    features['RawWordCount'] = len(re.findall(r'\w+', url))

    # Hostname Length
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    if hostname:
        features['HostnameLength'] = len(hostname)
    else:
        features['HostnameLength'] = 0

    # Path Length
    features['PathLength'] = len(urlparse(url).path)

    return pd.Series(features)


# Apply feature extraction to each URL in the dataframe
extracted_features = df['URL'].apply(extract_features)

# Merge extracted features with the original dataset
df = pd.concat([df, extracted_features], axis=1)

# Save the modified DataFrame back to CSV
df.to_csv('your_updated_file.csv', index=False)

df.head()

from google.colab import files

files.download('your_updated_file.csv')