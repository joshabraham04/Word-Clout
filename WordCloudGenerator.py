###################################
# RUN THE FUNCTION FROM THIS FILE #
###################################

# importing all the libraries required for this WordCloud generator
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import wordcloud
from ElectRobo import wordMap, imageName, candidateName

mask = np.array(Image.open("Masks/" + imageName))

imageColors = wordcloud.ImageColorGenerator(mask)

AK = wordcloud.WordCloud(background_color="white", mask=mask, contour_color='firebrick', contour_width=3,
                         max_words=1000000)
AK.generate(wordMap)
AK.to_file('WordClouds/' + candidateName + '_WordCloud.png')

plt.imshow(AK, interpolation='bilinear')
plt.axis("off")
plt.show()