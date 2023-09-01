tarted by user srvamr-sfaops
org.jenkinsci.plugins.github_branch_source.RateLimitExceededException: GitHub API rate limit exceeded
	at org.jenkinsci.plugins.github_branch_source.Connector$1.onError(Connector.java:586)
	at org.kohsuke.github.RateLimitHandler.onError(RateLimitHandler.java:43)
	at org.kohsuke.github.GitHubClient.detectKnownErrors(GitHubClient.java:417)
	at org.kohsuke.github.GitHubClient.sendRequest(GitHubClient.java:386)
Caused: org.kohsuke.github.HttpException: {"message":"API rate limit exceeded for 168.224.160.14. (But here's the good news: Authenticated requests get a higher rate limit. Check out the documentation for more details.)","documentation_url":"https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting"}
	at org.kohsuke.github.GitHubClient.interpretApiError(GitHubClient.java:543)
	at org.kohsuke.github.GitHubClient.sendRequest(GitHubClient.java:401)
	at org.kohsuke.github.GitHubClient.fetch(GitHubClient.java:121)
	at org.kohsuke.github.GitHubClient.checkApiUrlValidity(GitHubClient.java:323)
	at org.kohsuke.github.GitHub.checkApiUrlValidity(GitHub.java:1244)
	at org.jenkinsci.plugins.github_branch_source.ApiRateLimitChecker.verifyConnection(ApiRateLimitChecker.java:199)
	at org.jenkinsci.plugins.github_branch_source.Connector$GitHubConnection.verifyConnection(Connector.java:794)
	at org.jenkinsci.plugins.github_branch_source.Connector.connect(Connector.java:447)
	at org.jenkinsci.plugins.github_branch_source.GitHubSCMSource.retrieve(GitHubSCMSource.java:1679)
	at jenkins.scm.api.SCMSource.fetch(SCMSource.java:582)
	at org.jenkinsci.plugins.workflow.multibranch.SCMBinder.create(SCMBinder.java:101)
	at org.jenkinsci.plugins.workflow.job.WorkflowRun.run(WorkflowRun.java:311)
	at hudson.model.ResourceController.execute(ResourceController.java:107)
	at hudson.model.Executor.run(Executor.java:449)
Finished: FAILURE
