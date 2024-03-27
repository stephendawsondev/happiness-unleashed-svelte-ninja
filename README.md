
<br>

<div align="center">
    <h1 align="center"><strong> :relaxed: Happiness Unleashed :relaxed: </strong></h1>
    <p align="center"> - The app inspiring you to do more good -</p>
    <div> This project was made as an entry to <strong>World Happiness</strong>-hackathon organized by <img width="50"src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png"/> </div>
    <img align="center" src="https://res.cloudinary.com/dyoueyepq/image/upload/v1711376637/pyd0uu3jmz4sc8flkgfh.png" alt="HackathonHappy" width="800" />  

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

[View Live Version Here](https://happiness-unleashed-b388dd1f8f63.herokuapp.com/)
    
</div>

## Intro
Welcome to Happiness Unleashed! In a busy world where everyone's got a lot on their plate, being kind can sometimes get lost in the shuffle. That's where the Happiness Unleashed stands out as a guiding light. It's easy to feel overwhelmed by the demands of our schedules or the complexities of the world around us, but kindness has the power to break through these barriers.

**Picture this**: in a world where everyone is rushing to meet deadlines, fulfill obligations, and chase success, a single act of kindness can make someone's day better. Whether it's a genuine smile, a helping hand, or a nice gesture, these small acts can uplift spirits, foster connection, and create ripple effects of positivity.

We wanted to allow our users to spread a sense of happiness by using our happiness-unleashed challenges that inspire others to pay it forward. Imagine the happiness you feel after making someone smile, knowing you've made a difference, and the happiness that comes from spreading kindness. Let's challenge ourselves to break free from the busyness and self-absorption of modern life.

Together, we can make the world a brighter, happier place where each of us has the power to unleash waves of happiness and countless smiles. 

## Criteria
In this section, we will briefly discuss how our team addressed the applicable criteria:
-  CSS framework Bootstrap was used to built our user-friendly design
-  GitHub Project includes user stories and a detailed README.md; https://github.com/users/HMuraja/projects/7/views/1
-  We came up with a application to remind, engage and motivate the user to act kind in their daily live
-  Project demonstrates responsiveness, accessibility, and thorough testing
-  Beyond standard requirements these are our more innovative features/functionalities: create user accounts, create individual user posts, create own acts of kindness  
-  As a team we worked together in on respository, splitted task according to interest and skills
    - Backend focus: Stephen, Ann
    - Frontend focus: Felipe, Claudio, Soundarya and Florian
    - Content creation, images and documentation: Soundarya, Florian
    - Scrum Master: Hilla


## Goal
Our app aims to make kindness a daily habit by offering simple challenges that inspire users to turn their good intentions into actions.

- ➡️ **Problem**: In a world where kindness is plentiful but easily overlooked in the chaos of everyday life, our app provides a platform for users to share their acts of kindness, sparking a chain reaction of positivity.
- ➡️ **Objective**: We provide an application that fosters and simplifies kindness and happiness and can be integrated easily within our daily rountine.
- ➡️ **Target Audience**: People who are willing to include more happiness and kindness in their world by using smart applications.
- ➡️ **Benefits**: By promoting kindness, our app can create a more compassionate and connected community, where individuals feel happier and more fulfilled.

## Technologies
"Happiness Unleashed" is crafted using a blend of powerful technologies including Django for robust backend functionality, Bootstrap for sleek and responsive frontend design, and a mix of HTML, CSS, Python, and JavaScript to deliver a seamless and joyful user experience.

- **Programming**:                     HTML, CSS, Python, [Django]( https://github.com/django/django), [Bootstrap](https://getbootstrap.com/docs/5.3/layout/containers/)
- **Database**:                         [ElephantSQL](https://www.elephantsql.com/)
- **Image and Static-File Database**:   [Coudinary](https://cloudinary.com/)
- **Deployment Platform**:              [Heroku](https://www.heroku.com/home) 

## Features
- **Nav Menu** - The site's structure is visually represented within the navigation bar. It links to all the features accessible for the user. Menu is available on each page.

- **Landing Page** - Also the Home-page, actively encourages user engagement by proposing **four** acts of kindness that are randomized from a library of options. Refreshing page regenarets new acts of kindness.
- **View Act of Kindess Page** - If Act of kindness is clicked on the home-page, it leads to a new page displaying the act of kindess image and new 

- **Posts Page** - Users can view posts other usrrs have created to share how they have crried out their acts of kindness. Each post consists of description text, optional image, author of the post and related Act of Kindess.

- **About Page** - Users find a detailed explanation of the application's purpose and the developers' underlying motivations.

- **Meet the team** - Meet the team and read more about each member of the team.

- **Accounts** - When user is not logged in the navbar displays a dropdown of **"Log in"** and **"Sign Up"**-options, leading to respective forms. 

- **User Navigation Icon** - Once logged in Accounts-nav item changes to display username of the logged in user and a profile image. If clicked a dropdown menu appears, showing a "Log out"-link, "Admin" if logged in user is a superuser and "My Profile".
- 
- **My Profile** - Once Logged in, user can view their profile with basic information, like their name, location and email adress, these details can be changed. Logged in usr can also go into the acts-of kindness and save them onto their account, to "track" and "quantify" the amount of good they have performed. 

- **Post Form** - On the profile user can click on individual act of kindness and make a post describing how they carried out the given act of kindess. User can add a description and photo to detail the event. Posting will add a post on to the posts page.

## Design Process
**WEB PAGES**   
Above schema was made in the beginning of the project to help the team visualize the final application and pages. Apart of few details the final application ended up respecting the original plan.
<details>
    <summary>View the Schema</summary>
    <img src="images_README/app_structure.PNG" alt="image shows structure of the app. Landing page, login page, sign up page, profiles and more" width="400">
</details>

**WIREFRAMES**   
Here are shwon a few wireframes we used to set up the subpages. During the project slight adjustments has been made.
<details>
    <summary>View the Wireframes</summary>
    <div>
        <img src="images_README/wireframe.PNG" alt="Image shows wireframe" width="200">
        <img src="images_README/wireframe1.PNG" alt="Image shows wireframe" width="400">
        <img src="images_README/wireframe2.PNG" alt="Image shows wireframe" width="200">
    </div>
</details>

**ENITITY RELATIONSHIP DIAGRAM**   
Entity Relation Diagram (ERD) was completed before starting the process to visualize the data structures and models.
<details>
    <summary>View the Diagram</summary>
    <img src="images_README/model_structure.PNG" alt="image shows structure of database." width="400">
</details>

## Testing

- user interface/ experience testing
- url testing, internal, external
- test form submit
- content 
- responsiveness
- accessability
- images have alt types, aria labels


## Credits
- [Bootsrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/): Used to during the project to troubleshoot and implement features to the application.
- [Django Documentation](https://docs.djangoproject.com/en/5.0/): Documentation used to troubleshoot errors. 
- [Canva](https://www.canva.com/): USed to design application logo and illustrations.
- [Am I Responsive](https://ui.dev/amiresponsive): used generate RedMe image of the final project.
- [Unsplash](https://unsplash.com/): sources images for the application.
- [FreePik](https://www.freepik.com/): sourcced illustration for the webpage.
- [Favicon generator](https://favicon.io/): Used to convert logot to favicon.
- [Markdown Badges](https://github.com/Ileriayo/markdown-badges): Source for the badges used in this documentation.
