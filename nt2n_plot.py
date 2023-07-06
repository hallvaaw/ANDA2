import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data_arac = pd.read_csv("nt2n_arac_summary_cells.csv")
data_ctrl = pd.read_csv("nt2n_ctrl_summary_cells.csv")


ctrl_count_list = list(data_ctrl["Count"]) # Replace "Count" with "Mean_length" for neurite lengths
ctrl_list1 = ctrl_count_list[0:12]
ctrl_list2 = ctrl_count_list[12:24]
ctrl_list3 = ctrl_count_list[24:36]
ctrl_list4 = ctrl_count_list[36:48]
ctrl_list5 = ctrl_count_list[48:60]
ctrl_list6 = ctrl_count_list[60:72]
ctrl_list7 = ctrl_count_list[72:84]
ctrl_list8 = ctrl_count_list[84:96]
ctrl_list9 = ctrl_count_list[96:108]
ctrl_list10 = ctrl_count_list[108:120]
ctrl_list11 = ctrl_count_list[120:132]
ctrl_list12 = ctrl_count_list[132:144]
ctrl_list13 = ctrl_count_list[144:156]

arac_count_list = list(data_arac["Count"]) # Replace "Count" with "Mean_length" for neurite lengths
arac_list1 = arac_count_list[0:12]
arac_list2 = arac_count_list[12:24]
arac_list3 = arac_count_list[24:36]
arac_list4 = arac_count_list[36:48]
arac_list5 = arac_count_list[48:60]
arac_list6 = arac_count_list[60:72]
arac_list7 = arac_count_list[72:84]
arac_list8 = arac_count_list[84:96]
arac_list9 = arac_count_list[96:108]
arac_list10 = arac_count_list[108:120]
arac_list11 = arac_count_list[120:132]
arac_list12 = arac_count_list[132:144]
arac_list13 = arac_count_list[144:156]

arac_dict = {
    "arac_1" : arac_list1,
    "arac_2" : arac_list2,
    "arac_3" : arac_list3,
    "arac_4" : arac_list4,
    "arac_5" : arac_list5,
    "arac_6" : arac_list6,
    "arac_7" : arac_list7,
    "arac_8" : arac_list8,
    "arac_9" : arac_list9,
    "arac_10" : arac_list10,
    "arac_11" : arac_list11,
    "arac_12" : arac_list12,
    "arac_13" : arac_list13
}

ctrl_dict = {
    "ctrl_1" : ctrl_list1,
    "ctrl_2" : ctrl_list2,
    "ctrl_3" : ctrl_list3,
    "ctrl_4" : ctrl_list4,
    "ctrl_5" : ctrl_list5,
    "ctrl_6" : ctrl_list6,
    "ctrl_7" : ctrl_list7,
    "ctrl_8" : ctrl_list8,
    "ctrl_9" : ctrl_list9,
    "ctrl_10" : ctrl_list10,
    "ctrl_11" : ctrl_list11,
    "ctrl_12" : ctrl_list12,
    "ctrl_13" : ctrl_list13
}



arac_df = pd.DataFrame(arac_dict)
arac_df_transposed = arac_df.transpose()
arac_mean = np.mean(arac_df_transposed)
arac_sd = np.std(arac_df_transposed)

ctrl_df = pd.DataFrame(ctrl_dict)
ctrl_df_transposed = ctrl_df.transpose()
ctrl_mean = np.mean(ctrl_df_transposed)
ctrl_sd = np.std(ctrl_df_transposed)


time_points = [i * 6 for i in range(0, 12)]
# time_points.insert(0, 0)

sns.set_style("white")
fig, ax = plt.subplots(figsize = (10, 6))

# Labels for y-axis
# neurites_labels = list(range(0, 80, 10))
cells_labels = list(range(0, 150, 20))
# attachment_labels = list(range(0, 16, 2))


ax.errorbar(range(len(arac_list1)), ctrl_mean, yerr = ctrl_sd, color = "grey", capsize = 6, linewidth = 0.5)
ax.plot(range(len(arac_list1)), ctrl_mean, color = "grey", linewidth = 5) # Plotting line
ax.plot(range(len(arac_list1)), ctrl_mean, "o", label = "Control", color = "grey", markersize = 12) # Plotting points

ax.errorbar(range(len(arac_list1)), arac_mean, yerr = arac_sd, color = "grey", capsize = 6, linewidth = 0.5)
ax.plot(range(len(arac_list1)), arac_mean, color = "darkgrey", linewidth = 5) # Plotting line
ax.plot(range(len(arac_list1)), arac_mean, "^", label = "AraC", color = "grey", markersize = 12) # Plotting triangles

ax.set_ylim(0, 145) # Adjust y-axis
ax.set_title("Cell body count", size = 40) # Plot title
ax.set_xticks(list(range(12)))
ax.set_xticklabels(time_points, size = 22)
ax.set_yticklabels(cells_labels, size = 25) # Y-axis tick labels
ax.set_xlabel("Hours", size = 30, labelpad = 10)
ax.set_ylabel("Cell bodies", size = 30, labelpad = 10)

ax.legend(loc = 'upper left', shadow = True, prop = {"size":16})

fig.tight_layout()
plt.savefig("NT2N_arac_cells.png")
