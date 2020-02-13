import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

youtube_vid= pd.read_csv('USvideos_modified.csv')
first_five=youtube_vid.head()

like=pd.DataFrame(zip(first_five.channel_title,first_five.likes,first_five.dislikes),columns=['channel_tittle','likes','dislikes'])
print(like)

like.plot.bar()

plt.bar(like['likes'],like['dislikes'])
plt.title("LIKES & DISLIKES")
plt.xlabel("Likes and dislikes")
plt.ylabel("COUNT")
plt.xticks(np.arange(0,5), like['channel_tittle'], rotation=90)
plt.savefig("bar_graph_likes_dislikes.png")

plt.show()



