# RetroPc E-Commerce Website

An ecommerce website for the selling of vintage PC hardware

# Objectives

## User Stories

### Viewing and Navigating
- As a **shopper** I would like to **view a list of products**
- As a **shopper** I would like to **view individual product details**
- As a **shopper** I would like to **easily view the total of my purchases at any time**

### Registration and User Accounts
- As a **site user** I would like to **easily register for an account**
- As a **site user** I would like to **easily login / logout**
- As a **site user** I would like to **easily recover my password**
- As a **site user** I would like to **recieve a confirmation after registering**
- As a **site user** I would like to **have a personalised user profile**
### Sorting and Searching
- As a **shopper** I would like to **sort the list of products**
- As a **shopper** I would like to **select the product category**
- As a **shopper** I would like to **sort multiple categories simultaneously**
- As a **shopper** I would like to **search for a product by name or description**
- As a **shopper** I would like to **see what I've searched for an the number of results**
### Purchasing and Checkout
- As a **shopper** I would like to **select the quantity of product when purchasing**


# Marketing

## Marketing Strategy

## Facebook Business

A mockup of a Facebook business page has been created for the retro-pc webiste. As this was A real Facebook marketing site could be used to advertise the business, promote the products sold on the website and communicate directly with customers. 

<details>
  <summary><strong style="color:skyblue">Facebook Marketing Page:</strong></summary>
  <img src="./docs/images/retro-pc-fb-business-page.png" alt="navbar"/>
  </details>

## Newsletter Signup

A newsletter signup form was implemented via a Django form. This allows users to enroll in the site newsletter. Details of users signed up to the newsletter can be accessed in the administration backend.

On signing up to the newsletter, a toast is posted confirming the subscription. If a user already is a subscriber; they receive a toast confirming that they have already subscribed to the newsletter and no new data is posted to the database.

In addition to capturing the user's email, the date that the user subscribed to the newsletter is also recorded.

<details>
  <summary><strong style="color:skyblue">Newsletter Form:</strong></summary>
  <img src="./docs/images/newsletter-form.png" alt="newsletter-form-image"/>
  </details>

<details>
  <summary><strong style="color:skyblue">Newsletter Admin Panel:</strong></summary>
  <img src="./docs/images/newsletter-sub-list.png" alt="newsletter-admin-panel"/>
  </details>  

<details>
  <summary><strong style="color:skyblue">Newsletter Subscriber Detail:</strong></summary>
  <img src="./docs/images/newsletter-subscriber.png" alt="newsletter-subcriber"/>
  </details>  

# SEO 

# Design

## Wireframes

## Color Palette
A broad color palette was chosen for the site with a range of complimenting colors chosen. In choosing the color palette, my objective was to select a color palette that would create a strong visual identity with a number of colors with high contrast.

