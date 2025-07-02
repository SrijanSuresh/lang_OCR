# translate.py
from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-ja-en")

def translate_text(text_list):
    results = []
    for text in text_list:
        result = translator(text)
        results.append(result[0]['translation_text'])
    return results

if __name__ == "__main__":
    sample = ["こんにちは世界", "メニュー"]
    translated = translate_text(sample)
    print(translated)
