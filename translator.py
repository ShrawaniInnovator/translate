#!/usr/bin/env python
# coding: utf-8

# In[2]:


import googletrans
from googletrans import Translator
import sacrebleu
import matplotlib.pyplot as plt

# Initialize the Google Translator
translator = Translator()

# Function to translate text using Google Translate API
def translate_text(text, dest_language):
    translation = translator.translate(text, dest=dest_language)
    return translation.text

# Function to calculate BLEU score
def calculate_bleu(reference, hypothesis):
    bleu = sacrebleu.sentence_bleu(hypothesis, [reference])
    return bleu.score

# Supported languages and their codes
languages = {
    "english": "en",
    "french": "fr",
    "spanish": "es",
    "german": "de",
    "hindi": "hi",
    "chinese": "zh-cn",
    "arabic": "ar",
    "russian": "ru",
    "portuguese": "pt",
    "italian": "it"
}

# Predefined Multi-Language Dataset for testing
dialogue_dataset = [
    {"en": "Hello, how are you?", "fr": "Bonjour, comment ça va?", "es": "Hola, ¿cómo estás?", "de": "Hallo, wie geht es dir?", "hi": "नमस्ते, आप कैसे हैं?", "zh-cn": "你好，你好吗？", "ar": "مرحبًا، كيف حالك؟", "ru": "Привет, как дела?", "pt": "Olá, como você está?", "it": "Ciao, come stai?"},
    {"en": "I am fine, thank you.", "fr": "Je vais bien, merci.", "es": "Estoy bien, gracias.", "de": "Mir geht es gut, danke.", "hi": "मैं ठीक हूँ, धन्यवाद।", "zh-cn": "我很好，谢谢。", "ar": "أنا بخير، شكرا لك.", "ru": "Я в порядке, спасибо.", "pt": "Estou bem, obrigado.", "it": "Sto bene, grazie."},
    {"en": "What is your name?", "fr": "Comment tu t'appelles?", "es": "¿Cómo te llamas?", "de": "Wie heißt du?", "hi": "आपका नाम क्या है?", "zh-cn": "你叫什么名字？", "ar": "ما اسمك؟", "ru": "Как тебя зовут?", "pt": "Qual é o seu nome?", "it": "Come ti chiami?"},
    {"en": "My name is John.", "fr": "Je m'appelle John.", "es": "Me llamo John.", "de": "Ich heiße John.", "hi": "मेरा नाम जॉन है।", "zh-cn": "我叫约翰。", "ar": "اسمي جون.", "ru": "Меня зовут Джон.", "pt": "Meu nome é John.", "it": "Mi chiamo John."},
    {"en": "Let's go to the market.", "fr": "Allons au marché.", "es": "Vamos al mercado.", "de": "Lass uns zum Markt gehen.", "hi": "चलो बाजार चलते हैं।", "zh-cn": "让我们去市场。", "ar": "دعنا نذهب إلى السوق.", "ru": "Пойдем на рынок.", "pt": "Vamos ao mercado.", "it": "Andiamo al mercato."},
    {"en": "I love programming.", "fr": "J'adore la programmation.", "es": "Me encanta programar.", "de": "Ich liebe es zu programmieren.", "hi": "मुझे प्रोग्रामिंग पसंद है।", "zh-cn": "我喜欢编程。", "ar": "أنا أحب البرمجة.", "ru": "Я люблю программирование.", "pt": "Eu amo programar.", "it": "Amo programmare."}
]

# Function to test dataset translation and calculate BLEU score
def test_translation_with_dataset(dataset, source_lang, target_lang):
    source_lang_code = languages.get(source_lang.strip().lower())
    target_lang_code = languages.get(target_lang.strip().lower())

    if not source_lang_code or not target_lang_code:
        print(f"Languages '{source_lang}' or '{target_lang}' are not supported.")
        return

    # Lists to store sentences and their BLEU scores
    bleu_scores = []
    sentences = []

    for item in dataset:
        source_text = item[source_lang_code]
        reference_translation = item[target_lang_code]

        # Translate the source text to the target language
        translated_text = translate_text(source_text, target_lang_code)

        # Calculate BLEU score
        bleu_score = calculate_bleu(reference_translation, translated_text)

        # Store the BLEU score and the sentence
        bleu_scores.append(bleu_score)
        sentences.append(source_text)

        # Display results
        print(f"Source ({source_lang}): {source_text}")
        print(f"Reference Translation ({target_lang}): {reference_translation}")
        print(f"Translated: {translated_text}")
        print(f"BLEU Score: {bleu_score:.2f}\n")

    # Plot BLEU scores as a graph
    plot_bleu_scores(sentences, bleu_scores)

