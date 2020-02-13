import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

youtube_vid= pd.read_csv('USvideos_modified.csv')
first_five=youtube_vid.head()

views_channel=pd.DataFrame(zip(first_five.channel_title,first_five.views),columns=['channel_title','views'])
print(views_channel)

plt.pie(views_channel['views'], labels = views_channel['channel_title'], autopct ='% 1.1f %%', shadow = True)
plt.axis('equal')
plt.tight_layout()
plt.savefig("pie_chart_no_of_views.png")

plt.show()