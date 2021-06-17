import matplotlib.pyplot as plt
import numpy as np


#######################################################################
# setup for figure
#######################################################################
fig = plt.figure(dpi=300)

# labels for x-axis / y-axis
x_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
y_labels = ['0', '40', '80', '120', '160', '200']

# location for x labels
x_ticks = np.arange(len(x_labels))
y_ticks = np.linspace(0.0, 200.0, 6)

# the width of the bars
width = 0.25

f_size = 6
legend_size = 10

#######################################################################
# sub-figure (3, 3, 1)
#######################################################################

y11 = [34.9, 59.45, 83.6, 107.9, 132.05, 156.0, 178.5, 196.65, 200.0, 200.0]
y12 = [25.15, 50.35, 73.9, 99.4, 126.5, 152.25, 178.2, 196.65, 200.0, 200.0]
y13 = [35.1, 58.05, 81.4, 104.75, 127.6, 151.15, 173.25, 191.9, 200.0, 200.0]

ax1 = plt.subplot(3, 3, 1)

# set_xticks
ax1.set_xticks(x_ticks)
ax1.set_yticks(y_ticks)

ax1.set_xticklabels(x_labels, fontsize=f_size)
ax1.set_yticklabels(y_labels, fontsize=f_size)

# set title of sub-figure (3, 3, 1)
ax1.set_title("ratio=1.2 \u03B8=0.2", fontsize=f_size)

# draw a dummy point without color
plt.scatter(1.0, 200.0, marker='o', s=200, facecolors='none')

# draw bars for each algorithm
rects1 = ax1.bar(x_ticks - width, y11, width, label='GDA-RH')
rects2 = ax1.bar(x_ticks, y12, width, label='GDA-RO')
rects3 = ax1.bar(x_ticks + width, y13, width, label='ACDA')


# legend of figures
ax1.legend((rects1, rects2, rects3),     # The line objects
           ('GDA-RH', 'GDA-RO', 'ACDA'),   # The labels for each line
           loc="upper left",   # Position of legend
           borderaxespad=0.1,    # Small spacing around legend box
           # title="Legend Title",  # Title for the legend
           fontsize= 5
           )

# x-axis / y-axis of figures
fig.text(0.5, 0.04, 'Rank of hospitals', ha='center', va='center', fontsize=legend_size)
fig.text(0.03, 0.5, 'Number of matched doctors', ha='center', va='center', rotation='vertical', fontsize=legend_size)




#######################################################################
# sub-figure (3, 3, 2)
#######################################################################

y21 = [67.25, 98.85, 123.5, 147.0, 167.0, 184.6, 196.3, 199.95, 200.0, 200.0]
y22 = [40.85, 76.35, 108.75, 140.95, 169.8, 187.45, 197.35, 199.95, 200.0, 200.0]
y23 = [69.9, 98.4, 122.0, 144.0, 163.2, 180.85, 192.85, 198.95, 200.0, 200.0]

ax2 = plt.subplot(3, 3, 2)

# set_xticks
ax2.set_xticks(x_ticks)
ax2.set_yticks(y_ticks)

ax2.set_xticklabels(x_labels, fontsize=f_size)
ax2.set_yticklabels(y_labels, fontsize=f_size)

# set title of sub-figure (3, 3, 2)
ax2.set_title("ratio=1.2 \u03B8=0.5", fontsize=f_size)

# draw bars for each algorithm
rects1 = ax2.bar(x_ticks - width, y21, width, label='GDA-RH')
rects2 = ax2.bar(x_ticks, y22, width, label='GDA-RO')
rects3 = ax2.bar(x_ticks + width, y23, width, label='ACDA')

# draw a dummy point without color
plt.scatter(1.0, 1.0, marker='o', s=200, facecolors='none')


#######################################################################
# sub-figure (3, 3, 3)
#######################################################################

y31 = [150.65, 177.7, 190.6, 195.75, 198.5, 199.5, 199.95, 200.0, 200.0, 200.0]
y32 = [128.7, 178.7, 195.05, 199.25, 199.95, 200.0, 200.0, 200.0, 200.0, 200.0]
y33 = [146.0, 173.6, 187.15, 193.95, 197.45, 199.05, 199.85, 200.0, 200.0, 200.0]

