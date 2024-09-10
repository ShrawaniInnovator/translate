
# Multilingual Translator with BLEU Score Calculation

This project implements a "Multilingual Translator" using the Google Translate API and evaluates the translation quality using both Standard and Adaptive BLEU Scores. It also visualizes the comparison of BLEU scores with a bar graph.

 #Features

- Translate between 10 supported languages: English, French, Spanish, German, Hindi, Chinese, Arabic, Russian, Portuguese, and Italian.
- Calculate Standard BLEU and Adaptive BLEU scores for translations.
- Predefined multilingual dialogue dataset for testing.
- Visualize BLEU score comparisons using Matplotlib.

# Technologies Used

- Python
- Google Translate API (`googletrans`)
- sacrebleu (for BLEU score calculation)
- Matplotlib (for graph visualization)

# Installation

1. Clone the repository:
   
    git clone https://github.com/your-username/multilingual-translator-bleu.git
   

2. Install the required dependencies:

    pip install googletrans==4.0.0-rc1 sacrebleu matplotlib
 

# Usage

1. Run the script:
    
    python translator.py


2. Input the source and target languages (from the supported list), and the predefined dataset will be used to calculate and visualize BLEU scores for translations.

# Example

Supported Languages: English, French, Spanish, German, Hindi, Chinese, Arabic, Russian, Portuguese, Italian

- Source Language: English
- Target Language: French
- The program will display translations, calculate BLEU Scores, and show a bar graph comparing standard and adaptive BLEU scores.

# Future Enhancements

- Integration of user-input text for real-time translation.
- Expand to more languages.
  
# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

