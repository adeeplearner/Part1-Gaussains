import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def Gaussian1D(x, mu, sigma):
    ATerm = 1/(sigma * np.sqrt(2 * math.pi))
    BTerm = np.exp(-0.5 * ((x-mu)/sigma) ** 2)
    return ATerm * BTerm

def saveIntroFigure():
    x_grid = np.linspace(-6, 6, 100)
    y = Gaussian1D(x_grid, 0, 1)

    plt.figure()
    ax = plt.gca()
    plt.plot(x_grid, y)
    # ax.fill_between(x_grid,y,0, alpha=0.3, color='r')
    plt.grid()
    plt.savefig('figures/pt1/gaussian_1d_intro.png', dpi=100, bbox_inches='tight')

def saveVaryingMeanGif():
    from PIL import Image
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

    print('*' * 60)
    print('Generating gif for varying MU')
    print('*' * 60)
    x_grid = np.linspace(-6, 6, 100)
    fig = plt.figure()
    canvas = FigureCanvas(fig)
    sigma = 1.0
    MU = np.arange(-3, 3, 0.1)
    fig_list = []
    for idx, mu in enumerate(MU):
        print('%d/%d' % (idx, MU.shape[0]))
        y = Gaussian1D(x_grid, mu, sigma)
        ax = plt.gca()
        plt.plot(x_grid, y)
        # ax.fill_between(x_grid,y,0, alpha=0.3, color='r')
        plt.grid()
        plt.ylim([-0.01, 0.45])
        plt.title('Gaussian1D with $\mu=%0.1f$, $\sigma=%0.01f$' % (mu, sigma))
        #plt.savefig('figures/pt1/varyMeanGif/gaussian_1d_mu_%0.5d.png' % idx, dpi=100, bbox_inches='tight')
        canvas.draw()

        # figure to image help from: https://stackoverflow.com/questions/35355930/matplotlib-figure-to-image-as-a-numpy-array
        fig_image = np.frombuffer(canvas.tostring_rgb(), dtype='uint8')
        fig_list.append(Image.fromarray(fig_image.reshape(canvas.get_width_height()[::-1] + (3,))))
        plt.clf()
    
    # gif help from: https://note.nkmk.me/en/python-pillow-gif/
    fig_list[0].save('figures/pt1/varyMeanGif/gaussian_1d_mu.gif',
               save_all=True, append_images=fig_list[1:], optimize=False, duration=40, loop=0)
    print('*' * 60)
    print(' ')

def saveVaryingStdGif():
    from PIL import Image
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

    print('*' * 60)
    print('Generating gif for varying SIGMA')
    print('*' * 60)
    x_grid = np.linspace(-6, 6, 100)
    fig = plt.figure()
    canvas = FigureCanvas(fig)
    mu = 0
    SIGMA = np.arange(0.01, 3, 0.1)
    fig_list = []
    for idx, sigma in enumerate(SIGMA):
        print('%d/%d' % (idx, SIGMA.shape[0]))
        y = Gaussian1D(x_grid, mu, sigma)
        ax = plt.gca()
        plt.plot(x_grid, y)
        # ax.fill_between(x_grid,y,0, alpha=0.3, color='r')
        plt.grid()
        plt.title('Gaussian1D with $\mu=%0.1f$, $\sigma=%0.2f$' % (mu, sigma))
        # plt.savefig('figures/pt1/varyStdGif/gaussian_1d_std_%0.5d.png' % idx, dpi=100, bbox_inches='tight')
        canvas.draw()

        # figure to image help from: https://stackoverflow.com/questions/35355930/matplotlib-figure-to-image-as-a-numpy-array
        fig_image = np.frombuffer(canvas.tostring_rgb(), dtype='uint8')
        fig_list.append(Image.fromarray(fig_image.reshape(canvas.get_width_height()[::-1] + (3,))))
        plt.clf()
    
    # gif help from: https://note.nkmk.me/en/python-pillow-gif/
    fig_list[0].save('figures/pt1/varyStdGif/gaussian_1d_std.gif',
               save_all=True, append_images=fig_list[1:], optimize=False, duration=40, loop=0)
    print('*' * 60)
    print(' ')

if __name__ == '__main__':
    saveIntroFigure()
    saveVaryingMeanGif()
    saveVaryingStdGif()