ax3 = plt.subplot(3, 3, 3)

# set_xticks
ax3.set_xticks(x_ticks)
ax3.set_yticks(y_ticks)

ax3.set_xticklabels(x_labels, fontsize=f_size)
ax3.set_yticklabels(y_labels, fontsize=f_size)

# set title of sub-figure (3, 3, 3)
ax3.set_title("ratio=1.2 \u03B8=0.8", fontsize=f_size)

# draw bars for each algorithm
rects1 = ax3.bar(x_ticks - width, y31, width, label='GDA-RH')
rects2 = ax3.bar(x_ticks, y32, width, label='GDA-RO')
rects3 = ax3.bar(x_ticks + width, y33, width, label='ACDA')

# draw a dummy point without color
plt.scatter(1.0, 1.0, marker='o', s=200, facecolors='none')



#######################################################################
# sub-figure (3, 3, 4)
#######################################################################

y41 = [41.55, 73.2, 102.45, 132.25, 160.4, 186.95, 199.4, 200.0, 200.0, 200.0]
y42 = [32.85, 64.6, 96.15, 129.85, 161.15, 187.45, 199.35, 200.0, 200.0, 200.0]
y43 = [34.65, 58.85, 80.8, 103.05, 126.85, 150.6, 173.65, 191.9, 200.0, 200.0]

ax4 = plt.subplot(3, 3, 4)

# set_xticks
ax4.set_xticks(x_ticks)
ax4.set_yticks(y_ticks)

ax4.set_xticklabels(x_labels, fontsize=f_size)
ax4.set_yticklabels(y_labels, fontsize=f_size)

# set title of sub-figure (3, 3, 4)
ax4.set_title("ratio=1.5 \u03B8=0.2", fontsize=f_size)

# draw bars for each algorithm
rects1 = ax4.bar(x_ticks - width, y41, width, label='GDA-RH')
rects2 = ax4.bar(x_ticks, y42, width, label='GDA-RO')
rects3 = ax4.bar(x_ticks + width, y43, width, label='ACDA')

# draw a dummy point without color
plt.scatter(1.0, 1.0, marker='o', s=200, facecolors='none')



#######################################################################
# sub-figure (3, 3, 5)
#######################################################################

y51 = [74.3, 111.35, 143.0, 168.05, 187.45, 197.5, 199.85, 200.0, 200.0, 200.0]
y52 = [53.0, 98.95, 138.55, 169.95, 189.25, 197.8, 199.8, 200.0, 200.0, 200.0]
y53 = [68.25, 99.15, 123.15, 143.3, 163.4, 181.0, 192.05, 199.4, 200.0, 200.0]

ax5 = plt.subplot(3, 3, 5)

# set_xticks
ax5.set_xticks(x_ticks)
ax5.set_yticks(y_ticks)

ax5.set_xticklabels(x_labels, fontsize=f_size)
ax5.set_yticklabels(y_labels, fontsize=f_size)

# set title of sub-figure (3, 3, 5)
ax5.set_title("ratio=1.5 \u03B8=0.5", fontsize=f_size)

# draw bars for each algorithm
rects1 = ax5.bar(x_ticks - width, y51, width, label='GDA-RH')
rects2 = ax5.bar(x_ticks, y52, width, label='GDA-RO')
rects3 = ax5.bar(x_ticks + width, y53, width, label='ACDA')

# draw a dummy point without color
plt.scatter(1.0, 1.0, marker='o', s=200, facecolors='none')


#######################################################################
# sub-figure (3, 3, 6)
#######################################################################

y61 = [163.5, 190.6, 198.8, 199.75, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0]
y62 = [161.25, 193.25, 198.9, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0]
y63 = [149.15, 175.2, 188.65, 195.15, 198.2, 199.45, 199.9, 200.0, 200.0, 200.0]

ax6 = plt.subplot(3, 3, 6)

# set_xticks
ax6.set_xticks(x_ticks)
ax6.set_yticks(y_ticks)

ax6.set_xticklabels(x_labels, fontsize=f_size)
ax6.set_yticklabels(y_labels, fontsize=f_size)

# set title of sub-figure (3, 3, 6)
ax6.set_title("ratio=1.5 \u03B8=0.8", fontsize=f_size)

