def projectNameSegments = currentBuild.fullProjectName.split('/')
def technology = projectNameSegments[-1]
