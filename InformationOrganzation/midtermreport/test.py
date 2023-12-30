import matplotlib.pyplot as plt

k_values = [5, 10, 15, 20, 25]
f1_scores = [0.53, 0.7, 0.72, 0.73, 0.74] # Hypothetical F1@k scores

plt.figure(figsize=[10,5])
plt.plot(k_values, f1_scores, marker='o')

plt.title('F1@k Convergence Plot')
plt.xlabel('k (Number of Retrieved Documents)')
plt.ylabel('F1@k Score')

plt.grid()
plt.show()