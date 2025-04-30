import numpy as np
import matplotlib.pyplot as plt

sims    = ['EAGLE','Illustris','TNG','SIMBA']
markers = ['P','d','o','X']
offsets = [+0.08,+0.04,-0.04,-0.08]

fig = plt.figure(figsize=(10,5))
ax  = plt.gca()

for index, sim in enumerate(sims):
    color  = 'C%s' %index
    marker = markers[index]
    
    x = np.arange(0,9) + offsets[index]
    y = np.load(f'./{sim}/median_grad.npy') ## Medians
    y_down = np.load(f'./{sim}/16th_percentile_grad.npy') ## 16th percentile
    y_up   = np.load(f'./{sim}/84th_percentile_grad.npy') ## 84th percentile

    ax.errorbar( x, y, yerr=(y-y_down,y_up-y), capsize=3, color=color, marker=marker, linestyle='none', markeredgecolor='k',
                 markersize=8, capthick=1.5, elinewidth=1.5, zorder=100, label=sim)
    
    ax.errorbar( x, y, yerr=(y-y_down,y_up-y), capsize=4, color='k', marker=marker, linestyle='none',
                 markersize=8, capthick=3, elinewidth=3, zorder=99)
    
ax.set_xlabel('Redshift')
ax.set_ylabel('Gradient [dex/kpc]')

xmin, xmax = ax.get_xlim()
ax.set_xlim(xmax, xmin)

plt.legend(frameon=False,loc='lower right')

plt.tight_layout()
plt.savefig('test_make_plot.pdf',bbox_inches='tight')