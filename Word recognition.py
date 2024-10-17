import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag

# دانلود داده‌های مورد نیاز nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# متنی که می‌خواهید پردازش کنید
text = """
Natural Language Processing (NLP) is a field of artificial intelligence that gives computers the ability to understand text and spoken words in much the same way human beings can.
"""

# تقسیم متن به جملات
sentences = sent_tokenize(text)

# تقسیم جملات به کلمات
words = word_tokenize(text)

# حذف کلمات توقف (Stopwords) که برای تحلیل مهم نیستند
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

# برچسب‌گذاری کلمات کلیدی (Parts of Speech Tagging)
pos_tags = pos_tag(filtered_words)

# نمایش نتایج
print("Sentences:", sentences)
print("Words:", words)
print("Filtered Words (without stopwords):", filtered_words)
print("POS Tags:", pos_tags)
