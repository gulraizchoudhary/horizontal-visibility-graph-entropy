import numpy as np
import matplotlib.pyplot as plt

def construct_hvg(time_series):
    n = len(time_series)
    hvg = np.zeros((n, n), dtype=bool)

    for i in range(n):
        for j in range(i+2, n):
            if (np.all(time_series[i+1:j] < time_series[i]) and np.all(time_series[i+1:j] < time_series[j])):
                hvg[i, j] = True
                
    return hvg

def count_edges(hvg):
    return np.sum(hvg)


def shannon_entropy(frequencies):
    total_count = sum(frequencies)
    probabilities = [count / total_count for count in frequencies]
    entropy = -sum(prob * np.log2(prob) for prob in probabilities if prob != 0)
    return entropy


def kl_divergence(p, q):
    
    # Compute KL divergence
    return p * np.log(p / q)
    

# Example time series
series = np.array([6,5,6,4,6,1,6])

n = len(series)

window = 3

frequency = []
for i in range(0, n-window+1):
    time_series=series[i:i+window]

    # Construct horizontal visibility graph
    hvg = construct_hvg(time_series)
    
    # Count the number of edges
    num_edges = count_edges(hvg)
    print("Number of edges in the HVG"+ str(i)+": "+str(time_series), num_edges)
    
    frequency.append(num_edges)
    # Plot the time series and the HVG
    plt.subplot(1, 2, 1)
    plt.plot(time_series, marker='o')
    plt.title('Time Series window '+str(i))
    
    plt.subplot(1, 2, 2)
    plt.imshow(hvg, cmap='binary', origin='upper')
    plt.title('Horizontal Visibility Graph')
    plt.show()

print("Grouped Horizontal Visibility Graph Entropy: "+str(shannon_entropy(frequency)))

visible_motifs = np.count_nonzero(frequency)
non_visible_motif = visible_motifs-(window-1)

divergence = kl_divergence(visible_motifs/len(frequency), non_visible_motif/len(frequency))
print("Visible and Non-visible: Horizontal Visibility Graph Entropy: "+str(divergence))


