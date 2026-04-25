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



### Site Owner Goals
The site owner wants to:
- Improve communication between shifts
- Reduce operational errors caused by missing information
- Enforce structured handover data
- Maintain a secure, authenticated system

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

![Register](doc/img/register.png)

---

### Homepage

![Homepage](doc/img/homepage.png)

---

### Draw List Page

![Draw List](doc/img/draw_list.png)

---

### Draw Detail Page

![Draw Detail](doc/img/draw_detail.png)

---

### Comment Section

![Comments](doc/img/comments.png)

---

### Subscription Page

![Subscription](doc/img/subscription.png)

---

### Stripe Checkout

![Stripe Checkout](doc/img/stripe_checkout.png)

---

### Payment Success Page

![Success](doc/img/payment_success.png)

---

### Payment Cancel Page

![Cancel](doc/img/payment_cancel.png)

---

### Profile Page

![Profile](doc/img/profile.png)

---

### Edit Profile Page

![Edit Profile](doc/img/edit_profile.png)

---

### Admin Panel

![Admin](doc/img/admin.png)

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

- Edit and delete comments  
- Email notifications for new draws  
- Admin dashboard with statistics  
- Multiple subscription tiers  
- Automated draw results integration  

These features are planned for future development.

---