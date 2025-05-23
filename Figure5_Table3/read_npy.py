import numpy as np
import matplotlib.pyplot as plt

sims    = ['TNG50-1','TNG50-2','TNG50-3','TNG100-1','TNG100-2','TNG300-1']
markers = ['*','X','o','p','d','P']
offsets = [+0.09,+0.06,+0.03,-0.03,-0.06,-0.09]

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