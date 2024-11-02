import random

roles = [
    'Local resident',
    'Geologist',
    'Farmer/land owner',
    'Climate scientist',
    'Local Congressional representative',
    'Local business owner',
    'Member of environmental group',
    'Public health official',
    'Oil company executive',
    'Hydrologist',
    'Lawyer'
]

'''
assigner function.
inputs: list of student names; list of roles defined above
returns: dictionary of schedule keyed by team name
'''
def assign_roles(students, roles):
    
    # shuffle students
    random.shuffle(students)
    
    # base 4 teams. Can be updated to 2 for smaller classes
    n_teams = 4
    n_students = len(students)
    base_team_size = n_students // n_teams
    team_sizes = {}
    
    # calculate number of students per team
    for i in range(n_teams):

        if i < n_students % n_teams:
            team_sizes[i] = base_team_size
        else:
            team_sizes[i] = base_team_size
            
            
    # intialize a list to assign students to teams
    groups = []
    start = 0
    
    # use team sizes dictionary to set size of teams
    # assign shuffled students into num_teams groups
    for size in team_sizes.values():
        groups.append(students[start:start + size])
        start += size
            
    # divide groups of shuffled students into debate teams
    debate_schedule = {
        'Pro Fracking Ban 1': groups[0],
        'Against Fracking Ban 1': groups[1],
        'Pro Fracking Ban 2': groups[2],
        'Against Fracking Ban 2': groups[3]
    }
    
    
    # intialize full schedule
    
    full_schedule = {}
    for debate, team in debate_schedule.items():
        
        # shuffle roles for randomization for teams
        random.shuffle(roles)
        
        #intialize a new dict for each team roles
        #ensures each team can have any role
        team_roles = {}
        
        for n, team_member in enumerate(team):
            
            # assign role to each team member
            team_roles[team_member] = roles[n % len(roles)]
            
            # update debate side with team roles
            full_schedule[debate] = team_roles

        
    return full_schedule



def read_students(filename="students.txt"):
    
    # read students file for student names
    with open(filename, "r") as f:
        students = [line.strip() for line in f if line.strip()]
    return students

if __name__ == "__main__":
    students = read_students() 
    debate_schedule = assign_roles(students, roles)
    for debate, assignments in debate_schedule.items():
        print(f'\n{debate} ({len(assignments)} members):')
        for member, role in assignments.items():
            print(f' - {member} ({role})')
    print('')