# Function to plot BLEU scores using Matplotlib
def plot_bleu_scores(sentences, scores):
    plt.figure(figsize=(10, 6))
    plt.barh(sentences, scores, color='skyblue')
    plt.xlabel('BLEU Score')
    plt.ylabel('Source Sentences')
    plt.title('BLEU Scores for Translations')
    plt.xlim(0, 100)
    plt.show()

# Example usage: test predefined dataset for English to French translation
def main():
    print("Supported Languages: English, French, Spanish, German, Hindi, Chinese, Arabic, Russian, Portuguese, Italian")

    # Input source and target languages
    source_lang = input("Enter the source language: ").lower()
    target_lang = input("Enter the target language: ").lower()

    # Test translation and evaluate BLEU score using the predefined dataset
    test_translation_with_dataset(dialogue_dataset, source_lang, target_lang)

if __name__ == "__main__":
    main()


# In[1]:


import googletrans
from googletrans import Translator
import sacrebleu
import matplotlib.pyplot as plt

# Initialize the Google Translator
translator = Translator()

# Function to translate text using Google Translate API
def translate_text(text, dest_language):
    translation = translator.translate(text, dest=dest_language)
    return translation.text

# Function to calculate standard BLEU score
def calculate_bleu(reference, hypothesis):
    bleu = sacrebleu.sentence_bleu(hypothesis, [reference])
    return bleu.score

# Function to calculate adaptive BLEU score (based on sentence length)
def calculate_adaptive_bleu(reference, hypothesis):
    bleu_score = calculate_bleu(reference, hypothesis)
    sentence_length = len(hypothesis.split())
    
    # Apply a weight based on sentence length (longer sentences get a slight boost)
    adaptive_bleu_score = bleu_score * (1 + 0.05 * sentence_length)
    
    # Ensure the adaptive BLEU score does not exceed 100
    return min(adaptive_bleu_score, 100)

# Supported languages and their codes
languages = {
    "english": "en",
    "french": "fr",
    "spanish": "es",
    "german": "de",
    "hindi": "hi",
    "chinese": "zh-cn",
    "arabic": "ar",
    "russian": "ru",
    "portuguese": "pt",
    "italian": "it"
}

# Predefined Multi-Language Dataset for testing
dialogue_dataset = [
    {"en": "Hello, how are you?", "fr": "Bonjour, comment ça va?", "es": "Hola, ¿cómo estás?", "de": "Hallo, wie geht es dir?", "hi": "नमस्ते, आप कैसे हैं?", "zh-cn": "你好，你好吗？", "ar": "مرحبًا، كيف حالك؟", "ru": "Привет, как дела?", "pt": "Olá, como você está?", "it": "Ciao, come stai?"},
    {"en": "I am fine, thank you.", "fr": "Je vais bien, merci.", "es": "Estoy bien, gracias.", "de": "Mir geht es gut, danke.", "hi": "मैं ठीक हूँ, धन्यवाद।", "zh-cn": "我很好，谢谢。", "ar": "أنا بخير، شكرا لك.", "ru": "Я в порядке, спасибо.", "pt": "Estou bem, obrigado.", "it": "Sto bene, grazie."},
    {"en": "What is your name?", "fr": "Comment tu t'appelles?", "es": "¿Cómo te llamas?", "de": "Wie heißt du?", "hi": "आपका नाम क्या है?", "zh-cn": "你叫什么名字？", "ar": "ما اسمك؟", "ru": "Как тебя зовут?", "pt": "Qual é o seu nome?", "it": "Come ti chiami?"},
    {"en": "My name is John.", "fr": "Je m'appelle John.", "es": "Me llamo John.", "de": "Ich heiße John.", "hi": "मेरा नाम जॉन है।", "zh-cn": "我叫约翰。", "ar": "اسمي جون.", "ru": "Меня зовут Джон.", "pt": "Meu nome é John.", "it": "Mi chiamo John."},
    {"en": "Let's go to the market.", "fr": "Allons au marché.", "es": "Vamos al mercado.", "de": "Lass uns zum Markt gehen.", "hi": "चलो बाजार चलते हैं।", "zh-cn": "让我们去市场。", "ar": "دعنا نذهب إلى السوق.", "ru": "Пойдем на рынок.", "pt": "Vamos ao mercado.", "it": "Andiamo al mercato."},
    {"en": "I love programming.", "fr": "J'adore la programmation.", "es": "Me encanta programar.", "de": "Ich liebe es zu programmieren.", "hi": "मुझे प्रोग्रामिंग पसंद है।", "zh-cn": "我喜欢编程。", "ar": "أنا أحب البرمجة.", "ru": "Я люблю программирование.", "pt": "Eu amo programar.", "it": "Amo programmare."}
]

