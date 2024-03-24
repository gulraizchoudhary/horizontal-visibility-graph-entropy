# Group Horizotal Visibility Graph Entropy
Transform time series into horizontal visibility graph and then counts the number of edges in each sliding window. The shannon entropy is calculated based on the frequency of number of edges. The Shannon entropy is a measure of uncertainity. The value of entropy will be higher if the frequencies of edge groups have normal distribion otherwise, lower entropy value.

# Time Irreversibility Between Visibile and Non-visible Horizotal Visibility Graph Motifs
Transform time series into horizontal visibility graph. A graph motif is visible if there is an edge in the hvg graph constructed on sliding window, otherwise, non-visibile. Kullback-Leibler divergence, also known as relative entropy, is used as a measure to calculate the distance between two
distributions. In specific, we apply KLD to measure the distance between the distribution of visibility and non-visible motifs. The process is irreversible if the value obtained is higher than
0, otherwise reversible. Values close to 1 depicts higher degree of time irreversibility.

Graph motifs fall into two categories: visibility and non-visibility. Visibility motifs show significant variation, while non-visible motifs consist of the following types within the chosen window:

No change: All data points in the window are identical.
Steady increase without fluctuations.
Steady decrease without intermediate fluctuations.
Steady increase followed by a decrease without intermediates.


## Output: window of size 5
```bash
Number of edges in the HVG0: [6 5 6 4 6 1] 2
Number of edges in the HVG1: [5 6 4 6 1 6] 2
Number of edges in the HVG2: [6 4 6 1 6 1] 2
Number of edges in the HVG3: [4 6 1 6 1 1] 1
Number of edges in the HVG4: [6 1 6 1 1 1] 1
Number of edges in the HVG5: [1 6 1 1 1 1] 0
Number of edges in the HVG6: [6 1 1 1 1 1] 0
Grouped Horizontal Visibility Graph Entropy: 1.5566567074628228
Time Irreversibility of Visible and Non-visible: 0.6544933799101108
```

!["Number of edges in the HVG 0"](https://github.com/gulraizchoudhary/horizontal-visibility-graph-entropy/blob/main/img/Figure_w5_0.png)
!["Number of edges in the HVG 1"](https://github.com/gulraizchoudhary/horizontal-visibility-graph-entropy/blob/main/img/Figure_w5_1.png)
!["Number of edges in the HVG 2"](https://github.com/gulraizchoudhary/horizontal-visibility-graph-entropy/blob/main/img/Figure_w5_2.png)
!["Number of edges in the HVG 0"](https://github.com/gulraizchoudhary/horizontal-visibility-graph-entropy/blob/main/img/Figure_w5_3.png)
!["Number of edges in the HVG 1"](https://github.com/gulraizchoudhary/horizontal-visibility-graph-entropy/blob/main/img/Figure_w5_4.png)
!["Number of edges in the HVG 2"](https://github.com/gulraizchoudhary/horizontal-visibility-graph-entropy/blob/main/img/Figure_w5_5.png)
!["Number of edges in the HVG 2"](https://github.com/gulraizchoudhary/horizontal-visibility-graph-entropy/blob/main/img/Figure_w5_6.png)

## Acknowledgements
Credit goes to Gulraiz Iqbal Choudhary, You may consider to read the following paper for more understanding and cite it if you have used the algorithm. 


G. I. Choudhary, W. Aziz, I.R. Khan, S. Rahardja and P. Fränti, 
“Analysing the dynamics of inter beat interval time series using grouped horizontal visibility graph”, 
IEEE Access, 7 (1), 9926-9934, December 2019. https://www.doi.org/10.1109/ACCESS.2018.2890542


G. I. Choudhary, W. Aziz, and P. Fränti, 
“Detection of time irreversibility in interbeat interval time series by visible and nonvisible motifs from horizontal visibility graph”, 
Biomedical Signal Processing and Control, 62, 10205, 2020. https://doi.org/10.1016/j.bspc.2020.102052


## License
[MIT](https://choosealicense.com/licenses/mit/)
