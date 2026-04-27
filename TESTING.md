## Manual Testing

All core functionality of the Midas Lotto application was manually tested to ensure the system behaves as expected across different user interactions. The table below outlines the test cases performed, expected outcomes, and results.

---

## Manual Test Cases

| Page | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| **Navbar** |  |  |  |
|  | Click on Logo | Redirects user to the homepage | Pass |
|  | Click on Draws link | Redirects to draw list page | Pass |
|  | Click on Login link | Redirects to login page | Pass |
|  | Click on Register link | Redirects to registration page | Pass |
|  | Click on Profile link | Redirects to user profile page | Pass |
|  | Click on Logout link | Logs user out and redirects to homepage | Pass |

---

## Login Page

| Page | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| Login Page | Enter valid username and password | User is authenticated and redirected | Pass |
| Login Page | Enter invalid credentials | Error message is displayed | Pass |
| Login Page | Submit empty form | Validation errors are displayed | Pass |
| Login Page | Click register link | Redirects to registration page | Pass |

---

## Register Page

| Page | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| Register Page | Enter valid registration details | Account is created and user is logged in | Pass |
| Register Page | Submit empty form | Validation errors are displayed | Pass |
| Register Page | Enter mismatched passwords | Error message is displayed | Pass |
| Register Page | Enter existing username | Validation error is displayed | Pass |

---

## Homepage

| Page | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| Homepage | View homepage | Hero section, winnings, current draw and subscription section are displayed | Pass |
| Homepage | Click Join Current Month | Redirects to subscription page | Pass |
| Homepage | Click View Draws | Redirects to draw list page | Pass |
| Homepage | View current month winnings | Correct monthly winnings are displayed | Pass |
| Homepage | View overall winnings | Correct total winnings are displayed | Pass |

---

## Draw List Page

| Page | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| Draw List | View draw list | All available draws are displayed | Pass |
| Draw List | Click on a draw title | Redirects to draw detail page | Pass |
| Draw List | View draw date and winnings | Correct draw information is displayed | Pass |

---

## Draw Detail Page

| Page | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| Draw Detail | View draw detail | Draw title, date, result and winnings are displayed | Pass |
| Draw Detail | View draw image | Image is displayed if uploaded | Pass |
| Draw Detail | View comments | Comments linked to the draw are displayed | Pass |
| Draw Detail | Click back/navigation links | User can navigate without errors | Pass |

---

## Comments Section

| Page | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| Comments | Add a valid comment while logged in | Comment appears under the draw | Pass |
| Comments | Submit empty comment | Validation error is displayed | Pass |
| Comments | Try to comment while logged out | User is asked to log in | Pass |
| Comments | View comments on draw detail page | Comments are displayed with username and date | Pass |

---

## Profile Page

| Page | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| Profile | View profile while logged in | Username, email and subscription information are displayed | Pass |
| Profile | View profile while logged out | User is redirected to login page | Pass |
| Profile | Click Edit Profile | Redirects to edit profile page | Pass |
| Profile | View subscription history | User subscriptions are displayed | Pass |
| Profile | View subscription expiry | Expiry date is displayed if subscription exists | Pass |

---

## Edit Profile Page

| Page | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| Edit Profile | View edit form | Form is pre-filled with existing user data | Pass |
| Edit Profile | Update valid profile details | Changes are saved successfully | Pass |
| Edit Profile | Submit invalid data | Validation errors are displayed | Pass |
| Edit Profile | Click save | User is redirected back to profile page | Pass |

---

## Subscription Page

| Page | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| Subscription | View subscription page | Current month, price and remaining draws are displayed | Pass |
| Subscription | Confirm subscription | User is redirected to Stripe Checkout | Pass |
| Subscription | Try joining with no remaining draws | Error message is displayed | Pass |
| Subscription | Try joining same month twice after payment | User is prevented from duplicate subscription | Pass |
| Subscription | View calculated amount | Prorated price is displayed correctly | Pass |

