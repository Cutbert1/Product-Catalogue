# Local Hand Craft Product Catalogue - Shoperite
## Introduction
This project is for local community craft men to post their hand made products for reviews, improvements and marketing hence, organise exhibitions to market and promote their locally hand made products and businesses.
#### Project Purpose and user Demography
The project is aimed at local community craft men, who uses locally sourced biodegradable materials to produce eco-friendly products. Users can post their products for improvement reviews, market promotion and organise product exhibition for local community. There for promote house hold usage for bio degradable products.
## Design
### Entity Relationship Diagram
![lucid1](./static/images/readme-images/design/lucid1.jpg)
![lucid2](./static/images/readme-images/design/lucid2.jpg)
![lucid3](./static/images/readme-images/design/lucid3.jpg)
![lucid4](./static/images/readme-images/design/lucid4.jpg)
![lucid5](./static/images/readme-images/design/lucid5.jpg)
### Colour Scheme
### Topography
## Features
The core features/functionality of  this project is categorised as below. Future improvements are also highlighted in this section.
#### Navbar
A responsive navigation header where all the links to other html pages are embedded rendered through base.html inclucing dropdown for Signup and Log in.
![navbar-feature](./static/images/readme-images/features%20-images/navbar.jpg)
Each navbar item takes you to the desired page.
#### Exhibition page
Details of upcoming exhibition for local craft men (users) to view and register for the event. Includes date and time stamp of registration to enable admin filtering and capacity management.
![exhibition1](./static/images/readme-images/features%20-images/exhibition1.jpg)
![exhibition2](./static/images/readme-images/features%20-images/exhibition2.jpg)
![exhibition3](./static/images/readme-images/features%20-images/exhibition3.jpg)
#### Home page
Displays a paginated  list of products, with marketers/producers name, price of price and date and time posted ready for reviews and promotion
![home](./static/images/readme-images/features%20-images/home.jpg)
#### Pagination
This includes page numbers and a clearer indication of the current page.
![pagination](./static/images/readme-images/features%20-images/pagination.jpg)
#### Prodct Detail page
Displays a product when clicked from the home page, with product image, price and  descriptions with approved and unapproved reviews.
![product-details1](./static/images/readme-images/features%20-images/product-details1.jpg)
![product-details2](./static/images/readme-images/features%20-images/product-details2.jpg)
#### Logout Page
Takes you to a sign out page when clicked with a button to finally signout. 
![logout](./static/images/readme-images/features%20-images/logout.jpg)
#### Admin Panel
Page for site owner(super user) to manage products, user reviews and exhibition registrations.
![admin](./static/images/readme-images/features%20-images/admin.jpg)
#### Sign Up page
Displays a sign up page were email address is optional, and details the password criteria ![sign-up](./static/images/readme-images/features%20-images/sign-up.jpg)

#### Future features Improvement 
Project can be improved by adding ordering page where unregistered site users can purchase an item
## Manual Testing
### User Story with Acceptance criteria Features Testing
#### User Story: Site Admin log in

