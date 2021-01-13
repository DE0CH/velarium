# Crit B

# Use Cases

### Iteration 1

### Iteration 2
The client feedback that she would like to use the help of students to manage some paper for her but would not want them to change who can edit the papers. Therefore I have decided to refactor the user into three groups: standard, editor and admin. Standard users can only view the website and bookmark for themselves, editors can, in addition, add, edit and remove papers, and admin can, in addition, manage the permissions of users. 

### Iteratioion 3
![Landing Page Iteration 3](img/landing%20page%20iteration%203.png)
\

I have added a header to navigate to different functions of the web app, and designed a favicon for the website.

# UML

# Mockup

## Landing Page
This is the page that the user first sees when he/she open the application. It presents them options for their search. Layout is powered by Bootstrap.

### Iteration 1
![Landing Page Iteration 1](img/landing%20page%20iteration%201.png)
\

### Iteration 2
![Landing Page Iteration 2](img/landing%20page%20iteration%202.png)
\

After the first iteration, the client game me feedback that she would want to be able to select multiple topic and approaches for each search box. After I have found no way to implement it with Bootstrap and I didn't want to write UI from scratch because it will inevitably look ugly, I found out that I could use a framework called Semantic UI.

### Iteration 3
![Landing Page Iteration 3](img/landing%20page%20iteration%203.png)
\

In this iteration, I have added a navigation bar and a sign in with Google option. 

## Results Page

### Iteration 1
![Results Page Iteration 1](img/results%20page%20iteration%201.png)
\

This is the page where users get their search results in these card-like info boxes, from which they can see the results. 

### Iteration 2
![Results Page Iteration 2](img/results%20page%20iteration%202.png)
\

This iteration is unchanged in principle compared with the first iteration, but since I changed the framework, the design looks different.

## Edit Tags Page
This page is used to add and delete tag and tag groups in the database.

### Iteration 1
![Edit Tags Page Iteration 1](img/edit%20tags%20page%20iteration%201.png)
\

# Design Description
The program is entirely based on the web, part of the functionality will be accomplished through JS running on client's computer, but a core part of the program will be accomplished through back-end code in Python running on Heroku and storage stored in AWS S3.  The UI will be rendered using client's web browser


# Class Dictionary




### Properties

This class does not have any property.

## Class - Paper
This class represents a paper stored in the database

### Iteration 1
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

### Iteration 2
|Property Name|Signature         |Description                                                                                                                |
|-------------|------------------|---------------------------------------------------------------------------------------------------------------------------|
|title        |title:String      |This is the title of the pape that the user inputs, short and direct.                                                      |
|description  |description:String|This is the description of the paper that the user inputs. It can be used as a abstract of the paper.                      |
|tags         |tags: String[]    |This returns the tags that the paper is associated with through manual assignment or automatic detection by the classifier.|
|pdf          |pdf: File         |This stores the pdf of the paper                                                                                           |
|png          |png: File         |This stores the screenshot of the first page to be displayed on the results page.                                          |
|text         |text: String[]    |This is the content of the paper, extracted in plain text form to increase the search speed.                               |

I realised that the user wants more flexibility to add and remove tag that I cannot foresee during development, so I've generalized the class to allow for more flexibility.

### Methods
This class does not have any method.

## Class - Search Engine

This is an API for interacting with the search engine that returns the paper given some phrases. The implementations of the methods are not shown here. It might be implemented with the Google Search Engine or one that I write myself. A search engine is algorithm-based, therefore it's difficult to break it down into smaller methods. 
