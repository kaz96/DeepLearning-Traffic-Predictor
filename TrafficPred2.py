from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import os
import pandas as pd
import matplotlib.animation as animation
import matplotlib as mpl
import numpy as np
import datetime

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)


fig=plt.figure()


cwd = os.getcwd()
direct = (cwd + "/roads/ausroad")


map = Basemap(projection = 'mill',
              llcrnrlat=-37.868924,
              llcrnrlon=144.861161,
              urcrnrlat=-37.772217,
              urcrnrlon=145.087438)


HawLat, HawLong =  -37.8076153,144.9703478

xpt,ypt = map(HawLong,HawLat)

map.fillcontinents()
map.readshapefile(direct,'roads')




plt.annotate("LATROBE  ST SW OF VICTORIA ST",(xpt,ypt),xytext=(5, 5), textcoords='offset points')




csv = pd.read_csv("processed2.csv")



# max_cars =np.max(cars.astype(np.int))
# min_cars =np.min(cars.astype(np.int))
#
# # Time 00:00:01,00:00:02


# ONLY Time Columns
date=csv.loc[:,"dt_general"]


removecolumns = csv[csv.columns.difference(['nb_scats_site','ds_location','dt_general','lane_mvt','nb_detector'])]
noOfColumns=len(removecolumns.columns)




datetime.datetime.today().strftime('%A')


print(date.shape[0])

# max_cars = removerows.max(axis=1)
# min_cars = removerows.min(axis=1)
removerows = removecolumns.iloc[[0]]

# COLOUR MAP
norm = plt.Normalize(vmin=0, vmax=100)
pointcolors = plt.cm.ScalarMappable(norm)
col = pointcolors.to_rgba(removerows)

cax = plt.imshow(col, interpolation='nearest')
# sc = plt.scatter(xpt, ypt,zorder=10)
cm = plt.colorbar(cax)

for index,dateindex in enumerate(date):
    print(index)
    print(dateindex)
    plt.xlabel("Date: " + date[index])
    removerows = removecolumns.iloc[[index]]
    col = pointcolors.to_rgba(removerows)

    plots=[]
    test = 0
    def animate(i):

        for j, a in enumerate(plots):
            a.remove()
        plots[:] = []

        sc = plt.scatter(xpt, ypt,color=col[0][i],zorder=10)
        print(removecolumns.columns[i])
        plots.append(sc)
        plt.title('Time:' + removerows.columns[i])
        return sc

    ani = animation.FuncAnimation(fig, animate, frames=noOfColumns, interval=20,repeat=False,save_count=noOfColumns)

    ani.save('video/'+str(index)+'.mp4', writer=writer)



   # plt.show()






