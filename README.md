# Tivix-Coding-Task

 Creating a blogging application using Django Framework
 -----------------------------------------------------------
 
 What does this application do?
 * Lists all the exsiting posts, latest post being the first.
 * Creates a new post by clicking create button on the top right corner of the home page.
 * Edits the post by clicking on the post and then click the edit button on the top right corner.
 * Full details of the post:title, description and date.
 
 Implementation details:
 ------------------------------------------------------------
 
* Used Django framework to handle requests.                                                                              
* Used Bootstrap to style the web pages.
* Used converage tool for measuring code coverage.
* Used Django forms to create a form for new post.
* Used sqlite database to store all the posts.
 
 Testing details:
 -------------------------------------------------------------
 
I performed blackbox testing and unit testing on this application. As a user, I used the application to create, edit, list the posts. I have written unit test cases to test the functionality of all the components. There are two files: tests_views.py and tests_models.py which are related to tests. I used Client() from django.test to simulate as a user. With that client, I have tested the functions in views.py . 
 
Code coverage:
-------------------------------------------------------------

To measure code coverage, I used converage tool which I tried for the first time and I liked it. My code achieved a coverage of ** 88% ** overall.
 
 Documentation: 
 -------------------------------------------------------------
 All files are well documented. I have writted comments for each function to get an idea about it.

