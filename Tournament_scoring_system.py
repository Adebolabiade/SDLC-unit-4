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

# Event results
event_results = {
    "Maths Quiz": ["Alice", "Frank", "kara", "paula", "Bob"],
    "Obstacle Race": ["Bob", "Grace", "leo", "Quinn", "Jack"],
    "Debate": ["Charlie", "Holly", "Mason", "Alice", "Riley"],
    "Chess": ["David", "Mia", "Ian", "Nina", "Sophie"],
    "Code Sprint": ["Ella", "Jack", "Oscar", "Tom", "Mia"]
}

# Calculate scores based on event results
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

    return "\n".join(output)

# Prompt user for input
team_input = input("Enter the team name to view: ")
event_input = input("Enter the event name to view: ")

# Display the result
print(display_team_event_summary(team_input, event_input))