|Key Features|   User Value   |Functionality Test|Outcome|
|:------------|:----------------|:-------------|:------------|
|As a site admin I can login to admin panel|Enable site admin (super user) manage products|Click on login and user super user credentials to log in and append /admin to urls. ![signin](./static/images/readme-images/manual-test-images/superuser-login.jpg) ![admin](./static/images/readme-images/manual-test-images/admin.jpg) |Logged into Django admin panel. ![admin2](./static/images/readme-images/manual-test-images/admin2.jpg)|
|As a site admin, I can add products|Enable site admin (super user) to add products for review.|Click on add products, input product details and save. ![add-products](./static/images/readme-images/manual-test-images/add-product.jpg) ![product-details](./static/images/readme-images/manual-test-images/product-details.jpg) ![save](./static/images/readme-images/manual-test-images/product-details1.jpg)|Product added to product list. ![product-list](./static/images/readme-images/manual-test-images/product-list.jpg)|
|As a site admin, I can delete products|Enable site admin (super user) to delete products.|Click on product change, select product you want to delete, the click delete ![product-change](./static/images/readme-images/manual-test-images/product-change.jpg) ![product-delete](./static/images/readme-images/manual-test-images/product-delete.jpg) ![product_delete2](./static/images/readme-images/manual-test-images/product-delete2.jpg)|Product deleted from the database, hence not visible to users|
|As a site admin, I can update products|Enable site admin (super user) to update all feilds of product details.|Click on product change, select product you want to update, make the update and save. ![product-change](./static/images/readme-images/manual-test-images/product-change.jpg) ![save](./static/images/readme-images/manual-test-images/product-details1.jpg)|Product Updated|
|As a site admin, I can leave product on draft with out publishing|Enable site admin (super user) to leave products on draft, henece not visible to users until it's published|Select draft on product status. ![draft](./static/images/readme-images/manual-test-images/draft.jpg)|Product on draft status hence not visible to users for review|
#### User Story: View list of products on home page
|Key Features|   User Value   |Functionality Test|Outcome|
|:------------|:----------------|:-------------|:------------|
|When there are multiple approved products in the database, these products are shown as a list. The user sees a list of products once they open the home page|User views all products on landing page. |Signed up and not signed up users to view list on products on landing page|View list of products as a user.![view-product-list](./static/images/readme-images/manual-test-images/view-product-list.jpg)|
|The user has access to all product names and pagination, to select what to review.|User can view paginated list of products|Login as a user to view list on products on landing page, click next to view more products|More list of product is shown to the user when page number is clicked. ![pagination](./static/images/readme-images/manual-test-images/paginated.jpg)|
#### User Story: Open product details
|Key Features:|   User Value   |Functionality Test|Outcome|
|:------------|:----------------|:-------------|:------------|
|Site user, click on any product of your choice to view product details|Site user to learn more about the product|Click on a product to render the full product description|Renders full product description when list item is clicked. ![product-description](./static/images/readme-images/manual-test-images/product-description.jpg)|
#### User Story: View Reviews
|Key Features:|   User Value   |Functionality Test|Outcome|
|:------------|:----------------|:-------------|:------------|
| Non registered site user can click on a product to read approved reviews|Site user read product reviews left by others to understand more about the product |Click on a product to render the reviews on the product|Renders approved reviews left on the product ![reviews](./static/images/readme-images/manual-test-images/reviews.jpg)|
#### User Story: Approve Reviews
|Key Features:|   User Value   |Functionality Test|Outcome|
|:------------|:----------------|:-------------|:------------|
|Logged in super user can approve or disapprove reviews|Super user filter out questionable reviews|Log into admin panel and approve reviews  |Review is_approveed ![approved](./static/images/readme-images/manual-test-images/approve.jpg)|
#### User Story: Read about up coming Exhibition and register
|Key Features:|   User Value   |Functionality Test|Outcome|
|:------------|:----------------|:-------------|:------------|
|On selecting exhibition link upcoming exhibition details is seen|Read about upcoming exhibition|Click on exhibition link to view exhibition details| Renders upcoming exhibition details ![upcoming-exhibition](./static/images/readme-images/manual-test-images/upcoming-exhibition.jpg) ![exhibition-details](./static/images/readme-images/features%20-images/exhibition2.jpg)|
|Site user can register for upcoming exhibition|Register to attend exhibition|Fill in the registration form and submit ![registration](./static/images/readme-images/manual-test-images/registration.jpg)|Form submitted  ![submit-alert](./static/images/readme-images/manual-test-images/submitt-alert.jpg)|
#### User Story: Manage Exhibition registration requests
|Key Features:|   User Value   |Functionality Test|Outcome|
|:------------|:----------------|:-------------|:------------|
|Identify read and unread exhibition registration request|Site admin can see how many left to process|Log into admin panel, read rigistration and check is_read|View read and unread exhibition registration ![is_read](./static/images/readme-images/manual-test-images/is_read.jpg) ![read-count](./static/images/readme-images/manual-test-images/read-count.jpg)|
#### User Story: Update or Delete review of a product
|Key Features:|   User Value   |Functionality Test|Outcome|
|:------------|:----------------|:-------------|:------------|
|Logged in user can update their review|Enable user to edit their review|Click edit on the review you want to edit, update and click update to submit ![edit](./static/images/readme-images/manual-test-images/edit.jpg) ![edit2](./static/images/readme-images/manual-test-images/edit2.jpg)|Updated review is submitted ![edit3](./static/images/readme-images/manual-test-images/edit3.jpg)|
|Logged in user can delete their review|Enable user to delete|Click delete, then click the modal delete ![delete1](./static/images/readme-images/manual-test-images/delete1.jpg)|Review deleted ![delete2](./static/images/readme-images/manual-test-images/delete2.jpg)|
#### User Story: SignUp
|Key Features:|   User Value   |Functionality Test|Outcome|
|:------------|:----------------|:-------------|:------------|
|Site user can signup with username and password|Enable user to review products|Click on Signup, provide username and password then signup ![signup](./static/images/readme-images/manual-test-images/signup.jpg)|Successfully signed up ![signup2](./static/images/readme-images/manual-test-images/signup2.jpg)|
|Signed up user can login and review products|Review products|Click on a product and provide review ![signup-review](./static/images/readme-images/manual-test-images/signup-review.jpg)|Review submitted|

