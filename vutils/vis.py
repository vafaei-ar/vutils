
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animale_array(xm,fname,lbls=None,cmap='gray',figsize=(7,7),fps=25,vmin=None,vmax=None):

    '''
    This function helps to make an animation from a (2+1+1)d array (xy+t+c)
    
    '''
    # from IPython.display import HTML
    fig, ax = plt.subplots(figsize=figsize)

    ax.set_xlim((0, xm.shape[1]))
    ax.set_ylim((0, xm.shape[2]))
    ax.axis('off')
    if not lbls is None:
        plt.title(lbls[0],fontsize=10)
    plt.tight_layout()

    im = ax.imshow(np.flipud(xm[0,:,:]),cmap=cmap,vmin=vmin,vmax=vmax)

    pbar = tqdm(total=len(xm))
    def init():
        im.set_data(np.flipud(xm[0,:,:]))
        if not lbls is None:
            plt.title(lbls[0],fontsize=10)
        return (im,)

    # animation function. This is called sequentially
    def animate(i):
        pbar.update(1)
        data_slice = np.flipud(xm[i,:,:])
        im.set_data(data_slice)
        if not lbls is None:
            plt.title(lbls[i],fontsize=10)
        return (im,)

    # call the animator. blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=xm.shape[0], interval=200, blit=True)

    # HTML(anim.to_html5_video())

    # Set up formatting for the movie files
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=fps, metadata=dict(artist='Me'), bitrate=1000)
    anim.save(fname+'.mp4', writer=writer)

