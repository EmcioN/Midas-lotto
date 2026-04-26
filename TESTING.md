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