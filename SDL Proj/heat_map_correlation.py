import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

youtube_vid = pd.read_csv('USvideos_modified.csv')

corrmat = youtube_vid.corr()

cg = sns.clustermap(corrmat, cmap="YlGnBu", linewidths=0.1)
plt.setp(cg.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
plt.savefig("heat_map_correlation.png")

plt.show()
