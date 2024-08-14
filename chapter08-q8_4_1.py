import re

def extract_words(text):

    pattern = r'[a-zA-Z- ]+\d+'
    
    words = re.findall(pattern, text)
    
    return words

text = "かなり昔のRX-7で東京駅まで送ってもらい、成田空港からBoeing787で高松空港まで行き、帰りはN700系で岡山から帰りました。"

extracted_words = extract_words(text)
print(extracted_words)