---

## Stripe Checkout

| Page | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| Stripe Checkout | Complete payment with valid test card | Payment succeeds and user is redirected to success page | Pass |
| Stripe Checkout | Cancel payment | User is redirected to cancel page | Pass |
| Stripe Checkout | Payment succeeds | Stripe webhook confirms payment | Pass |
| Stripe Checkout | Webhook received | Subscription becomes active | Pass |
| Stripe Checkout | Payment not completed | Subscription remains pending | Pass |

---

## Payment Success Page

| Page | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| Success Page | Return after successful payment | Success message is displayed | Pass |
| Success Page | Click Back to Profile | Redirects user to profile page | Pass |
| Success Page | Check profile after webhook | Subscription status shows active | Pass |

---

## Payment Cancel Page

| Page | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| Cancel Page | Cancel Stripe payment | Cancel message is displayed | Pass |
| Cancel Page | Click Try Again | Redirects to subscription page | Pass |
| Cancel Page | Check profile after cancel | Subscription does not become active | Pass |

---

## Admin Panel

| Page | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| Admin | Log in as admin | Admin dashboard is accessible | Pass |
| Admin | Create monthly summary | Monthly summary is saved | Pass |
| Admin | Create draw | Draw is saved and displayed on site | Pass |
| Admin | Upload draw image | Image is saved and displayed | Pass |
| Admin | Set current draw | Current draw appears on homepage | Pass |
| Admin | Set subscription price | Price appears on subscription page | Pass |
| Admin | View subscriptions | Payment and active status are visible | Pass |

---

## Logout

| Page | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| Logout | Click logout | User session ends and homepage is displayed | Pass |
| Logout | Try to access profile after logout | User is redirected to login page | Pass |

---

## Responsive Testing

| Device | Test | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| Mobile | Open homepage | Layout adjusts correctly | Pass |
| Mobile | Open navbar | Navbar collapses and expands correctly | Pass |
| Tablet | View draw detail page | Content remains readable | Pass |
| Desktop | View full site | Layout displays correctly | Pass |

---

## Browser Testing

| Browser | Expected Result | Pass/Fail |
| --- | --- | --- |
| Google Chrome | Site works correctly | Pass |
| Microsoft Edge | Site works correctly | Pass |
| Firefox | Site works correctly | Pass |

---

## User Stories Validation

All defined user stories for the Midas Lotto project have been successfully fulfilled through manual testing.

| User Story | Evidence |
|-----------|----------|
| As a user, I want to register an account so that I can join the lotto | Registration and login tested successfully |
| As a user, I want to log in so that I can access my profile and subscriptions | Authentication and session handling tested |
| As a user, I want to view the current draw so I can see the latest results | Homepage current draw display tested |
| As a user, I want to view all draws so that I can check past results and winnings | Draw list page tested |
| As a user, I want to view a single draw in detail so I can see results, images, and comments | Draw detail page tested |
| As a user, I want to comment on a draw so that I can share my thoughts with others | Comment creation tested |
| As a user, I want to join the current month subscription so that I can participate in the lotto | Subscription flow tested |
| As a user, I want to pay for my subscription securely so that my payment is handled safely | Stripe Checkout and webhook tested |
| As a non-authenticated user, I am restricted from protected pages | Access control and login redirects tested |

---

## Html Validation

### Login Page

![List](/doc/img/loginvalid.png)

### Main Page

![List](/doc/img/mainvalid.png)

### REgister Page

![List](/doc/img/registervalid.png)

### Draw Page

![List](/doc/img/drawvalid.png)

### Draw Detail Page

![List](/doc/img/drawdvalid.png)

### Profile Page

![List](/doc/img/profilevalid.png)

### Profile Edit Page

![List](/doc/img/editvalid.png)

### Join Subscription Page

![List](/doc/img/joinsvalid.png)

### Success page

![List](/doc/img/svalid.png)

### P404 Page

