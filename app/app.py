from flask import Flask, render_template
from github import Github

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

FAVORITE_REPO = 'facebook/react'


@app.route('/')
def github_issues():
    page = 0
    github = Github(app.config['GITHUB_ACCESS_TOKEN'])
    repo = github.get_repo(FAVORITE_REPO)
    issues = []
    for issue in repo.get_issues().get_page(page):
        issues.append({
            'number': issue.number,
            'title': issue.title,
            'state': issue.state,
            'labels': issue.labels
        })
    return render_template('index.html',
                           repo_name=FAVORITE_REPO,
                           issues=issues)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
