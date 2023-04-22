# Leabhar Maith


## Introduction
  
<br>    


This is a README for an e-commerce website for a hypothetical business called 'Leabhar Maith', meaning 'good book' in Irish. 
Leabhar Maith is a business to customer (B2C) e-commerce site, selling literary products to the user, namely books written in English and Irish by Irish authors. The deliverables will expand in future to include journals, paperweights and stationary with an Irish literary theme. Customers sign up to create an online account and pay via single payments using Stripe. 


Features of this business-focused website include a shopping cart, a catalogue of products that is curated and updated quarterly and is searchable by author or title, an online payment system that can save the customer’s preferred mode of payment, a quarterly email newsletter sign-up, and a featured product every season from a different boutique manufacturer, which comes free with no extra postage fee when the customer spends €70. 


The site was developed using Python in the Django framework and styled using CSS and Bootstrap. ElephantSQL is used for the database and Heroku for deployment. 


'Leabhar Maith' means 'good book' in Irish.


<br>

![mock-up of site on different sized devices](assets/images/amiresponsive.png)

<br>

## Contents


* [User Experience R&D](#User-Experience,-Research-and-Design)
    * [Strategy](#Strategy)
    * [Scope](#Scope)
    * [Structure](#Structure)
    * [Skeleton](#Skeleton)
    * [Surface](#Surface)
* [Web Marketing Strategy](#Web-Marketing-Strategy)
* [Features](#Features)
* [Data Model](#Data-Model)
* [Testing](#Testing)
* [Deployment](#Deployment)
* [Credits, Sources & Acknowledgements](#Credits,-Sources-&-Acknowledgements)


<br>


## User Experience, Research and Design
<br>


I looked at a range of online bookshops, most of which constituted the online presence of a physical shop or chain of shops, such as Waterstones (https://www.waterstones.com/), Easons (https://www.easons.com/) or my local favourite, Vibes and Scribes (https://www.vibesandscribes.ie/). The book industry in Ireland is one where smaller, one-off independent bookshops do not necessarily have a web presence at all, such as my closest bookshop in East Cork, Midleton Books (it does have a Facebook page at: https://www.facebook.com/midletonbooks/). On the other hand, the Book Depository (owned by Amazon) offers free delivery in Ireland, practically every book going, but no physical shop at all (https://www.bookdepository.com/).

<br>

Given the impersonal e-commerce feel of many online bookshops, even those that are linked to a physical shop well grounded in a local area, such as Vibes & Scribes, I wanted to create an alternative that brings a personal feel to online book shopping. Rather like a friendly and knowledgable bookshop owner or assistant, Leabhar Maith offers a curated selection of up to eight books per quarter, recommended by the site owner. The selection changes every four months, with the seasons, so that there is a Spring selection of books, a Summer collection, and so on, bringing a dash of fashion-industry excitement to the concept of new collections being revealed, as well as an ancient feel of Ireland’s connection with the land. Past selections and the books in them can still be accessed and purchased by the site user. There's also the feeling of a book-club to the site, a little like the Guardian bookshop, which is linked to books featured in the Guardian and has a book-club subscription. Subscriptions would be an obvious idea for a future feature of this business. There is a newsletter sign-up that connects the user with new offers and reviews, some of which will eventually be written by selected Leabhar Maith readers. Readers are 'at home' with Leabhar Maith, and can contribute and feel part of it.


Even though Leabhar Maith offers a sense of belonging for the buyer, where there is a feeling of familiarity and friendliness rather than anonymity, users may make purchases in guest-mode. 

<br>

### **Strategy**

<br>

**An Agile Approach**

<br>


Despite being in a team of... one... I used an Agile approach to designing, planning and developing the site. Well, actually, I did get together with another software engineering student from a software testing course, and we pretended we were in a work-place team for the testing of features. We communicated via the ‘issues’ comments on the GitHub project for Leabhar Maith, and this can be seen on the details for each issue/ user-story/ feature-needed-docket. He taught me some of the terminology used for software testing, and we use this in the comments, which was great! 


The first step was to gather the  user stories and record them using  GitHub project tools. An MVP (Minimum Viable Product) was then designed around the requirements that most directly met the needs of each user story. These were then attached to iterations that were time-boxed using the ‘milestones’ feature in GitHub. The list of milestones/ iterations is located at: https://github.com/farah-maria/LeabharMaith/milestones and can be viewed in proper order according by due date at:


https://github.com/farah-maria/LeabharMaith/milestones?direction=asc&sort=due_date&state=open

<br>
<center><img src="assets/images/iterations.png" alt="iterations 1-4" width="80%"/></center>
<br>   

Note: issues were not closed using the tick box, but by placing them in the ‘done’ column on the kanban board, so it appears that none of the iterations were completed if judged by the percentage bar. A comment in each states its completion, though.


All of these points, as well as  their testing status, were organised using a kanban board in GitHub. This is called ‘Leabhar Maith Kanban Board’ and it is located at:


https://github.com/users/farah-maria/projects/6/


<br>
<center><img src="assets/images/kanban.png" alt="kanban board" width="80%"/></center>
<br>   

The scope of the project can be seen on the board, which I mainly limited to MVP requirements, each of which correlate with the Code Institute pass criteria for the project. 

<br>

### **Scope**

<br>
The project specification outlining the scope of Leabhar Maith is, in this case, necessarily defined by Code Institute marking criteria. It is roughly described as follows:
<br>
Project purpose:
<br>
In this project, you'll build a Full-Stack site based on business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.
<br>
You will also need to create a dummy social media product page as part of your marketing strategy, a newsletter sign-up and SEO.  
<br>
The site owner, logging in as a particular user, should be able to see a list of all their past orders.
<br>
Your site should be a Full Stack Web application that incorporates Authentication and role-based Authorisation functionality.
<hr>
<br>
As shown later in this document, there is a Facebook business page for Leabhar Maith, where news and discounts are aimed at growing the pool of potential site users.
<br>

I used the ‘issues’ feature in GitHub to create a list of features necessary to meet the MVP outlined above. GitHub labels were used to order these according to priority, using the MoSCoW method..

<br>

*	Must have
*	Should have
*	Could have (in the future => future features for another iteration)
*	Will not have

<br>

The list of issues used to fill the kanban board can be found at: 


https://github.com/farah-maria/LeabharMaith/issues

<br>

A list of user stories can be found at:


https://github.com/farah-maria/LeabharMaith/issues?q=is%3Aopen+is%3Aissue+label%3A%22USER+STORY%22

<br>
By clicking on a user story heading, the full user story can be accessed with its attached list of functionalities and testing notes.
<br>

Each user story was listed as an ‘issue’, and this was connected via the comments to a list of features needed to fulfil the needs voiced by the story. All aspects of the project associated with the Pass criteria supplied by the Code Institute were labelled ‘Must have’ for the MVP, and these were prioritised by me over all other issues.

<br>

Due to time constraints, certain features were not included in the scope of this project, and none of these are in the ‘Must have’ category. 

<br>

•	I was not able to prioritise descriptive and easy to understand/ short links for the images used on the site, though this doesn’t make any difference on the user experience and user interface side of things, other than the fact that it affects SEO and therefore a potential user is slightly less likely to find the website on Google. (Labelled ‘Will not have’ in Github issues.)

<br>

•	I was not able to prioritise connecting up the email validation for successful transactions on the site, which would have provided the user with a  receipt. They do, however, receive feedback in the form of a pop-up message to say whether or not their payment was successful. 

<br>

Certain features which went above and beyond the MVP list of ‘must-haves’  were included in the scope of this project...

<br>

•	A submittable contact form was included on  a ‘contact us’ page, with a pop-up message that provides validation for the success/ failure of the message being sent. These messages can be accessed via the admin panel when super user credentials are used to log-in. (This was labelled ‘Could have’) 

<br>

•	Three easy to use forms are available for shop staff to enter, delete, read and edit all records relating to stock. These options can be viewed by the ‘my account’ option in the navigation bar when super user credentials are used to log-in. Only one back-end form was required by examiners for this project, but only one form would not have added enough functionality to extend to the featured products sold on the site as well as the books and the authors. 

<br>

All  user stories relating to ‘Must have’ functionalities, which defined the scope of this project, can be found at:

https://github.com/farah-maria/LeabharMaith/issues?q=is%3Aopen+is%3Aissue+label%3A%22MUST+HAVE%22+label%3A%22USER+STORY%22