### Lighthouse Performance
|View Tested|   Outcome of the audit |Screenshot of clear Validator output|
|:------------|:----------------|:-------------|
|Mobil|Lighthouse report, mobile|![mobile](./static/images/readme-images/lighthouse/exhibition-mobile.jpg)|
|Desktop|Lighthouse report, desktop|![desktop](./static/images/readme-images/lighthouse/exhibition-desktop.jpg)|
### Validation Testing - HTML and Custom CSS [W3C HTML](https://validator.w3.org/) and [W3C CSS Jigsaw](https://jigsaw.w3.org/css-validator/)
|Page Tested|Screenshot of Errors and Warnings   |Solution Applied|Screenshot of clear Validation Output|
|:------------|:----------------|:-------------|:------------|
|Home page|![error](./static/images/readme-images/validation-test-images/home-page%20error.jpg)|Fix </a> end tag to align with nesting rules. Remove the trailing slash on <hr/> to clear the info message. This wasn’t an error|No error but warning for possible misuse of aria-label ![error-fix](./static/images/readme-images/validation-test-images/home-page%20warning.jpg)|
|Exhibition page|![error](./static/images/readme-images/validation-test-images/exhibition-page-error.jpg)|Fixed unclosed div tag and other open elements|![error-fix](./static/images/readme-images/validation-test-images/exhibition-page-fix.jpg)|
|Product details page|![error1](./static/images/readme-images/validation-test-images/product-details-error1.jpg) ![error2](./static/images/readme-images/validation-test-images/product-details-error2.jpg) ![error3](./static/images/readme-images/validation-test-images/product-details-error3.jpg)|Removed title tag, update p tag not to be a child of strong tag and used article tag|![fix](./static/images/readme-images/validation-test-images/product-details-error-fix.jpg)|
|style.css|N/A|N/A|![css](./static/images/readme-images/validation-test-images/css.jpg)|
### Validation Testing - Python Store app [PEP8 Python Validator](https://pep8ci.herokuapp.com/)
|Page Tested|Screenshot of Errors and Warnings   |Solution Applied|Screenshot of clear Validation Output|
|:------------|:----------------|:-------------|:------------|
|models.py|No error or warning|N/A|![store-model](./static/images/readme-images/validation-test-images/store-model.jpg)|
|views.py|No error or warning|N/A|![store-views](./static/images/readme-images/validation-test-images/store-views.jpg)
|forms.py|No error or warning|N/A|![store-forms](./static/images/readme-images/validation-test-images/store-forms.jpg)|
|admin.py|No error or warning|N/A|![store-admin](./static/images/readme-images/validation-test-images/store-admin.jpg)|
|urls.py|No error or warning|N/A|![store-urls](./static/images/readme-images/validation-test-images/store-urls.jpg)|
### Validation Testing - Python Exhibition app [PEP8 Python Validator](https://pep8ci.herokuapp.com/)
|Page Tested|Screenshot of Errors and Warnings   |Solution Applied|Screenshot of clear Validation Output|
|:------------|:----------------|:-------------|:------------|
|models.py|No error or warning|N/A|![exhibition-model](./static/images/readme-images/validation-test-images/exhibition-model.jpg)|
|views.py|No error or warning|N/A|![exhibition-views](./static/images/readme-images/validation-test-images/exhibition-views.jpg)|
|forms.py|No error or warning|N/A|![exhibition-forms](./static/images/readme-images/validation-test-images/exhibition-forms.jpg)|
|admin.py|No error or warning|N/A|![exhibition-admin](./static/images/readme-images/validation-test-images/exhibition-admin.jpg)|
|urls.py|No error or warning|N/A|![exhibition-urls](./static/images/readme-images/validation-test-images/exhibition-urls.jpg)|
### Validation Testing - JavaScript [JSHint](https://jshint.com/)
|Page Tested|Screenshot of Errors and Warnings   |Solution Applied|Screenshot of clear Validation Output|
|:------------|:----------------|:-------------|:------------|
|reviews.js|No error, 22 warnings about using ES6 version of JSHint|N/A|![js](./static/images/readme-images/validation-test-images/js.jpg)|
### Browser compatibility
|Browser Tested|Functionality Tested|Visual Consistency|Outcome|
|:------------:|:----------------:|:-------------:|:-------------:|
|![chrome](./static/images/readme-images/browser-compatibility/chrome.jpg)|Navigation, Forms, Links and Buttons|Layout, design, content display is consistent|Good ![chrome1](./static/images/readme-images/browser-compatibility/chrome1.jpg)|
|![edge](./static/images/readme-images/browser-compatibility/edge.jpg)|Navigation, Forms, Links and Buttons|Layout, design, content display is consistent|Good ![edge1](./static/images/readme-images/browser-compatibility/edge1.jpg)|
|![firefox](./static/images/readme-images/browser-compatibility/firefox.jpg)|Navigation, Forms, Links and Buttons|Layout, design, content display is consistent|Good ![forefox1](./static/images/readme-images/browser-compatibility/firefox1.jpg)|
### Screen sizes Responsiveness  
|Device Tested|Site responsive >=700px |Site responsive <699px|Render as expected|
|:------------:|:----------------:|:-------------:|:--------------:|
|iPhone 12 Pro (Mobile)|N/A|Good|Good 390px X 844px ![iPhone 12 pro](./static/images/readme-images/Screen%20sizes%20Responsivenes/iPhone12pro.jpg)|  
|iPad Mini (Tablet)|Good|N/A|Good 768px X 1024px ![iPad Mini](./static/images/readme-images/Screen%20sizes%20Responsivenes/iPad-mini.jpg)|
|iPad Air (Laptop)|Good|N/A|Good 820px X 1180px ![iPad air](./static/images/readme-images/Screen%20sizes%20Responsivenes/iPad-air.jpg)|
|Nest Hub Max (Desktop)|Good|N/A|Good 1280px X 800px ![nest hub max](./static/images/readme-images/Screen%20sizes%20Responsivenes/Net-bub-max.jpg)|

