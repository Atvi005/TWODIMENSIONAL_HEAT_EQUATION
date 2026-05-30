import matplotlib.pyplot as plt
import numpy as np


N = 51
L = 1
h = L / (N - 1)
iterations = 0
epsilon = 1e-8


T = np.zeros((N, N))
T[0, :] = 1
T_new = np.zeros((N, N))
T_new[0, :] = 1

numerical_error = 1.0


iteration_history = []
error_history = []


while numerical_error > epsilon:
    
    
    T_new[1:-1, 1:-1] = 0.25 * (
        T[:-2, 1:-1] +  # North (i-1)
        T[2:, 1:-1]  +  # South (i+1)
        T[1:-1, :-2] +  # West  (j-1)
        T[1:-1, 2:]     # East  (j+1)
    )

  
    numerical_error = np.sum(np.abs(T - T_new))
    
   
    iterations += 1
    T[:] = T_new 
    
  
    if iterations % 1000 == 0:
        iteration_history.append(iterations)
        error_history.append(numerical_error)

print(f"Calculation complete! Total Iterations: {iterations}")




plt.figure(1, figsize=(8, 5))
plt.semilogy(iteration_history, error_history, 'k-')
plt.title("Convergence History")
plt.xlabel("Iterations")
plt.ylabel("Numerical Error")
plt.grid(True, which="both", ls="--", alpha=0.5)


x_dom = np.linspace(0, L, N)
y_dom = np.linspace(L, 0, N)
X, Y = np.meshgrid(x_dom, y_dom)

plt.figure(2, figsize=(8, 6))

contour = plt.contourf(X, Y, T, levels=72, cmap='viridis') 
plt.colorbar(contour, label="Temperature")
plt.title("Temperature Distribution T(X,Y)")

plt.show()