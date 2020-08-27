<h1 align="center">Delitaly - Milestone 4</h1>

[View the live project here.](https://delitaly.herokuapp.com)


Hello! My name is Renato, and I’m a student at Code Institute. This is my fourth Milestone, and in this project I used HTML, CSS3, Bootstrap (first time), Javascript, Python, Django and Stripe.
I chose to build an e-commerce based on an existing business here in Cork (Ireland), Delitaly, this gave me more inspiration, and also the chance to understand how complex is a real e-commerce. At every feature added to this project, I realised that I could have added other hundreds. Learning how to code just open your mind to infinite ideas that you could build and apply to the project you are working on, and other project that you could build. Of course many of these ideas need much experience to be developed.

I hope you like this project.


## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, you will be enraptured straight away by colourful Italian food on a white background, this will make you feel immediately engaged with the subject.
        2. The Visitor will find some categories as soon as they open the homepage with no effort.
        3. The index has a main navbar, the navbar has five categories, easy to explore, and subcategories. The user will find it simple, easy, clean, a good experience, and at the same time rich in content. 
        4. The index has also a search bar, in case the user would like to find a product straight away.
        5. Next to the Navbar a visitor will easily find a profile icon and a shopping bag.
        6. Just below, there is also a banner with an offer for free delivery to get the attention, shipping cost is very relevant when you buy online.
        7. The same banner also offers further links to reach the shop in different ways, Facebook, Instagram, Whatsapp, Email, and a link to see the location on Google Maps. The business doesn't have Instagram yet, but I added the hashtag since they are often tagged.

    -   #### Returning Visitor Goals

        1. A Returning Visitor will find always new products and speciality homemade, to have also the chance to find traditional Italian products as well as they make in Italy.

    -   #### Frequent User Goals
        1. A Frequent User will always find new offers, new products, a clean UI, clean Design, a good interaction with the business, the whatsapp link will also give the chance to contact directly the business straight away, asking for info, availability, and any other info they would need.

    -   #### ADMIN User Goals
        1. The Admin(Superuser) will find all the CRUD operations available in order to fully manage the products and the shop.
        2. A simple user(not Superuser) can register in order to have his own information saved in the system, always available for future purchases, can buy products as any other online shop.


-   ### Design
    -   #### Colour Scheme
        -   Main Background: #ffffff; (white)
        -   Footer and main banner background: #343a40; (Bootstrap bg-dark - dark grey)
        -   Links and buttons: Green, #597718, #90A74C
        -   h1, h2, h3, h4: #37490f (green)
        -   h5, h6: #597718 (green)
        -   Paragraph: #555 (grey)

    -   #### Others
        -   Buttons and Forms have 5px border radius

    -   #### Typography
        -   'Montserrat'

*   ### Wireframes
    -   Started with Balsamiq, but I continued simply coding on my VS Code since Bootstrap made it much easier.


## Features

-   Responsive on all device sizes (Tested)


## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used
-   [Django](https://www.djangoproject.com)
-   [Bootstrap](https://getbootstrap.com)
-   [EmailJS](https://www.emailjs.com/)

1. [Heroku](https://www.heroku.com/)
    - Heroku was used to deploy the [website](https://delitaly.herokuapp.com). 
2. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
3. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
4. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Montserrat' font.
5. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used to add all the icons throughout the project.
6. [AWS](https://aws.amazon.com) 
    - Amazon Web Server was used to store CSS and Images.
7. [Stripe](https://stripe.com/)
    - Stripe was used to manage payments
8. [Adobe-Illustator](https://www.adobe.com/ie/products/illustrator.html)
    - Adobe Illustrator was used to create the logo
9. - NOTE: All the images have been accurately chosen on many different png providers such as: [subpng](https://www.subpng.com/), [nextpng](https://www.nextpng.com/), [pngio](https://pngio.com/), [pngfind](https://www.pngfind.com/), and many others through the web.




## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - Errors fixed, replace background-color: none with background-color: #ffffff.
-   Validator with HTML has been a bit harder because of Python and some issues that HTML kept finding because of bootstrap. No real issues.


### Further Testing

-   The Website was tested on Google Chrome, Firefox and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7 Plus, iPad.
-   A large amount of testing was done to ensure that all pages were linking correctly.


### Known Bugs

- The select/option tags in the forms on the website were not adapted to Safari because of lack of time. I could fix this in my previous Milestone, but I could not complete this with this last one. My apologies.
- In this project, unlike the previous one, I didn't remove outline on buttons or links (i.e. outline: none;), this in order to match needs for who can't use a mouse or have a visual impairment, where outline is essential when navigating a web document using the TAB key (or equivalent).

## Deployment

### GitHub Pages, Heroku and Visual Studio Code

-   The [project](https://delitaly.herokuapp.com) was deployed to [GitHub](https://github.com/Renato79/delitaly) Pages linked to [Heroku](www.heroku.com).
-   Heroku manages app deployments with [Git](https://git-scm.com/), the popular version control system.
-   To code this project I used a code editor on my computer, [Visual Studio Code](https://www.visualstudio.com/)for [macOS](https://en.wikipedia.org/wiki/MacOS)  

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Renato79/delitaly)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Renato79/delitaly)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/Renato79/delitaly/
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/Renato79/delitaly/
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Content

- Text into the pages Policy and Shipments have been taken online and adapted to my project.
- Almost all the product descriptions have been found online.
- Info like prices, titles, scores have been invented.
- README.md used is a [Code Institute](https://codeinstitute.net/) sample and was found [here](https://github.com/Code-Institute-Solutions/SampleREADME/blob/master/README.md)


### Acknowledgements

-   I will be always grateful to Code Institute for the help that they provided when I needed, during this particular difficult year. I found Code Institute an amazing experience, and I wish it could continue. Thank you!
                                                                                                                                
                                                                                                                                
