# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer
# from sumy.nlp.stemmers import Stemmer
# from sumy.utils import get_stop_words
# import pyttsx3

# # nltk.download('punkt')
# # nltk.download('punkt_tab')
# engn = pyttsx3.init()
# voices = engn.getProperty('voices')
# engn.setProperty('voice', voices[0].id)  # 0 for male, 1 for female
# engn.setProperty('rate', 150)

# def discourse_aware_summary(text, sentence_count=2):
    
#     # Create a plaintext parser
#     parser = PlaintextParser.from_string(text, Tokenizer("english"))
    
#     # Use the LSA summarizer
#     stemmer = Stemmer("english")
#     summarizer = LsaSummarizer(stemmer)
#     summarizer.stop_words = get_stop_words("english")
    
#     # Generate summary
#     summary = summarizer(parser.document, sentence_count)
    
#     return " ".join(str(sentence) for sentence in summary)

# # Example usage
text = """
Our project embarks on creating a cutting-edge system that harmoniously combines speech-to-text, translation, and text-to-speech technologies. 
At its core, the system leverages advanced speech recognition algorithms to accurately transcribe spoken language into text. 
This transcription process is pivotal as it converts verbal communication into a format that machines can process.
Once the speech is converted into text, it undergoes a translation phase where sophisticated machine learning models and natural language processing techniques come into play. 
These models are trained on vast multilingual datasets to ensure high accuracy and context-aware translations, bridging linguistic gaps and enabling seamless communication across different languages.
The final phase involves text-to-speech synthesis, which transforms the translated text back into spoken words. Utilizing state-of-the-art text-to-speech engines, this step ensures that the output is natural and intelligible, mirroring human speech as closely as possible. 
The synthesized speech is designed to be clear and emotionally nuanced, enhancing the listening experience.
This integrated system aims to facilitate real-time, multilingual communication, making it invaluable for various applications such as international business meetings, travel assistance, and accessibility tools for individuals with speech or hearing impairments. 
By removing language barriers, our project aspires to foster global understanding and connectivity, offering a robust, user-friendly solution for diverse communication needs.
"""
# summary = discourse_aware_summary(text,input("Summarize to how many lines: "))
# print(summary)

# engn.say("summerized text is, "+summary)
# engn.runAndWait()



import tkinter as tk
from tkinter import scrolledtext, messagebox
from PIL import Image, ImageTk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import pyttsx3

# Initialize text-to-speech engine

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 for male, 1 for female
engine.setProperty('rate', 150)

def discourse_aware_summary(text, sentence_count=2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    stemmer = Stemmer("english")
    summarizer = LsaSummarizer(stemmer)
    summarizer.stop_words = get_stop_words("english")
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary)

def summarize_text():
    try:
        text = text_input.get("1.0", tk.END)
        sentence_count = int(sentence_count_input.get())
        global summary
        summary = discourse_aware_summary(text, sentence_count)
        summary_output.delete("1.0", tk.END)
        summary_output.insert(tk.END, summary)
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number of sentences.")

# Speak the summarized text
def speak_summary():
    engine.say(summary)
    engine.runAndWait()


# Create the main window
root = tk.Tk()
root.title("Text Summarization and Speech")

title=tk.Label()
# Text input
tk.Label(root, text="Enter Text:").grid(row=0, column=0, padx=10, pady=10)
text_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=15)
text_input.grid(row=0, column=1, padx=10, pady=10)

# Sentence count input
tk.Label(root, text="Number of Sentences:").grid(row=1, column=0, padx=10, pady=10)
sentence_count_input = tk.Entry(root)
sentence_count_input.grid(row=1, column=1, padx=10, pady=10)

# Summary output
tk.Label(root, text="Summary:").grid(row=2, column=0, padx=10, pady=10)
summary_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=15)
summary_output.grid(row=2, column=1, padx=10, pady=10)

#speak button
image = Image.open("Web Dev\IMG\micpic.png")
# image = image.resize((50, 50))  # Resize to 50x50 pixels
photo = ImageTk.PhotoImage(image)
summarize_button = tk.Button(root, command=speak_summary,image=photo,border=0)
summarize_button.grid(row=2, column=2, padx=10, pady=10)

# Summarize button
summarize_button = tk.Button(root, text="Summarize", command=summarize_text,bg="orange",fg="black",padx=50,pady=5,border=0)
summarize_button.grid(row=6, column=1, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
