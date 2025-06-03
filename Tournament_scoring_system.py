# Constants
EVENTS = ["Maths Quiz", "Obstacle Race", "Debate", "Chess", "Code Sprint"]
POINTS = [10, 8, 6, 4, 2]  # Points for 1st to 5th place

# Storage structures
teams ={
    "Team Alpha": ["Alice", "Bob", "Charlie", "David", "Ella"], "Team Beta"



    
}  # team_name: [member1, member2, ...]
        



individuals = ["Alice", "Bob", "Charlie", "David", "Ella""Frank", "Grace", "Holly", "Ian", "Jack""Kara", "Leo", "Mason", "Nina", "Oscar""Paula", "Quinn", "Riley", "Sophie", "Tom"]  # list of individual names
scores = {}  # name: total_score

# Function to add a team
def register_team(team_name, members):
    teams[team_name] = members
    for member in members:
        scores[member] = 0  # initialise score

# Function to register individual participants
def register_individual(name):
    individuals.append(name)
    scores[name] = 0

# Function to record scores for an event
def record_event_results(event_name, participants_ranked):
    print(f"\nScoring for {event_name}")
    for i, name in enumerate(participants_ranked):
        if i < len(POINTS):
            scores[name] += POINTS[i]
            print(f"{name} awarded {POINTS[i]} points.")
        else:
            print(f"{name} gets 0 points.")

# Function to display all scores
def display_scores():
    print("\n--- Final Scores ---")
    for name, score in scores.items():
        print(f"{name}: {score} points")

# Main Program Logic
# Register teams
register_team("Team Alpha", ["Alice", "Bob", "Charlie", "David", "Ella"])
register_team("Team Beta", ["Frank", "Grace", "Holly", "Ian", "Jack"])
register_team("Team Omega", ["Kara", "Leo", "Mason", "Nina", "Oscar"])
register_team("Team Zeta", ["Paula", "Quinn", "Riley", "Sophie", "Tom"])

# Register individuals
register_individual("Liam")
register_individual("Mia")
register_individual("Noah")
register_individual("Uma")
register_individual("Zane")

# Record results for each event (top 5 for each)
record_event_results("Maths Quiz", ["Alice", "Grace", "Liam", "Noah", "Bob"])
record_event_results("Obstacle Race", ["Charlie", "Mia", "Frank", "Ian", "Jack"])
record_event_results("Debate", ["Ella", "David", "Holly", "Alice", "Noah"])
record_event_results("Chess", ["Liam", "Mia", "Grace", "Bob", "Charlie"])
record_event_results("Code Sprint", ["Noah", "Alice", "Frank", "Liam", "Mia"])

# Display final scores
display_scores()
