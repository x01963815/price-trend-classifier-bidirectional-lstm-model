
# coding: utf-8

# In[55]:


import matplotlib.pyplot as plt
import matplotlib
import numpy as np


# In[3]:


def find_contiguous_colors(colors):
    # finds the continuous segments of colors and returns those segments
    segs = []
    curr_seg = []
    prev_color = ''
    for c in colors:
        if c == prev_color or prev_color == '':
            curr_seg.append(c)
        else:
            segs.append(curr_seg)
            curr_seg = []
            curr_seg.append(c)
        prev_color = c
    segs.append(curr_seg) # the final one
    return segs


# In[50]:


def plot_multicolored_lines(x,y,colors):
    segments = find_contiguous_colors(colors)
    plt.figure(figsize=(20,10))
    start= 0
    for seg in segments:
        end = start + len(seg)
        plt.plot(x[start:end],y[start:end],lw=2,c=seg[0]) 
        start = end

