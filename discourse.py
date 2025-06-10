import random

# Constants
EVENTS = ["Maths Quiz", "Obstacle Race", "Debate", "Chess", "Code Sprint"]
POINTS = [10, 8, 6, 4, 2]

# Predefined Teams and Members
teams = {
    "Group Alpha": ["Alice", "Bob", "Charlie", "David", "Ella"],
    "Group Beta": ["Frank", "Grace", "Holly", "Ian", "Jack"],
    "Group Omega": ["Kara", "Leo", "Mason", "Nina", "Oscar"],
    "Group Zeta": ["Pam", "Quinn", "Riley", "Sophie", "Tom"]
}

# Individual Competitors
individuals = ["Liam", "Mia", "Noah"]

# Scores dictionary
scores = {member: 0 for team in teams.values() for member in team}
scores.update({ind: 0 for ind in individuals})

# Event results (randomly generated participants and scores)
event_results = {}

# Randomly assign event participants and their rankings
all_participants = list(scores.keys())

for event in EVENTS:
    random.shuffle(all_participants)
    event_results[event] = all_participants[:5]

# Calculate scores based on random event results
for event, participants in event_results.items():
    for i, name in enumerate(participants):
        if name in scores and i < len(POINTS):
            scores[name] += POINTS[i]

# Function to calculate team total scores
def calculate_team_scores():
    team_scores = {}
    for team_name, members in teams.items():
        team_scores[team_name] = sum(scores[member] for member in members)
    return team_scores

# Function to display team event and total performance
def display_team_event_summary(team_name, event_name):
    if team_name not in teams:
        return "Error: Please enter a valid team name."

    if event_name not in EVENTS:
        return "Error: Please enter a valid event name."

    output = [f"--- {team_name} ---", f"Scores in '{event_name}':"]
    event_participants = event_results.get(event_name, [])

    for member in teams[team_name]:
        if member in event_participants:
            rank = event_participants.index(member)
            output.append(f"{member}: {POINTS[rank]} points")
        else:
            output.append(f"{member}: 0 points")

    output.append("\nTotal Scores:")
    for member in teams[team_name]:
        output.append(f"{member}: {scores[member]} points")

    team_scores = calculate_team_scores()
    total_score = team_scores[team_name]
    ranking = sorted(team_scores.items(), key=lambda x: x[1], reverse=True)
    standing = [i + 1 for i, team in enumerate(ranking) if team[0] == team_name][0]

    output.append(f"\n{team_name} Total Score: {total_score} points")
    output.append(f"{team_name} Standing: #{standing}")

    # Team leaderboard
    output.append("\n--- Team Leaderboard ---")
    for name, score in ranking:
        output.append(f"{name}: {score} points")

    # Top 10 individuals
    output.append("\n--- Top 10 Individual Leaderboard ---")
    top_individuals = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:10]
    for name, score in top_individuals:
        output.append(f"{name}: {score} points")

    # Event leaderboard
    output.append(f"\n--- {event_name} Leaderboard ---")
    leaderboard = []
    for i, name in enumerate(event_participants):
        if name in scores and i < len(POINTS):
            leaderboard.append((name, POINTS[i]))
    leaderboard.sort(key=lambda x: x[1], reverse=True)

    for name, pts in leaderboard:
        output.append(f"{name}: {pts} points")

    return "\n".join(output)

# Advanced prompt system
print("Welcome to the Tournament Scoring System\n")

# Display teams as numbered list
print("Select a team from the list below:")
team_list = list(teams.keys())
for i, team in enumerate(team_list, 1):
    print(f"{i}. {team}")

# Input team selection
try:
    team_choice = int(input("\nEnter the number corresponding to your chosen team: "))
    if 1 <= team_choice <= len(team_list):
        selected_team = team_list[team_choice - 1]
    else:
        print("Error: Please select a valid team number.")
        exit()
except ValueError:
    print("Error: Please enter a valid number.")
    exit()

# Display events as numbered list
print("\nSelect an event from the list below:")
for i, event in enumerate(EVENTS, 1):
    print(f"{i}. {event}")

# Input event selection
try:
    event_choice = int(input("\nEnter the number corresponding to your chosen event: "))
    if 1 <= event_choice <= len(EVENTS):
        selected_event = EVENTS[event_choice - 1]
    else:
        print("Error: Please select a valid event number.")
        exit()
except ValueError:
    print("Error: Please enter a valid number.")
    exit()

# Display the result
print("\n" + display_team_event_summary(selected_team, selected_event))
