# Leabhar Maith


## Introduction
  
<br>    


This is a README for an e-commerce website for a hypothetical business called 'Leabhar Maith', meaning 'good book' in Irish. 


Leabhar Maith is a business to customer (B2C) e-commerce site, selling literary products to the user, namely books written in English and Irish by Irish authors. The deliverables will expand in future to include journals, paperweights and stationary with an Irish literary theme. Customers sign up to create an online account and pay via single payments using Stripe. 


Features of this business-focused website include a shopping cart, a catalogue of products that is curated and updated quarterly and is searchable by author or title, an online payment system that can save the customer’s preferred mode of payment, a quarterly email newsletter sign-up, and a featured product every season from a different boutique manufacturer, which comes free with no extra postage fee when the customer spends €70. 


The site was developed using Python in the Django framework and styled using CSS and Bootstrap. ElephantSQL is used for the database and Heroku for deployment. 


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
* [Entity Relationship Diagram](#Entity-Relationship-Diagram)
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
<br>

**Project purpose:**

<br>
<em>In this project, you'll build a Full-Stack site based on business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.
<br>
<br>
You will also need to create a dummy social media product page as part of your marketing strategy, a newsletter sign-up and SEO.  
<br>
<br>
The site owner, logging in as a particular user, should be able to see a list of all their past orders.
<br>
<br>
Your site should be a Full Stack Web application that incorporates Authentication and role-based Authorisation functionality.</em>
<br>
<br>
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

<br>

####  Summary of Main In-Scope Features:
<br>

* Responsive navigation bar with product search, dropdown menu with book categories, user account access, registration option, and special dropdown list from navbar for shop staff/ superusers who want to edit/ add/ delete stock.
<br>

* A shopping basket to add books to or edit contents/ delete contents.
<br>

* Checkout page that’s easy-to-edit and retains products between visits.
<br>

* Basic information about the business on an ‘about us’ page.
<br>

* Registration option,  with editable data for delivery address and contact details. Profile page on 
‘my account’ shows the customer’s order history and saved of delivery and contact info.

<br>

* Users can receive info on books and upcoming collections through signing up to the newsletter.
<br>

* Free delivery on orders over 50 EUR.
<br>

* Free ‘featured product of the season’ sent out to customers making a purchase of 70 EUR or more. 
<br>

* Page with privacy policy in accordance with GRDP regulations.
<br>

* A ‘contact us’ form with form validation and encouragement to users to send in book recommendations.
<br>

* Link to Facebook business page on the web home page and products page.
<br>

* Newsletter sign-up page with validation.
<br>

* Fully functional Stripe payment checkout in test mode for the purposes of this project.
<br>

* Fully set-up Facebook business page to complement the site.
<br>

* SEO considerations implemented: meta description of content and key search words in head of code. sitemap.xml and robots.txt files are also included in the code. 
<br>

* Advertising campaign for 'badly made books' notebook company to mutually increase brand reach. Their A6 notebook is the first season's 'featured product' - a concept to allow for ongoing advertising slots for different Irish stationary companies, to increase revenue for Leabhar Maith. 
<br>
### Future Features

<br>

While a subscription service option would certainly suit Leabhar Maith, for this initial version of the project it only offers one-off purchases, as I was learning to set up Stripe payment integration for the first time.  A subscription service would be a great future feature. 
Meanwhile, the curation of groups of books encourages buying multiple books, plus there is a cost benefit to larger purchases in terms of free delivery and the featured product of the season free of charge.
<br>.
As mentioned above in the 'Scope' section, email validation also has yet to be implemented.
<br>

* To implement: a subscription service for all 6-8 books per quarter at 10% off the full cost.
<br>

* To implement: email validation messages for successful purchases sent to the customer.
<br>

* To implement: delivery cost realistic to areas being delivered to rather than a flat 10%
<br>

* To implement: a book blog to extend branch reach and customer involvement.
<br>

* To implement: creation of the newsletter content, which could involve reaching out to existing subscribers to submit book reviews and musings, as well as features about Irish authors and the Irish language.
<br>

* To implement: literary and Irish language events run by Leabhar Maith to grow the reach of the brand and increase subscriber base.
<br>

* To implement: extend advertising for Irish crafts and stationary companies.
<br>

* To implement: functionality for users to leave reviews. 
<br>
<br>

### **Structure**
<br>

* Homepage will be the landing pad with key links attached to the navbar .
<br>

* The navbar will provide the menu of options for all available pages. All pages are reachable from every other page via the navbar. 
<br>

* Book category page filterable by genre/ category of book .
<br>

* Clicking on a book or the ‘further info’ button underneath will take user to the book detail page. It can be added to the shopping basket here, where the user can either continue shopping or checkout and pay.
<br>

* The Navbar menu will collapse and be responsive for mobile and tablet devices.
<br>

* Title of the site is a clickable link back to the home page.
<br>
<br>

### **Skeleton** / **Wireframes**
<br>
I used Balsamiq to create a skeleton of what the main two landing pages of the site would look like, combined with mock-ups from a very similar e-commerce practice-project I completed with the Code Institute called 'Boutique Ado'. The Boutique Ado page mock-ups will form the template for my own equivalent pages on the Leabhar Maith site, e.g. the shopping basket icon on the navbar will turn blue and start showing the basket total when the user starts adding books to it in a similar way, and the icon for the shopping cart will be the same. I won't be reinventing the wheel in terms of the appearance and structure of my e-commerce site, but I will be adapting the code and creating new features where this suits the specific needs of an online bookshop. 
<br>
<br>
<center><img src="assets/images/wireframeHome.png" alt="Homepage wireframe" width="60%"/></center>
<br>   
<br>
<center><img src="assets/images/wireframeProducts.png" alt="Products page, mobile design, wireframe" width="40%"/></center>
<br>   
<br>
<center><img src="assets/images/mockupNav.png" alt="navigation bar mockup" width="60%"/></center>
<br>   
<br>
The product detail page shown below will show the information required for a book rather than an item of clothing (ISBN, author, title, publisher etc) and there will be an image of the book cover to the left of the information. But the rough style and positioning of the buttons will remain the same.
<br>
<br>
<center><img src="assets/images/mockProdDetail.png" alt="navigation bar mockup" width="80%"/></center>
<br>
<br>
<center><img src="assets/images/mockupSignup.png" alt="registration page" width="60%"/></center>
<br>   
<br>
<center><img src="assets/images/mockupSignIn.png" alt="sign-in page" width="60%"/></center>
<br>   
<br>
<center><img src="assets/images/mockupProfile.png" alt="profile page" width="60%"/></center>
<br>   
<br>
<center><img src="assets/images/mockBasket.png" alt="Shopping Basket" width="60%"/></center>
<br>   
<br>
<center><img src="assets/images/mockAddProd.png" alt="Add product page for staff" width="60%"/></center>
<br>   
<br>
Bottom of add product page for staff below (need to scroll down):
<br>
<br>
<center><img src="assets/images/mockupAddProduct.png" alt="Add product page" width="60%"/></center>
<br>   
<br>

### **Surface**

<br>
<br>
Colour palette: the colours are based around shades of green, as the colour green is associated with the 'Emerald Isle' of Ireland.
<br>
Fonts: the fonts will have a literary theme, with handwritten-style headings and old fashioned book-type font for the main text and title of the website. 
<br>
Logo/ favicon: the logo will be an image of a green coloured book or a pile of green coloured books.
<br>
<br>
### **Entity Relationship Diagram**

<br>
<center><img src="assets/images/erd.png" alt="ERD image" width="90%" target="_blank"/></center>
<br>   