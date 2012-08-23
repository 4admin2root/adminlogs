# do this before importing pylab or pyplot
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib
import StringIO,Image

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1,2,3])
fig.savefig('test.png')

imgdata = StringIO.StringIO()
fig.savefig(imgdata, format='png')
imgdata.seek(0) # rewind the data
im = Image.open(imgdata)
