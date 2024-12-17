import random 
import math

def sim_anneal(ini, in_temp, max_iter, cool):
    # Initialize current state and best state
    curr_s = ini
    best_s = curr_s
    best_c = obj(best_s)  
    temp = in_temp  # Set the initial temperature

    # While the temperature is above a threshold
    while temp > 1:
        #Perform iterations at current temperature
        for i in range(max_iter):
            new_s = neig(curr_s)  
            curr_c = obj(curr_s)  
            new_c = obj(new_s)  

            # Decide whether to accept the new state based on the acceptance probability
            if ap(curr_c, new_c, temp) > random.random():
                curr_s = new_s  # Move to the new state
            # Update the best state found so far if the new state is better
            if new_c < best_c:
                best_s = new_s
                best_c = new_c
        # Cool down the temperature
        temp *= cool
    
    return best_s, best_c  # Return the best state and its cost

def neig(state):
    # Generate a neighboring state by modifying a random element
    new_s = state.copy()  
    ind = random.randint(0, len(state) - 1)  
    new_s[ind] += random.uniform(-1, 1)  
    return new_s  

def obj(state):
    # Objective function to evaluate the cost of a state
    c = 1
    for i in state:
        c += i**2 + 2*i + 1 
    return c  

def ap(curr_c, new_c, temp):
    # Acceptance probability function based on the current and new costs and temperature
    if new_c < curr_c:
        return 1  
    else:
        return math.exp((curr_c - new_c) / temp)  #

# Run the simulated annealing algorithm with initial state, temperature, iterations, and cooling rate
print(sim_anneal([1, 2, 3, 4, 5], 1000, 1000, 0.99))