### Accessibility
|Color Contrats Testing|Alternative Text for Images |Outcome|
|:------------|:------------------|:---------------:|
## Technologies Used
* Bootstrap
* Django
* Summernote
* Cloudinary
* Whitenoise
* Django Crispy Forms
* Gunicorn
* Database
* Heroku
### Languages Used
* Python
* JavaScript
* HTML
* CSS
* DTL

## Bugs
#### Bugs Resolved
|Bug|   Description |Solution Applied|Result|
|:------------|:----------------|:-------------|:------------|
#### Bugs Unresolved
|Bug|   Description |Solution Applied|Result|
|:------------|:----------------|:-------------|:------------|
### Libraries
## Deployment
### Deployment Steps
* Ensure all installed packages are in requirements.txt
![requirement](./static/images/readme-images/deployment/requirement.jpg)
* Ensure Procfile has web process followed by the command to execute Django project.
* On settings.py set DEBUG=False
![debug](./static/images/readme-images/deployment/debug.jpg)
* Fork or clone product-catalogue repository
* Sign into Heroku and go to settings tab and ensure all config variables are added, Key:Value pairs
![settings](./static/images/readme-images/deployment/settings.jpg)
* Go to Deploy tab to continue deployment
* Ensure Heroku App is linked to GitHub repository
![github](./static/images/readme-images/deployment/github.jpg)
* Click on deploy branch
![deploy](./static/images/readme-images/deployment/deploy.jpg)

## Credits
### Codes
* Code Institue Django Project. **I Think therefore I Blog**
### Tutorials
* Tutor Support
* [stackflow](https://stackoverflow.com/questions)
### Text Content
* Wikipedia