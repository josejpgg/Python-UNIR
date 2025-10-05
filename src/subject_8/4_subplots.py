import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2)
# activar las grillas en cada subplot de una figura
for ax in axs.flat:
    ax.grid(True)








fig, axs = plt.subplots(2, 3)
# ajustar el espacio entre subplots
plt.subplots_adjust(wspace=0.4, hspace=0.6)









import matplotlib.gridspec as gridspec
# control más detallado sobre la disposición de subplots
gs = gridspec.GridSpec(3, 3)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1, :-1])
ax3 = plt.subplot(gs[1:, -1])
ax4 = plt.subplot(gs[-1, 0])
ax5 = plt.subplot(gs[-1, -2])


