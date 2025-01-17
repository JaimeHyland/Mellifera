# Testing


#### [<< Return to Readme](https://github.com/JaimeHyland/Mellifera/blob/main/README.md)


## Contents

1. [Manual Testing](#manual-testing)
2. [DevTools](#devtools)
3. [Automated Testing](#automated-testing)
    * [Code Validation](#code-validation)
    * [Browser Validation](#browser-validation)
4. [User Stories](#user-stories)
5. [User Testing](#user-testing)
    * [My Mentor](#my-mentor)
    * [User review](#user-review)
6. [Post Review Changes](#post-review-changes)

# Manual Testing

### **The following checks were completed on both listed browsers, any issues have been captured and documented below with screenshots.**
 
**<details><summary>Sitewide</summary>**

+ [Navbar & Banner](#navbar-and-banner)
+ [Footer](#footer)
+ [Search bar](#search-bar)
    
</details>

**<details><summary>Home / About / Faq</summary>**

+ [Home Page](#home-page)
+ [About](#about-page)
+ [FAQ](#faq-page)
    
</details>

**<details><summary>Authorisation</summary>**

+ [Sign In / Logout](#sign-in-and-logout)
+ [Register](#register)
+ [Allauth templates](#allauth-templates)
    
</details>

**<details><summary>Conversions</summary>**

+ [Conversions Page](#conversions-page)
+ [Conversion Detail Page](#conversion-detail-page)
+ [Save to Profile Feature](#save-to-profile-feature)
+ [Add a conversion Page](#add-conversion-page)
+ [Edit conversion Page](#edit-conversion-page)
+ [Delete conversion function](#delete-conversion-function)
+ [Listing token Page](#listing-token-page)

</details>

**<details><summary>Merchandise</summary>**

+ [Merchandise Page](#merchandise-page)
+ [Product Detail Page](#product-detail-page)
+ [Add Product Page](#save-to-profile-feature)
+ [Edit Product Page](#add-conversion-page)

</details>

**<details><summary>Bag / Checkout</summary>**

+ [Shopping Bag Page](#shopping-bag-page)
+ [Checkout Page](#checkout-page)
+ [Checkout Success Page](#checkout-success-page)

</details>

**<details><summary>Profiles</summary>**

+ [My Profile Page](#my-profile-page)
+ [Order History Page](#order-history-page)
+ [My Listings Page](#my-listings-page)
+ [Saved Listings Page](#saved-listings-page)

</details>

**<details><summary>Management Pages</summary>**

+ [Conversion Management Page](#conversion-management-page)


</details>

### Testing completed using the following browsers: 

* Google Chrome (Version  88.0.4324.192) using MacOS on a monitor running at 1920 x 1080.
* Safari (Version 14.0.3 (16610.4.3.1.4)) using MacOS on a monitor running at 1920 x 1080.
* Apple iPad Pro 11" -  Safari and Google Chrome.
* Apple iPhone X - Safari and Google Chrome.

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

#  **Sitewide**

### Navbar and Banner

* Verify hover effects are present on all nav links. ✔
* Check all links in the nav element direct users to expected pages. ✔
* Check all links in the mobile nav element direct users to the expected pages. ✔
* Verify login and register links remove once a user is logged into the site. ✔
* Verify admin/superuser specific links appear in 'My Account' dropdown. ✔
* Verify scrolling banner displays and is animated. ✔

### Footer
* Verify social icons link to the corresponding social media websites and that they open in a new window when clicked. ✔
* Verify the year is rendered as the current year in the copyright caption. ✔

### Search Bar
* Check an existing search term to achieve render the conversions template with search query applied. ✔
![Search - True](documentation/testing/img/search-true.png) 

* Check a non-existent search term to render the conversions template with search query applied. ✔
![Search - False](documentation/testing/img/search-false.png) 

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Home Page**
* Verify the page loads responsively on all device sizes. ✔
* Verify site-entry overlay only loads on the initial page and does NOT load if refreshed in the same browser tab. ✔:
* Verify When clicked the site-overlay fades (1500ms) and the element is removed. ✔
* Verify the 'grow' animation on the logo in the site-overlay functions as expected. ✔
* Check all links in index.html direct users to the correct routes. ✔

# **About Page**
* Verify the page loads responsively on all device sizes. ✔
* Verify images load as expected and scale accordingly based on browser. ✔

# **FAQ Page**
* Verify the page loads responsively on all device sizes. ✔
* Verify questions are clickable, to toggle display of relevant answers to users. ✔

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Sign In and Logout**
* Verify pages load as expected and responsively on all device sizes. ✔
* Check all links operate as required ✔

### Sign in and logout Fixes
- Remove home link from sign-in page - Not required


# **Register**
* Check signup process functions as expected, including verification email being sent to a new user ✔
* Verification email received ✔
* User Confirmed ✔

    ![Email - Sent](documentation/testing/img/verify-email-sent.png)
    ![Email - Recieved](documentation/testing/img/verify-email.png)
    ![User - Confirmed](documentation/testing/img/email-confirmed.png) 

# **Allauth templates**
* Check page styling is adjusted for all templates provided from allauth, to match the site theme -:x:

### Allauth template Fixes
- Various templates do not contain white text or appropriate margin and padding - AMEND AS REQUIRED

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Conversions Page**
* Verify the page loads responsively on all device sizes. ✔

* Check all buttons/links function as expected :
    1. Filter category buttons ✔
    2. View Details button ✔
    3. Save to Profile button ✔
    4. Sort by dropdown ✔
    5. Pagination links ✔
    6. Back to top link ✔
    7. Carousel controls ✔

* Verify pagination is active, four listings (max) are present per page ✔

* Verify carousel displays the listings first three images ✔:

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Conversion Detail Page**

* Verify the page loads responsively on all device sizes. ✔

* Check all buttons/links function as expected:
    1. Contact Seller button ✔
    2. Save to profile button ✔
    3. Image links open in new tab ✔
    4. Back to conversions link ✔
    5. Back to top link ✔
    6. Carousel controls ✔

* Verify 'inactive' listing can only be viewed by listing owner or admin. ✔

    ![Inactive - listing - regular user](documentation/testing/img/inactive-listing.png)

* Verify 'inactive' listing is labelled to admin and listing owner ✔

    ![Inactive - listing - regular user](documentation/testing/img/inactive-listing-admin.png)

## Images
* CSS image grid displays 6 conversion images in the bottom section of the page (viewports 768px and above) ✔
* Verify listings with more than six images have an owl-carousel element with controls rendered below the CSS image grid :x:
* Verify the owl-carousel contains ALL listing images with controls on viewports below 768px, the CSS image grid is not displayed ✔:

## Conversion Detail Fixes

* Add 'owl-carousel' controls on viewports larger than 767px

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Save to Profile Feature**

- [x] Verify only registered users can use the save to profile feature (users will be prompted to sign in) ✔
- [x] Verify listings can only be added to the user profile once (toast messages provide feedback to the user) ✔
    ![User - Confirmed](documentation/testing/img/save-item-first.png)

    ![User - Confirmed](documentation/testing/img/save-item-false.png)

    ![User - Confirmed](documentation/testing/img/save-item-true.png)

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Add Conversion Page**
* Verify the page loads responsively on all device sizes. ✔
* Verify only logged in users can access the 'add_conversion' template ✔
* Verify links work as expected 
    * Go to profile ✔
    * View listing token ✔
* Verify form validation prevents the user from submitting the form with errors ✔
* Verify all validation is as expected and supports the user experience :x:
* Verify that once the form is submitted and validated, the user is redirected to the newly created listing - rendering the conversion_detail template ✔ 
* Verify the newly created listing is NOT active ✔
* Verify the newly created listing is viewable in the user profile 'my_listings' template ✔

## Add conversion form fixes
* Make vehicle dimensions able to be decimals - change IntegerField - DecimalField in the model.

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Edit Conversion Page**
* Verify the page loads responsively on all device sizes. ✔
* Verify users can only access the 'edit_conversion' template for listings which they have previously created (exception - Admin/superuser can edit all listings) ✔
* Verify 'back-to' link is dynamically rendered to the template:
    * Admin/Superuser - BACK TO CONVERSION MANAGEMENT ✔
    * Listing creator - BACK TO MY LISTINGS ✔
* Check all listing content is rendered to the form, ready for a user to edit ✔
* Check all images have the ability to 'delete' if desired ✔
* Check that three NEW image upload elements are present at the bottom of the form ✔
* Verify that users are able to add/remove/update image files and save changes -:x:

## Edit form fixes
* It is not possible to update an image file if the delete checkbox is active - add a note to users in the form

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Delete Conversion Function**
* Verify users may request deletion only of listings which they have previously created (exception - Admin/superuser can delete all listings) ✔
* Verify a modal to confirm deletion is displayed to the user before commencing with deletion of listing ✔
* Verfify listings are deleted from the database once the process is confirmed and completed ✔

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Listing Token Page**
* Verify the page loads responsively on all device sizes. ✔
* Verify links work as expected 
    * Standard Listing ✔
    * Extended Listing (disabled) ✔
    * Quarterly Listing (disabled) ✔

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Merchandise Page**
* Verify the page loads responsively on all device sizes. ✔
* Verify links work as expected 
    1. Filter category buttons ✔
    2. View Product Details (product card) ✔
    3. Edit product button (visible to admin/superuser only) ✔
    4. Delete product button (visible to admin/superuser only) ✔
    5. Sort by dropdown ✔
    6. Back to top link ✔

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Product Detail Page**
* Verify the page loads responsively on all device sizes. ✔
* Verify links/buttons work as expected 
    1. Keep Shopping ✔
    2. Add to bag ✔
    3. Product Image (opens in new tab - large) ✔
    4. Product quantity buttons (not able to reduce the quantity to below 1) ✔
    5. Edit product button (visible to admin/superuser only) ✔
    6. Delete product button (visible to admin/superuser only) ✔
* Verify sizes dropdown is rendered for products which include sizes ✔

## Product Detail - Listing Token
* Verify 'inactive' listings dropdown is rendered if the product is a listing token ✔
* Verify quantity buttons are removed for 'listing token' product ✔
* Verify quantity of an item cannot be manually adjusted from the default of 1 ✔
* Verify 'keep shopping' button is changed to 'back to listing levels' button ✔

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Add Product Page**
* Verify the page loads responsively on all device sizes. ✔
* Verify only logged admin/superusers can access the 'add_product' template ✔
* Verify form validation prevents user from submitting the form with errors ✔
* Verify that once the form is submitted and validated, the user is redirected to the newly created product - rendering the product_detail template ✔ 

# **Edit Product Page**
* Verify the page loads responsively on all device sizes. ✔
* Verify only superusers can access the 'edit_product' template for ✔
* Check all product content is rendered to the form, ready for a superuser to edit ✔
* Verfify the 'clear' image checkbox works as expected if checked when the form is submitted. ✔
* Verify that once the form is submitted, the user is redirected to the product_detail template for the recently updated product ✔

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Shopping Bag Page**
* Verify the page loads responsively on all device sizes. ✔
* Verify all session bag contents render to the shopping bag template ✔
* Verify totals and delivery is accurately calculated and displayed to the user ✔
* Verify links/buttons work as expected
    1. Product quantity buttons (cannot be reduced below 1) ✔
    2. Update / Remove product buttons ✔
    3. Keep Shopping button ✔
    4. Secure checkout button ✔
* For listing tokens: -
    * Verify update button is removed ✔
    * Verify quantity cannot be adjusted ✔

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Checkout Page**
* Verify the page loads responsively on all device sizes. ✔
* Verify the order summary displays as expected ✔
* User details populate from userprofile (default delivery info, name and email) if registered user ✔
* Save delivery infomation checkbox - if checked form data is added/updated to user profile ✔
* Stripe card element verification/validation works as expected ✔
* Verify buttons work as expected
    1. Adjust bag (returns user to shopping bag) ✔
    2. Complete Order (generates order, redirects to checkout_success) ✔
* If bag total is £0.00 -
    1. Stripe element is not present on the page (checkout_free template rendered) - payment not required to complete order ✔

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Checkout Success Page**
* Verify the page loads responsively on all device sizes. ✔
* Verify the order details displayed are as expected ✔
* Verify all links work as expected ✔
* Verify a confirmation order email is sent to the user :x:

## Checkout Success Fixes
* Order confirmation email was not being received in the deployed webapp for all orders.
    * The code used to trigger sending an email was relocated into the checkout_success view from the paymentintent.successful webhook. Making this change ensured emails were being sent for all orders, including those of £0.00 value.

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **My Profile Page**
* Verify the page loads responsively on all device sizes. ✔
* Verify all links to other profile pages work as expected ✔
* Default delivery information is displayed in the rendered form, if present.
* Verify the 'update information' feature works as expected for the default delivery information ✔

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Order History Page**
* Verify the page loads responsively on all device sizes. ✔
* Verfify all previous orders associated with the userprofile display on this page ✔
* Verify order number links work as expected, rendering checkout_success template with corresponding order details ✔

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **My Listings Page**
* Verify the page loads responsively on all device sizes. ✔
* Verify all listings created by the user, are displayed within card elements on this page ✔
* Verify all buttons on listing cards work as expected 
    1. Goto listing(conversion_detail template) ✔
    2. Edit listing(edit_conversion template) ✔
    3. Delete listing(delete_conversion function) ✔
* Verify the listing status is displayed to the user in the card footer 
    1. Active listing (green text) ✔
    2. Inactive listing (orange text + button to view pricing) ✔

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Saved Listings Page**
* Verify the page loads responsively on all device sizes. ✔
* Verify all listings saved to the userprofile, are displayed within card elements on this page ✔
* Verify all buttons on listing cards work as expected 
    1. View Listing(conversion_detail template) ✔
    2. Remove Listing(remove_saved_listing function) ✔
* Verify the listing status is displayed to the user in the card footer if inactive ✔
* Verify listing cannot be viewed if inactive (View listing button disabled) ✔

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Conversion Management Page**
* Verify the page loads responsively on all device sizes. ✔
* Verify access to this template is limited to superusers only ✔
* Verify all conversion listings are able to be displayed on this template - Using the buttons 'Active Listings' & 'Awaiting Approval' the user will filter displayed content based on the listing status ✔
* Each listing summary is displayed in a card element.
* Card elements contain the following buttons in their footer, buttons function as expected:
    1. View Details (conversion_detail template) ✔
    2. Edit Conversion (edit_conversion template) ✔
    3. Delete Conversion (delete_conversion function) ✔
    4. Contact Seller (displays contact into the card element footer) ✔
    4. Delist / Approve listing (changes listing 'isactive' status) ✔

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **DevTools**

Google DevTools was used within Google Chrome on macOS throughout the development process. 

* Testing responsiveness of the site across several device models. 
    * Media queries are written accordingly to support major devices available in dev tool testing environment.

* Target elements and style with CSS, to test potential changes before coding them into relevant HTML.

* Console used to support the development of JavaScript code.
    * console.log used at various points to check values of variables and function outputs, whilst developing logic for site.
    * Upon site completion - the console was checked for any errors
    * Once the site was completed, the console was checked for any errors on each page ✔:

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **Automated Testing**

## Validating the HTML, CSS and JS code

All of my code passed the following validation tests/services:
- HTML: [W3C Markup Validation Service](https://validator.w3.org/)
- CSS: [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/)
- HTML & CSS [Dead Link Checker](https://www.deadlinkchecker.com/website-dead-link-checker.asp)
- JS: [jshint](https://jshint.com/)

* There were various HTML and CSS validation issues to resolve. These mainly referred to formatting my code and were easily fixable across the site.


## Lighthouse Performance Testing

* The site was testing using Lighthouse in Google Chrome Devtools, with no concerning issues highlighted.

![Lighthouse performance results](documentation/testing/img/lighthouse-testing.png)

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# **User Stories**

## Viewing and Navigation
### User Story 1

### As a site visitor: View a list of products/conversions available
    
* The site navigation is clear and easily allows access to both merchandise and conversions listing pages.
* The home page has a call to action button - allowing users direct access to conversion page, without the use of the navbar.  

### User Story 2

### As a site visitor: View individual product / listing details
    
* In the conversions listings page, each listing has a 'view details' button, it can be clicked to gain access to the conversion_detail template.
* Each product image in the merchandise listings can be clicked to gain access to the product_detail template


### User Story 3

### As a site visitor: Easily view my shopping bag with a total of my purchases at any time.

* In the top-nav element which is fixed to the top of each page, a shopping bag icon is present, it can be clicked to gain access to the bag template to view bag contents.

### User Story 4

### As a site visitor: Learn more about the business and services offered

* Upon visiting the site initally, the site purpose is clearly displayed to users ('WILD MILE CONVERSIONS - A platform to buy and sell unique converted vehicles')
* A scrolling banner at the top of each page promotes services and news to keep the user informed.

## Registration and User Accounts

### User Story 5

### As a site visitor: Easily register for an account

* In the top-nav element, a my_account icon is displayed. When clicked a dropdown will display a link to register.
* Restricted areas of the site for registered users only, will prompt users to sign in or register and provide them with the relevant pages/information to achieve this.

### User Story 6

### As a site visitor: Easily login or log out of the site

* In the top-nav element, a my_account icon is displayed. When clicked a dropdown will display a link to login or to log out.

### User Story 7

### As a site visitor: Easily recover my password in case I forget it

* On the sign-in page a 'forgot password' link will direct the user to input their registered email address, associated with their user account. A link will be emailed to the user to reset their password.

### User Story 8

### Receive an email confirmation after registering to verify my registration was successful

* Newly registered users will need to confirm their email address as part of the signup process. In order to validate their account, they will receive an email from wildmileconversions@gmail.com

### User Story 9

### As a registered user: Have a personalized user profile

* All registered users will have access to 'my_profile' template. This will contain information unique to their user profile, such as order history, saved listings, delivery information and more.

## Sorting and Searching

### User Story 10

### As a site visitor: Sort listings or products - Easily find listings based on price or category which fit my criteria

* Category filtering functionality is embedded into both conversions and merchandise pages, to allow users to display results of matching category criteria.
* Displayed products or listings can be sorted by name, price, category on the page. Merchandise can further be sorted by rating.

### User Story 11

### As a site visitor: Search for a listing using keywords - Easily see what I've searched for and the number of results

* A search bar is present on the conversions page, users may use this to search listing titles and descriptions. 
* The search will return all matching listings and display them on the page. As well as a summary of the search term and the number of matches found.
* This feature has been extended to the merchandise products page.

### User Story 12 + 13

### As a registered user: Save a listing to my profile to easily view the listing at a later date from my profile

* Users can easily use the button 'save to profile' on any active listing on the site. The button is present on both the conversions template and the conversion_detail template.
* Users can easily manage all saved listings in their profile, in the 'saved_listings' page. Easily remove them from the save listings page, using the 'remove_listing' button.

## Selling as a registered user

### User Story 14

### As a registered user: List a conversion on the site Easily

* The site navigation offers users a direct link to 'sell a conversion'. 
* Adding a listing to the platform is completed using a single form, with clear instructions on the 'sell_conversion' template.

### User Story 15

### As a registered user: Receive an email when my conversion is submitted for approval, to verify my listing token has been received and the order confirmed

* The site will automatically generate an order summary and display this to the user at the checkout success page.
* Users will receive an email order confirmation upon completion of an order. The email contains information about listing tokens and how to check the status of a listing in their profile.

### User Story 16 + 17

### As a registered user: Edit, Remove my listings - to keep listings up to date or remove if no longer available for sale.

* In the user profile - my_listings. Users can easily edit their listings by clicking the 'Edit Listing' button, present on the listing card element.
* In the user profile - my_listings. Users can easily delete their listings by clicking the 'Delete Listing' button, present on the listing card element. A confirmation modal will pop up when this is pressed, to confirm deletion with the user before removing it from the database.

### User Story 18

### As a registered user: View how long my listing will be published in my profile so that I'm aware of when the item will no longer be advertised on the site.

* This feature has been added to the future features list for the webapp. Due to time constraints this feature will not be available on launch. The user can still check if the listing is live or not, in the my_listings page of their profile.

### User Story 19

### As a registered user: Engage in conversation with potential buyers - to move forward will potential sale or learn more about a listing.

* Site visitors may find contact information for a seller by clicking the 'contact seller' button on the respective conversion_detail page.
* As a seller, I can update my contact information on the edit conversion page.
* A future feature will allow two-way conversion within the webapp between the seller and potential buyer, in the form of a messaging system - Namely: Message Portal

## Enquiring to purchase a conversion

### User Story 20

### As a site visitor: Easily locate contact information for the seller of a conversion.

* This is covered in User Story 19, please review the content above.

## Purchasing and Checkout

### User Story 21

### As a shopper: Easily select merchandise/items to purchase - size and qty if required.

* The site merchandise section has an intuitive filter and search functionality, to assist the user with finding relevant items/products.
* Product detail pages display information clearly and include options for selecting sizes where applicable.
* Product quantity is easily adjustable using the buttons on the product_detail page.

### User Story 22 + 23

### As a shopper: Be able to review items in my shopping bag before payment, Adjust product quantity.

* The shopping bag page renders a full summary of all items currently in the user's bag.
* Product quantity can be adjusted on the shopping bag page.
* Products can be completely removed from the bag on the shopping bag page.

### User Story 24 + 25

### As a shopper: Check out easily, easily enter payment information, feel secure.

* The checkout page is designed to be easily used, with information clear to the user and the page looks great on all screen sizes, due to a responsive design.
* The payment input section is provided by a third-party recognised business called 'Stripe'. They are widely used and offer secure and fast payment authentication for users.

### User Story 26

### As a shopper: View an order confirmation after checkout.

* Once checkout is complete, a checkout_success page is rendered for the user. It contains all order details and information required about payment and delivery.

### User Story 27

### As a shopper: Receive an email order confirmation after checkout.

* As detailed in user story 15. Users will receive an order confirmation email upon checkout, this will provide users with all information required to review the order details.

### User Story 28 + 29

### As site admin: Add/Edit/Delete merchandise products.

* Site admin can easily find controls to edit and delete existing products on their respective product_detail pages and within the product card element on the products page.
* Site admin can find a link to the 'add merchandise' page in the 'My Account' dropdown nav menu. This will render a simple form, which allows the user to add an item to the merchandise section of the site.

### User Story 30 + 31

### As site admin: Review and approve user listings.

* Site admin can find a link to the  'conversion management' page in the 'My Account' drop-down nav menu.
* The conversion management page hosts the functionality for site admin to view all listings in the database, with controls to display either 'active' or 'inactive' listings within card elements on the page.
* Controls are available within each listing card element to 'approve' or 'delist' from the site as required, as well as controls to 'edit', 'delete', 'view' and 'contact seller'.


<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# User Testing

## My-Mentor

A series of feedback and suggestions had been highlighted during a call on Saturday 30th January 2021. Action has been taken for all of these suggestions and changes to the site and code. 

Any changes are documented below in the section - (Post Review Changes)


<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>

# Post Review Changes

* The following was addressed post-testing and feedback. (changes are detailed in commit history dated 15/04/2021 onwards) :
    1. Remove the sitewide search functionality for conversions - implement function into conversions page only.
    2. Add search function to merchandise/products page.
    3. Add further conditional coding to site navigation, to improve user experience.
    4. Combine manage conversions and approve conversions pages, to create one dynamic page for displaying listings to site admin.
    5. Make fixed height cards in 'my_listings' and 'saved_listings' templates.
    6. Add confirm delete modals for merchandise and products throughout the site.
    7. Remove the home link from sign-in page.
    8. Adjust z-index on 'my-account' dropdown menu, to fix the issue when empty toast messages element was preventing the use of nav dropdown upon sign in.
    9. Create error handling templates for 400,403,404,500 errors.
    10. Move confirmation email code to checkout_success view, to ensure emails are sent to users for all orders.
    11. Update vehicle length, height and width fields in CamperConversion.model from IntegerField to DecimalField(max-digits=3, decimal_places=2)   - to allow upto 9.99 values to be entered.
    12. Change the z-index of the back to top button, so that it works when overlapping the site footer.

<div align="right">
    <a href="#contents"> ⇧ Back To Contents </a>
</div>