# draw bars for each algorithm
rects1 = ax6.bar(x_ticks - width, y61, width, label='GDA-RH')
rects2 = ax6.bar(x_ticks, y62, width, label='GDA-RO')
rects3 = ax6.bar(x_ticks + width, y63, width, label='ACDA')

# draw a dummy point without color
plt.scatter(1.0, 1.0, marker='o', s=200, facecolors='none')



#######################################################################
# sub-figure (3, 3, 7)
#######################################################################

y71 = [50.15, 88.05, 123.7, 160.45, 189.35, 199.45, 200.0, 200.0, 200.0, 200.0]
y72 = [45.3, 85.4, 124.25, 162.3, 188.85, 199.1, 199.95, 200.0, 200.0, 200.0]
y73 = [34.95, 58.95, 82.15, 105.5, 126.9, 151.1, 172.6, 191.6, 200.0, 200.0]

ax7 = plt.subplot(3, 3, 7)

# set_xticks
ax7.set_xticks(x_ticks)
ax7.set_yticks(y_ticks)

ax7.set_xticklabels(x_labels, fontsize=f_size)
ax7.set_yticklabels(y_labels, fontsize=f_size)

# set title of sub-figure (3, 3, 7)
ax7.set_title("ratio=2.0 \u03B8=0.2", fontsize=f_size)

# draw bars for each algorithm
rects1 = ax7.bar(x_ticks - width, y71, width, label='GDA-RH')
rects2 = ax7.bar(x_ticks, y72, width, label='GDA-RO')
rects3 = ax7.bar(x_ticks + width, y73, width, label='ACDA')

# draw a dummy point without color
plt.scatter(1.0, 1.0, marker='o', s=200, facecolors='none')




#######################################################################
# sub-figure (3, 3, 8)
#######################################################################

y81 = [91.9, 138.9, 174.85, 192.3, 197.6, 199.5, 200.0, 200.0, 200.0, 200.0]
y82 = [83.4, 138.45, 175.45, 192.25, 197.5, 199.45, 200.0, 200.0, 200.0, 200.0]
y83 = [67.8, 96.85, 123.9, 146.65, 165.0, 181.6, 194.7, 199.95, 200.0, 200.0]

ax8 = plt.subplot(3, 3, 8)

# set_xticks
ax8.set_xticks(x_ticks)
ax8.set_yticks(y_ticks)

ax8.set_xticklabels(x_labels, fontsize=f_size)
ax8.set_yticklabels(y_labels, fontsize=f_size)

# set title of sub-figure (3, 3, 8)
ax8.set_title("ratio=2.0 \u03B8=0.5", fontsize=f_size)

# draw bars for each algorithm
rects1 = ax8.bar(x_ticks - width, y81, width, label='GDA-RH')
rects2 = ax8.bar(x_ticks, y82, width, label='GDA-RO')
rects3 = ax8.bar(x_ticks + width, y83, width, label='ACDA')

# draw a dummy point without color
plt.scatter(1.0, 1.0, marker='o', s=200, facecolors='none')




#######################################################################
# sub-figure (3, 3, 9)
#######################################################################

y91 = [178.75, 197.1, 199.55, 199.9, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0]
y92 = [178.7, 196.65, 199.45, 199.9, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0]
y93 = [146.25, 174.35, 187.75, 194.35, 197.7, 199.45, 200.0, 200.0, 200.0, 200.0]

ax9 = plt.subplot(3, 3, 9)

# set_xticks
ax9.set_xticks(x_ticks)
ax9.set_yticks(y_ticks)

ax9.set_xticklabels(x_labels, fontsize=f_size)
ax9.set_yticklabels(y_labels, fontsize=f_size)

# set title of sub-figure (3, 3, 9)
ax9.set_title("ratio=2.0 \u03B8=0.8", fontsize=f_size)

# draw bars for each algorithm
rects1 = ax9.bar(x_ticks - width, y91, width, label='GDA-RH')
rects2 = ax9.bar(x_ticks, y92, width, label='GDA-RO')
rects3 = ax9.bar(x_ticks + width, y93, width, label='ACDA')

# draw a dummy point without color
plt.scatter(1.0, 1.0, marker='o', s=200, facecolors='none')


plt.show()
