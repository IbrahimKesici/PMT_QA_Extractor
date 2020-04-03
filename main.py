from jira import JiraIssue
import requests

def main():
    response = connectAPI()
    issues = getJiraIssues(response)

    for issue in issues:
        print(f"{issue}")
        

def connectAPI():
    api = f"http://jira.mercer.com/rest/api/2/search?jql=project%20=%20CL%20AND%20issuetype%20=%20%22PMT%20Price%20Analysis%22%20AND%20%20status%20!=%20Completed%20AND%20%22CL_Fast%20track_QA%22%20%20=%20Yes%20AND%20%22CL_Peer%20Reviewer%22%20!=%20unassigned&fields=customfield_26350,customfield_26665&maxResults=500"
    response = requests.get(api)

    if response.status_code != 200:
        #TODO: logging
        raise Exception ("GET request to API has failed")
    
    return response.json()

def getJiraIssues(response):
    issues = response["issues"]

    jiraIssues = []
    for issue in issues:
        key = issue["key"]
        location = issue["fields"]["customfield_26350"]["value"]
        email = issue["fields"]["customfield_26665"]["emailAddress"]
        
        newJiraIssue = JiraIssue(key=key, location=location,reviewerEmail=email)
        jiraIssues.append(newJiraIssue)

    return jiraIssues

if __name__ == "__main__":
    main()