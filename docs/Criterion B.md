# Criterion B

## Record of Tasks
|Task number|Planned Action                                                                        |Planned Outcome                                                                   |Time Estimated|Target Date (yyyy/mm/dd)|Criterion|Stage      |
|-----------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|--------------|------------------------|---------|-----------|
|1          |Interview with the client to understand her needs                                     |Understand her needs and have a vision for the website                            |2 hours       |2020/10/12              |A        |Planning   |
|2          |Preliminary research to find out the tools to use                                     |Understand the strength and weakness of of different frameworks and make a choice |5 hours       |2020/10/20              |A        |Planning   |
|3          |Create the mockup for the website                                                     |Completed the mockups                                                             |2 hours       |2020/10/28              |A        |Design     |
|4          |Create a rough prototype for the UI with hardcoded data                               |Client confirms whether it is something she wants                                 |4 hours       |2020/11/4               |B, C     |Design     |
|5          |Restructure the website UI as per client's request                                    |Client is happy with the new design                                               |5 hours       |2020/11/14              |C        |Developing |
|6          |Restructure the data structure of the website to allow for more flexibility           |Client can create new tags and remove old ones                                    |5 hours       |2020/11/19              |C        |Developing |
|7          |Setting the browser to upload directly to the s3 bucket instead of through the server |Website is much faster simply because the file server is located more locally     |5 hours       |2020/11/25              |C        |Developing |
|8          |Fix a bug in django-storage because :(                                                |The bug is fixed and the issue is still unaddressed by the library developers :(  |2 hours       |2020/12/4               |C        |Developing |
|9          |Create the add tags page                                                              |The page is finished and functional                                               |5 hours       |2020/12/14              |C        |Developing |
|10         |Integrate log in with google                                                          |User can log in with Google and the UI looks integrated                           |6 hours       |2020/12/19              |C        |Developing |
|11         |Refactor the user types so that different users have different permissions            |User with their respective permissions can accomplish different tasks             |2 hours       |2020/12/22              |C        |Developing |
|12         |Add an admin page for admins to manage user permissions                               |Admins can change the permissions of other users                                  |3 hours       |2020/12/26              |C        |Developing |
|13         |Write the search engine                                                               |The search engine works and returns relevant results                              |4 hours       |2021/1/2                |C        |Developing |
|14         |Write the edit paper page                                                             |User can edit the paper even after it is uploaded                                 |3 hours       |2021/1/5                |C        |Developing |
|15         |Get the client feedback for the finished product                                      |Client is happy                                                                   |2 hours       |2020/1/9                |E        |Feedback   |


## Use Cases

### Iteration 1

![User Cases Iteration 1](img/use%20cases%20iteration%201.png)
\

### Iteration 2

![User Case Iteration 2](img/use%20cases%20iteration%202.png)
\

The client feedback that she would like to use the help of students to manage some paper for her but would not want them to change who can edit the papers. Therefore I have decided to refactor the user into three groups: standard, editor and admin. Standard users can only view the website and bookmark for themselves, editors can, in addition, add, edit and remove papers, and admin can, in addition, manage the permissions of users. 

### Iteration 3

![Landing Page Iteration 3](img/landing%20page%20iteration%203.png)
\

I have added a header to navigate to different functions of the web app, and designed a favicon for the website.

## UML

## Mockup

### Landing Page
This is the page that the user first sees when he/she open the application. It presents them options for their search. Layout is powered by Bootstrap.

#### Iteration 1

![Landing Page Iteration 1](img/landing%20page%20iteration%201.png)
\

#### Iteration 2

![Landing Page Iteration 2](img/landing%20page%20iteration%202.png)
\

After the first iteration, the client game me feedback that she would want to be able to select multiple topic and approaches for each search box. After I have found no way to implement it with Bootstrap and I didn't want to write UI from scratch because it will inevitably look ugly, I found out that I could use a framework called Semantic UI.

#### Iteration 3

![Landing Page Iteration 3](img/landing%20page%20iteration%203.png)
\

In this iteration, I have added a navigation bar and a sign in with Google option. 

### Results Page

#### Iteration 1

![Results Page Iteration 1](img/results%20page%20iteration%201.png)
\

This is the page where users get their search results in these card-like info boxes, from which they can see the results. 

#### Iteration 2

![Results Page Iteration 2](img/results%20page%20iteration%202.png)
\

This iteration is unchanged in principle compared with the first iteration, but since I changed the framework, the design looks different.

### Edit Tags Page

This page is used to add and delete tag and tag groups in the database.

#### Iteration 1

![Edit Tags Page Iteration 1](img/edit%20tags%20page%20iteration%201.png)
\

## Design Description
The program is entirely based on the web, part of the functionality will be accomplished through JS running on client's computer, but a core part of the program will be accomplished through back-end code in Python running on Heroku and storage stored in AWS S3.  The UI will be rendered using client's web browser


## Class Dictionary

### Class - Paper
This class represents a paper stored in the database

#### Properties
##### Iteration 1
|Property Name|Signature                           |Description                                                                                                                                                      |
|-------------|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|tags         |tags: String[]                      |This returns the tags that the paper is associated with through manual assignment or automatic detection by the classifier.                                      |
|topics       |topics: String[]                    |Self-explanatory. Similar as above.                                                                                                                              |
|approaches   |approaches: String[]                |Self-explanatory. Similar as above.                                                                                                                              |
|methods      |methods: String[]                   |Self-explanatory. Similar as above.                                                                                                                              |
|ethics       |ethics: String[]                    |Self-explanatory. Similar as above.                                                                                                                              |
|pdf          |pdf: File                           |This stores the pdf of the paper                                                                                                                                 |
|png          |png: File                           |This stores the screenshot of the first page to be displayed on the results page.                                                                                |
|text         |text: String[]                      |This is the content of the paper, extracted in plain text form to increase the search speed.                                                                     |

#### Iteration 2
|Property Name|Signature         |Description                                                                                                                |
|-------------|------------------|---------------------------------------------------------------------------------------------------------------------------|
|title        |title:String      |This is the title of the paper that the user inputs, short and direct.                                                      |
|description  |description:String|This is the description of the paper that the user inputs. It can be used as a abstract of the paper.                      |
|tags         |tags: String[]    |This returns the tags that the paper is associated with through manual assignment or automatic detection by the classifier.|
|pdf          |pdf: File         |This stores the pdf of the paper                                                                                           |
|png          |png: File         |This stores the screenshot of the first page to be displayed on the results page.                                          |
|text         |text: String[]    |This is the content of the paper, extracted in plain text form to increase the search speed.                               |

I realised that the user wants more flexibility to add and remove tag that I cannot foresee during development, so I've generalized the class to allow for more flexibility.

#### Methods
This class does not have any method.

### Class - Search Engine
This is an API for interacting with the search engine that returns the paper given some phrases. The implementations of the methods are not shown here. It might be implemented with the Google Search Engine or one that I write myself. A search engine is algorithm-based, therefore it's difficult to break it down into smaller methods. 

#### Properties
This class does not have any property.

#### Methods
##### Iteration 1
|Method Name |Signature                                                                                                                             |Description                                                                                              |
|------------|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
|searchPapers|searchPapers(keywords: String[], tags: String[], topics: String[], approaches: String[], methods: String[], ethics: String[]): Paper[]|This returns the set of paper, in order of relevance, based on a series of parameters the user has given.|

##### Iteration 2
|Method Name |Signature                                                        |Description                                                                                              |
|------------|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
|searchPapers|searchPapers(keywords: String[], tags:Tag[], user: User): Paper[]|This returns the set of paper, in order of relevance, based on a series of parameters the user has given.|

Since the refactor, the tags do not have their hard coded tag groups, so the method parameter is less. 

### Class - User
This class represents a registered user

#### Properties

##### Iteration 1
|Property Name|Signature     |Description                                                                     |
|-------------|--------------|--------------------------------------------------------------------------------|
|name         |name: String  |The name of the user.                                                          re |
|email        |name: Email   |The email of the user.                                                          |
|type         |type: UserType|The type of the user, i.e. whether it is a standard user, an editor or an admin.|

##### Iteration 2
|Property Name|Signature         |Description                                                                     |
|-------------|------------------|--------------------------------------------------------------------------------|
|name         |name: String      |The name of the user.                                                           |
|email        |name: Email       |The email of the user.                                                          |
|type         |type: UserType    |The type of the user, i.e. whether it is a standard user, an editor or an admin.|
|bookmarks    |bookmarks: Paper[]|The papers that the users have bookmarked.                                      |

This iteration reflects the added functionality of allowing users to bookmark paper and having users who have different permissions. 

#### Methods
This class does not have have any method.

## Algorithm / DFD
The following code is written in python-like pseudocode.

### Uploaded Paper processing
```
def process_pdf(paper):
    screenshot = screenshot_pdf(paper)
    text = extract_text(paper)
    return screenshot, text

def screenshot_pdf(paper):
    ... # To be implemented using external library
    return screenshot

def extract_text(paper):
    raw_text = ... # To be implemented using external library
    text = raw_text.lower().replace(continuous-white-space, " ").replace(punctuations, "")
```

### Search algorithm
```
def search_ranked(terms, tags, user):
    terms = terms.lower().replace(continuous-white-space, " ").replace(punctuations, "")
    scores = {}
    for paper in database.all_papers:
        scores[paper] = 0
    for paper in database.all_papers:
        score = scores[paper]
        if paper.is_bookmarked_by(user):
            scores += weighting
        score += levenshtein_distance_score(terms, paper.title) * weighting
        socre += levenshtein_distance_score(terms, paper.description) * weighting
        score += levenshtein_distance_score(terms, paper.text) * weighting
        # paper.tags_contains_count(tags) is the size of the intersection of tags of the paper and tags.
        # paper.tags_no_contain_count(tags) count the size of the relative complement of the tags in the paper in tags.
        score += paper.tags_contains_count(tags) / len(tags) * weighting
        score += paper.tags_no_contain_count(tags) / len(max([paper.tags_no_contain_count(tags) for paper in database.all_papers]))
    return scores.sorted_by_value()
```

### Infrastructure

![Infrastructure Iteration 1](img/infrastructure%20iteration%201.png)
\

### Upload Paper 

![Upload Paper Iteration 1](img/upload%20paper%20iteration%201.png)
\

### Search Results

![Search Results Iteration 1](img/search%20results%20iteration%201.png)
\

## Test Plan 
|Action to Test                                                                                                            |Method of Testing                                              |Expected Results                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |Success Criteria|
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
|When the upload is invalid, it should gracefully fall back to an none-intrusive error message                             |Alpha Testing, Beta Testing, User Acceptance Testing, Debugging|Normal Input: The user uploads a paper. Expected Output: The website responds immediately to user's and start processing. Abnormal Input: The user selects a file that is not a PDF, leaves some fields empty, or clicks the button multiple times. Expected Output: The website should nicely notify the user that they have not inputted the right data (i.e. no js alter()). The user should not be able to submit the form multiple times. Extreme Input: Adversary tries to upload paper into the base without permission. Expected Output: The website should block the request.|1.1, 2.2        |
|User should be notified when there is an error in the server                                                              |Alpha Testing, Debugging                                       |Normal Input: Everything works in the server. Expected Output: Everything proceeds as normal. Abnormal Input: The server crashes. Expected Output: A custom 500 page that notifies the user that something went wrong in the server. Extreme Input: The server crashes again when trying to catch the error. Expected Output: falls back to an even safer error page that is more unlikely to fail.                                                                                                                                                                                   |All             |
|If a paper fails to upload or process, the server should display as much information as possible without entirely crashing|Alpha Testing, Debugging                                       |Normal Input: Everything works. Expected Output: Everything proceeds as normal. Abnormal Input: The file is corrupt such that the server cannot process the file. Expected Output: when the user requests for the file, the server should display that the file has failed to render, but the failure should not affect any other paper. Extreme Input: the file triggers an exception in unexpected place. Expected Output: the paper that is being uploaded should be the only paper that is affect by the bug.                                                                     |1.3, 1.6, 1.7   |
|User can log in                                                                                                           |Alpha Testing, Beta Testing, User Acceptance Testing           |Normal Input: the user logs in with Google clicking the right buttons. Expected Output: the user logs in as normal. Abnormal Input: the users logs in with the wrong email account. Expected Output: the user is still logged in, but they can log out. Extreme Input: the user does not accept any cookie. Expected Output: login fails.                                                                                                                                                                                                                                             |1.4, 2.1, 2.2   |
|Support for zooming                                                                                                       |Alpha Testing, User Acceptance Testing                         |Normal Input:the user views it on a desktop or laptop with a large screen, or the user views it on a phone with a small screen. Expected Output: The website functions as normal and all functions are accessible. Abnormal Input: The user zooms in roo much. Expected Output: The website UI breaks down. Extreme Input: none                                                                                                                                                                                                                                                       |3.1             |
|All the links in the website are valid                                                                                    |Alpha Testing, Beta Testing, User Acceptance Testing           |Normal Input: The user clicks on a link on the page. Expected Output: the website functions as normal. Abnormal Input: The user enters something random into the browser address bar. Expected Output: the website returns a nice 404 page with helpful links. Extreme Input: attacker tries to inject code with the url. Expected Output: the server blocks it.                                                                                                                                                                                                                      |All             |
