import matplotlib.pyplot as plt

divs = ["", "DIV 1", "DIV 2", "DIV 3", "", ""]
manuell = [-60, 482.28125, 3291.33125, 2238.31875, -60, -60] # Keep the -60
anda = [-60, 190.78848, 730.991059999997, 1389.28842, -60, -60] # Keep the -60
nt = [-60, 310.63670805, 1023.327094, 958.317503, -60, -60] # Keep the -60

plt.figure(figsize = (10, 8), facecolor = "white")
plt.plot(divs, manuell, "x", label = "Manual", markersize = 12, color = "#060606")
plt.plot(divs, anda, "o", label = "ANDA", markersize = 12, color = "#060606")
plt.plot(divs, nt, "s", label = "NeuroTrack", markersize = 10, color = "#060606")
plt.ylim(0, 3900) # y-scale axis limit
plt.xlim(0, 4)
plt.yticks(size = 16)
plt.xticks(size = 16)
plt.ylabel("Length in µm", size = 20)
plt.legend(fontsize = 15)
# plt.savefig("neurite_comp.png")
