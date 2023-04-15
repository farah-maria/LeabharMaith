# Leabhar Maith
# Leabhar Maith

## Introduction

<br> 

This is a README for an e-commerce website for a hypothetical business called 'Leabhar Maith', meaning 'good book' in Irish. 
Leabhar Maith is a business to customer (B2C) e-commerce site, selling literary products to the user, namely books written in English and Irish by Irish authors. The deliverables will expand in future to include journals, paperweights and stationary with an Irish literary theme. Customers sign up to create an online account and pay via single payments using Stripe.

Features of this business-focused website include a shopping cart, a catalogue of products that is curated and updated quarterly and is searchable by author or title, an online payment system that can save the customer’s preferred mode of payment, a quarterly email newsletter sign-up, and a star rating / reviews system from Goodreads via the Goodreads API.

The site was developed using Python in the Django framework and styled using CSS and Bootstrap. PostgreSQL/ ElephantSQL is used for the database and Heroku for deployment. 

'Leabhar Maith' means 'good book' in Irish.

<br>

## Contents

* [User Experience R&D](#user-experience,-research-and-design)
    * [Strategy](#strategy)
    * [Scope](#Scope)
    * [Structure](#Structure)
    * [Skeleton](#Skeleton)
    * [Surface](#Surface)
* [Web Marketing Strategy](#Web-marketing-strategy)
* [Features](#Features)
* [Data Model](#Data-Model)
* [Testing](#Testing)
* [Deployment](#Deployment)
* [Credit & Attributes](#Credit-&-attributes)

<br>

## User Experience, Research and Design

I looked at a range of online bookshops, most of which constituted the online presence of a physical shop or chain of shops, such as Waterstones (https://www.waterstones.com/), Easons (https://www.easons.com/) or my local favourite, Vibes and Scribes (https://www.vibesandscribes.ie/). The book industry in Ireland is one where smaller, one-off book stores do not necessarily have a web presence at all, such as my closest bookshop in East Cork, Midleton Books (it does have a Facebook page at: https://www.facebook.com/midletonbooks/). On the other hand, the Book Depository (owned by Amazon) offers free delivery in Ireland, practically every book going, but no physical shop at all (https://www.bookdepository.com/).

Given the impersonal e-commerce feel of many online bookshops, even those that are linked to a physical shop that is well grounded in a local area, such as Vibes & Scribes, I wanted to create an alternatrive that brings a personal feel to online book shopping. Rather like a friendly and knowledgable bookshop owner or assistant, Leabhar Maith offers a curated and small selection of books that recommended by the site owner. The selection changes every quarter, with the seasons, so that there is a Spring selection of books, a Summer collection, and so on. The chosen books reflect the season, and past selections and the books in them can still be accessed and purchased by the site user. There's the feeling of a bookclub to the site (a little like the Guardian bookshop, which is linked to books featured in the Guardian and has a bookclub subcription). There is a newsletter sign-up that connects the user with articles and reviews, some of which are actually written by Leabhar Maith readers. Readers are 'at home' with Leabhar Maith, and can contribute reviews or musings.

A subscription service option would certainly suit Leabhar Maith, but for the this intial version of the project it only offers one-off purchases. The curation of groups of books, however, encourages buying multiple books and there is a discount on purchases of three books or more. 

Leabhar Maith offers a bookclub-type sense of belonging for the buyer, where there is a feeling of familiarity and friendliness rather than anonymity. Users can purchase a book in anonymous-guest-mode, however. 

------

Despite being in a team of... one... I used an Agile approach to designing, planning and developing the site.

First of all, 'user stories' were put together and recorded using the GitHub project tools, and a MVP (Minimum Viable Product) was then designed around the requirements that most directly met the needs of each user story.
 