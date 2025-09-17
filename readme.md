The project key for SonarQube should be extracted from the SonarQube UI (`sonar.pfizer.com`) while creating or selecting a project. The project key is a unique identifier for your project in SonarQube, and it is required for configuration in your workflow and the `sonar-project.properties` file.
***
### How to Extract and Use SonarQube Project Key
#### Extracting the Project Key from SonarQube
- Log in to `sonar.pfizer.com`.
- Go to **Projects** and select or create the desired project.
- After selecting the project, the **Project Key** will be displayed in the project overview/dashboard or within the project settings.
- Copy the project key (for example: `pfizer_sfdi-devops-tools-infra`).
#### Process
> To configure SonarQube scan for the GitHub repository:
>
> - Retrieve the project key directly from SonarQube (`sonar.pfizer.com`).  
>   Recommended navigation: Projects → Select your project → Project Settings → Project Key.
>   Example: `"sonar.projectKey=pfizer_sfdi-devops-tools-infra"`.
> - Add the project key in your repository’s root `sonar-project.properties` file:
>   ```
>   sonar.projectKey=pfizer_sfdi-devops-tools-infra
>   ```
> - Make sure the `.github/workflows/sonarqube.yml` refers to this key as needed by your workflow or scanner.
#### 3. Update `.github/workflows/sonarqube.yml`
- Example snippet to include in your workflow:
 ```yaml
 name: SonarQube Scan with custom action
on:
  workflow_dispatch:
   push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened]



jobs:
  sonarqube:
    name: SonarQube Scan
    continue-on-error: true
    runs-on: [self-hosted, bolt-ubuntu]



    steps:
      - name: Checkout Codebase
        uses: actions/checkout@v4
        with:
          fetch-depth: 0



      - name: SonarQube Scan
        uses: pfizer-github-automation/sonar-scan-action@main
        env:
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
          SONAR_ROOT_CERT: ${{ secrets.SONAR_ROOT_CERT }}
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
 ```
- Ensure this job runs on pull requests and main branch pushes as in your original config.
### Checking Status in SonarQube
- After a pull request triggers a GitHub Action scan, check the status of the scan directly in the SonarQube project dashboard at `sonar.pfizer.com` to confirm the results and quality gates.
***