In defining the colors in the HTML code, custom [Tailwind color codes](https://tailwindcss.com/docs/customizing-colors) were defined; the hex codes corresponding to the custome codes were as follows:


| Color          |Hex Code        |
|----------------|----------------|
|      Yellow    |  `#D97706`     | 
|      Blue      |`#235789`       |
|      Black     |`#000000`       |
|      White     |`#F4F4F5`       |
|      Red       |`#9B1D20`       |
|      Green     | `#3F8D48`      |
|      Pure-white| `#FFF`         |
|      Gray      |`#cbd5e1`       |




## Fonts

# Database Model & Schema

# Design


## Wireframes

- Footer
- Header
- Homepage
- Store Page
- Login
- Logout
- Signup
- Cart
- Checkout
- Product Adminsitration


## Color Palette

The following color palette was used for the design of the site. The objective was to use a color palette with a high degree of contrast. The color scheme was derived from the [dmg theme](https://github.com/monkeytypegame/monkeytype/blob/master/frontend/static/themes/dmg.css) from the MonkeyType typing application []






## Fonts
# Database Model & Schema
# Features
  ## Implemented Features

  - Toast Functionality
  - Newsletter Sign-up Form
  - Admin Product Management
  - Payment Integration
  - User Authentication 
  - Custom 404 Page


  ## Future Additional Features
# Testing
Test of the site is documented in the TESTING.md file

# Deployment

## Local CLone
In order to make a local clone, the recommended approach is to use the command line interface. The following steps should be taken :

- Navigate to the repository [website](https://github.com/eoinlarkin/retro-pc)
- By clicking on the `Code` button, it is possible to copy the HTTPS link for the repository
- Open the commandline interace on the local computer and navigate to the working directory into which you wish to clone the repository.
- Open commandline interface on your computer
- Enter the following command:  
  `git clone https://github.com/eoinlarkin/retro-pc.git`
- Press Enter. Your local clone will be created.

## Heroku Deployment
Heroku was chosen as the hosting platform for the application.

In order to deploy the application to Heroku, the following steps should be followed:

- Create a `requirements.txt file: pip freeze > requirements.txt`

- Define a Procfile with the following content for use by Heroku; this should sit in the the root directory: web: gunicorn trax.wsgi

- Create a new application in Heroku.

- Add the following Heroku Resources:
  - Heroku Postgres  

- Define the following Environmental Variables in Heroku:

  |Key	          | Value                         |
  |---------------|-------------------------------|
  |DATABASE_URL   |Heroku postgres database URL   |
  |SECRET_KEY     | application secret key        |

- Create the database schema locally by running the following Django commands:
`python manage.py makemigrations`  
`python manage.py migrate`

- Create a superuser for the application: python manage.py createsuperuser

- Add the hostname of Heroku app to allowed ALLOWED_HOSTS in settings.py: `ALLOWED_HOSTS = ['Heroku app URL', 'localhost]`

- Push the code to GitHub

- Ensure the Heroku CLI is installed and authenticated. Link the local repository to the Heroku Application with the following command:  
`heroku create -a APP_NAME`

- Push the code to Heroku with the following command: git push heroku

# Technologies Used
  ## Languages
  ## Tools


- [VScode](https://code.visualstudio.com/)
  All coding was completed in VS Code.
- [Heroku](https://www.heroku.com/)
  Heroku was used for the deployment of the app.
- [Black])(https://github.com/psf/black)
  Black was used as the Linter for Python files.
- [Stripe](www.stripe.com)
  Stripe was used as the payments platform.
- [Django](https://www.djangoproject.com/)
  The Django framework was used to develop the site.
- [TailwindCSS](https://tailwindcss.com/)
  TailwindCSS was used as teh CSS framework to accelerate development of the site.
- [coolors.co](https://coolors.co/)
  Potential site palettes were tested with Coolors.
- [Figma](https://www.figma.com/templates/wireframe-kits/)
  Wireframes for the site were generated using Figma
- [gauger.io](gauger.io)
  This website was used to generate the favicon using an icon from Font Awesome.
- [Markdown TOC](https://ecotrust-canada.github.io/markdown-toc/)
  For generating the formatted table of contents in markdown

# Credits
  ## Libraries
  ## Code

  - **[Sticky Footer](https://stackoverflow.com/questions/59812003/tailwindcss-fixed-sticky-footer-on-the-bottom)**  


  - **[CSS Not Rendering Locally](https://stackoverflow.com/questions/35557129/css-not-loading-wrong-mime-type-django)**

  - **[404 Error](https://www.vectorstock.com/royalty-free-vector/power-plug-and-cloud-icon-in-shape-on-a-white-vector-29024655">)**
 
 - **[Custom Tailwind Fonts](https://blog.logrocket.com/how-to-use-custom-fonts-tailwind-css/)


  ## HTML / CSS
  ## Images
    - Cover image sourced from Unsplash
      https://unsplash.com/photos/yP89apz2TAA
  ## Other
- `venv` was used to manage the python dependencies 







