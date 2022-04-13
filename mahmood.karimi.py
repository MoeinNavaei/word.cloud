
from wordcloud_fa import WordCloudFa

wc = WordCloudFa()
with open(r'C:\Users\PC\Desktop\123.txt', encoding='utf-8') as file:
    text = file.read()
print(text)
wc = WordCloudFa(background_color="white", width=1200, height=800, include_numbers=False,  max_words=50, min_font_size=1, max_font_size=500)

#wc.add_stop_words(['چیز' , 'همه' ])
word_cloud = wc.generate(text)
#frequencies = wc.process_text(text)
#word_cloud = wc.generate_from_frequencies(frequencies)
print(text)
#image = word_cloud.to_image()
#image.show()
#image.save('mahmood.telegram.png')