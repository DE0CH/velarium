# Criterion A
## Description of Scenario

My client is a psychology teacher in my school. For the subject Psychology, students often need to quote studies to support their claims in their exams or research paper. The categorization for the papers is very specific to IB as well, such as the nine designated topics, the three different approaches. There is also a very specific set of studies that are considered valid for the examination. In my initial meeting with her (See Interview Transcript #1 in Appendix), she said that students can benefit greatly from a search engine that can filter the studies for them as they would not need to manually go through all the studies themselves on the internet to find the relevant ones. The current search engine such as Google Scholar and Jstor are not suitable for the specific scenario as they contain a very large dataset, many of the papers are not suitable for IB Psychology. She told me that she would want students to be able to search for specific topics and approaches. She would also want to be able to guide students through manually tagging papers.

## Rational
I judge that using a web app would be most suitable for the Scenario. More specifically, using Django + Python + Semantic UI as the development frameworks, SQL, AWS S3 as the database and storage, and deploying on Heroku. A web app is chosen over a conventional app for several reasons. First, the database will be updated periodically by the teacher, so it would be convenient if all the students and teacher share the same database in order to eliminate the duplication of files. Second, a web app would load faster as it does not require download from the user. Third, it works cross platform as it would only require a web browser, which exist on almost all platforms such as Mac, Windows, Ubuntu Desktop,  smartphones and tablets. It significantly widens the compatibility of the program without requiring the programmer to make a program for every platform. While cross platforms tools such as electron does exist, those are unnecessary as the project would not need to be run offline. In addition, the city of the client has a well-built internet infrastructure, so a slow or unavailable internet is not a concern. Lastly, making this a web app significantly reduces the maintenance cost as an update can be pushed out instantly for everyone when there is a feature update. 

The reason to choose Python and Django as the back end framework is predominately due to the connivance. Python is chosen over other programming language such as Java and C++ because of the faster development speed in trade of the slower runtime speed (Barot). The program does not need to have excellent performance as there would not be too much traffic. A web development framework would be very beneficial as that eliminates the need to write a web app from scratch. Plain HTML, CSS and Javascript (i.e. a static website) is not suitable for this project as the database will be dynamically updated by the client. For the exact reason, Django is chosen over other Python web development frameworks such as Flask because it has a very well-built interface for SQL databases that allow the user to interface with Python instead of SQL syntax (Singh). 

I choose Semantic UI as the front end development framework because it speeds up the development time as well. Semantic UI is particularly useful as it has a very large library of beautiful elements and modules for developers to incorporate into their design. 

## Success Criteria

### 1. Functionality
1. Admins and Editors can upload paper and add tags.
2. The search function would return relevant result.
3. Admins can add students to add studies to the website's database.
4. The user can to see the thumbnail and successfully download the PDF.
5. The storage is large enough to store all the PDFs in the database.


### 2. Security
1. Only the editors can modify the database.
2. Only the admins can modify manage user permissions.
3. The site in encrypted in transit.
4. Plain text password is never stored in the database. 

### 3. Accessibility
1. The UI still works when it's zoomed in or viewed on a smaller device like a mobile screen.

# Criterion B

## Record of Tasks
|Task number|Planned Action                                                 |Planned Outcome                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |Time Estimated|Target Date (yyyy/mm/dd)|Criterion|Stage         |
|-----------|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|------------------------|---------|--------------|
|1          |Interview with the client to understand her needs              |Understand her needs and have a vision for the website                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |2 hours       |2020/10/12              |A        |Planning      |
|2          |Preliminary research to find out the tools to use              |Understand the strength and weakness of of different frameworks and make a choice                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |5 hours       |2020/10/20              |A        |Planning      |
|3          |Create the UI mockup for the website                           |Completed the mockups                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |2 hours       |2020/10/28              |A        |Design        |
|4          |Create a rough prototype for the UI with hardcoded data        |Client confirms whether it is something she wants                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |4 hours       |2020/11/4               |B, C     |Design        |
|5          |Push the project to Heroku and host the website                |The website is accessible through the internet                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |1 hour        |2020/11/4               |C        |Implementation|
|6          |Restructure the website UI as per client's request to allow for multiple selection for tags|Client is happy with the new design                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |5 hours       |2020/11/14              |E        |Testing       |
|7          |Restructure the data structure of the website to allow for more flexibility|Client can create new tags and remove old ones                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |5 hours       |2020/11/19              |C        |Developing    |
|8          |Test that I can create new paper objects in the database with new user interface|The objects would be created without no error                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |3 hours       |2020/11/20              |C        |Testing       |
|9          |Setting the browser to upload directly to the s3 bucket instead of through the server|Website is much faster simply because the file server is located closer to the client and has a higher bandwidth                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |5 hours       |2020/11/25              |C        |Developing    |
|10         |Fix a bug in django-storage :(                                 |The bug is fixed and the issue is still unaddressed by the library developers :(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |2 hours       |2020/12/4               |C        |Developing    |
|11         |Create the add tags page                                       |The page is finished and functional                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |5 hours       |2020/12/14              |C        |Developing    |
|12         |Integrate log in with google                                   |User can log in with Google and the UI looks integrated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |6 hours       |2020/12/19              |C        |Developing    |
|13         |Refactor the user types so that different users have different permissions|User with their respective permissions can accomplish different tasks                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |2 hours       |2020/12/22              |C        |Developing    |
|14         |Add an admin page for admins to manage user permissions        |Admins can change the permissions of other users                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |3 hours       |2020/12/26              |C        |Developing    |
|15         |Write the search engine                                        |The search engine works and returns relevant results                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |4 hours       |2021/1/2                |C        |Developing    |
|16         |Write the edit paper page                                      |User can edit the paper even after it is uploaded                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |3 hours       |2021/1/5                |C        |Developing    |
|17         |Get the client feedback for the finished product               |Client is happy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |2 hours       |2020/1/9                |E        |Testing       |
|18         |Conduct user training by given the client a 20 minute walk through of the program|The user knows how to use the website                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |20 minutes    |2020/1/20               |E        |Implementation|


## Use Cases

### Iteration 1 
![User Cases Iteration 1](img/use%20cases%20iteration%201.png)
\

### Iteration 2
![User Case Iteration 2](img/use%20cases%20iteration%202.png)
\

The client feedback that she would like to use the help of students to manage some paper for her but would not want them to change who can edit the papers (See Meeting #2 transcript in Appendix). Therefore I have decided to refactor the user into three groups: standard, editor and admin. Standard users can only view the website and bookmark for themselves, editors can, in addition, add, edit and remove papers, and admin can, in addition, manage the permissions of users.

## UML

### Iteration 1
![UML Iteration 1](img/uml%20iteration%201.png)
\

### Iteration 2
![UML Iteration 2](img/uml%20iteration%202.png)
\

This UML reflects changes in the data structure from one specific to the structure of psychology units and paper to that of a general tagging system. As I talked my client, it was difficult for me to get all the tag groups that she needs, and there seemed to be more she would want later (see Meeting #2 Transcript in Appendix). Therefore I have decided to hand the control of the specific tags to user and generalize the data structure to accommodate it. The user now also has their type, allowing them to have different permission to edit the content. 

## Mockup

### Landing Page
This is the page that the user first sees when he/she open the application. It presents them options for their search. Layout is powered by Bootstrap.

#### Iteration 1
![Landing Page Iteration 1](img/landing%20page%20iteration%201.png)
\ 

#### Iteration 2
![Landing Page Iteration 2](img/landing%20page%20iteration%202.png)
\ 

After the first iteration, the client gave me feedback that she would want to be able to select multiple topic and approaches for each search box (See Meeting #2 Transcript in Appendix). After I have found no way to implement it with Bootstrap and I didn't want to write UI from scratch because it will inevitably look ugly, I found out that I could use a framework called Semantic UI.

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
The program is a web app, so part of the functionality will be accomplished through JS running on client's computer, but a core part of the program will be accomplished through back-end code in Python running on Heroku and storage stored in AWS S3.  The UI will be rendered using client's web browser.


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
|pdf          |pdf: File                           |This stores the pdf of the paper.                                                                                                                                |
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

I realised that the the client might want more flexibility to add and remove tag that I cannot foresee during development, so I've generalized the class to allow for more flexibility.

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

Since the refactor, the tags do not have their hard coded tag groups, so the method has fewer parameters. 

### Class - User
This class represents a registered user

#### Properties

##### Iteration 1
|Property Name|Signature     |Description                                                                     |
|-------------|--------------|--------------------------------------------------------------------------------|
|name         |name: String  |The name of the user.                                                           |
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
This class does not have any method.

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

In the algorithm, the `weighting` is different for each aspect. The specific values are to be fined tuned after the database is populated.

### Infrastructure / Database Design
![Infrastructure Iteration 1](img/infrastructure%20iteration%201.png)
\

The structure of the SQL database:

```
codestudy::DATABASE=> \d
                           List of relations
 Schema |               Name                |   Type   |     Owner
--------+-----------------------------------+----------+----------------
 public | auth_group                        | table    | ivpfdqmvlivkii
 public | auth_group_id_seq                 | sequence | ivpfdqmvlivkii
 public | auth_group_permissions            | table    | ivpfdqmvlivkii
 public | auth_group_permissions_id_seq     | sequence | ivpfdqmvlivkii
 public | auth_permission                   | table    | ivpfdqmvlivkii
 public | auth_permission_id_seq            | sequence | ivpfdqmvlivkii
 public | auth_user                         | table    | ivpfdqmvlivkii
 public | auth_user_groups                  | table    | ivpfdqmvlivkii
 public | auth_user_groups_id_seq           | sequence | ivpfdqmvlivkii
 public | auth_user_id_seq                  | sequence | ivpfdqmvlivkii
 public | auth_user_user_permissions        | table    | ivpfdqmvlivkii
 public | auth_user_user_permissions_id_seq | sequence | ivpfdqmvlivkii
 public | codestudy_paper                   | table    | ivpfdqmvlivkii
 public | codestudy_paper_tags              | table    | ivpfdqmvlivkii
 public | codestudy_paper_tags_id_seq       | sequence | ivpfdqmvlivkii
 public | codestudy_tag                     | table    | ivpfdqmvlivkii
 public | codestudy_tagclass                | table    | ivpfdqmvlivkii
 public | codestudy_user                    | table    | ivpfdqmvlivkii
 public | codestudy_user_bookmarks          | table    | ivpfdqmvlivkii
 public | codestudy_user_bookmarks_id_seq   | sequence | ivpfdqmvlivkii
 public | django_admin_log                  | table    | ivpfdqmvlivkii
 public | django_admin_log_id_seq           | sequence | ivpfdqmvlivkii
 public | django_content_type               | table    | ivpfdqmvlivkii
 public | django_content_type_id_seq        | sequence | ivpfdqmvlivkii
 public | django_migrations                 | table    | ivpfdqmvlivkii
 public | django_migrations_id_seq          | sequence | ivpfdqmvlivkii
 public | django_session                    | table    | ivpfdqmvlivkii
(27 rows)
```
![AWS S3 Bucket](img/aws%20s3%20bucket.png)

### Upload Paper 
![Upload Paper Iteration 1](img/upload%20paper%20iteration%201.png)
\ 

### Search Results
![Search Results Iteration 1](img/search%20results%20iteration%201.png)
\ 

## Test Plan 
|Action to Test                                                                                                             |Method of Testing                                              |Expected Results                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |Success Criteria|
|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
|When the upload is invalid, it should gracefully fall back to an none-intrusive error message                              |Alpha Testing, Beta Testing, User Acceptance Testing, Debugging|Normal Input: The user uploads a paper. Expected Output: The website responds immediately to user's and start processing. Abnormal Input: The user selects a file that is not a PDF, leaves some fields empty, or clicks the button multiple times. Expected Output: The website should nicely notify the user that they have not inputted the right data (i.e. no js alter()). The user should not be able to submit the form multiple times. Extreme Input: Adversary tries to upload paper into the base without permission. Expected Output: The website should block the request.|1.1, 2.2        |
|User should be notified when there is an error in the server                                                               |Alpha Testing, Debugging                                       |Normal Input: Everything works in the server. Expected Output: Everything proceeds as normal. Abnormal Input: The server crashes. Expected Output: A custom 500 page that notifies the user that something went wrong in the server. Extreme Input: The server crashes again when trying to catch the error. Expected Output: falls back to an even safer error page that is more unlikely to fail.                                                                                                                                                                                   |All             |
|If a paper fails to upload or process, the server should display as much information as possible without entirely crashing |Alpha Testing, Debugging                                       |Normal Input: Everything works. Expected Output: Everything proceeds as normal. Abnormal Input: The file is corrupt such that the server cannot process the file. Expected Output: when the user requests for the file, the server should display that the file has failed to render, but the failure should not affect any other paper. Extreme Input: the file triggers an exception in unexpected place. Expected Output: the paper that is being uploaded should be the only paper that is affect by the bug.                                                                     |1.3, 1.5, 1.6   |
|User can log in                                                                                                            |Alpha Testing,Beta Testing,User Acceptance Testing             |Normal Input: the user logs in with Google clicking the right buttons. Expected Output: the user logs in as normal. Abnormal Input: the users logs in with the wrong email account. Expected Output: the user is still logged in, but they can log out. Extreme Input: the user does not accept any cookie. Expected Output: login fails.                                                                                                                                                                                                                                             |1.4, 2.1, 2.2   |
|Support for zooming                                                                                                        |Alpha Testing, User Acceptance Testing                         |Normal Input:the user views it on a desktop or laptop with a large screen, or the user views it on a phone with a small screen. Expected Output: The website functions as normal and all functions are accessible. Abnormal Input: The user zooms in roo much. Expected Output: The website UI breaks down. Extreme Input: none                                                                                                                                                                                                                                                       |3.1             |
|All the links in the website are valid                                                                                     |Alpha Testing,Beta Testing,User Acceptance Testing             |Normal Input: The user clicks on a link on the page. Expected Output: the website functions as normal. Abnormal Input: The user enters something random into the browser address bar. Expected Output: the website returns a nice 404 page with helpful links. Extreme Input: attacker tries to inject code with the url. Expected Output: the server blocks it.                                                                                                                                                                                                                      |All             |
|The Admin can assign new editors                                                                                           |Alpha Testing, Beta Testing, Integration Testing               |Normal Input: the user tries to add new user to editors. Expected Output: the user can edit the database now. Abnormal Input: none. Extreme Input: none                                                                                                                                                                                                                                                                                                                                                                                                                               |1.3             |
|The PDF processor can successfully screenshot the first page of the PDF                                                    |Alpha Testing, User Acceptance Testing, Debugging              |Normal Input: the user uploads a valid PDF. Expected Output: the screenshot is successfully taken. Abnormal Input: The user selected the wrong PDF. Expected Output: the PDF is still processed, but the user can delete it later. Extreme Input: the user uploads an invalid PDF. Expected Output: the processor returns an error message                                                                                                                                                                                                                                            |1.5, 1.6        |
|Browser notifies that the site is encrypted in transit (in Firefox, there is a padlock icon on the left of the address bar)|Alpha Testing, Integrating Testing                             |Normal Input: the user requests for the HTTPS site. Expected Output: the server returns the signed and encrypted site. Abnormal Input: the user requests for the HTTP site. Expected Output: the server redirects the request to HTTPS. Extreme input: none.                                                                                                                                                                                                                                                                                                                          |2.3             |
|No plain text password stored in the database                                                                              |Alpha Testing, Debugging                                       |Input: none                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |2.4             |

# Criterion C
On a high level overview, the website I designed is a dynamic web application that uses tags, titles and descriptions to organise pdf documents in a database, which, specifically for my client, are psychology papers that students will use, but because the application is highly dynamic, it can also be used for other types of papers. I will give a general overview of technical skills and algorithms.

Most of the processing is done in the server backend, with some light processing mostly responsible for the UI in the front end. All the users using the website share the same database. 

## List of Technical Skills

- Using multiple frameworks and languages
- Using Django Models
- Using cloud storage (S3)
- Using JS to dynamically update the page content
- Concurrent programming with JS Promise
- Multithreading in the server to increase responsiveness
- Using presigned URL
- Securely handle API secrets in an open source application
- Graceful multiple fall backs to increase responsiveness 

## List of Algorithm Used

- Concurrency to improve responsiveness
- Memorisation for optimisation
- Primitive Search algorithm

## Part 1: UI Design and Dynamic Web Layout

The UI was designed with Semantic UI, rendered with the help of Django Template language with some custom JS script for the dynamic elements. 

Example 1: Using Django template language to implement loose coupling. Because all pages share the same menu items and UI library, I have put them in one HTML that allows subsequent pages to extend on that to reduce the code size, reducing the potential sources of bugs. The HTML comments illustrate the technical skills. 

In `codestudy/template/codestudy/base.html`:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
		...
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.css"> <!--Semantic UI libray-->
    <meta name="google-signin-client_id"
          content="330093561618-bc6pprilkfqi5sc6oibm376psnfe9tub.apps.googleusercontent.com"> <!--Log in with Google library-->
    <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}"/> <!--The favicon to be displayed-->
    <title>{% block title %}Code Study{% endblock %}</title>
</head>
<body>
<div class="ui menu">
		...
    {% if user.can_edit %} <!--Example of Dynamic UI. The options only show if the user has premission to edit the database-->
        <a class="item" id="menu-add-paper" href="{% url 'codestudy:add-paper' %}">Add Paper</a>
        <a class="item" id="menu-edit-tags" href="{% url 'codestudy:edit-tags' %}">Edit Tags</a>
    {% endif %}
    {% for tag_class in tag_classes %} <!--Example of Dynamic UI. The number of items in the menu expands as the user adds more tag class-->
        <div id="menu-{{ tag_class.pk }}" class="ui dropdown item">
            {{ tag_class.name }}
            <i class="dropdown icon"></i>
            <div class="menu">
                {% for tag in tag_class.tag_set.all %}
                    <a class="item" href="{% url 'codestudy:browse' tag_class.name tag.name %}">{{ tag.name }}</a>
                {% endfor %}
            </div>
        </div>
    {% endfor %}
    <a class="item" id="menu-all-papers" href="{% url 'codestudy:all-papers' %}">All Papers</a>
		...
</div>
	...
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW"
        crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.js"></script>
<script src="https://apis.google.com/js/api:client.js"></script>
<script>
		...
</script>
{% block js %} <!--Example of lose coupling in the Django template langauge. The block tag allows me to add more javascript based on the base-->
{% endblock %}
</body>
</html>
```

Example 2: Even though there are multiple ways to search for a paper, they all share the same HTML base template, except with different data. 

In `codestudy/templates/codestudy/results.html`:

```html
{% extends "codestudy/base.html" %}
{% load codestudy_tags %}
{% block title %}
    {{ page_title }} | Code Study
{% endblock %}
{% block content %}
    <div class="ui container">
        {% if not papers %} <!--Example of responsive UI design. If there is nothing, the UI displays a message affirmation so the page would not seem to not have loaded-->
            <div class="ui text container">
                <div class="ui message">
                    <div class="header">Nothing to Show</div>
                    <p>
                        There is nothing in the database that matches your search.
                    </p>
                </div>
            </div>
        {% endif %}
        <div class="ui three column stackable grid">
            {% for paper in papers %}
								... Layout for the paper. Omitted for concision.
								<!--Exampl of lose coupling. Depending on the paper variable passed in from Python script, the document will display different results-->
            {% endfor %}
        </div>
    </div>
{% endblock %}
{% block js %}
    <script>
				...
        function like(pk) { 
					  <!--Example of Dynamic web design. When the bookmark button is clicked, the JS immediately sends a request to the server to update the status. Notice that the user is not specified in the request because that is automatically delivered by a browser cookie for security purposes (because the cookie is signed upon login verification).--> 
            const likeBtn = $('#like-' + pk);
            const xhr = new XMLHttpRequest();
            xhr.open('GET', '{% url 'codestudy:bookmark' %}?pk=' + pk);
            xhr.send();
            if (likeBtn.hasClass('outline')) {
                likeBtn.removeClass('outline');
            } else {
                likeBtn.addClass('outline');
            }
        }
    </script>
{% endblock %}
```

The templates in combination with a helper function `get_base_context(request)` in `codestudy/views.py` allows the dynamic menu bar to be displayed across all pages without much effort. 

In `codestudy/views.py`:

```python
def get_base_context(request):
    return {
        'user': get_user(request),
				# get_user is a helper function that returns the User object. Implementation of it will be addressed in the next section.
        'tag_classes': TagClass.objects.all()
    }
```

Beside the dynamic rendering on the server side, the client also uses dynamic rendering implemented using JS. One prime example is in `codestudy/templates/codestudy/edit-tags.html`:

```jsx
...
function htmlToElement(html) {
    let template = document.createElement('template');
    html = html.trim(); // Never return a text node of whitespace as the result
    template.innerHTML = html;
    return template.content;
}

function addTag(tagClassPk, tagClassName) {
    const newTagInput = $('#new_tag_input_' + tagClassPk);
    const tagName = newTagInput.val();
    const tagPk = uuid.v4();
    // Get the tag name that user inputs and assign a UUID as the primary key
    changeLog.newTags.push({
        pk: tagPk,
        name: tagName,
        tagClass: tagClassName
    });
    // Push change to the changeLog to be sent to the server
    newTagInput.val('');
    $('#new_tags_' + tagClassPk).before(htmlToElement(`
        <tr id="tag_${tagPk}">
            <td>${tagName}</td>
            <td class="right aligned" onclick="deleteTag('${tagPk}')">
                <button class="ui icon button"><i class="trash icon"></i></button>
            </td>
        </tr>
    `));
    // Update the UI to reflect the added tag
}

function deleteTag(tagPk) {
    const tagUi = $(`#tag_${tagPk}`);
    const tagDeleteButton = tagUi.find('td > button');
    if (tagDeleteButton.hasClass('negative')) {
        tagDeleteButton.removeClass('negative');
        changeLog.deletedTags.delete(tagPk);
    } else {
        tagDeleteButton.addClass('negative');
        changeLog.deletedTags.add(tagPk);
    }
    // If the tag is not marked deleted, mark it deleted and vise versa.
    tagDeleteButton.removeClass('active');
}

function addTagClass() {
    const newTagClassInput = $('#new_tag_class_input');
    const tagClassName = newTagClassInput.val();
    if (tagClassName === '') { // Check if the input is empty and display an error message if so
        const TagClassError = $('#tag_class_error');
        TagClassError.removeClass('hidden');
        setTimeout(() => TagClassError.addClass('hidden'), 2000);
        return;
    }
    const tagClassPk = uuid.v4();
    // Get the tag name that user inputs and assign a UUID as the primary key
    changeLog.newTagClasses.push({
        pk: tagClassPk,
        name: tagClassName,
    });
    // Push change to the changeLog to be sent to the server
    newTagClassInput.val('');
    $('#new_tag_classes').before(htmlToElement(`
        <div id="tag_class_${tagClassPk}" class="ui stackable grid">
            <div class="twelve wide column">
                <h1>${tagClassName}</h1>
            </div>
            <div class="four wide column right aligned">
                <button class="ui icon fluid button" onclick="deleteTagClass('${tagClassPk}')"><i class="trash icon"></i></button>
            </div>
        </div>
        <table class="ui left aligned table">
            <tbody>
                <tr id="new_tags_${tagClassPk}">
                    <td>
                        <div class="ui input">
                            <input id="new_tag_input_${tagClassPk}" type="text" placeholder="New tag...">
                        </div>
                    </td>
                    <td class="right aligned">
                        <button class="ui icon button" onclick="addTag('${tagClassPk}', '${tagClassName}')"><i class="plus icon"></i></button>
                    </td>
                </tr>
            </tbody>
        </table>
    `));
    // Update the UI to reflect the added tag
}
...
```

Importantly, the webpage tracks and uploads only the changes to the database instead of the entire data The `addTag` and `addClass` functions adds the element to the webpage with the relevant click handler. Admittedly, using a string to render html element is not the most efficient and elegant approach. I should create reusable elements using frameworks like React, but judging this is the only page that requires such dynamic rendering, the improved efficiency would not justify the development cost. 

Another example of dynamic rendering is in selecting the ways to upload. The user can either choose to upload a link or a PDF by selecting from the dropdown menu. The JS element will then change the requirement validation of the form accordingly.

![Upload with File](img/upload%20with%20file.png)

![Upload with URL](img/upload%20with%20url.png)

In `codestudy/templates/codestudy/add-paper.html`:

```jsx
...
uploadOptionsSelect
    .dropdown({
        onChange: function (value, text, $selectedItem) {
            uploadOption = Number(value);
            if (uploadOption === uploadOptionsEnum.file) {
								// Change the element displayed on the screen
                pdf.removeAttr('hidden');
                link.attr('hidden', 'hidden');
								// Update form validation standard
                form.form({
                    fields:
                        {
                            title: 'empty',
                            description: 'empty',
                            pdf: 'empty',
                        }
                });
            } else if (uploadOption === uploadOptionsEnum.link) {
								// Change the element displayed on the screen
                pdf.attr('hidden', 'hidden');
                link.removeAttr('hidden');
								// Update form validation standard
                form.form({
                    fields:
                        {
                            title: 'empty',
                            description: 'empty',
                            link: 'empty',
                        }
                });
            } else {
								// Assertion to notify a potential source of bug
                console.assert(false, "Upload Option does not match any known type");
            }
        }
    })
;
...
```


## Part 2: Storage and Database

The storage was implemented in AWS S3, and database uses PostgresSQL build in on Heroku. This illustrates my technical ability of using cloud database and storage.

There are primarily three parts that enabled the cloud storage — provisioning and configuring an S3 bucket, integrating the storage into Django models, and optimisation by allowing the user to directly upload into the s3 bucket without having to go through the server. 

The bucket is called `codestudy` — the name of the application, and an IAM user is created in AWS with the following policy. The limited scope ensures that even if the API keys are leaked, other buckets and services would not be affected.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::codestudy"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObject"
            ],
            "Resource": "arn:aws:s3:::codestudy/*"
        }
    ]
}
```

Because the browser needs to upload paper into the database, I have to configure it so that it allows for cross-origin request that is normally blocked for security reasons ("Cross-origin resource"). It access from the `codestudy` url and `localhost` for development purposes.

```json
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "PUT",
            "POST",
            "HEAD",
            "DELETE"
        ],
        "AllowedOrigins": [
            "https://codestudy.herokuapp.com",
            "http://localhost:8000"
        ],
        "ExposeHeaders": []
    },
    {
        "AllowedHeaders": [],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```

The S3 database requires API keys and secrete, but because I intend to have the application open source, I cannot direly put the keys in plain text in the source code (D33tah). Therefore, I have put them in the environmental variable with a file `.env` which is untracked by git and separately uploaded onto heroku. 

In `main/settings.py`:
```python
import dotenv

# Load the environment variables from .env file if there is such a file on the disk
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
...

# Load the environment variables into Python variables
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
```

In `.env`:
```
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
```

These demonstrate my technical ability to use cloud storage effectively.

The integration in the Django model is achieved through using the (buggy) `django-storage` library. Because the storage library does not support the Hong Kong server, I have to use a lower level library `boto3` to sign the object urls.

In `main/storage_backends.py`:
```python
from abc import ABC
from storages.backends.s3boto3 import S3Boto3Storage
from utils import generate_presigned_url


class MediaStorage(S3Boto3Storage, ABC):
    
    def url(self, name, parameters=None, expire=None, http_method=None):
        if expire is None:
            expire = 3600
        response = generate_presigned_url(name, 600)
        return response
```

In `utils.py`:
```python
from django.conf import settings
import boto3
import botocore.client

# Make a persistent s3 client
s3_client = boto3.client('s3',
                         aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                         config=botocore.client.Config(s3={'addressing_style': 'virtual'}, signature_version='s3v4'),
                         region_name=settings.AWS_S3_REGION_NAME)


def generate_presigned_url(object_key, expiration):
    presigned_url = s3_client.generate_presigned_url('get_object',
                                                     Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                                                             'Key': object_key},
                                                     ExpiresIn=expiration)
    return presigned_url

```

In the previous code example, I have overridden the default general url function to use a lower level function provided by `boto3` and wrapped in `utils.py`.

JS in the browser allows the user to upload to s3 directly, greatly improving the speed of the website.

In `codestudy/templates/codestudy/add-paper.html`:
```html
...
<button type="button" class="ui fluid large teal button" id="fake-submit" onclick="fs()">Add</button>
<!-- fs stands for fake submit, btw -->
...
<script>
    ...
    async function fs() {
        const submit = $('#submit');
        // If the form is invalid, click the button so that the error can show. If the file is uploaded, click the 
        // button so that the form can be submitted. If a link is supplied, click the submit button normally because 
        // there is no extra step to handle file upload.
        if (uploaded || !form.form('is valid') || uploadOption === uploadOptionsEnum.link) {
            submit.click();
            return;
        }
        // The button that the user clicks is a dummy button so that the JS code can intercept.
        $('#fake-submit').css('display', 'none');
        bar.css('display', 'block');
        // Clean the data and get the upload credentials from the server.
        const s3Data = await getS3Data(pdf.val().replace(/C:\\fakepath\\/i, ''));
        let fileName = await uploadFile(pdf.prop('files')[0], s3Data);
        $('#pdf-key').val(fileName);
        pdf.val(null);
        // Clear the form validation.
        form.form({});
        uploaded = true;
        submit.click();
    }

    /** This gets the presigned data from the server in order for the browser to upload, and returns a Promise
     * of the data.
     * @param {string} fileName The file name of the file to be uploaded. Used as part of the presigned signature.
     * @return {Promise<Object>} The presigned S3 data.
     */
    function getS3Data(fileName) {
        return new Promise((resolve, reject) => {
            const url = "{% url 'codestudy:presign-s3' %}?" + $.param({file_name: fileName});
            $.get(
                url,
                data => resolve(data)
            )
        });
    }

    /**
     * Upload the file given file to the S3 bucket.
     * @param {File} file The file to be uploaded.
     * @param {Object} s3Data The presigned S3 data.
     * @return {Promise<string>} The object key in the S3 bucket.
     */
    function uploadFile(file, s3Data) {
        return new Promise(resolve => {
            postData = ... // Add the post data as required by s3 specifications.
            xhr.onreadystatechange = () => {
                if (xhr.readyState === 4 && (xhr.status === 200 || xhr.status === 204)) {
                    resolve(s3Data.fields.key);
                }
            };
            xhr.send(postData);
        });

    }
</script>
```

In particular in `getS3Data(fileName)`, I have demonstrated my ability to code using concurrency in JS through Promise. I have also demonstrated to dynamically communicate between the front-end and the back-end.

## Part 3: User Login, Permissions & Security
Logging in is achieved through Sign in with Google. I have decided not to use username and password because that leads to higher security vulnerability as now I have to handle hashing, salting and storing the user data safely myself (Scott). Sign in with Google is easier for use as well. 

In `codestudy/templates/base.html`:
```html
<script>
    function logout() {
        // Use JS to visit the logout url.
        const xhr = new XMLHttpRequest();
        xhr.open('GET', '{% url 'codestudy:logout' %}');
        xhr.onload = () => {
            location.reload();
        };
        xhr.send();
    }

    function sendIdToken(idToken) {
        // Send the id token to server for validation.
        var xhr = new XMLHttpRequest();
        xhr.open('POST', "{% url 'codestudy:login' %}");
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onload = function () {
            const response = JSON.parse(xhr.responseText);
            location.reload();
        };
        xhr.send('id-token=' + idToken + '&csrfmiddlewaretoken=' + '{{ csrf_token }}');

    }

    gapi.load('auth2', function () {
        // Retrieve the singleton for the GoogleAuth library and set up the client.
        const auth2 = gapi.auth2.init({
            client_id: '330093561618-bc6pprilkfqi5sc6oibm376psnfe9tub.apps.googleusercontent.com',
            cookiepolicy: 'single_host_origin',
            // Request scopes in addition to 'profile' and 'email'
            //scope: 'additional_scope'
        });
        const element = document.getElementById('loginBtn');
        // Attach sign-in with Google to the sign-in button. 
        auth2.attachClickHandler(element, {},
            function (googleUser) {
                const id_token = googleUser.getAuthResponse().id_token;
                sendIdToken(id_token)
            }, function (error) {
                console.error(error);
            });
    });
</script>
```

In `codestudy/views.py`:
```python
...
def login(request):
    """
    This is a Django handler function that verifies the login details according to the token gained by signing in with
    Google. Designed to be interacted programmatically
    :param request: The Django Request object
    :return: The login status in JSON format
    """
    if request.method == 'POST':
        id_token = request.POST['id-token']
        try:
            # Specify the CLIENT_ID of the app that accesses the backend:
            id_info = google.oauth2.id_token.verify_oauth2_token(id_token,
                                                                 google.auth.transport.requests.Request(),
                                                                 settings.G_CLIENT_ID)

            user = User.objects.get_or_create(pk=id_info['sub'])[0]
            # Save the user info provided by Google to the database.
            user.email = id_info['email']
            user.name = id_info['name']
            user.given_name = id_info['given_name']
            user.family_name = id_info['family_name']
            user.save()
            # Set the session cookie so that the user is rememberd.
            request.session['sub'] = user.pk
            success = True
        except ValueError:
            # Invalid token
            success = False
    else:
        raise Http404()
    return JsonResponse({
        'success': success
    })
...
def logout(request):
    """
    This is a Django handler function that logs the current user out, designed to be accessed programmatically.
    :param request:
    :return:
    """
    try:
        # Delete the session cookie.
        del request.session['sub']
        success = True
    except KeyError:
        success = False
    return JsonResponse({'success': success})
...
```

The logout function visits the log out page, which clears the session cookie. This demonstrates my technical ability to integrate existing framework into my own app. The login function verifies the login details. For security, the data is accepted through post because the django post function requires a Cross-site request forgery token, which prevents arbitrary access to the database. In addition, I followed the documentation and used the id-token, which is signed with the secrete key of the Google API. This demonstrates my ability to handle user authentication well. 

In order to prevent unauthorized access, not only is the corresponding url hidden from view, but direct access to the urls will return a 404 page as if the pages don't exist. 

In `codestudy/views.py`:
```python
def add_paper(request):
    if get_user(request) and get_user(request).can_edit:
        ...
    else:
        raise Http404()

```

## Part 4: PDF processing

I need to complete two tasks with the PDF: extract the first page as a PNG image, and extract the plain text from the PDF to be used by the search engine, which uses the algorithm of optimization by memorization. Thankfully I was able to find external high-level libraries: `pdf2image` and `textract`. All I needed to do was to wrap the library so that I can integrate it easily into the website.

In `codestudy/pdf_processor.py`:
```python
import pdf2image
import os
from django.contrib.staticfiles.storage import staticfiles_storage
import re
import logging
import uuid
import textract
import string


def pdf_to_png_and_save(paper):
    """
    Takes a paper with the pdf file, capture the first page as a png and saves it to the paper object.
    :param paper: The Paper object to be processed.
    :return: None
    """
    # noinspection PyBroadException
    try:
        # Grab the screenshot of the first page
        paper.pdf.seek(0, 0)
        pdf_byte = paper.pdf.read()
        image = pdf2image.convert_from_bytes(pdf_byte, last_page=1, dpi=100)[0]
        png_name = str(uuid.uuid4())
        image.save(png_name, 'PNG')
        with open(png_name, 'rb') as f:
            paper.png.save(os.path.basename(paper.pdf.name).replace('.pdf', '') + '.png', f)
        os.remove(png_name)
        paper.pdf.close()
    except:
        # Processing has filed, fall back to default failed image.
        logging.exception('exception occurred converting pdf to png')
        with open(staticfiles_storage.path('failed/failed.png'), 'rb') as f:
            paper.png.save('failed.png', f)


def get_text(paper):
    """
    Extract the text content in the pdf, turn all characters to lowercase and replace each continuous whitespace with
    one space.
    :param paper: The Paper object to be processed.
    :return: The plain text in the paper.
    """
    id1 = str(uuid.uuid4())
    _RE_COMBINE_WHITESPACE = re.compile(r"\s+")
    paper.pdf.seek(0, 0)
    with open(id1, 'wb') as of:
        of.write(paper.pdf.read())
    paper.pdf.close()
    text = textract.process(id1, extension='pdf').decode('utf-8')
    os.remove(id1)
    # Replace all white spaces with space:
    # https://stackoverflow.com/questions/2077897/substitute-multiple-whitespace-with-single-whitespace-in-python
    # Strip punctuation: https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
    return _RE_COMBINE_WHITESPACE.sub(" ", text).lower().translate(str.maketrans('', '', string.punctuation))
```

In the `pdf_to_png_and_save` function, I used fall backs and uses a `failed.png` file to be stored in the database, demonstrating my ability to gracefully fall back to increase responsiveness. I have also used lower level API such as `.seek(0,0)` to copy the file from Django file field onto the hard drive where `pdf2image` can access.

In the `get_text` function, not only did I extract the text, but also did preprocessing to replace each continuous span of white spaces with a single space to aid with finding the Levenshtein distance later during the search.

In `codestudy/views.py`:
```python
from .pdf_processor import pdf_to_png_and_save, get_text
...
def add_paper(request):
...
    def process(paper):
        pdf_to_png_and_save(paper)
        paper.text = get_text(paper)
        paper.save()
    Thread(target=process, args=(paper,)).start()
...
```

In order to search through the text in the PDF, I had to extract it as plain text first, but if I were to extract it every time the search is requested, it would be inefficient because extracting text from a PDF file is an expensive operation. Therefore, the text is only extracted once when the paper is initially uploaded, utilizing ptimization by memorisation. In addition, I have also used concurrency to improve responsiveness as the extraction can happen in the background after the user has gotten a response from the server.


## Part 5: The Search Engine

The search engine is quite a naive one, for the pseudocode of the algorithm, please see the criterion B document. The implementation is shown below.

In `codestudy/seach_engine.py`:
```python
from codestudy.models import Paper
import re
import string
import fuzzywuzzy.process


def search(terms, tags, user):
    """
    The search engine that returns a ranked result based on the search terms, tags and user. The search term uses
    Levenshtein distance to ranked the relevance to the search term. The tag is counted such that the number of tag in
    the portion search query that matches that in the database is linearly related to the ranking score. The proportion
    of the element that is in the search term but not in the database is linearly related to one minus the ranking
    score. The user is used to place a higher relevance to the papers that the user have bookmarked. The weighing of
    each factor is provided below.
    Weights:
    properties: 3/4
        title + description: 1/3
            title: 2/3
            description: 1/3
        tags: 1/3
            has_tag: 2/3
            no_tag: 1/3
        others: 1/3:
            star_count: 2/3
            field_search: 1/3
    star: 1/4
    :param terms: the search terms.
    :param tags: the search tags.
    :param user: the user logged in.
    :return: A list of paper, ranked.

    """
    _RE_COMBINE_WHITESPACE = re.compile(r"\s+")
    terms = _RE_COMBINE_WHITESPACE.sub(" ", terms).lower().translate(str.maketrans('', '', string.punctuation))
    tags = set(tags)
    texts = []
    text_scores = {}
    titles = []
    title_scores = {}
    descriptions = []
    descriptions_scores = {}
    scores = {}
    max_no_tag = 1
    max_bookmarker = 1
    for paper in Paper.objects.all():
        titles.append(paper.title)
        descriptions.append(paper.description)
        texts.append(paper.text)
        scores[paper] = 0
        if user and paper.is_bookmarked(user):
            scores[paper] += 1/4
        no_tag = 0
        for tag in paper.tags.all():
            if tag not in tags:
                no_tag += 1
        max_no_tag = max(max_no_tag, no_tag)
        max_bookmarker = max(max_bookmarker, paper.bookmarkers.count())
    fz = fuzzywuzzy.process.extract(terms, texts)
    for text, score in fz:
        text_scores[text] = score / 100
    fz = fuzzywuzzy.process.extract(terms, titles)
    for title, score in fz:
        title_scores[title] = score / 100
    fz = fuzzywuzzy.process.extract(terms, descriptions)
    for description, score in fz:
        descriptions_scores[description] = score / 100
    for paper in scores:
        scores[paper] += title_scores.get(paper.title, 0) * 3/4 * 1/3 * 2/3
        scores[paper] += descriptions_scores.get(paper.description, 0) * 3/4 * 1/3 * 1/3
        scores[paper] += text_scores.get(paper.text, 0) * 3/4 * 1/3 * 1/3
        scores[paper] += paper.bookmarkers.count() / max_bookmarker * 3/4 * 1/3 * 2/3
        tag_has = 0
        paper_tags = set([tag for tag in paper.tags.all()])
        for tag in tags:
            if tag in paper_tags:
                tag_has += 1
        scores[paper] += tag_has / max(1, len(tags)) * 3/4 * 1/3 * 2/3
        tag_no = 0
        for paper_tag in paper_tags:
            if paper_tag not in tags:
                tag_no += 1
        scores[paper] += (max_no_tag-tag_no) / max_no_tag * 3/4 * 1/3 * 1/3

    papers_ranked = [k for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)]
    return papers_ranked
```

## Part 6: Validation, Error handling and Fallbacks

Because of the unpredictability of the user input of a web app, when the website fails, it should give as much helpful information to the user as possible and the crash should affect as little part of the program as possible. 

The first action is to validate the user input in any form.

In `codestudy/templates/add-paper.html`:
```html
<script>
    const uploadOptionsSelect = $('#upload-option');
    const uploadOptionsEnum = Object.freeze({
        'file': 1,
        'link': 2,
    });
    let uploadOption = uploadOptionsEnum.file;
    uploadOptionsSelect
        .dropdown({
            onChange: function (value, text, $selectedItem) {
                uploadOption = Number(value);
                if (uploadOption === uploadOptionsEnum.file) {
                    pdf.removeAttr('hidden');
                    link.attr('hidden', 'hidden');
                    form.form({
                        fields:
                            {
                                title: 'empty',
                                description: 'empty',
                                pdf: 'empty',
                            }
                    });
                    // Change the view of the web page to display the file selection tool and update the validation so that the link is not required and the file is..
                } else if (uploadOption === uploadOptionsEnum.link) {
                    pdf.attr('hidden', 'hidden');
                    link.removeAttr('hidden');
                    form.form({
                        fields:
                            {
                                title: 'empty',
                                description: 'empty',
                                link: 'empty',
                            }
                    });
                    // Change the view of the web page to display the text input box and update the validation so that the file is not required and the link is..
                } else {
                    console.assert(false, "Upload Option does not match any known type");
                }
            }
        })
    ;
    uploadOptionsSelect.dropdown('set selected', uploadOptionsEnum.file);
</script>
```

This JS code in combination with that from Semantic UI verifies the input are not empty. Note that it is not necessary for me to sanitizes the input because Django automatically and by default escape strings so that code injection is impossible to my best knowledge. 

Because all the papers are rendered in one page using the Django template language, if a single rendering raises an exception, the entire page will fail to render. So I have added a few precautions to prevent that. 

In `codestudy/models.py`:
```python
class Paper(models.Model):
    ...

    png = models.FileField(default='failed.png')
    pdf = models.FileField(default='failed.pdf')
```

In case that fails,

in `codestudy/templates/codestudy/results.html`:
```html
...
{% if paper.png %}
    <img src="{{ paper.png.url }}" alt="{{ paper.title }}">
{% endif %}
...
{% if paper.link %}
    <a class="header" href="{{ paper.link }}">{{ paper.title }}</a>
{% elif paper.pdf %}
    <a class="header" href="{{ paper.pdf.url }}">{{ paper.title }}</a>
{% endif %}
```

In the above code, the template language checks if the files exists before trying to get the url from the model so that it would not show an exception. I have tested this by raising exceptions in various places to see if it crashes more than it should. 

This demonstrate my technical ability to handler errors gracefully. 

In addition, the 500 error also implement multiple level of fall backs. 

In `codestudy/views.py`:
```python
def handler500(request):
    try:
        context = get_base_context(request)
        context.update({
            'message': {
                'title': '500 Server Error',
                'description': 'Something went wrong. Please try again later.'
            }
        })
        return render(request, 'codestudy/base.html', context=context, status=500)
    except:
        return render(request, 'codestudy/500.html', status=500)
```

This function is hooked to the server error handler in Django. The first thing it tires is to have some dynamic element such as the header bar, but if that still fails (which sometimes happens if the database is corrupt), it would return a static 500 page with all the links and layout hardcoded to minimise the chances of faliure. 

# Criterion D
[Criterion D Screencast](https://de0ch.s3.ap-east-1.amazonaws.com/csia/Criterion-D.mp4) <https://de0ch.s3.ap-east-1.amazonaws.com/csia/Criterion-D.mp4>

# Criterion E

## Demonstration of Success Criteria

My client has said that I've met all the success criteria (See Appendix Meeting #3 Transcript). Here are some screenshots for demonstration. 

### 1.1. Admins and Editors can upload paper and add tags
![Add Paper](img/add%20paper.png)
\

![Edit Tags](img/edit%20tags.png)
\

### 1.2. The search function would return relevant result
![Search](img/search.png)
\

![Search Results](img/search%20results.png)
\

### 1.3. The admin can add students to add studies to the website's database
![Admin](img/admin.png)
\

### 1.4. The user can to see the thumbnail and successfully download the PDF
![All Papers](img/all%20papers.png)
\

### 1.5 The storage should be large enough to store all the PDFs in the database

There is no theoretical limit to the size of the S3 container as AWS charges by the amount of storage used.

### 2.1 Only editors can modify the database
![Add Paper 404](img/add%20paper%20404.png)
\

### 2.2. Only the admins can modify manage user permissions
![Admin 404](img/admin%20404.png)
\

### 2.3. The site in encrypted in transit
![SSL](img/ssl.png)
\

### 2.4. Plain text password is never stored in the database

Not Applicable because I used Sign-in with Google with which the authentication is handled by Google. 

### 3.1. The UI would still work when it's zoomed in or viewed on a smaller device like a mobile screen.
![Mobile](img/mobile.png)
\

## User Feedback
The user is very satisfied with the product. She said that it completely realises her vision (see Meeting #3 Transcript in Appendix). I was pleasantly surprised when she said she was actually going to use the website, and the app was not just an intellectual exercise. One improvement is to make an info page between the card and the PDF. The page can contain additional information such as the units the paper is related to, and similar papers (Meeting #3 Transcript). This will increase the functionality of the program and allow students to explore the subject more. 

Looking forward, there are a few improvements I formulated other than the client suggestions. First, I can improve the efficiency of the web program. SQL is, by design, very efficient for a general purpose database, but since the search engine requires searching through plan text, there might be a more efficient data structure to index the data. By controlling lower levels of the server, I could employ more layers of caching to make access faster. The complexity of the search grows linearly with the number of papers in the database, so if the database gets large, the search function might be unreasonably slow. In addition, I could also write a more sophisticated search algorithm. Right now the ranking algorithm is quite primitive with no research to back up the weight of different aspect I assigned it. In addition, I could also add a list layout in addition to the grid layout for the result page because some people prefer to see data in a list. 

# Appendix

## Source code

Also available on [Github](https://github.com/de0ch/csia) <https://github.com/de0ch/csia>.

### File Tree
```
.
+-- .env
+-- Aptfile
+-- LICENSE
+-- Procfile
+-- README.md
+-- app.json
+-- codestudy
|   +-- __init__.py
|   +-- admin.py
|   +-- apps.py
|   +-- init_utils.py
|   +-- logins.py
|   +-- migrations
|   |   +-- 0001_initial.py
|   |   +-- 0002_auto_20201229_1549.py
|   |   +-- 0003_user_can_edit.py
|   |   +-- 0004_auto_20201230_1106.py
|   |   +-- 0005_user_bookmarks.py
|   |   +-- 0006_auto_20210106_0236.py
|   |   +-- 0007_auto_20210202_1508.py
|   |   \-- __init__.py
|   +-- models.py
|   +-- pdf_processor.py
|   +-- search_engine.py
|   +-- static
|   |   +-- failed
|   |   |   +-- failed.pdf
|   |   |   \-- failed.png
|   |   +-- favicon.ico
|   |   \-- logo.png
|   +-- templates
|   |   \-- codestudy
|   |       +-- 500.html
|   |       +-- add-paper.html
|   |       +-- admin.html
|   |       +-- base.html
|   |       +-- edit-paper.html
|   |       +-- edit-tags.html
|   |       +-- index.html
|   |       +-- login.html
|   |       \-- results.html
|   +-- templatetags
|   |   +-- __init__.py
|   |   \-- codestudy_tags.py
|   +-- tests.py
|   +-- urls.py
|   \-- views.py
+-- main
|   +-- __init__.py
|   +-- settings.py
|   +-- storage_backends.py
|   +-- urls.py
|   \-- wsgi.py
+-- manage.py
+-- requirements.txt
+-- runtime.txt
\-- utils.py

8 directories, 49 files
```

### File Contents

In `csia/LICENSE`:
```
Copyright 2021 Deyao Chen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

```

In `csia/requirements.txt`:
```
# Ipython is just the best
ipython

# Safekeeping Credentials
python-dotenv

# Django
django

# Heroku stuff
django-heroku
psycopg2
gunicorn

# S3 Storage
django-storages
boto3

# PDF Processing
pdf2image

# Authentication
requests
google-auth

# Extract PDF text
textract

# Search Engine
python-Levenshtein
fuzzywuzzy

```

In `csia/app.json`:
```
{
  "name": "codestudy",
  "description": "A search engine for IB Psychology Studies",
  "image": "heroku/python",
  "repository": "https://github.com/heroku/python-getting-started",
  "keywords": ["ib", "psychology" ],
  "addons": [ "heroku-postgresql" ],
  "env": {
    "SECRET_KEY": {
      "description": "The secret key for the Django application.",
      "generator": "secret"
    }
  },
  "environments": {
    "test": {
      "scripts": {
        "test-setup": "python manage.py collectstatic --noinput",
        "test": "python manage.py test"
      }
    }
  }
}

```

In `csia/runtime.txt`:
```
python-3.8.7

```

In `csia/Aptfile`:
```
poppler-utils

```

In `csia/README.md`:
```
# Code Study
A webapp designed to categorise PDF research paper based on tags for academic disciplines such as psychology that needs to frequently look up papers. Originally developed as for International Baccalaureate computer science internal assessment. Website live on [codestudy.herokuapp.com](https://codestudy.herokuapp.com)

## Screenshots

### Home Page
![Home Page](docs/img/home%20page.png)

### Browse Papers
![All Papers Page](docs/img/all%20papers%20page.png)

### Add Paper
![Add Paper Page](docs/img/add%20paper%20page.png)

### Edit Tags
![Edit Tags Page](docs/img/edit%20tags%20page.png)

## Dear IB Examiner, 
Please see the (much better and more elegant than PDF) `docs/ib/ib_docs.md` markdown document for the write-up needed exclusively for the grades. 

## Development
I am still working on a development documentation. Depending on if people actually want to use it and whether I can find other developers to maintain and improve the project. For now, you can read the `docs/ib/ib_docs.md` to get a rough idea of the project. 

Let me know that you are interested in developing by staring this project. 

But for now, all the dependencies are listed in `requirements.txt`. You will also need apt packages listed in `AptFile`. The runtime is stated in `runtime.txt`.

## Licence
All parts of the program EXCEPT the IB related documents under `docs/ib` are available under the [MIT License](https://de0ch.mit-license.org/).


```

In `csia/utils.py`:
```
from django.conf import settings
import boto3
import botocore.client

s3_client = boto3.client('s3',
                         aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                         config=botocore.client.Config(s3={'addressing_style': 'virtual'}, signature_version='s3v4'),
                         region_name=settings.AWS_S3_REGION_NAME)


def generate_presigned_url(object_key, expiration):
    presigned_url = s3_client.generate_presigned_url('get_object',
                                                     Params={'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                                                             'Key': object_key},
                                                     ExpiresIn=expiration)
    return presigned_url

```

In `csia/.env`:
```
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
SECRET_KEY=...
IS_LOCAL=TRUE
DEBUG=FALSE

```

In `csia/manage.py`:
```
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

```

In `csia/Procfile`:
```
web: gunicorn main.wsgi --log-file -

```

In `csia/codestudy/models.py`:
```
from django.db import models
import uuid
from enum import IntEnum
# Create your models here.


class TagClass(models.Model):
    """
    A group of tags that have a title. For example, "Topic" is a tag class and under it there would be tags such as
    "Cognitive processes", "The individual and the group", "Cultural influences on behavior", etc.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag_class = models.ForeignKey(TagClass, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return self.name


class Paper(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField()
    description = models.TextField()
    text = models.TextField()
    png = models.FileField(max_length=262)  # 36 for UUID, 1 for '/' and 225 for filename length
    pdf = models.FileField(default='failed.pdf', max_length=262)
    link = models.TextField(null=True)
    tags = models.ManyToManyField(Tag)

    def is_bookmarked(self, user):
        """
        Get if the paper is bookmarked by the user.
        :param user: The User object in question.
        :return: Whether the paper is bookmarked.
        """
        return self.bookmarkers.filter(pk=user.pk).exists()

    def __str__(self):
        return self.title

    @property
    def nested_tag_names(self):
        """
        Get a dictionary of the names of all the tag classes as the keys, and the list of the names of all the tags as
        the values.
        :return: The dictionary.
        """
        tag_classes = {}
        for tag in self.tags.all():
            if tag.tag_class.name not in tag_classes:
                tag_classes[tag.tag_class.name] = []
            tag_classes[tag.tag_class.name].append(tag.name)
        return tag_classes


class UserType(IntEnum):
    """
    A Enum that maps the user type to integer. The mapping should be consistent with the front end JS code.
    """
    STANDARD = 1
    EDITOR = 2
    ADMIN = 3

    @classmethod
    def choices(cls):
        """
        Get a list of two-element tuples of the enum names and values. Helpful for specifying the data type in the database.
        :return: A list of two-element tuples of the enum names and values.
        """
        return [(key.value, key.name) for key in cls]


class User(models.Model):
    """
    Represents a logged in user.
    """
    id = models.TextField(primary_key=True, editable=False)
    type = models.IntegerField(choices=UserType.choices(), default=UserType.STANDARD)
    name = models.TextField()
    given_name = models.TextField()
    family_name = models.TextField()
    email = models.TextField()
    bookmarks = models.ManyToManyField(Paper, related_name='bookmarkers')

    def __str__(self):
        return self.name

    @property
    def all_types(self):
        """
        :return: All the user types as a dictionary of their names.
        """
        return [key.name for key in UserType]

    @property
    def can_edit(self):
        """
        :return: If the user have editing rights.
        """
        return self.type == UserType.EDITOR or self.type == UserType.ADMIN

    @property
    def is_admin(self):
        """
        :return: If the user is an admin
        """
        return self.type == UserType.ADMIN

    @property
    def type_lower(self):
        """

        :return: The name of the user type in lowercase.
        """
        return UserType(self.type).name.lower()


```

In `csia/codestudy/search_engine.py`:
```
from codestudy.models import Paper
import re
import string
import fuzzywuzzy.process


def search(terms, tags, user):
    """
    The search engine that returns a ranked result based on the search terms, tags and user. The search term uses
    Levenshtein distance to ranked the relevance to the search term. The tag is counted such that the number of tag in
    the portion search query that matches that in the database is linearly related to the ranking score. The proportion
    of the element that is in the search term but not in the database is linearly related to one minus the ranking
    score. The user is used to place a higher relevance to the papers that the user have bookmarked. The weighing of
    each factor is provided below.
    Weights:
    properties: 3/4
        title + description: 1/3
            title: 2/3
            description: 1/3
        tags: 1/3
            has_tag: 2/3
            no_tag: 1/3
        others: 1/3:
            star_count: 2/3
            field_search: 1/3
    star: 1/4
    :param terms: the search terms.
    :param tags: the search tags.
    :param user: the user logged in.
    :return: A list of paper, ranked.

    """
    _RE_COMBINE_WHITESPACE = re.compile(r"\s+")
    terms = _RE_COMBINE_WHITESPACE.sub(" ", terms).lower().translate(str.maketrans('', '', string.punctuation))
    tags = set(tags)
    texts = []
    text_scores = {}
    titles = []
    title_scores = {}
    descriptions = []
    descriptions_scores = {}
    scores = {}
    max_no_tag = 1
    max_bookmarker = 1
    for paper in Paper.objects.all():
        titles.append(paper.title)
        descriptions.append(paper.description)
        texts.append(paper.text)
        scores[paper] = 0
        if user and paper.is_bookmarked(user):
            scores[paper] += 1/4
        no_tag = 0
        for tag in paper.tags.all():
            if tag not in tags:
                no_tag += 1
        max_no_tag = max(max_no_tag, no_tag)
        max_bookmarker = max(max_bookmarker, paper.bookmarkers.count())
    fz = fuzzywuzzy.process.extract(terms, texts)
    for text, score in fz:
        text_scores[text] = score / 100
    fz = fuzzywuzzy.process.extract(terms, titles)
    for title, score in fz:
        title_scores[title] = score / 100
    fz = fuzzywuzzy.process.extract(terms, descriptions)
    for description, score in fz:
        descriptions_scores[description] = score / 100
    for paper in scores:
        scores[paper] += title_scores.get(paper.title, 0) * 3/4 * 1/3 * 2/3
        scores[paper] += descriptions_scores.get(paper.description, 0) * 3/4 * 1/3 * 1/3
        scores[paper] += text_scores.get(paper.text, 0) * 3/4 * 1/3 * 1/3
        scores[paper] += paper.bookmarkers.count() / max_bookmarker * 3/4 * 1/3 * 2/3
        tag_has = 0
        paper_tags = set([tag for tag in paper.tags.all()])
        for tag in tags:
            if tag in paper_tags:
                tag_has += 1
        scores[paper] += tag_has / max(1, len(tags)) * 3/4 * 1/3 * 2/3
        tag_no = 0
        for paper_tag in paper_tags:
            if paper_tag not in tags:
                tag_no += 1
        scores[paper] += (max_no_tag-tag_no) / max_no_tag * 3/4 * 1/3 * 1/3

    papers_ranked = [k for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)]
    return papers_ranked

```

In `csia/codestudy/logins.py`:
```
from .models import User


def get_user(request):
    """
    :param request: the django request object
    :return: a dictionary of the information of the user
    Get a dictionary of the currently logged in user
    """
    try:
        sub = request.session['sub']
        user = User.objects.get(pk=sub)
        return user
    except (KeyError, User.DoesNotExist):
        return None

```

In `csia/codestudy/__init__.py`:
```

```

In `csia/codestudy/apps.py`:
```
from django.apps import AppConfig


class CodeStudyConfig(AppConfig):
    name = 'codestudy'

```

In `csia/codestudy/init_utils.py`:
```
from .models import TagClass, Tag


def populate_new_database():
    """
    The client asked to have some specific tags, but because of the generality of the tag systems, the specific tags
    have to added manually. The function adds them programmatically.
    """
    tags_groups = {
        'Approaches': [
            'Biological',
            'Cognitive',
            'Sociocultural',
        ],
        'Topics': [
            'Brain & Behavior',
            'Hormones and pheromones and their effects on behavior',
            'The relationship between genetics and behavior',
            'Cognitive processes',
            'The reliability of cognitive processes',
            'Emotion and cognition',
            'The individual and the group',
            'Cultural origins of behavior and cognition',
            'Cultural influences on behavior',
        ],
        'Content': []
    }
    for tag_class, tags in tags_groups.items():
        tc = TagClass(name=tag_class)
        tc.save()
        for tag in tags:
            Tag(tag_class=tc, name=tag).save()


```

In `csia/codestudy/admin.py`:
```
from django.contrib import admin

# Register your models here.

```

In `csia/codestudy/pdf_processor.py`:
```
import pdf2image
import os
from django.contrib.staticfiles.storage import staticfiles_storage
import re
import logging
import uuid
import textract
import string


def pdf_to_png_and_save(paper):
    """
    Takes a paper with the pdf file, capture the first page as a png and saves it to the paper object.
    :param paper: The Paper object to be processed.
    :return: None
    """
    # noinspection PyBroadException
    try:
        paper.pdf.seek(0, 0)
        pdf_byte = paper.pdf.read()
        image = pdf2image.convert_from_bytes(pdf_byte, last_page=1, dpi=100)[0]
        png_name = str(uuid.uuid4())
        image.save(png_name, 'PNG')
        with open(png_name, 'rb') as f:
            paper.png.save(paper.pdf.name.replace('.pdf', '') + '.png', f)
        os.remove(png_name)
        paper.pdf.close()
    except:
        logging.exception('exception occurred converting pdf to png')
        with open(staticfiles_storage.path('failed/failed.png'), 'rb') as f:
            paper.png.save('failed.png', f)


def get_text(paper):
    """
    Extract the text content in the pdf, turn all characters to lowercase and replace each continuous whitespace with
    one space.
    :param paper: The Paper object to be processed.
    :return: The plain text in the paper.
    """
    id1 = str(uuid.uuid4())
    _RE_COMBINE_WHITESPACE = re.compile(r"\s+")
    paper.pdf.seek(0, 0)
    with open(id1, 'wb') as of:
        of.write(paper.pdf.read())
    paper.pdf.close()
    text = textract.process(id1, extension='pdf').decode('utf-8')
    os.remove(id1)
    # Replace all white spaces with space:
    # https://stackoverflow.com/questions/2077897/substitute-multiple-whitespace-with-single-whitespace-in-python
    # Strip punctuation: https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
    return _RE_COMBINE_WHITESPACE.sub(" ", text).lower().translate(str.maketrans('', '', string.punctuation))




```

In `csia/codestudy/tests.py`:
```
from django.test import TestCase

# Create your tests here.

```

In `csia/codestudy/urls.py`:
```
from django.urls import path, include
from . import views


app_name = 'codestudy'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    path('add-paper/', views.add_paper, name='add-paper'),
    path('add-paper/presign-s3', views.presign_s3, name='presign-s3'),
    path('edit-tags/', views.edit_tags, name='edit-tags'),
    path('edit-paper/<uuid:pk>/', views.edit_paper, name='edit-paper'),
    path('browse/<str:tag_class>/<str:tag>', views.browse, name='browse'),
    path('all-papers/', views.all_papers, name='all-papers'),
    path('login/', views.login, name='login'),
    path('admin/', views.admin, name='admin'),
    path('logout/', views.logout, name='logout'),
    path('bookmark/', views.bookmark, name='bookmark'),
    path('bookmarked/', views.bookmarked, name='bookmarked'),
    path('500/', views.invoke_500, name='invoke_500'),
]


```

In `csia/codestudy/views.py`:
```
from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
import logging
from .logins import get_user
from .models import TagClass, Tag, Paper, User, UserType
import os
from html import unescape
from .pdf_processor import pdf_to_png_and_save, get_text
from threading import Thread
import json
import uuid
from django.conf import settings
from utils import s3_client
import google.oauth2.id_token
import google.auth.transport.requests
from .search_engine import search as s_search
import enum
from django.db import DataError


def get_base_context(request):
    """

    :param request: The Django Request object
    :return: A structured dictionary with the context that needs to be
    displayed on all pages, including the User object all all Tag Classes for navigation
    """
    return {
        'user': get_user(request),
        'tag_classes': TagClass.objects.all()
    }


def index(request):
    """
    This is a Django handler function for the index page
    :param request: The Django Request object
    :return: The index page
    """
    if request.method == 'POST':
        return redirect('codestudy:index')
    else:
        context = get_base_context(request)
        return render(request, 'codestudy/index.html', context=context)


def search(request):
    """
    This is a Django handler function for the search page. Client would pass information into this function through
    HTTP GET parameters
    :param request: The Django Request object
    :return: The results g
    """
    tags = []
    for tag_class in TagClass.objects.all():
        tag_names = request.GET.getlist(tag_class.name)
        for tag_name in tag_names:
            tag = tag_class.tag_set.get(name=tag_name)
            tags.append(tag)
    terms = request.GET.get('terms', '')
    user = get_user(request)
    papers = s_search(terms, tags, user)
    context = get_base_context(request)
    context.update({
        'page_title': f'{terms}',
        'papers': papers,
    })
    return render(request, 'codestudy/results.html', context=context)


def browse(request, tag_class=None, tag=None):
    """
    This is a Django handler function for browsing all papers tagged with a specific tag
    :param request: The Django Request object
    :param tag_class: The name of the Tag Class
    :param tag: The name of the Tag
    :return: The results g
    """

    # Thought about using the pk of the tag, but used name instead as it is more human readable
    tag_class = unescape(tag_class)
    tag = unescape(tag)

    context = get_base_context(request)
    context.update({
        'page_title': tag,
        'papers': Tag.objects.get(name=tag, tag_class__name=tag_class).paper_set.all(),
    })
    return render(request, 'codestudy/results.html', context=context)


def all_papers(request):
    """
    This is a Django handler function for browser all papers in the database
    :param request: The Django Request object
    :return: The results page
    """
    context = get_base_context(request)
    context.update({
        'page_title': 'All Papers',
        'papers': Paper.objects.all(),
        'all_papers': True
    })
    return render(request, 'codestudy/results.html', context=context)


class UploadOption(enum.IntEnum):
    """
    This Enum specifies all upload options and their associated integer value that is used in the front end as well
    """
    FILE = 1
    LINK = 2


def add_paper(request):
    """
    This is a Django handler function for adding a paper into the database. This also handlers form submission through
    HTTP POST.
    :param request: The Django Request object
    :return: Depending on the request method, it either returns the upload UI, or a redirect to the index page
    """
    if get_user(request) and get_user(request).can_edit:
        if request.method == 'POST':
            title = request.POST.get('title', '')
            description = request.POST.get('description', '')
            paper = Paper(title=title, description=description)
            # Did not supply default value because it's better to crash and notify user and dev than silently fail.
            upload_option = UploadOption(int(request.POST['upload-option']))
            if upload_option == UploadOption.FILE:
                pdf_key = request.POST.get('pdf-key', 'failed.pdf')
                paper.pdf.name = pdf_key
                paper.save()

                def process(paper):
                    pdf_to_png_and_save(paper)
                    paper.text = get_text(paper)
                    try:
                        paper.save()
                    except DataError:
                        context = get_base_context(request)
                        context.update({
                            'message': {
                                'title': 'File Name Too Long',
                                'description': 'The file name of the PDF you just uploaded is too long. Please try to '
                                               'shorten it.'
                            }
                        })
                        return render(request, 'codestudy/base.html', context)

                Thread(target=process, args=(paper,)).start()

            elif upload_option == UploadOption.LINK:
                link = request.POST.get('link', '')
                paper.link = link
                paper.save()
            else:
                raise NotImplementedError('Upload Option does not match any known type')
            update_tag(request, paper)
            return redirect('codestudy:index')
        else:
            context = get_base_context(request)
            return render(request, 'codestudy/add-paper.html', context=context)
    else:
        raise Http404()


def presign_s3(request):
    """
    The files stored in the AWS S3 bucket are not public and requires authentication for security reasons as the
    client might want to limit the access to only certain users. Only certain people should be able to edit the
    database. As the user might leak the credentials through negligence or incompetence, the presigned url is only
    limited to one file for a certain time frame. Function designed to be interacted programmatically.
    :param request: The Django Request object
    :return: A Json string of the credentials
    """
    if get_user(request).can_edit:
        file_name = request.GET['file_name']
        file_name = os.path.join(str(uuid.uuid4()), file_name)

        presigned_post = s3_client.generate_presigned_post(
            Bucket=settings.AWS_STORAGE_BUCKET_NAME,
            Key=file_name,
            Fields={"Content-Type": 'application/pdf'},
            Conditions=[
                {"Content-Type": 'application/pdf'}
            ],
            ExpiresIn=600
        )
        return JsonResponse(presigned_post)
    else:
        raise Http404()


def edit_tags(request):
    """
    This is a Django handler function for editing the tag and tag class in the database
    :param request: The Django Request object
    :return: The edit tags page
    """
    if get_user(request) and get_user(request).can_edit:
        if request.method == 'POST':
            change_log = json.loads(request.POST['changeLog-json'])
            for new_tag_class in change_log['newTagClasses']:
                if new_tag_class['name']:
                    try:
                        TagClass.objects.get(name=new_tag_class['name'])
                    except TagClass.DoesNotExist:
                        TagClass(pk=uuid.UUID(new_tag_class['pk']), name=new_tag_class['name']).save()
            for new_tag in change_log['newTags']:
                if new_tag['name']:
                    tag_class = TagClass.objects.get(name=new_tag['tagClass'])
                    if not tag_class.tag_set.filter(name=new_tag['name']).exists():
                        Tag(pk=uuid.UUID(new_tag['pk']), name=new_tag['name'], tag_class=tag_class).save()
            for deleted_tag in change_log['deletedTags']:
                try:
                    Tag.objects.get(pk=deleted_tag).delete()
                except Tag.DoesNotExist:
                    logging.exception('Could not find tag in database')
            for deleted_tag_class in change_log['deletedTagClasses']:
                try:
                    TagClass.objects.get(pk=deleted_tag_class).delete()
                except TagClass.DoesNotExist:
                    logging.exception('Did not find tag class in database')

            return redirect('codestudy:edit-tags')
        else:
            context = get_base_context(request)
            return render(request, 'codestudy/edit-tags.html', context=context)
    else:
        raise Http404()


def edit_paper(request, pk):
    """
    This is a Django handler function for editing the tags and names for existing papers.
    :param request: The Django Request object
    :param pk: The primary key of the paper
    :return: The edit paper page
    """
    if get_user(request) and get_user(request).can_edit:
        if request.method == 'POST':
            paper = Paper.objects.get(pk=pk)
            if request.POST.get('delete', 'off') == 'on':
                paper.delete()
                return redirect('codestudy:all-papers')
            else:
                paper.title = request.POST.get('title', '')
                paper.description = request.POST.get('description', '')
                paper.save()
                update_tag(request, paper)
                return redirect('codestudy:edit-paper', pk)
        else:
            context = get_base_context(request)
            context.update({
                'paper': Paper.objects.get(pk=pk),
            })
            return render(request, 'codestudy/edit-paper.html', context=context)
    else:
        raise Http404()


def update_tag(request, paper):
    """
    This is a helper function that extract the tags in an HTTP POST form and update the tags for the paper object
    :param request: The Django Request object
    :param paper: the paper that needs to be updated
    :type paper: Paper
    :return: None
    """
    paper.tags.clear()
    for tag_class in TagClass.objects.all():
        tags = request.POST.getlist(str(tag_class.pk))
        for tag_pk in tags:
            tag = Tag.objects.get(pk=uuid.UUID(tag_pk))
            paper.tags.add(tag)
    paper.save()


def login(request):
    """
    This is a Django handler function that verifies the login details according to the token gained by signing in with
    Google. Designed to be interacted programmatically
    :param request: The Django Request object
    :return: The login status in JSON format
    """
    if request.method == 'POST':
        id_token = request.POST['id-token']
        try:
            # Specify the CLIENT_ID of the app that accesses the backend:
            id_info = google.oauth2.id_token.verify_oauth2_token(id_token,
                                                                 google.auth.transport.requests.Request(),
                                                                 settings.G_CLIENT_ID)

            user = User.objects.get_or_create(pk=id_info['sub'])[0]
            user.email = id_info['email']
            user.name = id_info['name']
            user.given_name = id_info['given_name']
            user.family_name = id_info['family_name']
            user.save()
            request.session['sub'] = user.pk
            success = True
        except ValueError:
            # Invalid token
            success = False
    else:
        raise Http404()
    return JsonResponse({
        'success': success
    })


def admin(request):
    """
    This is a Django handler function for the admin console
    :param request: The Django Request object
    :return: Rendered admin console page
    """
    if get_user(request) and get_user(request).is_admin:
        if request.method == 'POST':
            for user in User.objects.all():
                user.type = UserType[request.POST[user.pk].upper()]
                user.save()
            return redirect('codestudy:admin')
        else:
            context = get_base_context(request)
            context.update({
                'users': User.objects.all()
            })
            return render(request, 'codestudy/admin.html', context=context)
    else:
        raise Http404()


def logout(request):
    """
    This is a Django handler function that logs the current user out. Designed to be accessed programmatically.
    :param request:
    :return:
    """
    try:
        del request.session['sub']
        success = True
    except KeyError:
        success = False
    return JsonResponse({'success': success})


def handler404(request, exception):
    """
    This is a Django handler function designed to override the default 404 page to provide a nicer formatting that is
    consistent with the rest of the website
    :param request: The Django Request object
    :param exception: The Exception caught
    :return: The 404 page
    """
    context = get_base_context(request)
    context.update({
        'message': {
            'title': '404 Not Found',
            'description': 'This is no the web page you are looking for.',
        }
    })
    return render(request, 'codestudy/base.html', context=context, status=404)


# noinspection PyBroadException
def handler500(request):
    """
    This is a Django handler function for the 500 server error page. Because a server error can imply an serious issue
    such as corrupted database, a nice render of the 500 page may be impossible. So the server first attemps to nicely
    render the page with all the dynamic element, if it fails, it falls back to the safest render which does not contain
    any dynamic element
    :param request: The Django request object
    :return: The 500 error page
    """
    try:
        context = get_base_context(request)
        context.update({
            'message': {
                'title': '500 Server Error',
                'description': 'Something went wrong. Please try again later.'
            }
        })
        return render(request, 'codestudy/base.html', context=context, status=500)
    except:
        return render(request, 'codestudy/500.html', status=500)


def handler403(request, exception):
    """
    This is a Django handler function for HTTP 403 permission error
    :param request: The Django Request object
    :param exception: The exception caught
    :return: The 403 error page
    """
    logging.exception(exception)
    context = get_base_context(request)
    context.update({
        'message': {
            'title': '403 Permission Denied',
            'description': 'Looks like you don\'t have the permission to perform the action.'
        }
    })
    return render(request, 'codestudy/base.html', context=context, status=403)


def handler400(request, exception):
    """
    This is a Django handler function for 400 Bad Request error
    :param request: The Django Request object
    :param exception: The exception caught
    :return: The 400 error page
    """
    context = get_base_context(request)
    context.update({
        'message': {
            'title': '400 Bad Request',
            'description': 'Your client has issued a malformed or illegal request.'
        }
    })
    return render(request, 'codestudy/base.html', context=context, status=400)


def invoke_500(request):
    raise Exception


def bookmark(request):
    """
    This is a Django handler function for bookmarking a paper. This can be accessed either programmatically or directly
    by the user
    :param request: The Django Request object
    :return: A redirection
    """
    user = get_user(request)
    if user:
        paper = Paper.objects.get(pk=request.GET['pk'])
        if user.bookmarks.filter(pk=paper.pk).exists():
            user.bookmarks.remove(paper)
        else:
            user.bookmarks.add(paper)
        return redirect('codestudy:index')
    else:
        raise Http404()


def bookmarked(request):
    """
    This is a Django handler for viewing all bookmarked papers
    :param request: The Django Request object
    :return: The results page
    """
    user = get_user(request)
    if user:
        context = get_base_context(request)
        context.update({
            'page_title': 'Bookmarked',
            'papers': user.bookmarks.all()
        })
        return render(request, 'codestudy/results.html', context=context)
    else:
        raise Http404()

```

In `csia/codestudy/templatetags/__init__.py`:
```

```

In `csia/codestudy/templatetags/codestudy_tags.py`:
```
from django import template


register = template.Library()


@register.filter(name='is_bookmarked')
def is_bookmarked(paper, user):
    return paper.is_bookmarked(user)

```

In `csia/codestudy/migrations/0007_auto_20210202_1508.py`:
```
# Generated by Django 3.1.6 on 2021-02-02 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codestudy', '0006_auto_20210106_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='pdf',
            field=models.FileField(default='failed.pdf', max_length=262, upload_to=''),
        ),
        migrations.AlterField(
            model_name='paper',
            name='png',
            field=models.FileField(max_length=262, upload_to=''),
        ),
    ]

```

In `csia/codestudy/migrations/0002_auto_20201229_1549.py`:
```
# Generated by Django 3.1.4 on 2020-12-29 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codestudy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.TextField(editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('given_name', models.TextField()),
                ('family_name', models.TextField()),
                ('email', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='paper',
            name='pdf',
            field=models.FileField(default='failed.pdf', upload_to=''),
        ),
        migrations.AlterField(
            model_name='paper',
            name='png',
            field=models.FileField(default='failed.png', upload_to=''),
        ),
    ]

```

In `csia/codestudy/migrations/__init__.py`:
```

```

In `csia/codestudy/migrations/0004_auto_20201230_1106.py`:
```
# Generated by Django 3.1.4 on 2020-12-30 11:06

import codestudy.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codestudy', '0003_user_can_edit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='can_edit',
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.IntegerField(choices=[(1, 'STANDARD'), (2, 'EDITOR'), (3, 'ADMIN')], default=codestudy.models.UserType['STANDARD']),
        ),
    ]

```

In `csia/codestudy/migrations/0001_initial.py`:
```
# Generated by Django 3.1.4 on 2020-12-18 08:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TagClass',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('tag_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codestudy.tagclass')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('text', models.TextField()),
                ('png', models.FileField(upload_to='')),
                ('pdf', models.FileField(upload_to='')),
                ('tags', models.ManyToManyField(to='codestudy.Tag')),
            ],
        ),
    ]

```

In `csia/codestudy/migrations/0006_auto_20210106_0236.py`:
```
# Generated by Django 3.1.4 on 2021-01-06 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codestudy', '0005_user_bookmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='link',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bookmarks',
            field=models.ManyToManyField(related_name='bookmarkers', to='codestudy.Paper'),
        ),
    ]

```

In `csia/codestudy/migrations/0005_user_bookmarks.py`:
```
# Generated by Django 3.1.4 on 2020-12-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codestudy', '0004_auto_20201230_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bookmarks',
            field=models.ManyToManyField(to='codestudy.Paper'),
        ),
    ]

```

In `csia/codestudy/migrations/0003_user_can_edit.py`:
```
# Generated by Django 3.1.4 on 2020-12-30 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codestudy', '0002_auto_20201229_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='can_edit',
            field=models.BooleanField(default=False),
        ),
    ]

```

In `csia/codestudy/static/favicon.ico` (encoded as base 64):
```
AAABAAYAEBAAAAEACABoBQAAZgAAACAgAAABAAgAqAgAAM4FAAAwMAAAAQAIAKgO
AAB2DgAAQEAAAAEACAAoFgAAHh0AAICAAAABAAgAKEwAAEYzAAAAAAAAAQAgAP4H
AABufwAAKAAAABAAAAAgAAAAAQAIAAAAAAAAAQAAEgsAABILAAAAAQAAAAEAAK21
AACyuhAAt74gALzDMADCyEAAx8xQAMzRYADN0mQA0dZwANbagADZ3YgA4OOgAObo
sADr7cAA8PHQAPX24AD6+/AA////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwYAAAAA
AAAAAAAAAAAAAxARBgAAAAAAAQYGAQEBAxAREAMAAAAAAxAPBggPBhAREAMAAAAA
AhARAQAADAoREAMAAAAAAAsRDAAAAAUEBgMAAAAAAAAQEQkAAAABAwAAAAAAAAAA
EREJAAAAAAAAAAAAAAAAABERCQAAAAAAAAAAAAAAAAAQEQkAAAABAAAAAAAAAAAA
CxENAAAACQAAAAAAAAAAAAMREQEAAA4BAAAAAAAAAAAABhELAQgRBAAAAAAAAAAA
AAACCQkDAQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgA
AAAgAAAAQAAAAAEACAAAAAAAAAQAACUWAAAlFgAAAAEAAAABAACttQAAsroQALe+
IAC8wzAAwshAAMfMUADM0WAA0dZwANbagADb35AA4OOgAObosADr7cAA8PHQAPX2
4AD6+/AA////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoPAwAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAKEBAPAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChAQ
EBAPAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoQEBAQEAoAAAAAAAAAAAAAAAAC
BwsMDAcBAAEDAAAKEBAQEBAKAAAAAAAAAAAAAAAACA8QDgYECQ4EDQgAChAQEBAQ
CgAAAAAAAAAAAAAAAAoQEA0BAAAAAw8QCAoQEBAQEAoAAAAAAAAAAAAAAAAJEBAQ
AwAAAAAABxAJDxAQEBAKAAAAAAAAAAAAAAAABBAQEAsAAAAAAAAADwgDDxAQCgAA
AAAAAAAAAAAAAAAOEBAQBgAAAAAAAAAKCAADDwoAAAAAAAAAAAAAAAAAAxAQEBAC
AAAAAAAAAAUIAAACAAAAAAAAAAAAAAAAAAAJEBAQEAAAAAAAAAAAAQgAAAAAAAAA
AAAAAAAAAAAAAAwQEBAOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADxAQEAwA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQEBAQDAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAABAQEBAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEBAQEAwA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMEBAQDwAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAoQEBAQAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAABhAQEBAE
AAAAAAAAAAsAAAAAAAAAAAAAAAAAAAAAAAAADxAQEAcAAAAAAAAADwAAAAAAAAAA
AAAAAAAAAAAAAAAIEBAQCwAAAAAAAAMQAAAAAAAAAAAAAAAAAAAAAAAAAAANEBAQ
AgAAAAAAChABAAAAAAAAAAAAAAAAAAAAAAAAAAIPEBALAAAAAAMQEAQAAAAAAAAA
AAAAAAAAAAAAAAAAAAIMEBAKAgAGDwsPBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG
Cw4QDgoCAAMCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAKAAAADAAAABgAAAAAQAIAAAAAAAACQAANyEAADchAAAAAQAAAAEAAK21
AACyuhAAt74gALzDMADCyEAAx8xQAMzRYADR1nAA1tqAANvfkADg46AA5uiwAOvt
wADw8dAA9fbgAPr78AD///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAEIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAQ0QCgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAABDRAQEAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAENEBAQEBAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AQ0QEBAQEBAQCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB
DRAQEBAQEBANAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEN
EBAQEBAQEA0BAAAAAAAAAAAAAAAAAAAAAAAAAAIJDRAQEA8LBAAAAAMGAAAAAQ0Q
EBAQEBAQDQEAAAAAAAAAAAAAAAAAAAAAAAABCRAQEA8JCAgKEAsBAAwIAAABDRAQ
EBAQEBANAQAAAAAAAAAAAAAAAAAAAAAAAAMOEBAQDQEAAAAAAg0NChAIAAENEBAQ
EBAQEA0BAAAAAAAAAAAAAAAAAAAAAAAAAw8QEBAOAQAAAAAAAAENEBAIAQ0QEBAQ
EBAQDQEAAAAAAAAAAAAAAAAAAAAAAAACDxAQEBAEAAAAAAAAAAADEBAICBAQEBAQ
EBANAQAAAAAAAAAAAAAAAAAAAAAAAAANEBAQEAwAAAAAAAAAAAAAChAIAAoQEBAQ
EA0BAAAAAAAAAAAAAAAAAAAAAAAAAAgQEBAQEAYAAAAAAAAAAAAAAxAKAAAKEBAQ
DQEAAAAAAAAAAAAAAAAAAAAAAAAAAQ8QEBAQEAEAAAAAAAAAAAAAAA4MAAAAChAN
AQAAAAAAAAAAAAAAAAAAAAAAAAAACBAQEBAQDQAAAAAAAAAAAAAAAAoMAAAAAAgB
AAAAAAAAAAAAAAAAAAAAAAAAAAAADhAQEBAQCQAAAAAAAAAAAAAAAAYMAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAADEBAQEBAQCAAAAAAAAAAAAAAAAAEMAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAHEBAQEBAQBAAAAAAAAAAAAAAAAAABAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAKEBAQEBAQBAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAMEBAQEBAQBAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAMEBAQEBAQAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAPEBAQEBAQAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAQEBAQEBAQAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAMEBAQEBAQAwAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAMEBAQEBAQBAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAALEBAQEBAQBAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAIEBAQEBAQBgAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAFEBAQEBAQCAAAAAAAAAAAAAAAAAgAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAEBAQEBAQCwAAAAAAAAAAAAAAABAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAChAQEBAQDgAAAAAAAAAAAAAABBAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAABBAQEBAQEAIAAAAAAAAAAAAABxAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwQEBAQEAYAAAAAAAAAAAAACxAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMQEBAQEAwAAAAAAAAAAAABDxAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHEBAQEBAEAAAAAAAAAAAGEBAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChAQEBAMAAAAAAAAAAEPEBABAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoQEBAQCAAAAAAAAQwQEBAEAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHDxAQEAsCAAAFDQ8IChAEAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQgOEBAQEBAPCAEAAAUDAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgQEBAQAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAoAAAAQAAAAIAAAAABAAgAAAAAAAAQAABKLAAASiwAAAAB
AAAAAQAArbUAALK6EAC3viAAvMMwAMLIQADHzFAAzNFgANHWcADW2oAA29+QAODj
oADm6LAA6+3AAPDx0AD19uAA+vvwAP///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYQBgAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYQEBAGAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAYQEBAQEAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYQEBAQEBAQBgAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYQEBAQEBAQEBAG
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAYQEBAQEBAQEBAQEAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAYQEBAQEBAQEBAQEAYAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYQEBAQEBAQEBAQEAYA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIEBwgFAwAAAAAAAAAAAAAAAAAA
AAYQEBAQEBAQEBAQEAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADCg8QEBAQ
EBAOCAEAAAAAAwkAAAAAAAYQEBAQEBAQEBAQEAYAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAILEBAQEBANCAgIDRAPBQAAAA0MAAAAAAYQEBAQEBAQEBAQEAYAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPEBAQEA0EAAAAAAACDBAJAAoQDAAAAAYQ
EBAQEBAQEBAQEAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoQEBAQEA0BAAAA
AAAAAAAKEA4QEAwAAAYQEBAQEBAQEBAQEAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAoQEBAQEA8CAAAAAAAAAAAAAAoQEBAMAAYQEBAQEBAQEBAQEAYAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAgQEBAQEBAHAAAAAAAAAAAAAAABDhAQDAIQEBAQ
EBAQEBAQEAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUQEBAQEBAOAAAAAAAA
AAAAAAAAAAYQEAwABhAQEBAQEBAQEAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAEPEBAQEBAQBwAAAAAAAAAAAAAAAAAADhAMAAAGEBAQEBAQEAYAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAKEBAQEBAQEAEAAAAAAAAAAAAAAAAAAAkQDAAAAAYQ
EBAQEAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEEBAQEBAQEAwAAAAAAAAA
AAAAAAAAAAADEA4AAAAABhAQEAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
CxAQEBAQEBAIAAAAAAAAAAAAAAAAAAAAAA4QAAAAAAAGEAYAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAhAQEBAQEBAQBAAAAAAAAAAAAAAAAAAAAAAKEAAAAAAA
AAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcQEBAQEBAQEAAAAAAAAAAA
AAAAAAAAAAAABxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN
EBAQEBAQEA4AAAAAAAAAAAAAAAAAAAAAAAMQAgAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAABEBAQEBAQEBAMAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBAQEBAQEBAQCwAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgQ
EBAQEBAQEAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAJEBAQEBAQEBAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADBAQEBAQEBAQCAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwQ
EBAQEBAQEAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAMEBAQEBAQEBAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADBAQEBAQEBAQCAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwQ
EBAQEBAQEAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAMEBAQEBAQEBAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACxAQEBAQEBAQCAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgQ
EBAQEBAQEAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAGEBAQEBAQEBAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxAQEBAQEBAQDQAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP
EBAQEBAQEBAAAAAAAAAAAAAAAAAAAAAAAA0AAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAACxAQEBAQEBAQAwAAAAAAAAAAAAAAAAAAAAQQAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYQEBAQEBAQEAUAAAAAAAAA
AAAAAAAAAAAIEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
DxAQEBAQEBAJAAAAAAAAAAAAAAAAAAAAChAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAgQEBAQEBAQDQAAAAAAAAAAAAAAAAAAAA4QAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABDxAQEBAQEBACAAAAAAAA
AAAAAAAAAAIQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAgQEBAQEBAQBwAAAAAAAAAAAAAAAAAHEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAADRAQEBAQEA0AAAAAAAAAAAAAAAAADRAQAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIPEBAQEBAQBAAAAAAA
AAAAAAAABBAQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAABBAQEBAQEA0AAAAAAAAAAAAAAAwQEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAGEBAQEBAQCAAAAAAAAAAAAAgQEBAQBAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQPEBAQEBAGAAAA
AAAAAAcQEBAQEAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAQsQEBAQEAsDAAAABQwQDAQCCxAFAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAsQEBAQEBAQEBAOBgAAAAAGBgAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQUIDAwM
DAgFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAACAAAAAAAEAAAEACAAAAAAAAEAAAJVY
AACVWAAAAAEAAAABAACttQAAsroQALe+IAC8wzAAwshAAMfMUADM0WAA0dZwANba
gADb35AA4OOgAObosADr7cAA8PHQAPX24AD6+/AA////AAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAgEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMPDQEAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAADDxAQDQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAw8QEBAQDQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMPEBAQEBAQDQEAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAADDxAQEBAQEBAQDQEAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Aw8QEBAQEBAQEBAQDQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMPEBAQEBAQEBAQEBAQDQEA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAADDxAQEBAQEBAQEBAQEBAQDQEAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAw8Q
EBAQEBAQEBAQEBAQEBAQDQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMPEBAQEBAQEBAQEBAQEBAQEBAQ
DQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAADDxAQEBAQEBAQEBAQEBAQEBAQEBAQDQEAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAw8QEBAQ
EBAQEBAQEBAQEBAQEBAQEBAPAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMPEBAQEBAQEBAQEBAQEBAQEBAQEBAQ
DwMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAADDxAQEBAQEBAQEBAQEBAQEBAQEBAQEA8DAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAw8QEBAQEBAQ
EBAQEBAQEBAQEBAQEBAPAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMPEBAQEBAQEBAQEBAQEBAQEBAQEBAQDwMA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAADDxAQEBAQEBAQEBAQEBAQEBAQEBAQEA8DAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQHCAkM
DAwJCAUBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAw8QEBAQEBAQEBAQ
EBAQEBAQEBAQEBAPAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADCQ0QEBAQEBAQEBAQEBANBwEAAAAAAAAA
AAAAAAAACQAAAAAAAAAAAAAAAAMPEBAQEBAQEBAQEBAQEBAQEBAQEBAQDwMAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAEGDhAQEBAQEBAQEBAQEBAQEBAQEAoCAAAAAAAAAAAAAAkQBAAAAAAAAAAA
AAADDxAQEBAQEBAQEBAQEBAQEBAQEBAQEA8DAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIDxAQEBAQEBAQEBAQ
EA4MDA8QEBAQEA8IAAAAAAAAAAADEBAEAAAAAAAAAAAAAw8QEBAQEBAQEBAQEBAQ
EBAQEBAQEBAPAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAFDhAQEBAQEBAQEBAPCQQAAAAAAAAECQ4QEBANAwAA
AAAAAAwQEAQAAAAAAAAAAAMPEBAQEBAQEBAQEBAQEBAQEBAQEBAQDwMAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB
CxAQEBAQEBAQEBAPCAAAAAAAAAAAAAAAAAYOEBAPBQAAAAAIEBAQBAAAAAAAAAAD
DxAQEBAQEBAQEBAQEBAQEBAQEBAQEA8DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAw4QEBAQEBAQEBAQDQMAAAAA
AAAAAAAAAAAAAAEJEBAQBgAABhAQEBAEAAAAAAAAAw8QEBAQEBAQEBAQEBAQEBAQ
EBAQEBAPAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAYPEBAQEBAQEBAQEA0BAAAAAAAAAAAAAAAAAAAAAAAGEBAQ
CQgQEBAQEAQAAAAAAAMPEBAQEBAQEBAQEBAQEBAQEBAQEBAQDwMAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGEBAQ
EBAQEBAQEBAPAQAAAAAAAAAAAAAAAAAAAAAAAAAGEBAQEBAQEBAQBAAAAAADDxAQ
EBAQEBAQEBAQEBAQEBAQEBAQEA8DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABhAQEBAQEBAQEBAQEAQAAAAAAAAA
AAAAAAAAAAAAAAAAAAAHEBAQEBAQEBAEAAAAAw8QEBAQEBAQEBAQEBAQEBAQEBAQ
EBAPAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAYQEBAQEBAQEBAQEBAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL
EBAQEBAQEAQAAAMPEBAQEBAQEBAQEBAQEBAQEBAQEBAQDwMAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGEBAQEBAQ
EBAQEBAQDgEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEPEBAQEBAQBAACDxAQEBAQ
EBAQEBAQEBAQEBAQEBAQEA8DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxAQEBAQEBAQEBAQEBAGAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAYQEBAQEBAEAAENEBAQEBAQEBAQEBAQEBAQEBAQEBAP
AwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAEPEBAQEBAQEBAQEBAQDgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AA4QEBAQEAQAAAENEBAQEBAQEBAQEBAQEBAQEBAQDwMAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADBAQEBAQEBAQ
EBAQEBAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABhAQEBAQBAAAAAENEBAQ
EBAQEBAQEBAQEBAQEA8DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgQEBAQEBAQEBAQEBAQDgAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAADhAQEBAEAAAAAAENEBAQEBAQEBAQEBAQEBAPAwAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAADEBAQEBAQEBAQEBAQEBAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAHEBAQEAYAAAAAAAENEBAQEBAQEBAQEBAQDwMAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwQEBAQEBAQEBAQ
EBAQEAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQEBAQCAAAAAAAAAEN
EBAQEBAQEBAQEA8DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAGEBAQEBAQEBAQEBAQEBANAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAsQEBAIAAAAAAAAAAENEBAQEBAQEBAPAwAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAQ8QEBAQEBAQEBAQEBAQEAcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAABhAQEAgAAAAAAAAAAAENEBAQEBAQDwMAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIEBAQEBAQEBAQEBAQ
EBAQAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABEBAQDAAAAAAAAAAA
AAENEBAQEA8DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAQ8QEBAQEBAQEBAQEBAQEA8AAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAMEBAMAAAAAAAAAAAAAAENEBAPAwAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAGEBAQEBAQEBAQEBAQEBAQCwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAgQEAwAAAAAAAAAAAAAAAENDwMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4QEBAQEBAQEBAQEBAQ
EBAHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBAQDgAAAAAAAAAA
AAAAAAECAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAEEBAQEBAQEBAQEBAQEBAQEAQAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAEBAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAoQEBAQEBAQEBAQEBAQEBAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAMEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADxAQEBAQEBAQEBAQEBAQ
EA4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkQEAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAUQEBAQEBAQEBAQEBAQEBAQDAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAABhAQAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
CRAQEBAQEBAQEBAQEBAQEBAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAABEBAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANEBAQEBAQEBAQEBAQEBAQ
EAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJDwAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAARAQEBAQEBAQEBAQEBAQEBAQBAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF
EBAQEBAQEBAQEBAQEBAQEBAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgQEBAQEBAQEBAQEBAQEBAQ
EAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAADBAQEBAQEBAQEBAQEBAQEBAQAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN
EBAQEBAQEBAQEBAQEBAQEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAQEBAQEBAQEBAQEBAQEBAQ
DwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAACEBAQEBAQEBAQEBAQEBAQEBAMAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQQ
EBAQEBAQEBAQEBAQEBAQEAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBAQEBAQEBAQEBAQEBAQEBAQ
DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAGEBAQEBAQEBAQEBAQEBAQEBAMAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgQ
EBAQEBAQEBAQEBAQEBAQEAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBAQEBAQEBAQEBAQEBAQEBAQ
DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAIEBAQEBAQEBAQEBAQEBAQEBAMAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgQ
EBAQEBAQEBAQEBAQEBAQEAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBAQEBAQEBAQEBAQEBAQEBAQ
DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAIEBAQEBAQEBAQEBAQEBAQEBAMAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgQ
EBAQEBAQEBAQEBAQEBAQEAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABhAQEBAQEBAQEBAQEBAQEBAQ
DAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAEEBAQEBAQEBAQEBAQEBAQEBAPAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQQ
EBAQEBAQEBAQEBAQEBAQEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAhAQEBAQEBAQEBAQEBAQEBAQ
EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAEBAQEBAQEBAQEBAQEBAQEBAQAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO
EBAQEBAQEBAQEBAQEBAQEBAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwQEBAQEBAQEBAQEBAQEBAQ
EAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAACBAQEBAQEBAQEBAQEBAQEBAQBgAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF
EBAQEBAQEBAQEBAQEBAQEBAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIQEBAQEBAQEBAQEBAQEBAQ
EAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAA4QEBAQEBAQEBAQEBAQEBAQDAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAICQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
ChAQEBAQEBAQEBAQEBAQEBAPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAA8QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGEBAQEBAQEBAQEBAQEBAQ
EBABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEEBAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAEQEBAQEBAQEBAQEBAQEBAQEAQAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAgQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAsQEBAQEBAQEBAQEBAQEBAQBwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAACxAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABhAQEBAQEBAQEBAQEBAQ
EBAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOEBAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAADxAQEBAQEBAQEBAQEBAQEA4AAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAABAQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAJEBAQEBAQEBAQEBAQEBAQEAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAEEBAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIQEBAQEBAQEBAQEBAQ
EBAQBgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgQEBAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAoQEBAQEBAQEBAQEBAQEBAKAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAACxAQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAhAQEBAQEBAQEBAQEBAQEA4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAPEBAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAChAQEBAQEBAQEBAQ
EBAQEAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBAQEBAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAABDxAQEBAQEBAQEBAQEBAQCQAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAJEBAQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAHEBAQEBAQEBAQEBAQEBAOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AA4QEBAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMEBAQEBAQEBAQ
EBAQEBAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEEBAQEBAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIPEBAQEBAQEBAQEBAQEAoAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAoQEBAQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAUQEBAQEBAQEBAQEBAQEAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC
EBAQEBAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkQEBAQEBAQ
EBAQEBAQCgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgQEBAQEBAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAsQEBAQEBAQEBAQEBAQAgAAAAAAAAAA
AAAAAAAAAAAAAAAAAAACEBAQEBAQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAQ0QEBAQEBAQEBAQEBAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAsQ
EBAQEBAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQ0QEBAQ
EBAQEBAQEBAHAAAAAAAAAAAAAAAAAAAAAAAAAAAGEBAQEBAQEBAEAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQ0QEBAQEBAQEBAQEBADAAAAAAAA
AAAAAAAAAAAAAAAAAw8QEBAQEBAQEAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAQoQEBAQEBAQEBAQEA8DAAAAAAAAAAAAAAAAAAAAAAMPEBAQ
EBAQEBAQBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgQ
EBAQEBAQEBAQEA8DAAAAAAAAAAAAAAAAAAADDxAQEBAMDhAQEBAGAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMOEBAQEBAQEBAQEBAIAAAA
AAAAAAAAAAABCBAQEA8IAQAABA8QEAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAIDxAQEBAQEBAQEBAOBwIAAAAAAAADCQ8QEBALAQAA
AAAAAQ4QCgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAABCg8QEBAQEBAQEBAQEA4MDAwMDxAQEBAOBQAAAAAAAAAAAw8MAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQcNEBAQEBAQEBAQ
EBAQEBAQEBAOBgAAAAAAAAAAAAAABAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBgoOEBAQEBAQEBAQEA0JAwAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAwQEBAQEBAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAiVBORw0KGgoAAAANSUhEUgAA
AQAAAAEACAMAAABrrFhUAAAAM1BMVEUAta0QurJAyMKA2tZg0cwgvrew6ObQ8fD/
///A7euQ39tQzMcww7xw1tGg4+Dw+/rg9vVTRW/UAAAHhklEQVR42u2d26KjIAxF
q6ititX//9rpsfVaSSLQgWD240y17nUghAD2dhOJRCKRSCQSiUQikUgkEolEIpFI
JBK5K8tzNavIy9DP8z+Vq+r++FLdtFnoJ/sP0urA+6x7l3ZLyJ/9A1PVAteHNuCk
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
AAAAAElFTkSuQmCC
```

In `csia/codestudy/static/logo.png` (encoded as base 64):
```
iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAEGWlDQ1BrQ0dDb2xv
clNwYWNlR2VuZXJpY1JHQgAAOI2NVV1oHFUUPrtzZyMkzlNsNIV0qD8NJQ2TVjSh
tLp/3d02bpZJNtoi6GT27s6Yyc44M7v9oU9FUHwx6psUxL+3gCAo9Q/bPrQvlQol
2tQgKD60+INQ6Ium65k7M5lpurHeZe58853vnnvuuWfvBei5qliWkRQBFpquLRcy
4nOHj4g9K5CEh6AXBqFXUR0rXalMAjZPC3e1W99Dwntf2dXd/p+tt0YdFSBxH2Kz
5qgLiI8B8KdVy3YBevqRHz/qWh72Yui3MUDEL3q44WPXw3M+fo1pZuQs4tOIBVVT
aoiXEI/MxfhGDPsxsNZfoE1q66ro5aJim3XdoLFw72H+n23BaIXzbcOnz5mfPoTv
YVz7KzUl5+FRxEuqkp9G/Ajia219thzg25abkRE/BpDc3pqvphHvRFys2weqvp+k
rbWKIX7nhDbzLOItiM8358pTwdirqpPFnMF2xLc1WvLyOwTAibpbmvHHcvttU57y
5+XqNZrLe3lE/Pq8eUj2fXKfOe3pfOjzhJYtB/yll5SDFcSDiH+hRkH25+L+sdxK
EAMZahrlSX8ukqMOWy/jXW2m6M9LDBc31B9LFuv6gVKg/0Szi3KAr1kGq1GMjU/a
Lbnq6/lRxc4XfJ98hTargX++DbMJBSiYMIe9Ck1YAxFkKEAG3xbYaKmDDgYyFK0U
GYpfoWYXG+fAPPI6tJnNwb7ClP7IyF+D+bjOtCpkhz6CFrIa/I6sFtNl8auFXGMT
P34sNwI/JhkgEtmDz14ySfaRcTIBInmKPE32kxyyE2Tv+thKbEVePDfW/byMM1Km
m0XdObS7oGD/MypMXFPXrCwOtoYjyyn7BV29/MZfsVzpLDdRtuIZnbpXzvlf+ev8
MvYr/Gqk4H/kV/G3csdazLuyTMPsbFhzd1UabQbjFvDRmcWJxR3zcfHkVw9GfpbJ
meev9F08WW8uDkaslwX6avlWGU6NRKz0g/SHtCy9J30o/ca9zX3Kfc19zn3BXQKR
O8ud477hLnAfc1/G9mrzGlrfexZ5GLdn6ZZrrEohI2wVHhZywjbhUWEy8icMCGNC
UdiBlq3r+xafL549HQ5jH+an+1y+LlYBifuxAvRN/lVVVOlwlCkdVm9NOL5BE4wk
Q2SMlDZU97hX86EilU/lUmkQUztTE6mx1EEPh7OmdqBtAvv8HdWpbrJS6tJj3n0C
WdM6busNzRV3S9KTYhqvNiqWmuroiKgYhshMjmhTh9ptWhsF7970j/SbMrsPE1su
R5z7DMC+P/Hs+y7ijrQAlhyAgccjbhjPygfeBTjzhNqy28EdkUh8C+DU9+z2v/oy
eH791OncxHOs5y2AtTc7nb/f73TWPkD/qwBnjX8BoJ98VQNcC+8AAABcZVhJZk1N
ACoAAAAIAAQBBgADAAAAAQACAAABEgADAAAAAQABAAABKAADAAAAAQACAACHaQAE
AAAAAQAAAD4AAAAAAAKgAgAEAAAAAQAAAICgAwAEAAAAAQAAAIAAAAAAmuCr3gAA
AgtpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0i
YWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJk
ZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJk
Zi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9
IiIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90
aWZmLzEuMC8iPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9y
aWVudGF0aW9uPgogICAgICAgICA8dGlmZjpQaG90b21ldHJpY0ludGVycHJldGF0
aW9uPjI8L3RpZmY6UGhvdG9tZXRyaWNJbnRlcnByZXRhdGlvbj4KICAgICAgICAg
PHRpZmY6UmVzb2x1dGlvblVuaXQ+MjwvdGlmZjpSZXNvbHV0aW9uVW5pdD4KICAg
ICAgICAgPHRpZmY6Q29tcHJlc3Npb24+MTwvdGlmZjpDb21wcmVzc2lvbj4KICAg
ICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+
CqZd9jAAAApzSURBVHgB7Z1bbBVFGMcHQ2tCSywgRahgy6VNLbdGKTRyUYIIIfEG
PEjQBxI0asT4YiCGqPEBH0wIGH0h8IIRDPKgSYUgomATKCitQtO0iC1gQVqgjbQk
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
Su4tZwAAAABJRU5ErkJggg==
```

In `csia/codestudy/static/failed/failed.pdf` (encoded as base 64):
```
JVBERi0xLjMKJcTl8uXrp/Og0MTGCjQgMCBvYmoKPDwgL0xlbmd0aCA1IDAgUiAv
RmlsdGVyIC9GbGF0ZURlY29kZSA+PgpzdHJlYW0KeAGVkD8PgjAQxXc+xRP/FZXS
ViiwalzcSLqJE4mDCQPh+ycehyUxMmiatO8uvdzvvQ4VOiTnXqPpofj0DbWUNOlY
D0IburMc1uSyUCl9bnFy0GqcGF5bGpmXWYG0tIFrkThnoOEeuEEsIsRKZhDh0quV
F+uIlqUQG26Q2LLQELWooyigwSM373BXXBwT/42nlbXSFGYWb+dX772Y6IhgQCeC
cA7wwHwE7V1M8PHbluR5wxn87iD4DljbIpeWDeAj3yEw9xyTqV4TKFl9CmVuZHN0
cmVhbQplbmRvYmoKNSAwIG9iagoyMDQKZW5kb2JqCjIgMCBvYmoKPDwgL1R5cGUg
L1BhZ2UgL1BhcmVudCAzIDAgUiAvUmVzb3VyY2VzIDYgMCBSIC9Db250ZW50cyA0
IDAgUiAvTWVkaWFCb3ggWzAgMCA1OTUuMjc1NSA4NDEuODg5OF0KPj4KZW5kb2Jq
CjYgMCBvYmoKPDwgL1Byb2NTZXQgWyAvUERGIC9UZXh0IF0gL0NvbG9yU3BhY2Ug
PDwgL0NzMSA3IDAgUiA+PiAvRm9udCA8PCAvVFQyIDkgMCBSCj4+ID4+CmVuZG9i
agoxMCAwIG9iago8PCAvTGVuZ3RoIDExIDAgUiAvTiAzIC9BbHRlcm5hdGUgL0Rl
dmljZVJHQiAvRmlsdGVyIC9GbGF0ZURlY29kZSA+PgpzdHJlYW0KeAGdlndUU9kW
h8+9N73QEiIgJfQaegkg0jtIFQRRiUmAUAKGhCZ2RAVGFBEpVmRUwAFHhyJjRRQL
g4Ji1wnyEFDGwVFEReXdjGsJ7601896a/cdZ39nnt9fZZ+9917oAUPyCBMJ0WAGA
NKFYFO7rwVwSE8vE9wIYEAEOWAHA4WZmBEf4RALU/L09mZmoSMaz9u4ugGS72yy/
UCZz1v9/kSI3QyQGAApF1TY8fiYX5QKUU7PFGTL/BMr0lSkyhjEyFqEJoqwi48Sv
bPan5iu7yZiXJuShGlnOGbw0noy7UN6aJeGjjAShXJgl4GejfAdlvVRJmgDl9yjT
0/icTAAwFJlfzOcmoWyJMkUUGe6J8gIACJTEObxyDov5OWieAHimZ+SKBIlJYqYR
15hp5ejIZvrxs1P5YjErlMNN4Yh4TM/0tAyOMBeAr2+WRQElWW2ZaJHtrRzt7VnW
5mj5v9nfHn5T/T3IevtV8Sbsz55BjJ5Z32zsrC+9FgD2JFqbHbO+lVUAtG0GQOXh
rE/vIADyBQC03pzzHoZsXpLE4gwnC4vs7GxzAZ9rLivoN/ufgm/Kv4Y595nL7vtW
O6YXP4EjSRUzZUXlpqemS0TMzAwOl89k/fcQ/+PAOWnNycMsnJ/AF/GF6FVR6JQJ
hIlou4U8gViQLmQKhH/V4X8YNicHGX6daxRodV8AfYU5ULhJB8hvPQBDIwMkbj96
An3rWxAxCsi+vGitka9zjzJ6/uf6Hwtcim7hTEEiU+b2DI9kciWiLBmj34RswQIS
kAd0oAo0gS4wAixgDRyAM3AD3iAAhIBIEAOWAy5IAmlABLJBPtgACkEx2AF2g2pw
ANSBetAEToI2cAZcBFfADXALDIBHQAqGwUswAd6BaQiC8BAVokGqkBakD5lC1hAb
Wgh5Q0FQOBQDxUOJkBCSQPnQJqgYKoOqoUNQPfQjdBq6CF2D+qAH0CA0Bv0BfYQR
mALTYQ3YALaA2bA7HAhHwsvgRHgVnAcXwNvhSrgWPg63whfhG/AALIVfwpMIQMgI
A9FGWAgb8URCkFgkAREha5EipAKpRZqQDqQbuY1IkXHkAwaHoWGYGBbGGeOHWYzh
YlZh1mJKMNWYY5hWTBfmNmYQM4H5gqVi1bGmWCesP3YJNhGbjS3EVmCPYFuwl7ED
2GHsOxwOx8AZ4hxwfrgYXDJuNa4Etw/XjLuA68MN4SbxeLwq3hTvgg/Bc/BifCG+
Cn8cfx7fjx/GvyeQCVoEa4IPIZYgJGwkVBAaCOcI/YQRwjRRgahPdCKGEHnEXGIp
sY7YQbxJHCZOkxRJhiQXUiQpmbSBVElqIl0mPSa9IZPJOmRHchhZQF5PriSfIF8l
D5I/UJQoJhRPShxFQtlOOUq5QHlAeUOlUg2obtRYqpi6nVpPvUR9Sn0vR5Mzl/OX
48mtk6uRa5Xrl3slT5TXl3eXXy6fJ18hf0r+pvy4AlHBQMFTgaOwVqFG4bTCPYVJ
RZqilWKIYppiiWKD4jXFUSW8koGStxJPqUDpsNIlpSEaQtOledK4tE20Otpl2jAd
Rzek+9OT6cX0H+i99AllJWVb5SjlHOUa5bPKUgbCMGD4M1IZpYyTjLuMj/M05rnP
48/bNq9pXv+8KZX5Km4qfJUilWaVAZWPqkxVb9UU1Z2qbapP1DBqJmphatlq+9Uu
q43Pp893ns+dXzT/5PyH6rC6iXq4+mr1w+o96pMamhq+GhkaVRqXNMY1GZpumsma
5ZrnNMe0aFoLtQRa5VrntV4wlZnuzFRmJbOLOaGtru2nLdE+pN2rPa1jqLNYZ6NO
s84TXZIuWzdBt1y3U3dCT0svWC9fr1HvoT5Rn62fpL9Hv1t/ysDQINpgi0Gbwaih
iqG/YZ5ho+FjI6qRq9Eqo1qjO8Y4Y7ZxivE+41smsImdSZJJjclNU9jU3lRgus+0
zwxr5mgmNKs1u8eisNxZWaxG1qA5wzzIfKN5m/krCz2LWIudFt0WXyztLFMt6ywf
WSlZBVhttOqw+sPaxJprXWN9x4Zq42Ozzqbd5rWtqS3fdr/tfTuaXbDdFrtOu8/2
DvYi+yb7MQc9h3iHvQ732HR2KLuEfdUR6+jhuM7xjOMHJ3snsdNJp9+dWc4pzg3O
owsMF/AX1C0YctFx4bgccpEuZC6MX3hwodRV25XjWuv6zE3Xjed2xG3E3dg92f24
+ysPSw+RR4vHlKeT5xrPC16Il69XkVevt5L3Yu9q76c+Oj6JPo0+E752vqt9L/hh
/QL9dvrd89fw5/rX+08EOASsCegKpARGBFYHPgsyCRIFdQTDwQHBu4IfL9JfJFzU
FgJC/EN2hTwJNQxdFfpzGC4sNKwm7Hm4VXh+eHcELWJFREPEu0iPyNLIR4uNFksW
d0bJR8VF1UdNRXtFl0VLl1gsWbPkRoxajCCmPRYfGxV7JHZyqffS3UuH4+ziCuPu
LjNclrPs2nK15anLz66QX8FZcSoeGx8d3xD/iRPCqeVMrvRfuXflBNeTu4f7kufG
K+eN8V34ZfyRBJeEsoTRRJfEXYljSa5JFUnjAk9BteB1sl/ygeSplJCUoykzqdGp
zWmEtPi000IlYYqwK10zPSe9L8M0ozBDuspp1e5VE6JA0ZFMKHNZZruYjv5M9UiM
JJslg1kLs2qy3mdHZZ/KUcwR5vTkmuRuyx3J88n7fjVmNXd1Z752/ob8wTXuaw6t
hdauXNu5Tnddwbrh9b7rj20gbUjZ8MtGy41lG99uit7UUaBRsL5gaLPv5sZCuUJR
4b0tzlsObMVsFWzt3WazrWrblyJe0fViy+KK4k8l3JLr31l9V/ndzPaE7b2l9qX7
d+B2CHfc3em681iZYlle2dCu4F2t5czyovK3u1fsvlZhW3FgD2mPZI+0MqiyvUqv
akfVp+qk6oEaj5rmvep7t+2d2sfb17/fbX/TAY0DxQc+HhQcvH/I91BrrUFtxWHc
4azDz+ui6rq/Z39ff0TtSPGRz0eFR6XHwo911TvU1zeoN5Q2wo2SxrHjccdv/eD1
Q3sTq+lQM6O5+AQ4ITnx4sf4H++eDDzZeYp9qukn/Z/2ttBailqh1tzWibakNml7
THvf6YDTnR3OHS0/m/989Iz2mZqzymdLz5HOFZybOZ93fvJCxoXxi4kXhzpXdD66
tOTSna6wrt7LgZevXvG5cqnbvfv8VZerZ645XTt9nX297Yb9jdYeu56WX+x+aem1
72296XCz/ZbjrY6+BX3n+l37L972un3ljv+dGwOLBvruLr57/17cPel93v3RB6kP
Xj/Mejj9aP1j7OOiJwpPKp6qP6391fjXZqm99Oyg12DPs4hnj4a4Qy//lfmvT8MF
z6nPK0a0RupHrUfPjPmM3Xqx9MXwy4yX0+OFvyn+tveV0auffnf7vWdiycTwa9Hr
mT9K3qi+OfrW9m3nZOjk03dp76anit6rvj/2gf2h+2P0x5Hp7E/4T5WfjT93fAn8
8ngmbWbm3/eE8/sKZW5kc3RyZWFtCmVuZG9iagoxMSAwIG9iagoyNjEyCmVuZG9i
ago3IDAgb2JqClsgL0lDQ0Jhc2VkIDEwIDAgUiBdCmVuZG9iagozIDAgb2JqCjw8
IC9UeXBlIC9QYWdlcyAvTWVkaWFCb3ggWzAgMCA1OTUuMjc1NSA4NDEuODg5OF0g
L0NvdW50IDEgL0tpZHMgWyAyIDAgUiBdCj4+CmVuZG9iagoxMiAwIG9iago8PCAv
VHlwZSAvQ2F0YWxvZyAvUGFnZXMgMyAwIFIgPj4KZW5kb2JqCjkgMCBvYmoKPDwg
L1R5cGUgL0ZvbnQgL1N1YnR5cGUgL1RydWVUeXBlIC9CYXNlRm9udCAvV0tBTExW
K0NhbGlicmkgL0ZvbnREZXNjcmlwdG9yCjEzIDAgUiAvVG9Vbmljb2RlIDE0IDAg
UiAvRmlyc3RDaGFyIDMzIC9MYXN0Q2hhciA0NiAvV2lkdGhzIFsgNDU5IDQ3OSAy
MjkKMjI5IDQ5OCA1MjUgMjI2IDMzNSA1MjcgNTI1IDUyNSA1MjUgNTE3IDYxNSBd
ID4+CmVuZG9iagoxNCAwIG9iago8PCAvTGVuZ3RoIDE1IDAgUiAvRmlsdGVyIC9G
bGF0ZURlY29kZSA+PgpzdHJlYW0KeAFdkctqwzAQRff6Ci3TRfDYdV5gDCUl4EUf
1O0H2NI4CGpZyMrCf98rJU2hi7M4mgeamezYPDfWBJm9+0m1HORgrPY8TxevWPZ8
NlbkhdRGhZulNzV2TmQobpc58NjYYZJVJaTMPlAyB7/I1ZOeen6Ib29eszf2LFdf
xza9tBfnvnlkGySJupaaB7R76dxrN7LMUum60YibsKxR9ZfxuTiW+BEq8uuX1KR5
dp1i39kzi4qork6nWrDV/0J5ea3oh1tqkddVhKjc1qIqCigg2uZRH6EAeohaQgFU
Rd1AAXQTdQsF0DLqDgqICoq6hwKiXYoeoADJQ4x2UIBoatVDATTVKihA8j4maygg
2qQoQwFGQGfM/DtcHD+e6b5WdfEeG023TMuOSzSW7+d2k4sNEj8gpJpLCmVuZHN0
cmVhbQplbmRvYmoKMTUgMCBvYmoKMzA5CmVuZG9iagoxMyAwIG9iago8PCAvVHlw
ZSAvRm9udERlc2NyaXB0b3IgL0ZvbnROYW1lIC9XS0FMTFYrQ2FsaWJyaSAvRmxh
Z3MgNCAvRm9udEJCb3ggWy01MDMgLTMxMyAxMjQwIDEwMjZdCi9JdGFsaWNBbmds
ZSAwIC9Bc2NlbnQgOTUyIC9EZXNjZW50IC0yNjkgL0NhcEhlaWdodCA2MzIgL1N0
ZW1WIDAgL1hIZWlnaHQKNDY0IC9BdmdXaWR0aCA1MjEgL01heFdpZHRoIDEzMjgg
L0ZvbnRGaWxlMiAxNiAwIFIgPj4KZW5kb2JqCjE2IDAgb2JqCjw8IC9MZW5ndGgg
MTcgMCBSIC9MZW5ndGgxIDE5MTI4IC9GaWx0ZXIgL0ZsYXRlRGVjb2RlID4+CnN0
cmVhbQp4AdV7eViTV/r2ed8kJBACCRC2iAlEQAyICyK4QGSJLKKgRAOKsosWNxC3
qqVqt7R232xta1c7tctL0IqtbW3H7vs+023amXa62mWm7bS2yHef98lB6kx/3x/f
9V3X/AJ37vs85znnPec5KwHWd/W0MSPrZRo2oWVV01qmvvI7QDktG9Y7KJ1Wwpju
aPva5asonQkyuZZ3bm6ndP5RxszvdbQ1tVKa/QrO7YCB0lIOeEzHqvWbKJ3PK5jR
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
ufQbq3Q+00gOCb9DMoM0BpQ5KFntHs0j6q+VdEySLme1rsoBA5tfqRiqFyvShUrq
Av7urqlXQi5UmLd+sa9Pki6t65Pk4lolprKmntLn7d7NkooqlaQFvoBm376korpK
pZdrt1vVQ1wzuNS5lnb3dLt87pnM8qHlW4vG+pj5ZbMcGSlFRg5Fyu5IND4ywh4h
87ehCI07YuJUT6TJbpL525BJE+s2wcJDmR5eXeuJNNqNsrfQOM8ou42FxR63MWuC
59/62c/7SU92rV/a7YJc71K/kaqTengSL+Tgu3s90vwLhDTjOb//Ijf4LevGS62G
qv/9Iv8LcqT/BW38L29iH8MS8c0aknfhd5k7gR3AuUAvcA6wHdgGbAXOBrYAm4FN
wEZgA9ADrAe6gXXAWmANsBpYBXQCZwErgRVAB7AcaAfagFagBWgGmoBGYBmwFGgA
lgCLgXqgDvABi4CFgBeoBRYA84EaoBqYB8wFqoA5QCVQAZQDZcBswAOUAiVAMVAE
zALcQCFQAMwEZgDTgWlAPpAHTAVygSlADjAZmARMBCYA2cB4IAvIBFzAOCADGAuk
A2lAKjAGcAIpQDLgAOzAaCAJGAXYgEQgAYgH4oBYwArEANFAFGABzEAkEAGYgHDA
CIQBoYAB0AMhgA7QzhrCuwaQAQlgrFWCTToFDAK/Ar8AJ4GfgZ+AfwE/Aj8A3wP/
BP4BfAd8C3wDfA2cAL4CvgS+AD4HPgM+Bf4OfAJ8DPwN+CvwEfAh8BfgA+B94D3g
XeAd4M/An4C3gbeAN4E3gNeB14BXgVeAl4GXgBeBF4DngeeAZ4FngKeBp4AngePA
H4EngMeBY8BjwKPAI8BR4GHgIeAIMAAcBh4EDgEHgX4gAPQBCvAAcD9wH3AvcAC4
B/gDcDewH7gLuBO4A7gduA24FdgH3ALcDNwE7AVuBG4A9gDXA9cB1wLXAFcDVwFX
AlcAlwOXAZcCu4FLgIsBP3ARcCFwAXA+cB5rndUr7YLaCewAzgV6gXOA7cA2YCtw
NrAF2AxsAjYCG4AeYD3QDXQB64C1wBpgNbAK6ATOAlYCK4AOYDnQDrQBrUAL0Aw0
AY3AMmAp0AAsARYD9UAd4AMWAQsBL1ALLADmA9XAPGAuMAeoBCqAcqAMmA14gFKg
BChmrf/l2/R/e/Pq/tsb+F/ePsavZcMXM97Y+GVL8QdP+psZO3XVyD+AYtVsJetm
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
HOEYE51o0b+lh5c2NBzCkhg9xnEqrGFZaFioLiIeMbqa37Q0R3EaDair147jyJjO
T5h0ftakGxCLdPWYSTdzieP/Qea2YL+xBycpWI0g+Cd1knLBfyrkDsLwLRmkn92h
0Vnl6UZdQvkYzKnT162o/NO3LdcbwWVL163QYIEIXmLkJYuXGbl5iTvW8OXKop72
uVOHDbhdRSVZ45IsIVXXVvETSR/jiMdBZYjLLptQcHYpblk4t6JCh/e6jd65M5Zf
1CynYKZpNJhzg9/PW1ac6vPKPcLCP/uQ8HM1PrHHKwSfirBFlbPmzFnoKm7qXNHc
teL/AJJR7IkKZW5kc3RyZWFtCmVuZG9iagoxNyAwIG9iago5NTU1CmVuZG9iagox
IDAgb2JqCjw8IC9UaXRsZSAoTWljcm9zb2Z0IFdvcmQgLSBEb2N1bWVudDEpIC9Q
cm9kdWNlciAobWFjT1MgVmVyc2lvbiAxMC4xNS43IFwoQnVpbGQgMTlIMTE0XCkg
UXVhcnR6IFBERkNvbnRleHQpCi9DcmVhdG9yIChXb3JkKSAvQ3JlYXRpb25EYXRl
IChEOjIwMjAxMjE2MTUzNTA2WjAwJzAwJykgL01vZERhdGUgKEQ6MjAyMDEyMTYx
NTM1MDZaMDAnMDAnKQo+PgplbmRvYmoKeHJlZgowIDE4CjAwMDAwMDAwMDAgNjU1
MzUgZiAKMDAwMDAxMzk2NyAwMDAwMCBuIAowMDAwMDAwMzE5IDAwMDAwIG4gCjAw
MDAwMDMzMDIgMDAwMDAgbiAKMDAwMDAwMDAyMiAwMDAwMCBuIAowMDAwMDAwMzAw
IDAwMDAwIG4gCjAwMDAwMDA0MzMgMDAwMDAgbiAKMDAwMDAwMzI2NiAwMDAwMCBu
IAowMDAwMDAwMDAwIDAwMDAwIG4gCjAwMDAwMDM0NDUgMDAwMDAgbiAKMDAwMDAw
MDUzMCAwMDAwMCBuIAowMDAwMDAzMjQ1IDAwMDAwIG4gCjAwMDAwMDMzOTUgMDAw
MDAgbiAKMDAwMDAwNDA2NCAwMDAwMCBuIAowMDAwMDAzNjU5IDAwMDAwIG4gCjAw
MDAwMDQwNDQgMDAwMDAgbiAKMDAwMDAwNDMwMCAwMDAwMCBuIAowMDAwMDEzOTQ2
IDAwMDAwIG4gCnRyYWlsZXIKPDwgL1NpemUgMTggL1Jvb3QgMTIgMCBSIC9JbmZv
IDEgMCBSIC9JRCBbIDw3MGY3MTE4OTJjZjE3YTNjZGQ3MWE2OWE5OTY4MTE0Zj4K
PDcwZjcxMTg5MmNmMTdhM2NkZDcxYTY5YTk5NjgxMTRmPiBdID4+CnN0YXJ0eHJl
ZgoxNDE4NAolJUVPRgoxMiAwIG9iag08PC9NZXRhZGF0YSAxOCAwIFIvUGFnZXMg
MyAwIFIvVHlwZS9DYXRhbG9nPj4NZW5kb2JqDTE4IDAgb2JqDTw8L0xlbmd0aCAz
MzkyL1N1YnR5cGUvWE1ML1R5cGUvTWV0YWRhdGE+PnN0cmVhbQ0KPD94cGFja2V0
IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6
eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUg
WE1QIENvcmUgNS42LWMwMTcgOTEuMTY0NDY0LCAyMDIwLzA2LzE1LTEwOjIwOjA1
ICAgICAgICAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMu
b3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2Ny
aXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp4bXA9Imh0dHA6
Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOnBkZj0i
aHR0cDovL25zLmFkb2JlLmNvbS9wZGYvMS4zLyIKICAgICAgICAgICAgeG1sbnM6
ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIgogICAgICAgICAg
ICB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyI+
CiAgICAgICAgIDx4bXA6Q3JlYXRlRGF0ZT4yMDIwLTEyLTE2VDE1OjM1OjA2Wjwv
eG1wOkNyZWF0ZURhdGU+CiAgICAgICAgIDx4bXA6Q3JlYXRvclRvb2w+V29yZDwv
eG1wOkNyZWF0b3JUb29sPgogICAgICAgICA8eG1wOk1vZGlmeURhdGU+MjAyMC0x
Mi0xOVQyMDo0MjoyMSswODowMDwveG1wOk1vZGlmeURhdGU+CiAgICAgICAgIDx4
bXA6TWV0YWRhdGFEYXRlPjIwMjAtMTItMTlUMjA6NDI6MjErMDg6MDA8L3htcDpN
ZXRhZGF0YURhdGU+CiAgICAgICAgIDxwZGY6UHJvZHVjZXI+bWFjT1MgVmVyc2lv
biAxMC4xNS43IChCdWlsZCAxOUgxMTQpIFF1YXJ0eiBQREZDb250ZXh0PC9wZGY6
UHJvZHVjZXI+CiAgICAgICAgIDxkYzpmb3JtYXQ+YXBwbGljYXRpb24vcGRmPC9k
Yzpmb3JtYXQ+CiAgICAgICAgIDxkYzp0aXRsZT4KICAgICAgICAgICAgPHJkZjpB
bHQ+CiAgICAgICAgICAgICAgIDxyZGY6bGkgeG1sOmxhbmc9IngtZGVmYXVsdCI+
RmFpbGVkPC9yZGY6bGk+CiAgICAgICAgICAgIDwvcmRmOkFsdD4KICAgICAgICAg
PC9kYzp0aXRsZT4KICAgICAgICAgPGRjOmNyZWF0b3I+CiAgICAgICAgICAgIDxy
ZGY6QmFnLz4KICAgICAgICAgPC9kYzpjcmVhdG9yPgogICAgICAgICA8eG1wTU06
RG9jdW1lbnRJRD51dWlkOmI3YTY5NDFhLTE4MDgtOWQ0Ni1hY2YxLTIzY2E5NzMw
ZjA5OTwveG1wTU06RG9jdW1lbnRJRD4KICAgICAgICAgPHhtcE1NOkluc3RhbmNl
SUQ+dXVpZDphODMxYzg1ZC0xNzk2LTMwNGEtYWM1NS1iMDAwNjQ1Mjc4NjI8L3ht
cE1NOkluc3RhbmNlSUQ+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3Jk
ZjpSREY+CjwveDp4bXBtZXRhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
IAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAog
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAg
ICAgCjw/eHBhY2tldCBlbmQ9InciPz4NZW5kc3RyZWFtDWVuZG9iag0xOSAwIG9i
ag08PC9DcmVhdGlvbkRhdGUoRDoyMDIwMTIxNjE1MzUwNlopL0NyZWF0b3IoV29y
ZCkvTW9kRGF0ZShEOjIwMjAxMjE5MjA0MjIxKzA4JzAwJykvUHJvZHVjZXIobWFj
T1MgVmVyc2lvbiAxMC4xNS43IFwoQnVpbGQgMTlIMTE0XCkgUXVhcnR6IFBERkNv
bnRleHQpL1RpdGxlKEZhaWxlZCk+Pg1lbmRvYmoNeHJlZg0KMCAxDQowMDAwMDAw
MDAwIDY1NTM1IGYNCjEyIDENCjAwMDAwMTQ3MDIgMDAwMDAgbg0KMTggMg0KMDAw
MDAxNDc2NCAwMDAwMCBuDQowMDAwMDE4MjMzIDAwMDAwIG4NCnRyYWlsZXINPDwv
U2l6ZSAyMC9Sb290IDEyIDAgUi9JbmZvIDE5IDAgUi9JRFs8NzBGNzExODkyQ0Yx
N0EzQ0RENzFBNjlBOTk2ODExNEY+PEMyNjMyMkY1RTFFRDQyRUZBQkE0NDAxQjBG
RTgxQTg3Pl0vUHJldiAxNDE4ND4+DXN0YXJ0eHJlZg0xODQxNA0lJUVPRg0=
```

In `csia/codestudy/static/failed/failed.png` (encoded as base 64):
```
iVBORw0KGgoAAAANSUhEUgAAA4QAAAJYCAIAAAC1p7+MAAAACXBIWXMAAC4jAAAu
IwF4pT92AAAGsWlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJl
Z2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1w
bWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1Q
IENvcmUgNi4wLWMwMDMgNzkuMTY0NTI3LCAyMDIwLzEwLzE1LTE3OjQ4OjMyICAg
ICAgICAiPiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5
OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPiA8cmRmOkRlc2NyaXB0aW9uIHJkZjph
Ym91dD0iIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8i
IHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4
bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jl
c291cmNlRXZlbnQjIiB4bWxuczpwaG90b3Nob3A9Imh0dHA6Ly9ucy5hZG9iZS5j
b20vcGhvdG9zaG9wLzEuMC8iIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMv
ZWxlbWVudHMvMS4xLyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3Ag
MjIuMSAoTWFjaW50b3NoKSIgeG1wOkNyZWF0ZURhdGU9IjIwMjAtMTItMTZUMjM6
MzM6MzMrMDg6MDAiIHhtcDpNZXRhZGF0YURhdGU9IjIwMjAtMTItMTZUMjM6MzM6
MzMrMDg6MDAiIHhtcDpNb2RpZnlEYXRlPSIyMDIwLTEyLTE2VDIzOjMzOjMzKzA4
OjAwIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOmZhZDBmYWNkLTliZjYtNGFm
NS04YTc2LWZhM2Q1M2E4MTg5ZiIgeG1wTU06RG9jdW1lbnRJRD0iYWRvYmU6ZG9j
aWQ6cGhvdG9zaG9wOjMzOWM0ZjZiLTAyZTgtNjI0MC1iNzBjLWM1OGU1OTk0ZTFm
MyIgeG1wTU06T3JpZ2luYWxEb2N1bWVudElEPSJ4bXAuZGlkOmI4MzI0MDM5LTVm
MGYtNGVhOC05YjgxLTljYjYyOWQ1MDQ2MSIgcGhvdG9zaG9wOkNvbG9yTW9kZT0i
MyIgcGhvdG9zaG9wOklDQ1Byb2ZpbGU9InNSR0IgSUVDNjE5NjYtMi4xIiBkYzpm
b3JtYXQ9ImltYWdlL3BuZyI+IDx4bXBNTTpIaXN0b3J5PiA8cmRmOlNlcT4gPHJk
ZjpsaSBzdEV2dDphY3Rpb249ImNyZWF0ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9Inht
cC5paWQ6YjgzMjQwMzktNWYwZi00ZWE4LTliODEtOWNiNjI5ZDUwNDYxIiBzdEV2
dDp3aGVuPSIyMDIwLTEyLTE2VDIzOjMzOjMzKzA4OjAwIiBzdEV2dDpzb2Z0d2Fy
ZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgMjIuMSAoTWFjaW50b3NoKSIvPiA8cmRm
OmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5p
aWQ6ZmFkMGZhY2QtOWJmNi00YWY1LThhNzYtZmEzZDUzYTgxODlmIiBzdEV2dDp3
aGVuPSIyMDIwLTEyLTE2VDIzOjMzOjMzKzA4OjAwIiBzdEV2dDpzb2Z0d2FyZUFn
ZW50PSJBZG9iZSBQaG90b3Nob3AgMjIuMSAoTWFjaW50b3NoKSIgc3RFdnQ6Y2hh
bmdlZD0iLyIvPiA8L3JkZjpTZXE+IDwveG1wTU06SGlzdG9yeT4gPHBob3Rvc2hv
cDpUZXh0TGF5ZXJzPiA8cmRmOkJhZz4gPHJkZjpsaSBwaG90b3Nob3A6TGF5ZXJO
YW1lPSJGYWlsZWQgdG8gcHJvY2VzcyAgdGhlIGRvY3VtZW50IiBwaG90b3Nob3A6
TGF5ZXJUZXh0PSJGYWlsZWQgdG8gcHJvY2VzcyAgdGhlIGRvY3VtZW50Ii8+IDwv
cmRmOkJhZz4gPC9waG90b3Nob3A6VGV4dExheWVycz4gPC9yZGY6RGVzY3JpcHRp
b24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz6Z
Rpv1AAA1jklEQVR4nO3dX2hc14E/8Nsfv6dpsrQFtemkLGob0xa1eEIeRExKqIwI
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
t7Q3TFIURWNjY//6r/+aPFRHrVa7dOlS3Llneno64STa46GdarXayy+/HHeemJyc
/MlPfpJwgkwYSimKovn5+ampqbilURQVi8XkXpaDo/Dsk36Ipe4O7dRUV8Lood//
6enpV199NSHlVyqVixcvJpz7JycnFxcXU9anVSmP37GxsVdffTXhm1mtVldWVpK/
Hsnf7bgvZy6XO5gVGhluXyyuVCpf+9rXGq/0w36pVCoJB1Q2m/35z3+e/EN3eXk5
IWMlVyBUW5HwwVwud/ny5eTWOHmjxf3JQQpl0LlMTzf97ne/i1s0NjZ25cqVQweN
GxoaWlpayuVyTZf+93//dwe167Jr167FnV1KpdLi4mJyV00+n9/Y2IhburCwkHCD
1O7u7qFR49DhGE+fPr25uZnNZpPfNkDeeuuthKWlUqlYLCb3N4+Ojl6/fn1sbCzu
Devr62FvHp2cnLxy5UpyJ9zw8PDi4mLyvYzJ2yrOviSazWZXVlauXbuWz+f3fdtH
R0cfvNIP+6UxoUZTuVzu+vXrh15ymZ2dXVlZSahAwh2codqKe/fuxX3q0FAYRdHo
6GjCHQjr6+tN7/cIUiiDThilm9577724RT/72c9SriSTycT12P3+979vp1pHoFar
xXWTzM/PpxyXe2RkJKHZfXic833efffdhNWura2lHKt/eHj46tWrad7Z/5ID+qH9
xA8k/xyKouhXv/pVG9XrirGxsfTdQrOzs9PT03FLk8NTGo0Md+g1037YL1tbW3EX
f7PZ7PLycspbL06fPp0Q8eN+igdsK/7nf/6n6etjY2MpB5MfHR1N+A3wwQcf9Emh
DDphlG5KuLze0p12zz77bNPXu/7wQdviWv/GJcv06xkdHY07vS0tLTXt8KjX6wk3
Bc7Pz7d0W+3w8HBCp9EASeh+m56ebmnankwmc/ny5bil29vboQZ2SP+LruHVV19N
SG83b95suybpM1w/7JfGFJRNvfbaay01Ta+88krcorif4gHbiq546aWX4hYd3Q08
QQolIGGUrkloDb/1rW+1tKrka3bB1ev1t99+u+miNh75Tzi9NebL3ifhzJrNZr//
/e+3WoF8Pp8QWQZCvV5P6H5L6CCMMzw8PD8/H7e0kxjXtkKh0OqzU5lMJuFew7jv
cBopM1w/7JdarRZXh8nJyVafhslkMnHV3t7ePngFOWxbEadpVePk8/m7MVoK00EK
ZVAIo3TN0NBQXPPR6nTSfT6e3AcffNC0jzaXy7Uxl30mk4nr8Lhx48bBF+/cuRO3
qvPnz7eX4zufLD6shIDeRoZreOGFF+IWdRLj2nbmzJk2PpVwxXNvb6+9MUfTZ7h+
2C8JKW18fLyNCiT8tP7oo4/2vRK2rfj2t78dt6p/+7d/a7X0lIIUyqATRulHLf3K
773f/OY3TV9vNXM/8MwzzzR9vWlfwm9/+9u49Zw6daq9CsTdFzEoEgJ6wvW+ZEND
Q3F9YG3HuLaNjY21PaRUwha4fft2Gyv853/+55Tv7If9EleHbDbb3tc+odPu4D2R
YduKxx9/PG496+vrMzMzR/E1DlIog04Ype8c3bD53RIXB+PGJzrUd77znbhF++7W
r9frcY9idJJXMplMwhMD/S9uj2Sz2ZTPTDSV0AfWXoxr23e/+922P5vQ/5cQFuNk
s9n0NyX3w3759a9/3fSdL774Yg9uBwrYVkSHdf1ub2+Pj48Xi8XuTrYcpFAGnUHv
HyG3bt3q/XjdLdna2vrP//zPbk2Xd0QS4uCXvvSl9taZyWSy2WzTy3l37959+Nx/
8DrgA53klcbHj2KCnB5I2CMvvvhiJ2s+efJk3KKPP/64kzW3qu3sEkVRJpNpOj5o
1NZYaek3aT/sl3q9HvfUY6s3srchbFsR/e9l/eQh6NfX19fX1+fm5hpzZERRtG/I
2DZq2PtCGXTCKGE0Jhdp/PvQOWP6SkIcbO8WtGR//OMfH/7v3//+97h3JlwdS6PD
jweUsE06DBzDw8NxJ/59++Wofe1rX+vk488880zTVNTGWGnpN2k/7JeEo/Wxxx7r
pA5phG0rGl555ZW33347zTgke3t7D1+SGhsba9xK0cYdBUEKZaAJo/RCY6q3KIoO
ndmv//35z3/uZXF//etfH/7v/fv34975xBNPdFJQhx8P6EgDxze/+c2m59R9++Wo
ffazn+3k41/5yleavr63t1ev11u6Wv3UU0+lfGc/7JeEo7UHX/iwbUVDJpO5evVq
G9l3e3u70VbPzc01MmL6zssghTLQhFGOULlcPgbpc59PPvmkl8X94Q9/SPnODk/w
Pego6r3OA8fnP//5pq+n3y9d0eHdjQnd3n//+99bWvkXv/jFTmrS0LP90uOjdZ8+
aSuGh4c3NzcvXLiQMO17sgcZcXJy8kc/+lGacQCCFMrg8gATR2Jtbe3EiRNzc3Pt
JdHjNEdlz3QlJQyisIGDOH2+Xx6p42V4ePjatWsJQ7SmtL6+PjExsbi4mGbE0CCF
MqCEUbqsWq2eOXNmYWGhvY+XSqXNzc0f/vCH3a3V4Pr617+e8p0Jt+gdb8eyT/cY
6PP9cvyOl0Pbiqmpqdu3b5dKpQ4nuVhdXT179mzK0aCDFMrAcZmebqpWq2fPnk05
aef09PSD5xjGx8f7fNalB3p8iv3c5z6XsvQOT64Jd6MOrvv373d4de8vf/lL09fT
/0joilbv7Eyvw7tR29MP+6UHYTRsW9FUJpPJ5/P5fL5Wq926davth0d3dnZmZ2ev
Xr2a5msZpFAGizBK19Tr9QsXLiQk0cYoHk888URLk6f3m4QTzObmZiejJ3ZYeocn
+D6/qJog4Xpr539U3PPmaU78XfTRRx918tW6d+9e3KKjO6/3w35JuDm1B1/4sG1F
sqGhoUZALBaL9Xq9MVdWS7f47+zsvPnmm7Ozs31eKANBGKVrNjc3E+5VX1lZaXUa
6P6UcIrtQV9LQul/+tOfOllzG+Of94mEvr07d+50MkZMtVqN+3EV93z6Efnzn//c
SXaJG6K/wyunyfphvyTUoQeXAsK2Fek1ei6j/x1QKX3/5dLS0pkzZ9p72j1IofQt
94zSNa+//nrcos3NzeORRKMoGhoainu+qjF8VajS33vvvU7WHDdRTf9LmD6qwz8q
YZqlL3/5y52suVV3795t+7P1ej2u5ylubsmu6If9kpDg2/71VS6XT8TYN9Fl2Lai
bY3+y2KxePfu3VKplPzmbk3dHKRQ+ocwSnck9FWUSqWwF6S67pvf/GbT13szK0/c
hNpNJ6dOKWH3DYSvfvWrTV/f29vb3d1te7UJeaXH94x2MnfiwVkiHzjq/t1+2C9d
D8Rx9zw0neM0bFvRuXw+f+vWrYS5gt9///3jUShhCaN0R0JfRcLcfQMqbuLNX/7y
lz0o/dvf/nbcorbb6Bs3brRbnb6QMKPPzZs321tnrVaLu2LY4dTqbdjZ2Wk7vcVN
jx51NstoGv2wX+KO1r29vUql0kYF3n777aavN53jNGBbsby8HNeD29J6hoaGfvaz
n8Ut3Te4aZBCOQaEUboj4Yd+G6fthGjbD55++ummr+/t7W1tbbWxwlqtFteCH+zs
fO655+LWs7Ky0l7pyRNJ97+EuV6WlpbaGw7m2rVrcYuCDD321ltvtfGp5J37ne98
p4MaHa4f9ktCDHrnnXdaLX13d7elye4DthX/8A//ELeSfbcTHGpoaCihnzJ4oRwD
wijd8be//a1bq6rVan0+adPIyEjcrWDtxcG48+vk5OTBh50bE3M3ff/Ozk4b13Pb
G2alr2QymcnJybilv/jFL1pdYbVaTchwzz//fKsr7Nz6+nobPXkJO7fpt6u7+mG/
jI6Oxh0vbWzShJ8Ep06dOvhiwLYiYdqtNn7tp7zAFaRQjgFhlCPX6g/iS5cuHU1F
uun8+fNNX9/Z2VlbW2tpVZVKJe78Gnd7aFzpURTNzc21tMHL5XI/h9H0J7Af/ehH
cYvW19dbyuiNQcrilo6NjYWamfDixYtd3LltTB3ehn7YLwnHS6lUSt9BWy6X19fX
my6anJyMe747VFuRkOTW1tZavb887kjcd5NukEI5BoRRuuPJJ5+MW9RSB0CxWOzz
btGG8fHxuA6PhYWF9KfYarV68eLFpouy2WxcXGjaB/PA2bNnU0aWra2tubm5NO88
anFjDG1vb6fMCiMjIwmdcHNzcyl3Sq1WKxQKCYOU/eAHP0iznqOwt7fXrZ2bzWZ7
M8BFP+yXhKN1Z2fn0qVLaULS7u5uwvZMSPah2orkSyhvvvlmynKjKKpUKnHN8r5b
2IMUyjEgjNIdCYNLr6+vF4vFQyNFpVI5c+ZMXMfDA30yPXEmk0nunkzzJ29tbY2P
j8fdgnb+/Pm4q6hDQ0MJMz7v7e2Nj48fepJbXl4+d+5c8nt65gtf+ELcotnZ2YN3
1zXdtgmdcFEUzc3NLS4uJu+USqXy8ssvJ/wcmpycDDtIWZqdW6/XFxcXk3duwre3
64Lvl+SjdXt7++zZs8nPh5XL5YmJibiluVyu7dKPtK348Y9/HLfCpaWlNOVGUVQu
l6empuKWHrwpNkihDLrPfPrpp6HrQNfs7u4mtJi3bt06uoGC6/X6off3FAqFJ598
ct/Mn5VK5f79+2trawl9Hg+bn5+Pa6QS/vyNjY24S3jtfarhzJkzydVu/Mn7xvdu
/Mmvv/56wmhKuVwu4UGNKIrq9frZs2eTS29MeXXy5MmHnyGrVCp3795dWFhI+OA+
nQxymdLy8nJLD1HFzaGwtrZ26J9WKBS+8Y1vPPzxxoDbh84Ek81mr1+/fnQHUfLx
e7Aybe/cQ79d5XI5rhewvWakH/bLoUfr5OTks88++/DR2qjAoa3ToQ1FmtKPoq2o
1WrJV1Gi/52W+eCEzI0fPMlXTpoWHaRQBp0weqwEDKNR63mic/v+ot6H0Wq1evbs
2a6P0JnNZq9evXroKASVSiWh86CLehBGE9JPUwkTes3MzBzRnR5ra2tHOpNtS2G0
E4d+sbseRqM+2C/VavUobpNN+Hm8r/QgbUWrR1ZL4iY1DVIoA81lerrmzJkzoavQ
a8PDw8vLy11f7fLycprWdnR09NCpStLr4qracGhXSnpLS0tHMSLMysrKkSbRZN3d
0UEewAq+X4aHhzc2Nrpb+tjYWMofhKHainw+n3DPbicSZjMJUigDTRila4aGhrp1
yiwUCoMywtzIyEh3z3BpLvk9kM/nu7LNp6enuxgH2zA0NFQoFLqyqkwms7S01N1z
YUJHbG889dRTXdnRhUKhk0nhO9EP+6W7R+vY2FhL14JCtRWvvfZa15vTUqmU/EUK
UiiDSxilm7qSjUql0uzs7EsvvdSVKvXAyMjI5uZm5y1vLpfb3Nxstdcqn8+3OkDM
PpOTk8VisZM1dMUrr7zSrbNXJpNZXFxMeMYrvcZOCZtEGzo/uBpHVrfq04Z+2C/d
Olqnp6evXLnS6kCtQdqKTCZz5cqV6enpDgttyGaza2trh4bCIIUyuIRRuqyRjeJG
90g2OTm5ubnZaHESxkPpQ8PDw1euXOkkK5RKpWvXrrV3BWp0dPTWrVvt9TkVCoXF
xcU2Pth1jbNXV5JKw9TU1ObmZiddcZ3slKOQz+fbizK5XG5jY6NPzuXB90uHR2s2
m11ZWWn791uotqJYLK6trcWNoZZSoVD49a9/nf5+lSCFMog8wHSshH2AaZ9yuZz8
EOjDSqXSvueCoyja3d2dnZ1NWEPwB5iaaukPbzwTffCp0vbs7u6+++67KQexLxQK
L7300oNtnvAMbA8eYNqn8VBtwmZs6frs7u7uzZs3019RbeyU3ke39F/Fra2tX/3q
V2meB2rvbzmKB5gOCr5f6vX65uZm+qM1l8tNTU11sQJB2oqtra3Nzc1DB9F7WOMP
76ToIIUyQIRRjtbu7u6HH354586dfQmp0bBGUXQwg+5TLpf3je0yPz//+OOPnzp1
qpfZulXVarUxfcjBk/qDv/3o/oRGmDs4Jk6jfY+iqE86yXpsa2vrk08+OfhtjHqy
Uw7V6u+iRpaKmqX2xihFTzzxxED0JwXfL42j9eOPP246/lSjF/PQlqrD0qOetxWN
VuLevXtNfw80hpqKut1WBCmU/ieMAvSFrnfSAwwE94wCABCMMAoAQDDCKAAAwQij
AAAEI4wCABCMMAoAQDDCKAAAwQijAAAEI4wCABCMMAoAQDDCKAAAwQijAAAE85lP
P/00dB0AAHhE6RkFACAYYRQAgGCEUQAAghFGAQAIRhgFACAYYRQAgGCEUQAAghFG
AQAIRhgFACAYYRQAgGCEUQAAghFGAQAIRhgFACAYYRQAgGCEUQAAghFGAQAIRhgF
ACAYYRQAgGCEUQAAghFGAQAIRhgFACCY/xu6AnDkyuXy3Nxc00V3797tcWWwOwB4
mJ5RAACCEUYBAAhGGAUAIBj3jNLvTpw40fT1QqEwOzvb48oAHAPaVfqKnlEAAIIR
RgEACEYYBQAgGGEUAIBghFEAAIIRRgEACEYYBQAgGGEUAIBghFEAAIIxAxPst7W1
9cknn7z++ut7e3sPvz4/P//444+fOnVqaGiouyXW6/XNzc0oig4WOjk5+eyzzz7x
xBOjo6PdLbRzu7u7H3744fvvv7++vv7w6406P/bYY6dPn+5lfRo77t69e0tLS/sW
ZbPZ8+fPR1F0FLvvYbVa7datW1GzXRlFUaFQePLJJ3u/ZYKoVqu3b9++c+fO6urq
w683vh4nT54cHh4+dCWN7dl0nx7R8dg/B2PvGyII5TOffvpp6DrA/7e1tXXu3LkO
V7KysrLvTF8ul+fm5pq++e7duynf+bCxsbF/+Zd/6coJqVKpvPPOO/vCXJz5+fkX
Xngh+BmocbZOs6GiZnVOvztS2t3dvXnz5sGwEqcRTPP5fBtlJSiXy2trazs7Oynf
Pz09/b3vfS/9t6i72y1uNshSqZSwZeLqsG8OyUql8u///u/b29vJdUg+jqrV6srK
SppDY2xs7NVXXx0ZGTn0ncmO+mBMufUS3rlPyoboiNpV6CKX6SGKomh3d/fMmTMp
A9b29vbU1FSxWKzVam2XWK1WZ2ZmpqamUp78oihaWFg4derU2tpa24V2bmtr6+TJ
kyk3VHTEda5Wq8VicWJiIn0SjaJob29vbm7uxIkT3arV1tbW888/Pzc3lz6JRlG0
uro6NTU1MzOzu7vblWr0icXFxampqUOTaPS/x9Hi4mK9Xt+3qFwuj4+Ppzw0tre3
JyYmFhcX26luFEX9dDD2viGCfiCMQrS1tTUxMdFSkoiiaH19fXZ2tlqttlFi41yb
5oR90MLCwpkzZ9ort0PFYrG9LpaFhYWZmZnunjLX1tbS55W4Wp05c6aTLFiv1xvb
5OAV+ZQaQWp5ebntOvSVYrG476L8oVZXVwuFwsN5tFgspv+18/B6ZmZmDubaQ/XP
wVgul3vcEEGfEEZ51HVyDWtnZ+fChQutnv8WFxfbONfuK3d8fLyXPWr1en1mZqaT
5Le9vT07O9uVPNqIgAsLC52vamdnZ2JiYmtrq43PVqvVs2fPdrJNHlhaWioWi20E
qb5SLBbb2xrb29tvvvlmhyvZt56U+udgTHlpPq4ObTRE0D+EUR5p1Wq1w7updnZ2
3njjjfTvb6PrKM7ExETP8mihUGiv6+hhOzs7ly5d6nAl9Xq9UCh0JQI+cO7cuVbz
aCOJttqJlWB9fb1QKHRrbb23trbWyU5ZWlra3d1dXl7ucM821pPyzf1zMFYqlc4z
cUsNEfQVYZRH2oULFzpfyerqasrzUOfn2n0mJiZ6cHlubW2t8yTasL293eFtdl2J
xQedO3euUqmkfHO9Xr9w4ULbl+bjdL5xQvnNb37TeUf17OxsS/f+xnn33XfTvK1/
Dsa//e1vFy9e7LwC6Rsi6DeGdqKPnD59+uBzwXGP/R58BLUN+3q2xsbGXnrppfHx
8Uwm03il8eT4oU9J37x589CHecvlcvK5tjHuz8PPMjcGx2k6SNADFy5cuHr16oMK
d121Wj00ZzSeT3/qqace3giNgZ8OVr6T3sQ0sbhQKHzjG994+MnfxvBAN27cSP7s
xYsXr1+/nub56DfeeCP5r8jlclNTU/s2SKVSuX//fnIH2MLCwtNPP935g+E9dnBr
zM/P7/tDyuVy8i5oOhLWvl3ZOCKSt+Hq6uqrr76afET01cF4sHe2uw1R79tVaJWe
UYiiKMpms2tra1euXMnn8w+fSzKZTD6fv3bt2vz8fMLH33777eT112q1119/PW7p
5OTkrVu3Zmdn942qMzw8nM/nb968WSqV4j67s7PzH//xH8mld2JlZSX5DaVS6ebN
m/l8ft9ZcGRkpFH5Q9eQ0u7ubnIsnp6evn379uzs7L4xaIaGhvL5/JUrV9bW1rLZ
bNzH9/b2fvGLXxxajUqlknBtt/FFunbt2sENMjo6ms/n7969m3w5/q233jq0Dv2s
8WWempra9+c3dkHKWxFyudzm5ubBXdk4Im7dujU2Npbw8Q8++CBhaT8fjEfdEEF/
EkYhyuVy169fTx6ub2pqKuE8ure3l3yF7tq1a3EdKqVSaXFxMblDLp/Pb2xsxC1d
WFg4orFddnd3ky9lbmxsHDpg5+nTpzc3NxNSYErJKa1UKhWLxeROqdHR0evXryfk
mPX19UNvHk3IImm+SFEUzc7OJgT09fX1wb3YOjk5mfxlnp2dzeVyySvJZrPLy8sJ
Q+IPDQ397Gc/S/hG3b9/P2H9fXsw9qAhgv4kjEJ0+fLlNBdnX3nllYTz3x/+8Ie4
RbVaLe6a4Pz8fMrR10dGRhJuKLx27VqalbQq+fa7tbW1lBeUh4eHr1692klNkmNx
8lDtDxsaGlpaWkrIQ7/61a8SPr61tRV3nbQRoVKOgn769OmESPG73/0uzUr6TS6X
e+211w5926GPDL722muHbsahoaEf//jHcUvv3bsXt6ifD8ajboigbwmjPOpKpVKa
aQmjKMpkMi+++GLc0k8++SRuUdzJqXFnYZqiG0ZHR+MSzNLSUtc7R+v1esL16Pn5
+ZbmoBoeHk7oUzxUQrfo9PR0S9MpZTKZy5cvxy3d3t5O6JhsTBTZVJoI9bBXXnkl
btF7772Xfj39Y25uLs3tks8++2zC0lwul3Kmn+eeey5u0d/+9re4RX17MPagIYK+
JYzySMtms+Pj4+nf/61vfavVIur1etyNXD/96U9bXVtCgmlMid5FCcErm81+//vf
b3WF+Xz+0Eu0TdXr9YRu0enp6VZXODw8nHDv3c2bN5u+XqvV4qoxOTnZ6mSJmUwm
rubb29sDN2ZkLpdL+eMkk8kk3CmR/nfFF7/4xbhFf/3rX5u+3rcHYw8aIuhnwiiP
tB/+8IctPfp68uTJVov44IMPmt6glsvl2nhoOpPJxPXH3Lhxo9W1Jbtz507covPn
z7f3/H57o7omxOJCodBSf+QDL7zwQtyiuLySkDBaShIPJESKjz76qI0VBtRSt+Ln
P//5uEVxT3kflMlkWr0RuW8Pxh40RNDPDO3EI+2ZZ55p6f2f/exnWy3iN7/5TdPX
W7qy/LC4Oje607o4xtNvf/vbuEWnTp1qb53Jl2jjJMTil156qb2aDA0NTU9PN70P
ofEUyMFrpnHVyGaz7f1d+Xy+7a9Bv3nqqafSv/kf//Ef4xZ97WtfS7+eL37xiy2N
9tq3B2MPGiLoZ3pGeaR96Utfaun9bXTCxUW69D1A+3znO9+JW5Q8ok1L6vV63JM6
Y2Nj7XVGRoddoo0Ttw2z2WzK2+yaSuiYvH379sEXf/3rXzd984svvnh047wOioSL
5i1p+6uVRt8ejD1oiKCfCaM80rp1Bo2TEOlaPf08kHB18uDQ1m1LuEz83e9+t5M1
t/rxhG2Y8BhHGgnXOj/++OOD1YjrhHMDX9SleNT5+F8J+vlgPOqGCPqcy/Q80o66
Qysh0rV3l2GyP/7xj91a1d///ve4RY8//ngna2714wk16TAFDg8PZ7PZphHz4JZM
2JWPPfZYJ9XggSPNZP18MOpZ5xGnZxSO0J///OdeFhf3EHEbEoYNf+KJJzpZc6sf
P9IU+M1vfrPp6we3ZMKu7HCD0BuDezDCsSeMwhHq8Zh/vRnvusMI2MV+xM5TYNxj
3Qe3pOEbB92xPBjheBBGgdb0+P62/k+BbvgD6IQwCsfH17/+9R6UknAT51Ho/zsy
e7xBGAi9ORjheBBG4Qj1OEh97nOf69aqEmreYfZKuBu196v6y1/+0vT1lpKEMDoQ
BvdghGPP0/RwhBLOf5ubm52MkXnUEmp+//79NqareaDVy+4JF8E7v4L/+9//vunr
B5NEwv2p/X8jAdEgH4xw7OkZhSOUEKT6vDstoeZ/+tOfOllzwnRKTSVMNtPqqvap
VqtxQ4d+5StfSV+NLvb1cnQG92CEY08YhSM0NDQUNyb2hx9+2OPKtCSh5u+9914n
a46bxyhOwqRNra5qn6bTLDV8+ctf3vdKQs9Z25m4XC6fiFGtVtOvp16vt1RurVZr
raLHwuAejHDsCaNwtOJGsjw4x0+/iZtvvTHvdnvrTOiMTPDVr3616et7e3u7u7vt
1SRKDJFN7xnteia+d+9e09dbnea01Y69hKFbj7fBPRjheBNG4WjFzX75y1/+ssc1
adW3v/3tuEXvv/9+e+u8ceNGG59KmGnp5s2b7dWkVqutrq42XRSXBeN25d7eXqVS
aaMOb7/9dtPXW53mtNVw+ch2BA7uwQjHmzAKR+vpp59u+vre3t7W1lYbK6zVanHX
dtvusGzqueeei1u0srLSxgprtdrS0lIbH0yYrXFpaam9i87Xrl2LW/TDH/6w6esn
TpyI+8g777zTagV2d3dbmuw+4fmbVsNl278lBt3gHoxwvAmjcLRGRkbi7lRrL9LF
pajJycnuznDdmLq96aKdnZ1yudzqCuN6Ig+VyWQmJyfjlv7iF79odYXVajUhFj//
/PNNXx8dHY3bIOvr6612jr711ltxi06dOnXwxYTH+Vu6abVWq62vr6d//3EyuAcj
HG/CKIMq4emTfnP+/Pmmr+/s7KytrbW0qkqlEpei4m7x7ERczaMompuba+khm3K5
3HYYjaLoRz/6Udyi9fX1lpJxvV6/cOFC3NKxsbGEgasSNkipVErfR1sul+MS4eTk
5NDQ0MHXEx4GX11dTd8Pd+nSpZTvPJYG92DsjQFqVzlOhFH6XS6Xa/r69vb2oDwU
PD4+Htcfs7CwkD5IVavVixcvNl2UzWYTrmW3rWkX3QNnz55NmUe3trbm5uY6qcnI
yEhC5+jc3FzKzVir1QqFws7OTtwbfvCDHyR8PGFX7uzsXLp0KU0o3N3dTdgacfsx
4WHwKIreeOONQ8uNomh5eXl7ezvNO4+rwT0Yu+sYtKscJ8Io/e4LX/hC3KLZ2dmD
d3r1YUuayWSSuxiLxeKh1d7a2hofH4+7y/D8+fNHcVlwaGhofn4+bune3t74+Pih
5+/l5eVz5851XpmEztEoiubm5hYXF5M3Y6VSefnllxPS2OTk5OnTpxPWkLwrt7e3
z549m/yAf7lcnpiYiFuay+USKhB3M2sURaurq4uLiwnl1mq1YrHY3j27x8ngHozd
dQzaVY4TYZR+d/LkybhFOzs7586d2/fcwH/913/1snop5fP5uK6IKIrW19dPnTq1
vLx8MNhVKpVyufz8888n5LlcLpfP57tV1X2+//3vJ9Q8iqK5ubnnn3++XC7v6yWt
VCpra2snTpzoVgAaGRlJSMZRFK2urjY2475Taa1WK5fLMzMzU1NTCQNLZbPZn/zk
J4dWI3lX7uzsTExMFIvFfbuyUYczZ84k9xD/9Kc/TVj6zDPPJCxdXV09c+ZMuVze
lxvK5fLy8vKpU6ce2VtF9xncg7GLjke7yrFhOlD63ZNPPhm6Ct1x+fLls2fPJoSh
Rmhr9XJ2Npu9fPlyp5WLl8lk5ubmpqamEt6zt7fX4VX4lKampt57773kC81tZ9+f
//znTW/WPOjy5cvJ12HX19fX19db3Sbz8/PJ86yOjo7mcrmEewx2dnYSlvLAgB6M
XXRs2lWOBz2j9Lvk2xYHyPDw8PLyctdXu7y8fNTTao+OjpZKpW6trcNVLS0txQ0+
34mVlZXR0dGUbx4eHt7Y2OhuBcbGxpITf0NXQv/09HRyb/exN7gHY7ccm3aV40EY
pd8NDQ0VCoXQteiOkZGR7oaYjY2N5L60bsnn813Jo9PT0x2eBTOZzNLSUsLDTG1Y
WVlJvlX0oO7uyrGxsZQduqOjo9PT052UlcvlXn311U7WcDwM7sHYFcepXeUYEEYZ
AK+88spRdIYFMTIysrm52fmfk8vlNjc3e3nyy+fzrY59s8/k5GSxWOy8JplMZnFx
Mfn+0ZQam7HVJNrQrV05PT195cqV9I+8FIvFtgsdGxtbXl7u/8dremNwD8auOE7t
KoNOGGUAZDKZK1eudCV89IPh4eErV6500tFYKpWuXbvW+wuCo6Ojt27daq9XslAo
JD/u3aqpqanNzc1Oukg734wd7spsNruystJGQL9y5Uob/aON1JvyvthHxOAejJ07
Zu0qA00YZWBMTU3dvXu3VCqVSqWEARcHRT6fb/w56f+WbDZbKpVu374d8HHdoaGh
xcXFjY2N9GGoUChsbm7Ozs52vTLDw8ONyrR0wbGxGe/evdutzZjP52/fvt3Srszl
cqVS6ebNm+11ykZRVCwWNzY2UmbxycnJjY2NrnRLH0sDejB2xTFrVxlQn/n0009D
1wEeddVqtTHxycHHU7LZbGNYxFOnTvVhn1Zj+JsbN27se8I9l8s1Hsfp5al6a2vr
k08+uXPnzsGpnnq2GRu78uOPP15YWDi4tNEDd/Lkye52pDX2wtra2r5H6ScnJ599
9tn+/Ob0rcE9GGFwCaMAAATjMj0AAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAA
BCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQ
jDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAw
wigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEI
owAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOM
AgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAK
AEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigA
AMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAA
BCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQ
jDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAw
wigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEI
owAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOM
AgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAK
AEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigA
AMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAA
BCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQ
jDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAw
wigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEI
owAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOM
AgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAK
AEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigA
AMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAA
BCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQ
jDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAw
wigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEI
owAABCOMAgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMEIowAABCOM
AgAQjDAKAEAwwigAAMEIowAABCOMAgAQjDAKAEAwwigAAMH8PwOFBH4K5sevAAAA
AElFTkSuQmCC
```

In `csia/codestudy/templates/codestudy/edit-tags.html`:
```
{% extends 'codestudy/base.html' %}
{% block title %}
Edit Tags | Code Study
{% endblock %}

{% block content %}
    <div class="ui text container">

        {% for tag_class in tag_classes %}
            <div id="tag_class_{{ tag_class.pk }}" class="ui stackable grid">
                <div class="twelve wide column">
                    <h1>{{ tag_class.name }}</h1>
                </div>
                <div class="four wide column right aligned">
                    <button class="ui icon fluid button" onclick="deleteTagClass('{{ tag_class.pk }}')"><i
                            class="trash icon"></i></button>
                </div>
            </div>
            <table class="ui left aligned table">
                <tbody>
                {% for tag in tag_class.tag_set.all %}
                    <tr id="tag_{{ tag.pk }}">
                        <td>{{ tag.name }}</td>
                        <td class="right aligned">
                            <button class="ui icon button" onclick="deleteTag('{{ tag.pk }}')"><i
                                    class="trash icon"></i></button>
                        </td>
                    </tr>
                {% endfor %}
                <tr id="new_tags_{{ tag_class.pk }}">
                    <td>
                        <div class="ui input">
                            <input id="new_tag_input_{{ tag_class.pk }}" type="text" placeholder="New tag...">
                        </div>
                    </td>
                    <td class="right aligned">
                        <button class="ui icon button" onclick="addTag('{{ tag_class.pk }}', '{{ tag_class.name }}')"><i class="plus icon"></i>
                        </button>
                    </td>
                </tr>
                </tbody>
            </table>
        {% endfor %}
        <div id="new_tag_classes" class="ui stackable grid middle aligned">
            <div class="twelve wide column">
                <div class="ui fluid input">
                    <input id="new_tag_class_input" type="text" placeholder="New tag group...">
                </div>
                <div id="tag_class_error" class="ui pointing red basic label hidden">
                    Cannot be empty
                </div>
            </div>
            <div class="four wide column right aligned">
                <button class="ui icon fluid button" onclick="addTagClass()"><i class="plus icon"></i></button>
            </div>
        </div>
        <div class="ui right aligned grid">
            <div class="column">
                <form method="post">
                    {% csrf_token %}
                    <input id="changeLog-json" name="changeLog-json" hidden>
                    <button type="button" class="ui button" onclick="window.location.reload();">Cancel</button>
                    <button type="button" class="ui teal button" onclick="save()">Save</button>
                    <button type="submit" id="changeLog-submit" hidden></button>
                </form>
            </div>
        </div>
    </div>




{% endblock %}
{% block js %}
    <script src="https://cdnjs.cloudflare.com/ajax/libs/uuid/8.3.1/uuid.min.js"
            integrity="sha512-4JH7nC4nSqPixxbhZCLETJ+DUfHa+Ggk90LETm25fi/SitneSvtxkcWAUujvYrgKgvrvwv4NDAsFgdwCS79Dcw=="
            crossorigin="anonymous"></script>
    <script>
        $('#menu-edit-tags').addClass('active');

        /**
         * @param {String} html: HTML representing a single element
         * @return {DocumentFragment}
         * source: https://stackoverflow.com/questions/494143/creating-a-new-dom-element-from-an-html-string-using-built-in-dom-methods-or-pro/35385518#35385518
         */
        function htmlToElement(html) {
            let template = document.createElement('template');
            html = html.trim(); // Never return a text node of whitespace as the result
            template.innerHTML = html;
            return template.content;
        }

        let changeLog = {
            newTagClasses: [],
            deletedTagClasses: new Set(),
            newTags: [],
            deletedTags: new Set(),
        };

        /**
         * Add a tag in the tag class and render the corresponding UI element.
         * @param {string} tagClassPk The primary key of the tag class.
         * @param {string} tagClassName The name of the tag class.
         */
        function addTag(tagClassPk, tagClassName) {
            const newTagInput = $('#new_tag_input_' + tagClassPk);
            const tagName = newTagInput.val();
            const tagPk = uuid.v4();
            changeLog.newTags.push({
                pk: tagPk,
                name: tagName,
                tagClass: tagClassName
            });
            newTagInput.val('');
            $('#new_tags_' + tagClassPk).before(htmlToElement(`
                <tr id="tag_${tagPk}">
                    <td>${tagName}</td>
                    <td class="right aligned" onclick="deleteTag('${tagPk}')">
                        <button class="ui icon button"><i class="trash icon"></i></button>
                    </td>
                </tr>
            `));
        }

        /**
         * Mark a tag as deleted.
         * @param tagPk The primary key of the tag.
         */
        function deleteTag(tagPk) {
            const tagUi = $(`#tag_${tagPk}`);
            const tagDeleteButton = tagUi.find('td > button');
            if (tagDeleteButton.hasClass('negative')) {
                tagDeleteButton.removeClass('negative');
                changeLog.deletedTags.delete(tagPk);
            } else {
                tagDeleteButton.addClass('negative');
                changeLog.deletedTags.add(tagPk);
            }
            tagDeleteButton.removeClass('active');
        }

        /**
         * Add a tag class and add the UI onto the page.
         */
        function addTagClass() {
            const newTagClassInput = $('#new_tag_class_input');
            const tagClassName = newTagClassInput.val();
            if (tagClassName === '') {
                const TagClassError = $('#tag_class_error');
                TagClassError.removeClass('hidden');
                setTimeout(() => TagClassError.addClass('hidden'), 2000);
                return;
            }
            const tagClassPk = uuid.v4();
            changeLog.newTagClasses.push({
                pk: tagClassPk,
                name: tagClassName,
            });
            newTagClassInput.val('');
            $('#new_tag_classes').before(htmlToElement(`
                <div id="tag_class_${tagClassPk}" class="ui stackable grid">
                    <div class="twelve wide column">
                        <h1>${tagClassName}</h1>
                    </div>
                    <div class="four wide column right aligned">
                        <button class="ui icon fluid button" onclick="deleteTagClass('${tagClassPk}')"><i class="trash icon"></i></button>
                    </div>
                </div>
                <table class="ui left aligned table">
                    <tbody>
                        <tr id="new_tags_${tagClassPk}">
                            <td>
                                <div class="ui input">
                                    <input id="new_tag_input_${tagClassPk}" type="text" placeholder="New tag...">
                                </div>
                            </td>
                            <td class="right aligned">
                                <button class="ui icon button" onclick="addTag('${tagClassPk}', '${tagClassName}')"><i class="plus icon"></i></button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            `));
        }

        /**
         * Delete the tag class and update the UI element.
         * @param tagClassPk The primary key of the tag class.
         */
        function deleteTagClass(tagClassPk) {
            const tagClassUi = $(`#tag_class_${tagClassPk}`);
            const tagClassDeleteButton = tagClassUi.find('div > button');
            if (tagClassDeleteButton.hasClass('negative')) {
                tagClassDeleteButton.removeClass('negative');
                changeLog.deletedTagClasses.delete(tagClassPk);
            } else {
                tagClassDeleteButton.addClass('negative');
                changeLog.deletedTagClasses.add(tagClassPk);
            }
        }

        /**
         * Upload the changes to server through JSON.
         */
        function save() {
            changeLog.deletedTags = Array.from(changeLog.deletedTags);
            changeLog.deletedTagClasses = Array.from(changeLog.deletedTagClasses);
            const changeLogJson = $('#changeLog-json');
            changeLogJson.val(JSON.stringify(changeLog));
            const changeLogSubmit = $('#changeLog-submit');
            changeLogSubmit.click();
        }


    </script>
{% endblock %}
```

In `csia/codestudy/templates/codestudy/index.html`:
```
{% extends "codestudy/base.html" %}
{% block content %}
    <div class="ui text container">
        <h1 style="text-align: center">Search in Code Study</h1>
        <form class="ui form" action="{% url 'codestudy:search' %}" method="get" autocomplete="off">
            <input autocomplete="false" name="hidden" type="text" style="display:none;">
            <div class="field">
                <div class="ui left icon input">
                    <i class="search icon"></i>
                    <input type="text" name="terms" placeholder="Search Terms">
                </div>
            </div>
            <div class="ui stacked segment">
                {% for tag_class in tag_classes %}
                    <div class="field">
                        <select class="ui fluid search dropdown" multiple id="select-{{ tag_class.pk }}"
                                name="{{ tag_class.name }}">
                            <option value="">{{ tag_class.name }}</option>
                            {% for tag in tag_class.tag_set.all %}
                                <option value="{{ tag.name }}">{{ tag.name }}</option>
                            {% endfor %}
                        </select>
                    </div>
                {% endfor %}
            </div>

            <button type="submit" class="ui fluid large teal button">Search</button>


        </form>
    </div>

{% endblock %}
{% block js %}
    <script>
        {% for tag_class in tag_classes %}
            $('#select-{{ tag_class.pk }}').dropdown();
        {% endfor %}
        $('#menu-search').addClass('active');

    </script>
{% endblock %}

```

In `csia/codestudy/templates/codestudy/admin.html`:
```
{% extends 'codestudy/base.html' %}
{% block title %}
    Admin Console | Code Study
{% endblock %}
{% block content %}

    <div class="ui text container">
        <h1 style="text-align: center">Admin Console</h1>
        <div class="ui segment">
            <div class="ui stackable grid">
                <div class="twelve wide column">
                    <h1>Edit User Permissions</h1>
                </div>
            </div>
            <table class="ui left aligned table">
                <tbody>
                {% for user in users %}
                    <tr id="user_row_{{ tag.pk }}">
                        <td>{{ user.name }} &lt{{ user.email }}&gt</td>
                        <td class="right aligned">
                            <div class="ui buttons">
                                {% for user_type in user.all_types %}
                                    <button id="{{ user_type|lower }}_button_{{ user.pk }}" class="ui button"
                                            onclick="mark('{{ user.pk }}', '{{ user_type|lower }}')">{{ user_type|title }}</button>
                                {% endfor %}
                            </div>
                        </td>
                    </tr>
                {% endfor %}
                </tbody>
            </table>

            <div class="ui right aligned grid">
                <div class="column">
                    <form method="post">
                        {% csrf_token %}
                        {% for user in users %}
                            {% for user_type in user.all_types %}
                                <input type="radio" id="{{ user_type|lower }}_radio_{{ user.pk }}" name="{{ user.pk }}"
                                       value="{{ user_type|lower }}" hidden>
                            {% endfor %}

                        {% endfor %}
                        <input id="changeLog-json" name="changeLog-json" hidden>
                        <button type="button" class="ui button" onclick="window.location.reload();">Cancel</button>
                        <button type="submit" class="ui teal button">Save</button>
                        <button type="submit" id="changeLog-submit" hidden></button>
                    </form>
                </div>
            </div>
        </div>
    </div>

{% endblock %}
{% block js %}
    <script>
        {% for user in users %}
            $('#{{ user.type_lower }}_radio_{{ user.pk }}').prop('checked', true);
            $('#{{ user.type_lower }}_button_{{ user.pk }}').addClass('active');
        {% endfor %}
        function mark(id, type) {
            $('#' + type + '_radio_' + id).prop('checked', true);
            {% for user_type in users.0.all_types %}
                $('#{{ user_type|lower }}_button_' + id).removeClass('active');
            {% endfor %}
            $('#' + type + '_button_' + id).addClass('active');
        }
    </script>
{% endblock %}
```

In `csia/codestudy/templates/codestudy/base.html`:
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.css">
    <meta name="google-signin-client_id"
          content="330093561618-bc6pprilkfqi5sc6oibm376psnfe9tub.apps.googleusercontent.com">
    <link rel="shortcut icon" type="image/png" href="{% static 'favicon.ico' %}"/>
    <style>
        html, body {
            height: 100%;
            margin: 0;
        }

        .wrapper {
            min-height: 100%;

            /* Equal to height of footer */
            /* But also accounting for potential margin-bottom of last child */
            margin-bottom: -62px;
        }

        .footer {
            height: 48px;
            margin-top: 14px;
        }
        .push {
            height: 62px;
        }
    </style>
    <title>{% block title %}Code Study{% endblock %}</title>
</head>
<body>
<div class="wrapper">
    <div class="content">
        <div class="ui menu">
            <div class="header item"><a href="{% url 'codestudy:index' %}" style="color: black">Code Study</a></div>
            <a class="item" id="menu-search" href="{% url 'codestudy:index' %}">Search</a>
            {% if user.can_edit %}
                <a class="item" id="menu-add-paper" href="{% url 'codestudy:add-paper' %}">Add Paper</a>
                <a class="item" id="menu-edit-tags" href="{% url 'codestudy:edit-tags' %}">Edit Tags</a>
            {% endif %}
            {% for tag_class in tag_classes %}
                <div id="menu-{{ tag_class.pk }}" class="ui dropdown item">
                    {{ tag_class.name }}
                    <i class="dropdown icon"></i>
                    <div class="menu">
                        {% for tag in tag_class.tag_set.all %}
                            <a class="item"
                               href="{% url 'codestudy:browse' tag_class.name tag.name %}">{{ tag.name }}</a>
                        {% endfor %}
                    </div>
                </div>
            {% endfor %}
            <a class="item" id="menu-all-papers" href="{% url 'codestudy:all-papers' %}">All Papers</a>
            <div class="right menu">
                {% if user.pk %}
                    <div id="user-info" class="ui dropdown item">
                        {{ user.name }}
                        <i class="dropdown icon"></i>
                        <div class="menu">
                            <a class="item" href="{% url 'codestudy:bookmarked' %}"><i class="star icon"></i>Bookmarked
                                Papers</a>
                            {% if user.is_admin %}
                                <a class="item" href="{% url 'codestudy:admin' %}"><i class="edit icon"></i>Admin
                                    Console</a>
                            {% endif %}
                            <a class="item" onclick="logout()"><i class="sign-out icon"></i>Log out </a>
                        </div>
                    </div>
                {% else %}
                    <a id="loginBtn" class="item">
                        Sign In with Google
                    </a>
                {% endif %}
            </div>
        </div>

        {% if message %}
            <div class="ui text container">
                <div class="ui message">
                    <div class="header">{{ message.title }}</div>
                    <p>
                        {{ message.description }}
                    </p>
                </div>
            </div>
        {% endif %}
        {% block content %}
        {% endblock %}
        <div class="push"></div>
    </div>
</div>
<footer class="footer">
    <div class="ui footer segment">
        <div class="ui center aligned container">
            <div class="ui horizontal small divided link list">
                <a class="item" href="https://de0ch.mit-license.org/" target="_blank">Free &amp; Open Source
                    (MIT)</a>
                <a class="item" href="https://github.com/DE0CH/csia" target="_blank">Source Code on Github</a>
            </div>
        </div>
    </div>
</footer>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW"
        crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.js"></script>
<script src="https://apis.google.com/js/api:client.js"></script>
<script>
    {% for tag_class in tag_classes %}
        $('#menu-{{ tag_class.pk }}').dropdown();
    {% endfor %}
    $('#user-info').dropdown();

    function logout() {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', '{% url 'codestudy:logout' %}');
        xhr.onload = () => {
            location.reload();
        };
        xhr.send();
    }

    function sendIdToken(idToken) {
        var xhr = new XMLHttpRequest();
        xhr.open('POST', "{% url 'codestudy:login' %}");
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onload = function () {
            const response = JSON.parse(xhr.responseText);
            location.reload();
        };
        xhr.send('id-token=' + idToken + '&csrfmiddlewaretoken=' + '{{ csrf_token }}');

    }

    gapi.load('auth2', function () {
        // Retrieve the singleton for the GoogleAuth library and set up the client.
        const auth2 = gapi.auth2.init({
            client_id: '330093561618-bc6pprilkfqi5sc6oibm376psnfe9tub.apps.googleusercontent.com',
            cookiepolicy: 'single_host_origin',
            // Request scopes in addition to 'profile' and 'email'
            //scope: 'additional_scope'
        });
        const element = document.getElementById('loginBtn');
        auth2.attachClickHandler(element, {},
            function (googleUser) {
                const id_token = googleUser.getAuthResponse().id_token;
                sendIdToken(id_token)
            }, function (error) {
                console.log(error);
            });
    });
</script>
{% block js %}
{% endblock %}
</body>
</html>
```

In `csia/codestudy/templates/codestudy/add-paper.html`:
```
{% extends "codestudy/base.html" %}
{% block title %}
    Add Paper | Code Study
{% endblock %}
{% block content %}
    <div class="ui text container">
        <h1 style="text-align: center">Add Paper to Code Study</h1>
        <div class="ui form">
            <form method="post" autocomplete="off">
                <input autocomplete="false" name="hidden" type="text" style="display:none;">
                {% csrf_token %}
                <div class="field">
                    <div class="ui left icon input">
                        <i class="sticky note icon"></i>
                        <input type="text" name="title" placeholder="Title">
                    </div>
                </div>
                <div class="field">
                    <div class="ui left icon input">
                        <textarea rows="3" type="text" name="description" placeholder="Description"></textarea>
                    </div>
                </div>
                {% for tag_class in tag_classes %}
                    <div class="field">
                        <select class="ui fluid search dropdown" multiple id="select-{{ tag_class.pk }}"
                                name="{{ tag_class.pk }}">
                            <option value="">{{ tag_class.name }}</option>
                            {% for tag in tag_class.tag_set.all %}
                                <option value="{{ tag.pk }}">{{ tag.name }}</option>
                            {% endfor %}
                        </select>
                    </div>
                {% endfor %}

                <div class="field">
                    <div class="ui grid middle aligned">
                        <div class="ui four wide column">
                            <select class="ui fluid dropdown" name="upload-option" id="upload-option">
                                <option value="">Upload Method</option>
                                <option value="1">File</option>
                                <option value="2">Link</option>
                            </select>
                        </div>
                        <div class="ui twelve wide column">
                            <input type="file" name="pdf" id="pdf" accept=".pdf">
                            <input type="text" name="link" id="link" placeholder="Link" hidden>
                        </div>
                    </div>

                </div>
                <input type="text" name="pdf-key" id="pdf-key" hidden>
                <button type="button" class="ui fluid large teal button" id="fake-submit" onclick="fs()">Add</button>
                <button type="submit" id="submit" hidden></button>
            </form>
            <div class="ui teal progress" id="progress-bar" style="display:none;">
                <div class="bar"></div>
                <div class="label">Uploading</div>
            </div>

        </div>
    </div>
    <form method="get" action="{% url 'codestudy:presign-s3' %}" hidden>
        <input type="text" id="file-name" name="file-name">
    </form>
{% endblock %}
{% block js %}
    <!--suppress JSUnfilteredForInLoop -->
    <script>
        const bar = $('#progress-bar');
        bar.progress({
            value: 20,
            total: 200,
        });
        $('#menu-add-paper').addClass('active');
        {% for tag_class in tag_classes %}
            $('#select-{{ tag_class.pk }}').dropdown();
        {% endfor %}
        const uploadOptionsSelect = $('#upload-option');
        const uploadOptionsEnum = Object.freeze({
            'file': 1,
            'link': 2,
        });
        let uploadOption = uploadOptionsEnum.file;
        const pdf = $('#pdf');
        const link = $('#link');
        const form = $('.ui.form');
        uploadOptionsSelect
            .dropdown({
                onChange: function (value, text, $selectedItem) {
                    uploadOption = Number(value);
                    if (uploadOption === uploadOptionsEnum.file) {
                        pdf.removeAttr('hidden');
                        link.attr('hidden', 'hidden');
                        form.form({
                            fields:
                                {
                                    title: 'empty',
                                    description: 'empty',
                                    pdf: 'empty',
                                }
                        });
                    } else if (uploadOption === uploadOptionsEnum.link) {
                        pdf.attr('hidden', 'hidden');
                        link.removeAttr('hidden');
                        form.form({
                            fields:
                                {
                                    title: 'empty',
                                    description: 'empty',
                                    link: 'empty',
                                }
                        });
                    } else {
                        console.assert(false, "Upload Option does not match any known type");
                    }
                }
            })
        ;
        uploadOptionsSelect.dropdown('set selected', uploadOptionsEnum.file);


        let uploaded = false;

        /**
         * A click handler function for submitting submitting the form.
         */
        async function fs() {
            const submit = $('#submit');
            if (uploaded || !form.form('is valid') || uploadOption === uploadOptionsEnum.link) {
                submit.click();
                return;
            }
            $('#fake-submit').css('display', 'none');
            bar.css('display', 'block');
            const s3Data = await getS3Data(pdf.val().replace(/C:\\fakepath\\/i, ''));
            let fileName = await uploadFile(pdf.prop('files')[0], s3Data);
            $('#pdf-key').val(fileName);
            pdf.val(null);
            form.form({});
            uploaded = true;
            submit.click();
        }

        /** This gets the presigned data from the server in order for the browser to upload, and returns a Promise
         * of the data.
         * @param {string} fileName The file name of the file to be uploaded. Used as part of the presigned signature.
         * @return {Promise<Object>} The presigned S3 data.
         */
        function getS3Data(fileName) {
            return new Promise((resolve, reject) => {
                const url = "{% url 'codestudy:presign-s3' %}?" + $.param({file_name: fileName});
                $.get(
                    url,
                    data => resolve(data)
                )
            });
        }

        /**
         * Upload the given file to the S3 bucket.
         * @param {File} file The file to be uploaded.
         * @param {Object} s3Data The presigned S3 data.
         * @return {Promise<string>} The object key in the S3 bucket.
         */
        function uploadFile(file, s3Data) {
            return new Promise(resolve => {
                let xhr = new XMLHttpRequest();
                xhr.open('POST', s3Data.url);
                let postData = new FormData();
                for (const key in s3Data.fields) {
                    postData.append(key, s3Data.fields[key]);
                }
                postData.append('file', file);
                xhr.upload.addEventListener('progress', function (e) {
                    // Percentage of upload completed
                    bar.progress({
                        value: e.loaded,
                        total: e.total,
                    });
                });
                xhr.onreadystatechange = () => {
                    if (xhr.readyState === 4 && (xhr.status === 200 || xhr.status === 204)) {
                        resolve(s3Data.fields.key);
                    }
                };
                xhr.send(postData);
            });
        }
    </script>
{% endblock %}
```

In `csia/codestudy/templates/codestudy/500.html`:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.css">
    <link rel="shortcut icon" type="image/png" href="/static/favicon.ico">
    <title>Code Study</title>
</head>
<body>
<div class="ui menu">
    <div class="header item"><a href="/" style="color: black">Code Study</a></div>

</div>

    <div class="ui text container">
        <div class="ui message">
            <div class="header">500 Server Error</div>
            <p>
                Something went wrong. Please try again later.
            </p>
        </div>
    </div>

</body>
</html>
```

In `csia/codestudy/templates/codestudy/login.html`:
```
{% extends 'codestudy/base.html' %}
{% block content %}
    <div class="ui center aligned text container">
        <h1 style="text-align: center">Log in</h1>
        <div class="ui g-signin2" data-width="auto" data-longtitle="true"></div>
    </div>

{% endblock %}
{% block js %}
{% endblock %}
```

In `csia/codestudy/templates/codestudy/results.html`:
```
{% extends "codestudy/base.html" %}
{% load codestudy_tags %}
{% block title %}
    {{ page_title }} | Code Study
{% endblock %}
{% block content %}
    <div class="ui container">
        {% if not papers %}
            <div class="ui text container">

                <div class="ui message">
                    <div class="header">Nothing to Show</div>
                    <p>
                        There is nothing in the database that matches your search.
                    </p>
                </div>
            </div>
        {% endif %}
        <div class="ui three column stackable grid">
            {% for paper in papers %}
                <div class="column">
                    <div class="ui fluid special card">
                        <div class="blurring dimmable image">
                            <div class="ui dimmer transition hidden">
                                <div class="content">
                                    <div class="center">
                                        {% if paper.pdf %}
                                            <a class="ui inverted button" href="{{ paper.pdf.url }}">Open PDF</a>
                                        {% endif %}
                                    </div>
                                </div>
                            </div>
                            {% if paper.png %}
                                <img src="{{ paper.png.url }}" alt="{{ paper.title }}">
                            {% endif %}
                        </div>
                        <div class="content ">
                            {% if paper.link %}
                                <a class="header" href="{{ paper.link }}">{{ paper.title }}</a>
                            {% elif paper.pdf %}
                                <a class="header" href="{{ paper.pdf.url }}">{{ paper.title }}</a>
                            {% endif %}
                            <div class="description">
                                <p>{{ paper.description }}</p>
                            </div>
                        </div>
                        {% if paper.nested_tag_names %}
                            <div class="content">
                                <div class="description">
                                    {% for tag_class, tags in paper.nested_tag_names.items %}
                                        <p><b>{{ tag_class }}</b>: {{ tags|join:', ' }}</p>
                                    {% endfor %}
                                </div>
                            </div>
                        {% else %}
                            <div class="content">
                                <div class="description">
                                    No tag added
                                </div>
                            </div>
                        {% endif %}
                        {% if user %}
                            <div class="content">
                                <div class="ui two column grid middle aligned">
                                    <div class="column">
                                        {% if user.can_edit %}
                                            <a class="ui small teal button"
                                               href="{% url 'codestudy:edit-paper' paper.pk %}">Edit</a>
                                        {% endif %}
                                    </div>
                                    <div class="column right aligned">
                                        <i class="star icon {% if not paper|is_bookmarked:user %}outline{% endif %}"
                                           id="like-{{ paper.pk }}"
                                           onclick="like('{{ paper.pk }}')"></i>Bookmark
                                    </div>
                                </div>
                            </div>
                        {% endif %}
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
{% endblock %}
{% block js %}
    <script>
        {% if all_papers %}
            $('#menu-all-papers').addClass('active');
        {% endif %}
        $('.special.card .image').dimmer({
            on: 'hover'
        });

        function like(pk) {
            const likeBtn = $('#like-' + pk);
            const xhr = new XMLHttpRequest();
            xhr.open('GET', '{% url 'codestudy:bookmark' %}?pk=' + pk);
            xhr.send();
            if (likeBtn.hasClass('outline')) {
                likeBtn.removeClass('outline');
            } else {
                likeBtn.addClass('outline');
            }
        }
    </script>
{% endblock %}
```

In `csia/codestudy/templates/codestudy/edit-paper.html`:
```
{% extends 'codestudy/base.html' %}
{% block title %}
    Edit Paper
{% endblock %}
{% block content %}
    <div class="ui text container">
        <h1 style="text-align: center">Edit Paper {{ paper.title }}</h1>
        <div class="ui form">
            <form method="post" autocomplete="off">
                <input autocomplete="false" name="hidden" type="text" style="display:none;">
                {% csrf_token %}
                <div class="field">
                    <div class="ui left icon input">
                        <i class="sticky note icon"></i>
                        <input type="text" name="title" placeholder="Title" value="{{ paper.title }}">
                    </div>
                </div>
                <div class="field">
                    <div class="ui left icon input">

                        <textarea rows="3" name="description"
                                  placeholder="Description">{{ paper.description }}</textarea>
                    </div>
                </div>
                {% for tag_class in tag_classes %}
                    <div class="field">
                        <select class="ui fluid search dropdown" multiple id="select-{{ tag_class.pk }}"
                                name="{{ tag_class.pk }}">
                            <option value="">{{ tag_class.name }}</option>
                            {% for tag in tag_class.tag_set.all %}
                                <option value="{{ tag.pk }}">{{ tag.name }}</option>
                            {% endfor %}
                        </select>
                    </div>
                {% endfor %}
                <div class="field">
                    <button type="button" id="d" class="ui fluid large button" onclick="markDelete()"><i
                            class="trash icon"></i></button>
                </div>
                <input type="checkbox" id="delete" name="delete" value="on" hidden>
                <button type="submit" id="submit" class="ui fluid large teal button">Update</button>
            </form>
            <div class="ui teal progress" id="progress-bar" style="display:none;">
                <div class="bar"></div>
                <div class="label">Uploading</div>
            </div>

        </div>
    </div>

{% endblock %}
{% block js %}
    <script>
        let tags = [];
        {% for tag in paper.tags.all %}
            tags.push("{{ tag.pk }}");
        {% endfor %}
        console.log(tags);
        {% for tag_class in tag_classes %}
            $('#select-{{ tag_class.pk }}').dropdown('set selected', tags);
        {% endfor %}
        function markDelete() {
            const d = $('#d');
            const deleteMark = $('#delete');
            if (deleteMark.is(':checked')) {
                deleteMark.prop('checked', false);
                d.removeClass('red');
            } else {
                deleteMark.prop('checked', true);
                d.addClass('red');
            }
        }
    </script>
{% endblock %}
```

In `csia/main/__init__.py`:
```

```

In `csia/main/settings.py`:
```
"""
Django settings for home project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import django_heroku
import dotenv


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "iNZc97keQtytmd7x82q9zqBBzX6ZA8sKH8QpncbbqtfsTdRBA9dxAYmCLXQMPAhb"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'FALSE') == 'TRUE'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "codestudy",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]


WSGI_APPLICATION = "main.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE" : "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3")
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# S3 Integration
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'codestudy'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_EXPIRE = 300
AWS_S3_REGION_NAME = 'ap-east-1'

G_CLIENT_ID = '330093561618-bc6pprilkfqi5sc6oibm376psnfe9tub.apps.googleusercontent.com'

DEFAULT_FILE_STORAGE = 'main.storage_backends.MediaStorage'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = "/static/"

if os.getenv('IS_LOCAL', 'FALSE') != 'TRUE':
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True

django_heroku.settings(locals())

```

In `csia/main/urls.py`:
```
from django.urls import path, include
from codestudy import views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path('', include('codestudy.urls'))
]

handler404 = views.handler404
handler500 = views.handler500
handler403 = views.handler403
handler400 = views.handler400

```

In `csia/main/storage_backends.py`:
```
from abc import ABC
from storages.backends.s3boto3 import S3Boto3Storage
from utils import generate_presigned_url


class MediaStorage(S3Boto3Storage, ABC):

    def url(self, name, parameters=None, expire=None, http_method=None):
        if expire is None:
            expire = 3600
        response = generate_presigned_url(name, 600)
        return response


```

In `csia/main/wsgi.py`:
```
"""
WSGI config for home project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

```






## Meeting #1 Transcript

The transcript is reconstructed from shorthand notes.

Q: What is the website you want to build?

A: For the subject Psychology, we usually need to cite a lot of studies for the exam and research papers. I want to build an app that students can use to search through a database of studies that are made available by the IB and some studies that are selected by the teachers. I want to make it like the housing search, where you have different options for the search and it would return the relevant result. There are also three ways you can search, by approach, by topic and by key words.

Q: Do you have a similar website that I can use as an example?

A: Yes. It is at [https://www.squarefoot.com.hk/租樓/](https://www.squarefoot.com.hk/%E7%A7%9F%E6%A8%93/). If you go look you will see it's a catalogue for the housing in Hong Kong, you can get a lot of search terms for the housing in Hong Kong, like the price, the location. I want to make something similar for psychology studies.

Q: What is inadequate about the current search engine? 

A: Right now the search engine only searches the key words that are present in the papers themselves, not the ones that are inferred, also it only takes into account the key words that the author tagged, which might not be the same key words that are useful for the IB subject. In addition, the set of paper that are in its database is much larger than the ones that are needed for the IB, so the results are not as relevant. 

Q: Is a modern user interface important to you? Or are you okay with however it looks as long as it gets the job done?

A: A good user interface is not that important as long as it's usable. Definitely function over the user interface. 

Q: How fast does the search need to be? Does it need to return result within a second? 

A: I would say the faster the better, but it is fine if it takes somewhere around 10 seconds or even to a minute because searching otherwise like through Google Drive and other search engine would definitely take more than a minute. 

Q: How large is the set of all the all the studies that need to be on the database? 

A: There should be around 100 studies.

Q: Does the database need to updated? If so, how often? 

A: Roughly once in three months. I need to update the papers as new papers come out or IB uses some that were not previously used before. 

Q: Would you want the data to be linked to a Google Drive file or directly stored in the website. I need to know this because there are two types of configuration [technically: I need to know if I need to use S3], one with a larger database capable of storing media like PDFs and preview images, the other is smaller such that it can only store some text. 

A: Umm... I think a website that can give preview of the studies will be nice. It really depends on how you want to do it. If you want to link it back to a link in the Google Drive because it's easier it's find, but I hope that the students can see the first page of the study as a preview because that is the best for students. Especially when send them the PDFs on class, they see the first page of the PDF so it's easier for them to recognize the paper if they just see the first page. 

Q: How would you like the sign in to work? Sign in with Google or sign in with email and password?

A: Sign in with Google if that is not too difficult for you to implement. Because then I can just click on one button without having to worry about remembering  and typing in the password. 

Q: Would you just want you or all teachers to be able to access the edit page?

A: Just me is fine, but I also want to be able to add some students' email so they can add the papers in for me. They cannot add other students tho obviously. The changes also need to go through me before they can published on the database. I would also want the ability to add other teachers as admins, who are able to add and remove students' account.

## Meeting #2 Transcript
The transcript is reconstructed from shorthand notes.

Q: I have just sent you the link to the website, I just want to hear if it is something you are visioning. 

A: Yes that is exactly what I wanted. Although there is one problem, I would want students to be able to choose multiple topics and approaches. Because one study might have more than one tag, I want them to be able to choose multiple tags they want to search for. 

Q: Did I get all the tags that you need?

A: Not really. There are also ethics, experimental methods, and options. I'll send you a list of them soon. Then once you are done I can get the students to add the tags and organize the papers. It would also be good revision exercise as well.

## Meeting #3 Transcript
The transcript is reconstructed from shorthand notes.

Q: What do you think of the product? Have you had a chance to give it a try?

A: Yes. I think it's amazing. I can definitely use this for my class. 

Q: Is this product the same as what you have visioned? Is there anything else that I need to add to make it better?

A: It does everything I wanted it to do. I am really satisfied with the product. I don't think there's many other improvements that I need to make. 

Q: Here are the success criteria I have set for the product (hands her a printed list). Do you think the product has met all of them?

A: (looks at the list) I think so. It's quite a completed product.

Q: That's good to hear. But I need some "improvements" for IB grades, could you think of some. It can be anything because I am not going to implement them. 

A: (laughs) Sure. Let's see... Oh, you could have another info page when I click into a card that displays the unit and criteria the paper is associated to, and you can click on the topics that it associates with and go further into that. It will help students to find more resources.
