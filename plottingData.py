import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from movingAvg import movingAvg

data = pd.read_csv('newOrderedFile.csv', dtype = str, index_col = 0)
#print(data)
plt.figure(figsize = (12.0, 4.8), dpi=500)
plt.plot(data['DPR Approx'].astype(float), alpha = 0.3)
plt.plot(np.arange(3, len(data.index)-3), movingAvg(data['DPR Approx'].astype(float), 3), label = '7 Day Average')
plt.xticks([-18, 13, 44, 75, 102, 133, 162,\
			192, 222, 252, 283, 310, 340,\
			368, 395, 426], ["Nov '20", "Dec '20", \
			"Jan '21", "Feb '21", "Mar '21", "Apr '21",\
			"May '21", "Jun '21", "Jul '21", "Aug '21",\
			"Sep '21", "Oct '21", "Nov '21", "Dec '21",\
			"Jan '22", "Feb '22"])
plt.xlabel('Time', fontsize = 20)
plt.ylabel('Approximate Positivity Rate', fontsize = 16)
plt.legend()
plt.show()