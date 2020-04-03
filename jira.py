
class JiraIssue():
    counter = 1
    def __init__(self, key, location, reviewerEmail):
        self.key = key
        self.location = location
        self.reviewerEmail = reviewerEmail
        self.id = JiraIssue.counter
        JiraIssue.counter += 1

    def getKey(self):
        return self.key

    def getLocation(self):
        return self.location

    def getReviewerEmail(self):
        return self.reviewerEmail

    def __str__(self):
        return f"Issue {self.id}, {self.key}: {self.reviewerEmail} is responsible for {self.location}"


