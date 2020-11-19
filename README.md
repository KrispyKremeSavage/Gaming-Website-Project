Welcome to P4CharlieB's Project 

+~~~+

Project Plan: https://docs.google.com/document/d/1eBgE4SZKjJSPiQAgvamVGXAs8vmIWPWzyyUT6sc_re0/edit

+~~~+
October 23rd Directory:
Home Page: Upon opening the website link, you are taken to a website with our directory bar, header, and title.

NavBar Functions:
  Directory: Clicking the directory bar will bring you to the home page

  Home Screen: Clicking Home Screen will bring you to the home page

  Project Plan: Clicking Project Plan will bring you to a page containing a button to our project plan on google docs

  October 23rd Requirements: Clicking this button will bring you a dropdown menu
    Github: Clicking this will take you to a page with a button
      Group Github Project: clicking this button will take you to the github project

    IntelliJ:

    Project Themes: Clicking this will take you to another page filled with buttons
      Kaila's Website Art: this google drive has all the files to the digital art for this website created by Kaila

    Playgrounds: Clicking this will take you to another page filled with buttons

      Kaila's Website Playground: this playground was used while watching multiple youtube tutorials on how to utilize flask functions

      Kaila's Image Website Test:
      this playground was used while trying to test implementing her art into flask

      Eshaan's Pacman Playground: this playground was used to test out the pacman game for the gaming website

      Eshaan's Webpage Playground: this playground was used to figure out how flask websites work

      Calvin's Playground 1:

      Calvin's Playground 2:

      Brent's Playground 1:

      Brent's Playground 2:

Show each individual having a code checkin and comment

1 minute video encouraged, provide as a link from your Portfolio

+~~~+
Assignments and Purpose:
  Kaila:
    Website Artwork: When the proper research is done, we hope to have some custom elements implemented into the website.

    Trivia Game: Kaila took care of a trivia related game during our last project, and we hope to implement that idea as one of the games in our current project.
    
    Project Plan: Kaila has been in charge of organizing project plans and read.me's in regards to all our projects, so she is continuing to help make our projects more organized.

  Brent:
    Possible Ascii: Hopefully ascii art will be able to be an element in regards to the games we implement into our website.

    Games: Brent will be in charge of making sure the games we created are connected to the website.

    Website Design: Brent will be contributing to the website designs and concepts.

  Eshaan: 
    PacMan: Eshaan added a new, refined version of Pac Man on our website. It was based off of a potential model we
    were planning on using for our last project, but it got scratched.

    Pong: Eshaan added Pong to our website as well. This was a newly thought idea for more games.

    Snake: Eshaan added Snake to our website as well. This was a newly thought idea for more games.

    Website Code: Eshaan helped in regards to figuring out the science behind website code.

  Calvin:
    Design: Calvin will also contribute to the design aspects of the website.

    Modules: Calvin will be in charge of organizing modules for the project.

    Games: Games he created in our last project will hopefully be implemented into our current assignment.

How To Work With our Gaming Website

-Copy and paste this link into your search engine: http://104.63.255.27/
    -This will direct you to our website's homepage using an application route that has been defined by the function
    "home"
    -The function renders the html file named "home.html" which contains the html code for all of the games and their 
    specific icons (which are png images), using hrefs to direct the user to the specified app routes using defined
    functions, much like for the homepage, making the icons act as buttons
    -The file "base.html" contains the html code used for the navigation bar and the drop down menus, mainly using
    the variable "class" to equate it to the "nav-bar" function in order for it to enact as such, followed up by using
    hrefs to direct the user to the specified app routes using defined functions, also making the drop down options
    enact as buttons
        
-Trivia
    -When clicking on the png image for Trivia, the png image enacts as a direct path to the Trivia Game by using
    an href that is set to equal the application route to the function itself (/trivia), along with a url_for command
    being used to interlink the png image and the href together so that the image can act as a button
    -The code within mainly consists of if-else statements to process the answers given either as true or false, and
    there is also a timing delays to allow the user to prepare themselves an answer
   
-Random Number Generator (RNG)
    -When clicking on the png image for RNG, the png image enacts as a direct path to the RNG Game by using
     an href that is set to equal the application route to the function itself (/randomnum), along with a url_for command
     being used to interlink the png image and the href together so that the image can act as a button
    -The code in the game is based around "import random," as it uses the command "number = random.randint(1, 10)" to
    pick the number the user has to guess between 1 and 10
    -The code within also consists of a "while" statement that only allows the user up to 4 guesses, if statements to 
    indicate whether the user guessed too high or low, and a final "if else" statement to state if the user guessed 
    correctly OR if the user failed to guess correctly
    
-Battleship
    -When clicking on the png image for Battleship, the png image enacts as a direct path to the RNG Game by using
     an href that is set to equal the application route to the function itself (/), along with a url_for command
     being used to interlink the png image and the href together so that the image can act as a button
    
  
    



