from os import path
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import sys

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Usage:\n\tpython pri-tutor.py path_to_processed_text_file.txt wordcloud_background_image(optional)\n\t[And the result will be named as path_to_processed_text_file.png]")
else:
    if len(sys.argv) == 3:
        backgroundImg = sys.argv[2]
        customImg = np.array(Image.open(backgroundImg))
    else:
        customImg = None

    text = sys.argv[1]

    f = open(text).read()

    #customImg = np.array(Image.open(backgroundImg))


    wc = WordCloud(mask=customImg).generate(f)

    plt.imshow(wc)
    plt.axis("off")
    plt.show()

    resImgName = sys.argv[1].replace('.txt', '.png')
    wc.to_file(resImgName)

