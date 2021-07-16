from PIL import Image, ImageDraw, ImageFont
import pandas as pd

df = pd.read_csv('list1.csv', encoding='latin-1')  # To read the csv file
font = ImageFont.truetype('arial.ttf', 40)  # To set the font type and font size
for index, j in df.iterrows():  # To do the iterations through the rows
    img = Image.open("certificate.jpg")  # To open the template
    draw = ImageDraw.Draw(img)  # now getting the img ready on which we will draw
    draw.text(xy=(500, 390), text='{}'.format(j['name']), fill=(11, 216, 255), font=font)  # What things will be drawn to be written here
    img.save('pictures/{}.jpg'.format(j['name']))  # To save the image in the particular path