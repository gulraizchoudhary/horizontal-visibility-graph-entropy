# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 15:53:41 2024

@author: Gulraiz Iqbal Choudhary

#G. I. Choudhary, W. Aziz, I.R. Khan, S. Rahardja and P. Fränti, 
#“Analysing the dynamics of inter beat interval time series using grouped horizontal visibility graph”, 
#IEEE Access, 7 (1), 9926-9934, December 2019. https://www.doi.org/10.1109/ACCESS.2018.2890542
#
#
#G. I. Choudhary, W. Aziz, and P. Fränti, 
#“Detection of time irreversibility in interbeat interval time series by visible and nonvisible motifs from horizontal visibility graph”, 
#Biomedical Signal Processing and Control, 62, 10205, 2020. https://doi.org/10.1016/j.bspc.2020.102052
#
#
"""

import numpy as np
import matplotlib.pyplot as plt

#Transform time series into horizontal visibility graph
def construct_hvg(time_series):
    n = len(time_series)
    hvg = np.zeros((n, n), dtype=bool)

    for i in range(n):
        for j in range(i+2, n):
            if (np.all(time_series[i+1:j] < time_series[i]) and np.all(time_series[i+1:j] < time_series[j])):
                hvg[i, j] = True
                
    return hvg

#count number of edges in the given window
def count_edges(hvg):
    return np.sum(hvg)


#count the motifs having the same number of edges.
def count_occurrences(edges):
    counts = []
    for num in range(max(edges) + 1):  # Assuming the numbers in the list start from 0
        counts.append(edges.count(num))
    return counts


#Shannon entropy on grouped horizontal visibility graph
def shannon_entropy(frequencies):
    total_count = sum(frequencies)
    probabilities = [count / total_count for count in frequencies]
    entropy = -sum(prob * np.log2(prob) for prob in probabilities if prob != 0)
    return entropy


def kl_divergence(p, q):
    # Compute KL divergence
    if p == 0 or q == 0:
        return 0  # or any other appropriate value when division by zero occurs
    
    return p * np.log(p / q)
    

# Example time series
series = np.array([6,5,6,4,6,1,6,1,1,1,1,1])

n = len(series)

window = 6

edges = []
for i in range(0, n-window+1):
    time_series=series[i:i+window]

    # Construct horizontal visibility graph
    hvg = construct_hvg(time_series)
    
    # Count the number of edges
    num_edges = count_edges(hvg)
    print("Number of edges in the HVG"+ str(i)+": "+str(time_series), num_edges)
    
    edges.append(num_edges)
    # Plot the time series and the HVG
    plt.subplot(1, 2, 1)
    plt.plot(time_series, marker='o')
    plt.title('Time Series window '+str(i))
    
    plt.subplot(1, 2, 2)
    plt.imshow(hvg, cmap='binary', origin='upper')
    plt.title('Horizontal Visibility Graph')
    plt.show()

frequency = count_occurrences(edges)
print("Grouped Horizontal Visibility Graph Entropy: "+str(shannon_entropy(frequency)))


visible_motifs = np.count_nonzero(edges)
non_visible_motif = abs(len(edges)-visible_motifs)
p = visible_motifs/len(edges) 
q = non_visible_motif/len(edges)
divergence = kl_divergence(p, q)
print("Time Irreversibility of Visible and Non-visible: "+str(divergence))
