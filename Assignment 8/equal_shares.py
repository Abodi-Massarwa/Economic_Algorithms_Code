def elect_next_budget_item(votes, balances, costs):
    """
    Perform one step of the Method of Equal Shares for budget allocation.

    Parameters:
        votes (list): List of votes from citizens. Each citizen votes for a set of items.
        balances (list): Virtual balances of each citizen.
        costs (dict): Costs associated with each item.
    """
    # Step 1: Initialize variables
    min_cost = float('inf')  # Set initial minimum cost to infinity
    next_item = None  # Placeholder for the next elected item
    contributions = {}  # Dictionary to store contributions of each citizen

    # Step 2: Calculate the cost of each item and find the next item with the minimum cost
    for item, cost in costs.items():
        # Calculate the total cost of the item based on votes
        total_cost = sum(cost for vote in votes if item in vote)
        # Update minimum cost and next item if current item has lower cost
        if total_cost < min_cost:
            min_cost = total_cost
            next_item = item

    # If no votes were cast for any item, print a message and return
    if next_item is None:
        print("No votes were cast for any item.")
        return

    # Step 3: Calculate contributions and update balances
    votes_count = sum(1 for vote in votes if next_item in vote)  # Count total votes for the next item
    contribution_per_vote = costs[next_item] / votes_count if votes_count > 0 else 0  # Calculate contribution per vote
    for vote_index, vote in enumerate(votes):
        # Check if the citizen voted for the next item
        if next_item in vote:
            # Assign contribution per vote to the citizen
            contributions[vote_index] = contribution_per_vote
            # Update balance of the citizen
            balances[vote_index] -= contribution_per_vote

    # Step 4: Print the result
    print(f"Round 1: \"{next_item}\" is elected.")
    for vote_index, contribution in contributions.items():
        print(f"Citizen {vote_index + 1} pays {contribution:.2f} and has {balances[vote_index]:.2f} remaining balance.")


# Example data
votes = [
    {'Park in street X', 'Park in street Y'},
    {'Park in street Y', 'Park in street Z'},
    {'Park in street X', 'Park in street Z'}
]

balances = [10.0, 10.0, 10.0]

costs = {
    'Park in street X': 3.0,
    'Park in street Y': 4.0,
    'Park in street Z': 5.0
}

# Call the function with the example data
elect_next_budget_item(votes, balances, costs)

# Expected Output:
# Round 1: "Park in street X" is elected.
# Citizen 1 pays 1.50 and has 8.50 remaining balance.
# Citizen 2 pays 0.00 and has 10.00 remaining balance.
# Citizen 3 pays 1.50 and has 8.50 remaining balance.
