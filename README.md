![Comment](/static/images/hero.png)

[Link to page](https://midas-lotto-a19d21e3453e.herokuapp.com/)

# Midas Lotto

Midas Lotto is a web application designed to manage a workplace lottery system.  
It allows users to subscribe to monthly draws, track winnings, interact via comments, and securely pay using Stripe.

## Live Project

- Live Site: https://midas-lotto-a19d21e3453e.herokuapp.com/
- Repository: https://github.com/EmcioN/Midas-lotto

## Table of Contents
[UX](#ux)  
* [Goal for the Project](#goal-for-the-project)  
* [User Goals](#user-goals)  
* [User Stories](#user-stories)  
* [Site Owner Goals](#site-owner-goals)  
* [Design Choices](#design-choices)  
  * [Font](#font)  
  * [Icons](#icons)  
  * [Colours](#colours)  
  * [Structure](#structure)  
  * [Project Structure](#project-structure)  
  * [Wireframes](#wireframes)
  * [Data Schema](#data-schema)  
* [Features](#features)  
* [Future Plans](#future-plans)
* [Testing](#testing)  
* [Technologies Used](#technologies-used)  
  * [Languages](#languages)  
  * [Frameworks and Libraries](#frameworks-and-libraries)  
  * [Tools](#tools)    
* [Deployment](#deployment)  
* [Credits](#credits)

## Goal for the Project

The goal of Midas Lotto is to create a centralized, easy-to-use platform for managing a shared lottery system in a workplace environment.  
It replaces manual tracking and improves transparency, engagement, and fairness.

## User Goals

Users of Midas Lotto want to:

- Register and log in securely
- View the current lotto draw and latest results
- See past draws and total winnings
- Join the lotto subscription easily
- Pay securely for their subscription

## User Stories

- As a user, I want to register an account so that I can join the lotto.
- As a user, I want to log in so that I can access my profile and subscriptions.
- As a user, I want to view the current draw so I can see the latest results.
- As a user, I want to view all draws so that I can check past results and winnings.
- As a user, I want to view a single draw in detail so I can see results, images, and comments.
- As a user, I want to comment on a draw so that I can share my thoughts with others.
- As a user, I want to join the current month subscription so that I can participate in the lotto.
- As a user, I want to pay for my subscription securely so that my payment is handled safely.
- As a logged-in user, I want to delete my own comments so that I can manage content I have added.
- As a site owner, I want users to be prevented from deleting other users’ comments so that data remains secure.

### Site Owner Goals

The site owner wants to:
- Provide a clear and transparent lottery system for all users  
- Manage monthly draws and results efficiently  
- Automate subscription handling and reduce manual work  
- Ensure secure and reliable payment processing  
- Keep accurate records of winnings and subscriptions

## Design Choices

### Font
The application uses default system and Bootstrap fonts.  
These were chosen to ensure:
- High readability  
- Accessibility across devices  
- Consistent appearance without external dependencies  

---

### Icons
Minimal use of icons is applied throughout the interface to:
- Keep the design clean and uncluttered  
- Support navigation where needed  
- Maintain focus on content rather than decoration  

---

### Colours
The project uses a dark theme with gold accents to:
- Create a premium, lottery-inspired look  
- Improve contrast and readability  
- Highlight important information such as winnings and actions  

Primary colours:
- Gold (#d4af37) for highlights and buttons  
- Dark background for contrast  
- White text for clarity

### Structure
The application is structured around a clear user flow:
- Authentication (register, login, logout)  
- Homepage overview (current draw and winnings)  
- Draw list and draw detail views  
- Subscription and payment flow  
- Profile management  

Navigation is consistent across all pages using a fixed navbar.

---

### Login Page

![Login](doc/img/login.png)

---

### Register Page

![Register](doc/img/reg.png)

---

### Homepage

![Homepage](doc/img/mainp.png)

---

### Draw List Page

![Draw List](doc/img/draws.png)

---

### Draw Detail Page

![Draw Detail](doc/img/drawd.png)

---

### Comment Section

![Comments](doc/img/com.png)

### Delete comment button

![Comments](doc/img/deletebutton.png)

---

### Delete comment page

![Comments](doc/img/deletepage.png)

---

### Subscription Page

![Subscription](doc/img/joins.png)

---

### Stripe Checkout

![Stripe Checkout](doc/img/stripe.png)

---

### Payment Success Page

![Success](doc/img/pays.png)

---

### Payment Cancel Page

![Cancel](doc/img/paycancel.png)

---

### Profile Page

![Profile](doc/img/profile.png)

---

### Edit Profile Page

![Edit Profile](doc/img/profileedit.png)

---

### Admin Panel

![Admin](doc/img/adminp.png)

---

### Project Structure

Midas-Lotto/

├── accounts/ - Authentication and user profiles  
├── core/ - Homepage and base views  
├── lotto/ - Lotto system (draws, subscriptions, comments)  
├── media/ - Uploaded images  
├── static/ - CSS and static files  
├── templates/ - HTML templates  
├── config/ - Project configuration  
├── manage.py  
└── requirements.txt  

---

## Wireframes

The following wireframes were created during the planning stage.

![Wireframes](doc/img/wire1.png)

![Wireframes](doc/img/wire2.png)

![Wireframes](doc/img/wire3.png)

![Wireframes](doc/img/wire4.png)

---

## Data Schema

The application uses a relational PostgreSQL database with Django ORM models. The schema separates authentication, user profile data, lotto draw information, payment records, and user interaction data into logical entities. This helps avoid duplication and makes the application easier to maintain.

![Data Schema](doc/img/schema.png)

### User

The project uses Django's built-in User model to handle authentication, registration, login and account access.

Relationships:

- One User can have one Profile.
- One User can create many Draw Comments.
- One User can have many Subscriptions.

### Profile

The Profile model stores additional information about each user.

Fields include:

- full name
- department
- subscription expiry date

Relationships:

- Each Profile belongs to one User.
- One User can have one Profile.

### Monthly Summary

The Monthly Summary model stores information for each monthly lotto period.

Fields include:

- month
- year
- total winnings
- subscription price
- notes

Relationships:

- One Monthly Summary can have many Draws.
- One Monthly Summary can have many Subscriptions.

### Draw

The Draw model stores each individual lottery draw.

Fields include:

- title
- draw date
- draw number
- result text
- winnings amount
- current draw status

Relationships:

- Each Draw belongs to one Monthly Summary.
- One Draw can have many Draw Images.
- One Draw can have many Draw Comments.

### Draw Image

The Draw Image model stores images connected to individual draws.

Fields include:

- image
- caption

Relationships:

- Each Draw Image belongs to one Draw.
- One Draw can have many Draw Images.

### Draw Comment

The Draw Comment model stores user comments on draw detail pages.

Fields include:

- comment body
- created date

Relationships:

- Each Draw Comment belongs to one User.
- Each Draw Comment belongs to one Draw.
- One User can create many Draw Comments.
- One Draw can have many Draw Comments.

### Subscription

The Subscription model stores user lotto participation and payment status.

Fields include:

- number of draws paid for
- amount paid
- joined date
- expiry date
- active status
- payment completed status
- Stripe checkout session ID

Relationships:

- Each Subscription belongs to one User.
- Each Subscription belongs to one Monthly Summary.
- One User can have many Subscriptions.
- One Monthly Summary can have many Subscriptions.
- Payment status is updated through Stripe webhook events.

### Database Relationships Summary

| Model | Relationship | Related Model |
| --- | --- | --- |
| User | One-to-one | Profile |
| User | One-to-many | Draw Comment |
| User | One-to-many | Subscription |
| Monthly Summary | One-to-many | Draw |
| Monthly Summary | One-to-many | Subscription |
| Draw | One-to-many | Draw Image |
| Draw | One-to-many | Draw Comment |

This structure supports the main application features, including user registration, profile management, monthly lotto draws, draw images, comments, subscriptions, and Stripe payment confirmation.

---

## Features

### Authentication
- User registration and login  
- Secure access to user profile and subscriptions  

### Lotto System
- View current and past draws  
- Monthly and total winnings displayed  
- Current draw highlighted on homepage  

### Draw Interaction
- View detailed draw information  
- Comment on draws  
- See images related to each draw  

### Comment Management

- Authenticated users can create comments on draw pages and delete only their own comments. Delete actions use a confirmation page and CSRF-protected POST request to prevent accidental or unauthorised deletion.

### Subscription System
- Join monthly lotto subscription  
- Prorated pricing based on remaining draws  
- Track subscription status and expiry  

### Stripe Payments
- Secure payment processing via Stripe Checkout  
- Payment confirmation using webhooks  
- Clear success and cancellation feedback  

### Admin Management
- Create and manage draws  
- Upload images for draws  
- Set monthly subscription price  
- Control current draw  

### Responsive Design
- Fully responsive layout using Bootstrap  
- Optimised for desktop, tablet, and mobile use  

---

## Future Plans

Due to time constraints, some planned features were not implemented:
 
- Email notifications for new draws  
- Admin dashboard with statistics  
- Multiple subscription tiers  
- Automated draw results integration  

These features are planned for future development.

---

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

---

## Technologies Used

### Languages

- [HTML](https://en.wikipedia.org/wiki/HTML5)  
- [CSS](https://en.wikipedia.org/wiki/CSS)  
- [Python](https://www.python.org/)  
- JavaScript (used via Bootstrap components)  

---

### Frameworks and Libraries

- [Django](https://www.djangoproject.com/) - Backend framework used to build the application  
- [Bootstrap](https://getbootstrap.com/) - Used for responsive design and styling  
- [Stripe](https://stripe.com/) - Used for secure payment processing  
- [Cloudinary](https://cloudinary.com/) - Used for media storage and image hosting  
- [Gunicorn](https://gunicorn.org/) - WSGI server used for deployment  
- [Psycopg](https://www.psycopg.org/) - PostgreSQL database adapter  
- [Google Fonts](https://fonts.google.com) - Used for typography  
- [Balsamiq](https://balsamiq.com/) - Used to create wireframes  

---

### Tools

- [GitHub](https://github.com/) - Used for version control and repository hosting  
- [VS Code](https://code.visualstudio.com/) - Development environment  
- [Heroku](https://www.heroku.com/) - Used for deployment  
- [PostgreSQL](https://www.postgresql.org/) - Production database  
- [W3C HTML Validator](https://validator.w3.org/) - Used to validate HTML  
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - Used to validate CSS  
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Used for debugging and testing

---

### Deployment

Local Development

- Go to Github repo [here](https://github.com/EmcioN/Midas-lotto) 
press **< CODE >**, and press COPY.
or **FORK** my repo

![clone](/doc/img/clonefork.png)

- Go to your github repositories and create new repo, call it whatever you like. Press Create Repository it will lead you to another page, and press Gitpod it should open workspace for you
- Now you need to download all libraries and frameworks used in this project. Use command : 
```
pip3 install -r requirements.txt
```
- Log in to Heroku or create a new account.
- Click the New button in the top right corner and select Create New App.

![step](/doc/img/step1.png)

- Choose a unique name for your app and select the region you want it to run in, then click Create App.

![step](/doc/img/step2.png)

- Go to the Deploy tab and click on the Settings tab.

![step](/doc/img/step3.png)

- Scroll down to the Buildpack section and click Add Buildpack.

![step](/doc/img/step4.png)

- Select "python" and click Save Changes.
- Repeat step and add "node.js" as well.
- Make sure the Buildpacks are in the correct order by clicking and dragging them if necessary.

![step](/doc/img/step5.png)

- Go back to the top of the page and select the Deploy tab again.

![step](/doc/img/step6.png)

- Choose Github as the deployment method and confirm that you want to connect to your Github account.

![step](/doc/img/step7.png)

- Search for your repository name and click the connect button.
- Scroll to the bottom of the deploy page and select your preferred deployment type.
- You can choose to enable automatic deploys for automatic deployment when you push updates to Github.

![step](/doc/img/step8.png)

- That's it, your site should now be deployed!

---
## Credits
- [Code Institute](https://codeinstitute.net/ie/): A special acknowledgment to the Code Institute. Revisiting lessons there proved invaluable, reinforcing core concepts and strengthening my foundation.

- [Stack Overflow](https://stackoverflow.co/): An essential resource during this journey. The community's expertise and shared experiences on Stack Overflow were immensely beneficial in navigating challenges and troubleshooting issues.

- [YouTube Tutorials](https://www.youtube.com/): Many thanks to the numerous educators and developers on YouTube. Their shared knowledge and step-by-step tutorials provided clarity and depth to my understanding.

- I was helping myself with resources gathered during building my different projects. 

- A big thank you to my co-worker. The idea is to automate the entire process. She handles that, and I wanted to help her out a bit. We coordinated the website's style together, and she provided me with a hero image.

### Mentorship
Special thanks to my mentor for guidance, feedback, and support throughout the project.