![List](/doc/img/p404v.png)

## CSS Validation 

![List](/doc/img/cssvalid.png)

## Python Validation

### Accounts

### apps.py

![List](/doc/img/accappv.png)

### forms.py

![List](/doc/img/accformsv.png)

### models.py

![List](/doc/img/accmodelsv.png)

### signals.py

![List](/doc/img/accsignalsv.png)

### test.py

![List](/doc/img/acctestv.png)

### urls.py

![List](/doc/img/accurlsv.png)

### views.py

![List](/doc/img/accviewsv.png)

### Config

### asgi.py

![List](/doc/img/conasgiv.png)

### settings.py

![List](/doc/img/consetv.png)

### urls.py

![List](/doc/img/conuv.png)

### wsgi.py

![List](/doc/img/conwsgiv.png)

### Core

### apps.py

![List](/doc/img/coreappsv.png)

### test.py

![List](/doc/img/coretestv.png)

### urls.py

![List](/doc/img/coreurlsv.png)

### views.py

![List](/doc/img/coreviewsv.png)

### Lotto

### admin.py

![List](/doc/img/lottoadminv.png)

### apps.py

![List](/doc/img/lottoappsv.png)

### forms.py

![List](/doc/img/lottoformsv.png)

### models.py

![List](/doc/img/lottomodelsv.png)

### test.py

![List](/doc/img/lottotestv.png)

### urls.py

![List](/doc/img/lottourlsv.png)

### views.py

![List](/doc/img/lottoviewsv.png)

## Manual Testing and Fixes

Manual testing was carried out throughout the development of the Midas Lotto project. Features were tested after implementation, during debugging, and again after deployment to ensure consistency between local and production environments.

---

### Development Issues Found and Fixed

- **Template structure errors**  
  Some templates caused errors such as `'block tag with name title appears more than once'`. This occurred when full templates were accidentally nested inside other templates. The issue was resolved by ensuring each template contains only one `{% extends %}` and one set of `{% block %}` tags.

- **Missing database tables (migrations issue)**  
  On deployment, errors such as `relation "lotto_monthlysummary" does not exist` occurred. This was caused by migrations not being applied on Heroku. The issue was fixed by running migrations on the production database.

- **Incorrect Stripe object usage**  
  An error occurred when using `.get()` on Stripe session objects (`AttributeError: get`). This was fixed by accessing Stripe data using attributes (e.g., `session.payment_status`) instead of dictionary-style access.

- **Whitespace and indentation problems**  
  Python indentation errors caused views to fail. These were resolved by correcting code structure and consistent formatting.

- **Missing or incorrect imports**  
  Some views failed due to missing imports. These were fixed by reviewing error messages and adding the required imports.

- **Spelling mistakes and incorrect naming**  
  Errors in variable names and template references caused pages to break. These were corrected by ensuring consistent naming across files.

---

### Form and Input Testing

- Forms initially allowed invalid or empty input  
- Help text was not properly displayed, causing accessibility warnings  
- Error messages were unclear  

These issues were fixed by improving form validation, displaying help text, and adding clear error feedback.

---

### Payment Testing Issues

- Stripe payments succeeded but subscriptions remained pending  
- Webhook configuration was missing during early testing  
- Subscription status was not updating after payment  

These issues were resolved by:

- Implementing a Stripe webhook  
- Verifying webhook signatures  
- Updating subscription status after `checkout.session.completed` events  

---

### Deployment Testing Issues

- Errors such as `DisallowedHost` occurred due to missing `ALLOWED_HOSTS` configuration  
- CSRF errors occurred due to missing `CSRF_TRUSTED_ORIGINS`  
- Environment variables were not configured correctly on Heroku  

These issues were resolved by properly setting environment variables and updating Django settings for production.

---

### Static and Media Files

- Static files did not load correctly after deployment  
- The issue was caused by incorrect configuration and missing `collectstatic`  

This was resolved by configuring static files correctly and running `collectstatic`.

