import random

class ProjectInvestor:
    def __init__(self, numProjects, availableTime):
        self.numProjects = numProjects
        self.availableTime = availableTime
        self.projects = [self.generateRandomProject() for _ in range(numProjects)]

    def generateRandomProject(self):
        start = random.randint(0, 10)
        end = random.randint(start + 1, 15)
        profit = random.randint(10, 100)
        return (start, end, profit)

    def maximizeProfit(self):
        self.projects.sort(key=lambda x: x[2] / (x[1] - x[0]), reverse=True)

        print(self.projects)
        totalTime = 0
        totalProfit = 0
        selectedProjects = []

        for project in self.projects:
            start, end, profit = project
            if totalTime + (end - start) <= self.availableTime:
                totalTime += (end - start)
                totalProfit += profit
                selectedProjects.append(project)

        return selectedProjects, totalProfit

numProjects = 10
availableTime = int(input("Enter available time: "))
investor = ProjectInvestor(numProjects, availableTime)
selectedProjects, totalProfit = investor.maximizeProfit()

print("Selected projects:")
for project in selectedProjects:
    print(f"Start: {project[0]} days, End: {project[1]} days, Profit: {project[2]}")
print(f"Total profit: {totalProfit}")
