# Local Hand Craft Product Catalogue - Shoperite
## Introduction
This project is for local community craft men to post their hand made products for reviews, improvements and marketing hence, organise exhibitions to market and promote their locally hand made products and businesses.
#### Project Purpose and user Demography
The project is aimed at local community craft men, who uses locally sourced biodegradable materials to produce eco-friendly products. Users can post their products for improvement reviews, market promotion and organise product exhibition for local community. There for promote house hold usage for bio degradable products.
## Design
### Model Entity Relationship Diagram
### Colour Scheme
### Topography
## Features
The core features/functionality of  this project is categorised as below. Future improvements are also highlighted in this section.
#### Navbar
A responsive navigation header where all the links to other html pages are embedded rendered through base.html.
![navbar-feature](./static/images/readme-images/features%20-images/navbar-feature.jpg)
Each navbar item takes you to the desired page.
#### Exhibition page
Details of upcoming exhibition for local craft men (users) to view and register for the event
![exhibition1](./static/images/readme-images/features%20-images/exhibition1.jpg)
![exhibition2](./static/images/readme-images/features%20-images/exhibition2.jpg)
![exhibition3](./static/images/readme-images/features%20-images/exhibition3.jpg)
#### Home page
Displays a paginated  list of products, with marketers/producers name, price of price and date and time posted ready for reviews and promotion
![home](./static/images/readme-images/features%20-images/home.jpg)
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
Project can be improved by adding ordering page were  site unregistered site users can purchase an item
## Manual Testing
### User Story with Acceptance criteria Features Testing
#### User Story: As a **Site Admin** I can **log in** so that **I can manage products**

|Key Features|   User Value   |Functionality Test|Outcome|
|:------------|:----------------|:-------------|:------------|
|As a site admin I can login to admin panel|Enable site admin (super user) manage products|Click on login and user super user credentials to log in and append /admin to urls. ![signin](./static/images/readme-images/manual-test-images/superuser-login.jpg) ![admin](./static/images/readme-images/manual-test-images/admin.jpg) |Logged into Django admin panel. ![admin2](./static/images/readme-images/manual-test-images/admin2.jpg)|
|As a site admin, I can add products|Enable site admin (super user) to add products for review.|Click on add products, input product details and save. ![add-products](./static/images/readme-images/manual-test-images/add-product.jpg) ![product-details](./static/images/readme-images/manual-test-images/product-details.jpg) ![save](./static/images/readme-images/manual-test-images/product-details1.jpg)|Product added to product list. ![product-list](./static/images/readme-images/manual-test-images/product-list.jpg)|
|As a site admin, I can delete products|Enable site admin (super user) to delete products.|Click on product change, select product you want to delete, the click delete ![product-change](./static/images/readme-images/manual-test-images/product-change.jpg) ![product-delete](./static/images/readme-images/manual-test-images/product-delete.jpg) ![product_delete2](./static/images/readme-images/manual-test-images/product-delete2.jpg)|Product deleted from the database, hence not visible to users|
|As a site admin, I can update products|Enable site admin (super user) to update all feilds of product details.|Click on product change, select product you want to update, make the update and save. ![product-change](./static/images/readme-images/manual-test-images/product-change.jpg) ![save](./static/images/readme-images/manual-test-images/product-details1.jpg)|Product Updated|
|As a site admin, I can leave product on draft with out publishing|Enable site admin (super user) to leave products on draft, henece not visible to users until it's published|Select draft on product status. ![draft](./static/images/readme-images/manual-test-images/draft.jpg)|Product on draft status hence not visible to users for review|
#### User Story: As a **Site user** I can **see list of products on home page** so that **I can click the product I want to review**
|Key Features|   User Value   |Functionality Test|Outcome|
|:------------|:----------------|:-------------|:------------|
|When there are multiple approved products in the database, these products is shown as a list. The user sees a list of products once they open the home page|User views all products on landing page. |Login as a user to view list on products on landing page|View list of products as a user.![view-product-list](./static/images/readme-images/manual-test-images/view-product-list.jpg)|
|The user has access to all product names and pagination, to select what to review.|User can view paginated list of products|Login as a user to view list on products on landing page, click next to view more products|More list of product is shown to the user when next is clicked. ![pagination](./static/images/readme-images/manual-test-images/paginated.jpg)|
#### User Story: As a **Site User** I can **click on product** so that **view the full description**
|Key Features|   User Value   |Functionality Test|Outcome|
|:------------|:----------------|:-------------|:------------|
|Site user, click on any product of your choice to view product details|Site user to learn more about the product|Click on a product to render the full product description|Renders full product description when list item is clicked. ![product-description](./static/images/readme-images/manual-test-images/product-description.jpg)|

### Features Test Result Compilation
|Key Features|   Test Case  |Outcome|
|:------------|:----------------|:-------------|
### Lighthouse Performance
|View Tested|   Outcome of the audit  |Soulution Applied|Screenshot of clear Validator output|
|:------------|:----------------|:-------------|:------------|
### Validation Testing
|Page Tested|Screenshot of Errors and Warnings   |Solution Applied|Screenshot of clear Validation Output|
|:------------|:----------------|:-------------|:------------|
### Browser compatibility
|Browser Tested|Functionality Tested|Visual Consistency|Outcome|
|:------------:|:----------------:|:-------------:|:-------------:|
|Browser Tested|Intended Appearance|Intended Responsiveness|
|:------------:|:----------------:|:-------------:|
### Screen sizes Responsiveness  
|Device Tested|Site responsive >=700px |Site responsive <699px|Render as expected|
|:------------:|:----------------:|:-------------:|:--------------:|
### Pages Responsivnes
|Home Page|Register Page|Gallery Page|About Us Page|Donation Page|Thank you Page|
|:------------:|:----------------:|:-------------:|:--------------:|:--------:|
### Accessibility
|Color Contrats Testing|Alternative Text for Images |Outcome|
|:------------|:------------------|:---------------:|
## Technologies Used
### Languages Used
## Bugs
#### Bugs Resolved
|Bug|   Description |Solution Applied|Result|
|:------------|:----------------|:-------------|:------------|
#### Bugs Unresolved
|Bug|   Description |Solution Applied|Result|
|:------------|:----------------|:-------------|:------------|
### Libraries
## Deployment
## Credits
### Codes
### Tutorials
### Text Content