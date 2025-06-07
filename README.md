# demo_python_app

A simple Python app to demonstrate SonarCloud scanning.

# demo_python_app

A simple Python project with a standard `src/` layout, demonstrating how to run code analysis and coverage scans using SonarCloud.

---

## Project Structure
demo_python_app/
├── src/
│ └── demo_python_app/
│ ├── init.py
│ └── main.py
├── tests/
│ ├── init.py
│ └── test_main.py
├── setup.py
├── requirements.txt
├── sonar-project.properties
├── .gitignore
└── README.md

yaml
Copy
Edit


---

## Getting Started

### 1. Clone or download the repo

```bash
git clone <your_repo_url>
cd demo_python_app

2. Install dependencies

pip install -r requirements.txt

3. Run the app
python3 -m demo_python_app.main
Or directly:

python3 src/demo_python_app/main.py


You should see:

makefile
Copy
Edit
Addition: 15
Subtraction: 7

Running Tests
Run all tests using pytest:

bash
Copy
Edit
pytest

Measuring Test Coverage
Run tests with coverage measurement:

bash
Copy
Edit
coverage run -m pytest

View coverage report in the terminal:

bash
Copy
Edit
coverage report
Generate XML report (for SonarCloud):

bash
Copy
Edit

SonarCloud Setup and Scan
1. Create a SonarCloud account
Go to SonarCloud.io

Sign up for a free account (using GitHub or other)

Create a new organization (personal or team)

2. Create a project in SonarCloud
Connect your GitHub repository or create a project manually

Generate a SonarCloud token with Execute Analysis permissions

3. Configure sonar-project.properties
Update with your actual project key, organization, and token:

properties
Copy
Edit
sonar.projectKey=your_project_key
sonar.organization=your_org_name
sonar.host.url=https://sonarcloud.io
sonar.login=your_token

sonar.sources=src/demo_python_app
sonar.tests=tests
sonar.python.version=3
sonar.test.inclusions=tests/**/*.py
sonar.exclusions=**/__pycache__/**

sonar.python.coverage.reportPaths=coverage.xml
4. Run Sonar Scanner
Make sure you have sonar-scanner installed and on your PATH.

From the project root, run:

bash
Copy
Edit
sonar-scanner
The analysis will be uploaded to SonarCloud.

Additional Notes
The project uses a src/ folder layout to avoid import issues and keep the repo clean.

Tests are located in a top-level tests/ folder.

The project uses setup.py for packaging with package_dir={"": "src"}.

Coverage reports help SonarCloud measure how much of your code is tested.

Optional: Automate with GitHub Actions
You can create a GitHub Actions workflow to run tests, coverage, and Sonar scans on every push.

Feel free to reach out if you want help setting that up or have any questions!

vbnet
Copy
Edit

Copy this into a new file named `README.md` in your project root.

Let me know if you want me to generate a GitHub Actions workflow next!







You said:
