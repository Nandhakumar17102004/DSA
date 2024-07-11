class Heap:
    def __init__(self):
        heap=[]

class Project:
    def __init__(self, name, priority, deadline):
        self.name = name
        self.priority = priority
        self.deadline = deadline
        
    
    def __lt__(self, other):
        # Projects with higher priority come first
        return self.priority > other.priority

class ProjectManagement:
    def __init__(self):
        self.projects = []

    def submit_project(self, name, priority, deadline):
        project = Project(name, priority, deadline)
        heapq.heappush(self.projects, project)
        print(f"Project '{name}' submitted with priority {priority} and deadline {deadline}.")

    def assign_project(self):
        if self.projects:
            project = heapq.heappop(self.projects)
            print(f"Project '{project.name}' assigned.")
            return project
        else:
            print("No projects to assign.")
            return None

    def check_deadlines(self):
        current_date = datetime.date.today()
        for project in self.projects:
            if project.deadline < current_date:
                print(f"Project '{project.name}' missed its deadline!")
            else:
                days_remaining = (project.deadline - current_date).days
                print(f"Days remaining for project '{project.name}': {days_remaining}")

def main():
    pm = ProjectManagement()

    # Submitting projects
    pm.submit_project("Project A", 5, datetime.date(2024, 5, 15))
    pm.submit_project("Project B", 8, datetime.date(2024, 6, 30))
    pm.submit_project("Project C", 3, datetime.date(2024, 4, 20))

    # Checking deadlines
    pm.check_deadlines()

    # Assigning projects
    pm.assign_project()
    pm.assign_project()
    pm.assign_project()
    pm.assign_project()  # No projects left to assign

if __name__ == "__main__":
    main()
