Simple Web
=================
![ch.PNG](images/ch.PNG)

We are given a web page:

![page.PNG](images/page.PNG)

Regardless the box is checked or not we get:

![notauth.PNG](images/notauth.PNG)

First step that comes in mind is getting a look at the html-form in the source code:

![source.PNG](images/source.PNG)

Here we see a hidden input called "auth" with a value set to 0. Just by setting it to 1 and hitting the checkbox and the Submit button we get the flag:

![flag.PNG](images/flag.PNG)
