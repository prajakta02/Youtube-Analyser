import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

youtube_vid= pd.read_csv('USvideos_modified.csv')
first_five=youtube_vid.head()

channel_colors = ['#034694','#FFA500','#5CBFEB','#008000','#EF0107']
plt.bar(x=np.arange(1,6) , height=first_five['subscriber'],color=channel_colors)
plt.title("SUBSCRIBERS")
plt.xticks(np.arange(1,6), first_five['channel_title'], rotation=90)
plt.xlabel("CHANNEL NAME")
plt.ylabel("NO OF SUBSCRIBERS")
plt.savefig("bar_graph_no_of_subscribers.png")

plt.show()