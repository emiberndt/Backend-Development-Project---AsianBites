## Code Institute - Backend Development Milestone Project

This project aims is to provide a place where the user can search for books, the information about them, 
and a review writen by the user whom uploaded the book.
They will be able to upload new books and write their own review about it.

Live on Heroku pages [here](https://what2read.herokuapp.com/)

## Table of Contents:

- [UX](#ux)
  - [User Stories](#user-stories)
  - [Strategy](#strategy)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Integrations](#integrations)
  - [Workspaces](#workspaces)
- [Resources](#resources)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Media](#media)
  - [Code](#code)


## UX

### User Stories

- I want to easily understand the purpose of the site.
- I want to easily sign up to the website.
- I want to easily log in on my profile.
- I want to read information about books, and reviews about them.
- I want to have th option to be refered to where to buy a book.
- I want to upload books, their information, and write reviews about them.
- I want to have the option to edit or delete my own book reviews.

### Strategy

- Create a place where the users can create information about books, and add to the book library.
- Create a place where the users can create reviews of books.
- Create a place where users can browse through the book library, and read information and reviews about books.
- Create a place that is easy for the users to use.

### Scope

- Allow users to register as a user to the website.
- Allow users to log in into the website.
- Allow users to create, read, update and delete their own reviews.
- Allow users to create, edit, and delete their own reviews.

### Structure

Keep the website as simple as possible, to allow the users interaction with the site easy to use.

### Skeleton

- Navigation bar
  - **View Reviews** -  Description letting the user knows what the website is all about. 
  Browser/Search in the book library. Users can edit/delete their own reviews.
  - **Log In** - Allows exixting users to log in to their profile.
  - **Register** - Allows non-users to register to become a user.
  - **Profile** - After users log in, they are redirected to their profile, where they can 
  choose to add/read reviews.
  - **Add Review** - Form for the users to fill with books information, and write their own review, 
  and publish it to the book library.
  - **Log Out** - Will log out the users from their profile, redirecting them to the log in page.

### Surface
The overall UX is clean, simple, and similar on all pages to keep consistency.

### Colors:
background-color: #90a4ae

Colors from [Materalize](https://materializecss.com/):
- #000000 black
- #263238 blue-grey darken-4
- #9e9e9e grey
- #ff5722 deep-orange
- #ffffff white

### Typography :

[Google Fonts - font-family: 'Comfortaa', cursive;](https://fonts.google.com/specimen/Comfortaa?query=comfor)

## Technologies Used

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)

### Integrations

- [Google Fonts](https://fonts.google.com/)
- [Materalize](https://materializecss.com/)
- [jQuery](https://jquery.com/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [MongoDB](https://www.mongodb.com/)

### Workspaces

- [Gitpod](https://www.gitpod.io/)
- [GitHub](https://github.com/)
- [Heroku](https://www.heroku.com/)

## Resources

- [W3Schools](https://www.w3schools.com/) - General resource.
- [Stack Overflow](https://pt.stackoverflow.com/) - General resource.
- [Youtube](https://www.youtube.com/) - General resource.
- [Code Institute](https://learn.codeinstitute.net/) - Backend Development Module

## Code Validation

- [W3C](https://validator.w3.org/) - HTML Markup Validation.
- [W3C](https://jigsaw.w3.org/css-validator/) - CSS Validation.
- [JSHINT](https://jshint.com/) - JavaScript code warning & error check.
- [PEP8 online](http://pep8online.com/) - PEP8 validator.

## Testing

## User Stories

I want to easily understand the purpose of the site.

- **TEST**: When the users load the page they see the book library, and a brief explanation of what 
the site is about.

I want to easily sign up to the website.

- **TEST**: In the navbar, there is a link to register, which redirects to the Register page.

I want to easily log in on my profile.

- **TEST**: A simple fill-in form allows the user can easily login into their profile.

I want to read information about books, and reviews about them.

- **TEST**: After the user register/login to their profile, they will be redirected to their Profile page, 
where they 
can choose to read information about books, and reviews about them.

I want to upload books, their information, and write reviews about them.

- **TEST**: The Add Review page allows the users to fill in a form, to create an input in the book library. 
This will include like, book title, author, category, about the book in general, url for picture of the book, 
and url for where the book can be purschased.

I want to have th option to be refered to where to buy a book.

- **TEST**: Whenever a new book is added to the library, there is an input field where they can add the URL 
to a place where the book can be purchased. This feild is required in all the books in the library.

I want to have the option to edit or delete my own book reviews.

- **TEST**: There are buttons at the bottom of each of the user own book reviews, that can be edited or delete.

## Navigation links
- Made sure all links in the navigation bar works as they're suppose to.

- **View Reviews**:
    - Checked if the book library works as it should. Diplaying all the required information.
    - A logged in user will see the buttons 'edit' & 'delete' on the reviews that they've submited themselves.
    - If a user wants to delete a modal will appear for the user to confirm that is the action they want to make.
- **Register**:
    - Checked if the register process workes as it should. When the user has registered the log in information, 
    the user will be redirected to the correct page - the profile page.
- **Login**:
    - Checked if the log in process workes as it should. It will flash the correct messages when incorrect 
    username/password is submited. When it is the correct log in information the user will be redirected to 
    the correct page - the profile page.
- **Profile**:
    - Checked if the cards redirected to the correct pages 'Add Reviews' & 'Write Review'.
    - Checked that the profile page welcomed the user with it's username.
- **Add Reviews**:
    - Checked if the book form works as it should. Diplaying all the inputs.
    - Checked that the fields will require an input in each field of the form, if no information is provided the line will go red.
    - Checked if the book review is sent to the book library (view reviews) correctly.
- **Log out**:
    - Check if the user is logged out from their profile correctly.
    - Checked if a flash message confirms that the user has been signed out from the profile.

## Responsive Test
- [Am I Responsive](http://ami.responsivedesign.is/)
- Devtools test, everything displays as it should from 300px width up to 1920px:
Devices Iphone 8(375px), Iphone 11(414px), Xiaomi Redmi 9(393px), medium laptop(1280px), 
large desktop screen(1920px).

## Deployment

### Project Creation
- To create this project the [Code Institute Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template) was used.
- I was then directed to create new repository from template page and entered the repository name for the project, then clicked create 
repository from template button.
- My repository on GitHub ---> Gitpod button ---> my workspace.

### Deployment to Heroku
This project is deployed on [Heroku](https://www.heroku.com/).
- Go to [Heroku](https://www.heroku.com/) and login.
- On the dashboard, click on the 'New' button and select 'Create new app'.
- Enter the app name and select the closest region.
- In the 'Settings' tab, go on 'Config Vars' and add Configuration Variables from the project's env.py file.
- In the menu select the 'Deploy' option.
- Under 'Deployment method' select the GitHub option and search for your GitHub repository.
- Select Automatic deploys from the main branch and click 'Deploy Branch'.


## Credits
### Media
**Pictures**:
- [Add Book Review](https://pixabay.com/photos/typewriter-vintage-old-1248088/) from Pixabay, by: Devanath
- [Read Book Review](https://pixabay.com/photos/paper-heart-symbol-romance-1100254/) from Pixabay, by: DariuszSankowski

### Code
 - Code Institute – Lesson on Flask project, by: Tim Nelson
-  [Materialize](https://mariogusman.github.io/MS1-Bookdrops) A modern responsive front-end framework based on Material Design.
