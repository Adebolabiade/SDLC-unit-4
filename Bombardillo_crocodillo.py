# Constants
EVENTS = ["Maths Quiz", "Obstacle Race", "Debate", "Chess", "Code Sprint"]
POINTS = [12, 10, 8, 6,4]  # Points for 1st to 5th place

# Storage structures
teams = {
    "Team Alpha": ["Alice", "Bob", "Charlie", "David", "Ella"], 
    "Team Beta" : ["Frank", "Grace", "Holly", "Ian", "Jack" ],
    "Team Omega":["Kara", "Leo", "Mason", "Nina", "Oscar"],
    "Team Zeta" :["Paula", "Quinn", "Riley", "Sophie", "Tom"]

}  # team_name: [member1, member2, ...]
        
x= sorted(teams)       
print (x)



individuals = ["Liam","Mia" "Noah" "Uma" "Zane"]  # list of individual names
scores = {
"Alice": 12,
"Bob": 12,
"Charlie": 12,
"David": 12,
"Ella": 10,
"Frank": 8,
"Grace": 10, 
"Holly": 8,
"Ian": 10,
"Jack": 8,
"Kara": 6,
"Leo": 8,
"Mason": 6,
"Nina": 8,
"Oscar": 6,
"Paula": 4,
"Quinn": 6,
"Riley": 4,
"Sophie": 4,
"Tom": 4,
"Liam": 10,
"Mia": 10,
"Noah": 0,
"Uma": 6,
"Zane": 12,
}  # name: total_score

x=sorted(scores)
print (x)

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
record_event_results("Maths Quiz", ["Alice","Liam", "Frank", "Kara", "Paula",])
record_event_results("Obstacle Race", ["Bob", "Grace", "Leo", "Quinn",])
record_event_results("Debate", ["Charlie","Mia", "Holly", "Mason", "Riley",])
record_event_results("Chess", ["David", "Ian", "Nina","Uma", "Sophie",])
record_event_results("Code Sprint", ["Zane","Ella", "Jack", "Oscar", "Tom",])

# Display final scores
display_scores()
