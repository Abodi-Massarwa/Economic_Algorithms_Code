from typing import Tuple,List, Set

def print_output(l: List[List[float]]):
    print("************************************************************************************")
    if l is None:
        print("our budget is not feasible, try again with different settings and constraints.")
    else:
        print("our budget is decomposed , one option would be :")
        i = 1
        for alloc in l:
            print(f"Agent {i} budgets: {alloc}")
            i += 1
    # print("************************************************************************************")

def find_decomposition(budget: List[float], preferences: List[Set[int]]):
    """
    Finds the decomposition of budget allocation based on agent preferences.

    Parameters:
    - budget: A list where each element represents the budget for a specific subject.
    - preferences: A list of sets, where each set contains subject indices that an agent is interested in.

    Returns:
    - A matrix representing the allocation of budget for each agent and subject,
      or None if the budget cannot be decomposed.
    """
    # Determine the number of agents and subjects
    num_agents = len(preferences)
    num_subjects = len(budget)

    # Initialize a matrix for the decomposition with zeros
    decomposition = [[0 for _ in range(num_subjects)] for _ in range(num_agents)]

    # Calculate total budget and share per agent
    total_budget = sum(budget)
    share_per_agent = total_budget / num_agents if num_agents else 0

    # Check if any agent has no preferences. If so, return None.
    if any(len(pref) == 0 for pref in preferences):
        return None

    # Allocate budget for subjects based on agent preferences and validate the allocation
    for j in range(num_subjects):
        subject_budget = budget[j]

        # Find agents interested in the current subject
        interested_agents = [i for i in range(num_agents) if j in preferences[i]]

        # If no one is interested in the subject with a non-zero budget, return None
        if not interested_agents and subject_budget > 0:
            return None

        # Calculate the total possible share for the current subject
        total_possible_share = sum(share_per_agent - sum(decomposition[i]) for i in interested_agents)

        # If the total possible share is less than the subject's budget, return None
        if total_possible_share < subject_budget:
            return None

        # Allocate budget to interested agents while considering their preferences
        for i in interested_agents:
            if subject_budget <= 0:
                break

            max_possible_allocation = share_per_agent - sum(decomposition[i])
            possible_allocation = min(max_possible_allocation, subject_budget)
            decomposition[i][j] += possible_allocation
            subject_budget -= possible_allocation

    # Verify if allocation meets the share per agent
    if not all(abs(sum(allocation) - share_per_agent) < 1e-9 for allocation in decomposition):
        return None

    return decomposition

# Running the code
budget_1 = [100, 100, 100, 100]
preferences_1 = [{0}, {1}, {2}, {3}]
decomp = find_decomposition(budget_1, preferences_1)  # this is decomposable
print_output(decomp)

budget_2 = [100, 100]
preferences_2 = [{0}, {0}]
decomp = find_decomposition(budget_2, preferences_2)  # this is NOT decomposable
print_output(decomp)

budget_1 = [100, 100, 100, 100]
preferences_1 = [{0, 1}, {1, 0}, {2}, {3}]
decomp = find_decomposition(budget_1, preferences_1)  # this is decomposable
print_output(decomp)

budget_1 = [100, 100, 100, 100]
preferences_1 = [{0, 1}, {1, 0}, {2}, {3}]
decomp = find_decomposition(budget_1, preferences_1)  # this is decomposable
print_output(decomp)

budget_1 = [0, 100, 900]
preferences_1 = [{1, 2}, {1, 2}]
decomp = find_decomposition(budget_1, preferences_1)  # this is decomposable
print_output(decomp)

budget_1 = [100, 20, 180]
preferences_1 = [{0, 1, 2}, {1, 2, 0}, {1, 2, 0}]
decomp = find_decomposition(budget_1, preferences_1)  # this is decomposable
print_output(decomp)

budget_1 = [100, 20, 180]
preferences_1 = [{0, 1, 2}, {1, 2, 0}, {1, 2, 0}, {2}]
decomp = find_decomposition(budget_1, preferences_1)  # this is decomposable
print_output(decomp)

budget_1 = [100, 20, 180]
preferences_1 = [{0, 1, 2}, {1, 2, 0}, {1, 2, 0}, {0, 1, 2}]
decomp = find_decomposition(budget_1, preferences_1)  # this is decomposable
print_output(decomp)

budget_1 = [0]
preferences_1 = [{0}]
decomp = find_decomposition(budget_1, preferences_1)  # this is decomposable
print_output(decomp)