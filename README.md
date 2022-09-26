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


# SEO

# Design

## Wireframes
## COlor Palette
## Fonts

# Database Model & Schema

# Design


## Wireframes
## Color Palette

The following color palette was used for the design of the site. The objective was to use a color palette with a high degree of contrast. The color scheme was derived from the [dmg theme](https://github.com/monkeytypegame/monkeytype/blob/master/frontend/static/themes/dmg.css) from the MonkeyType typing application []

| Color             |Hex Code            |Tailwind            |                    |
|-------------------|--------------------|--------------------|--------------------|
| Background        |   #dadbdc          |  zinc 100           |                    |
| Main Color        |   #ae185e          | fuchsia-800                   |                    |
| Caret Color       |   #384693          | blue-900           |                    |
| Sub Color         |   #3846b1          | indigo 600         |                    |
| Sub Alt Color     |   #bec1d2          | slate-300          |                    |
| Text Color        |   #414141          | slate 600          |                    |
| Error Color       |   #ae185e          |                    |                    |
| Error Extra Color |   #93335c          |                    |                    |
| Extra Color       |   #80a053          |                    |                    |
| Error Extra Color |   #306230          |                    |                    |
| Background Focus  |   #306230          |                    |                    |




## Fonts
# Database Model & Schema
# Features
  ## Implemented Features
  ## Future Additional Features
# Testing

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







