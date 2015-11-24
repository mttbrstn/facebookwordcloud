#!/usr/bin/python2
import matplotlib.pyplot as plt
from scipy.misc import imread
from wordcloud import WordCloud, ImageColorGenerator
from bs4 import BeautifulSoup

url = open('FILE', 'r')
html = url.read()
url.close()

soup = BeautifulSoup(html, "lxml")

commentdiv = []
for line in soup.find_all(attrs={"class": "comment"}):
    commentdiv.append(line.get_text())
full_text = str(commentdiv)

exclude = ('\'', '\"', 'u\'', 'u\"')
words = ''.join(ch for ch in full_text if ch not in exclude)
image_coloring = imread("IMAGE")

wc = WordCloud(font_path="FONT",
               background_color="white", scale=4, max_words=5000,
               max_font_size=72, random_state=42)

# generate word cloud
wc.generate(words)

image_colors = ImageColorGenerator(image_coloring)
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
plt.figure()
plt.axis("off")
wc.to_file("wordcloud.png")
