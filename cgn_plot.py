import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data_arac = pd.read_csv("arac_summary_neurites.csv")
data_ctrl = pd.read_csv("ctrl_summary_neurites.csv")


ctrl_count_list = list(data_ctrl["Mean_length"]) # Replace "Count" with "Mean_length" for neurite lengths
ctrl_list1 = ctrl_count_list[0:12]
ctrl_list2 = ctrl_count_list[12:24]
ctrl_list3 = ctrl_count_list[24:36]
ctrl_list4 = ctrl_count_list[36:]

arac_count_list = list(data_arac["Mean_length"]) # Replace "Count" with "Mean_length" for neurite lengths
arac_list1 = arac_count_list[0:12]
arac_list2 = arac_count_list[12:24]
arac_list3 = arac_count_list[24:36]
arac_list4 = arac_count_list[36:]

arac_dict = {
    "arac_1" : arac_list1,
    "arac_2" : arac_list2,
    "arac_3" : arac_list3,
    "arac_4" : arac_list4
}

ctrl_dict = {
    "ctrl_1" : ctrl_list1,
    "ctrl_2" : ctrl_list2,
    "ctrl_3" : ctrl_list3,
    "ctrl_4" : ctrl_list4
}


arac_df = pd.DataFrame(arac_dict)
arac_df_transposed = arac_df.transpose()
arac_mean = np.mean(arac_df_transposed)
arac_sd = np.std(arac_df_transposed)

ctrl_df = pd.DataFrame(ctrl_dict)
ctrl_df_transposed = ctrl_df.transpose()
ctrl_mean = np.mean(ctrl_df_transposed)
ctrl_sd = np.std(ctrl_df_transposed)


time_points = [i * 12 for i in range(0, 12)]
# time_points.insert(0, 0)

sns.set_style("white")
fig, ax = plt.subplots(figsize = (10, 6))

# Labels for y-axis
neurites_labels = list(range(0, 30, 5))
cells_labels = list(range(0, 12000, 2000))
attachment_labels = list(range(0, 10000, 2000))


ax.errorbar(range(len(arac_list1)), ctrl_mean, yerr = ctrl_sd, color = "grey", capsize = 6, linewidth = 0.5)
ax.plot(range(len(arac_list1)), ctrl_mean, color = "grey", linewidth = 5) # Plotting line
ax.plot(range(len(arac_list1)), ctrl_mean, "o", label = "Control", color = "grey", markersize = 12) # Plotting points

ax.errorbar(range(len(arac_list1)), arac_mean, yerr = arac_sd, color = "grey", capsize = 6, linewidth = 0.5)
ax.plot(range(len(arac_list1)), arac_mean, color = "darkgrey", linewidth = 5) # Plotting line
ax.plot(range(len(arac_list1)), arac_mean, "^", label = "AraC", color = "grey", markersize = 12) # Plotting triangles

ax.set_ylim(0, 29) # Adjust y-axis
ax.set_title("Neurite length", size = 40) # Plot title
ax.set_xticks(list(range(12)))
ax.set_xticklabels(time_points, size = 22)
ax.set_yticklabels(cells_labels, size = 25) # Y-axis tick labels
ax.set_xlabel("Hours", size = 30, labelpad = 10)
ax.set_ylabel("Neurite length (px)", size = 30, labelpad = 10)

ax.legend(loc = 'upper left', shadow = True, prop = {"size":16})

fig.tight_layout()
plt.savefig("CGN_arac_neurite.png")