# Function to test dataset translation and calculate both BLEU scores
def test_translation_with_dataset(dataset, source_lang, target_lang):
    source_lang_code = languages.get(source_lang.strip().lower())
    target_lang_code = languages.get(target_lang.strip().lower())

    if not source_lang_code or not target_lang_code:
        print(f"Languages '{source_lang}' or '{target_lang}' are not supported.")
        return

    # Lists to store sentences and their BLEU scores
    standard_bleu_scores = []
    adaptive_bleu_scores = []
    sentences = []

    for item in dataset:
        source_text = item[source_lang_code]
        reference_translation = item[target_lang_code]

        # Translate the source text to the target language
        translated_text = translate_text(source_text, target_lang_code)

        # Calculate standard BLEU score
        standard_bleu_score = calculate_bleu(reference_translation, translated_text)

        # Calculate adaptive BLEU score
        adaptive_bleu_score = calculate_adaptive_bleu(reference_translation, translated_text)

        # Store the BLEU scores and the sentence
        standard_bleu_scores.append(standard_bleu_score)
        adaptive_bleu_scores.append(adaptive_bleu_score)
        sentences.append(source_text)

        # Display results
        print(f"Source ({source_lang}): {source_text}")
        print(f"Reference Translation ({target_lang}): {reference_translation}")
        print(f"Translated: {translated_text}")
        print(f"Standard BLEU Score: {standard_bleu_score:.2f}")
        print(f"Adaptive BLEU Score: {adaptive_bleu_score:.2f}\n")

    # Plot BLEU scores as a graph
    plot_bleu_scores(sentences, standard_bleu_scores, adaptive_bleu_scores)

# Function to plot both Standard and Adaptive BLEU scores using Matplotlib
def plot_bleu_scores(sentences, standard_scores, adaptive_scores):
    plt.figure(figsize=(12, 8))

    # Define the bar width for side-by-side bars
    bar_width = 0.35

    # Set the positions of the bars
    r1 = range(len(sentences))
    r2 = [x + bar_width for x in r1]

    # Plot standard BLEU scores
    plt.barh(r1, standard_scores, height=bar_width, color='skyblue', label='Standard BLEU Score')

    # Plot adaptive BLEU scores
    plt.barh(r2, adaptive_scores, height=bar_width, color='lightcoral', alpha=0.7, label='Adaptive BLEU Score')

    plt.yticks([r + bar_width / 2 for r in range(len(sentences))], sentences)
    plt.xlabel('BLEU Score')
    plt.ylabel('Source Sentences')
    plt.title('Standard BLEU vs Adaptive BLEU Scores')
    plt.xlim(0, 100)
    plt.legend()
    plt.show()

# Example usage: test predefined dataset for English to French translation
def main():
    print("Supported Languages: English, French, Spanish, German, Hindi, Chinese, Arabic, Russian, Portuguese, Italian")

    # Input source and target languages
    source_lang = input("Enter the source language: ").lower()
    target_lang = input("Enter the target language: ").lower()

    # Test translation and evaluate BLEU score using the predefined dataset
    test_translation_with_dataset(dialogue_dataset, source_lang, target_lang)

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




