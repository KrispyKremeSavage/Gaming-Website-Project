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

-Copy and paste this link into your search engine: http://104.63.255.27/ (should take you to Homepage)
    
    -This will direct you to our website's homepage using an application route that has been defined by the function
    "home"
    -The function renders the html file named "home.html" which contains the html code for all of the games and their 
    specific icons (which are png images), using hrefs to direct the user to the specified app routes using defined
    functions, much like for the homepage, making the icons act as buttons
    -The file "base.html" contains the html code used for the navigation bar and the drop down menus, mainly using
    the variable "class" to equate it to the "nav-bar" function in order for it to enact as such, followed up by using
    hrefs to direct the user to the specified app routes using defined functions, also making the drop down options
    enact as buttons
    -The homepage uses Jinja and Bootstrap to format the structure of the homepage and where the top bar is placed in 
    relation to everything else
        
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
     an href that is set to equal the application route to the function itself (/battleship), along with a url_for command
     being used to interlink the png image and the href together so that the image can act as a button
    -Uses "os" and "random" packages to randomize the location of the battleships
    -Uses if, else, and elif statements to indicate whether the user got a hit or missed

-Rock Paper Scissors
    
    -When clicking on the png image for Rock Paper Scissors, the png image enacts as a direct path to the RNG Game by using
     an href that is set to equal the application route to the function itself (/rocks), along with a url_for command
     being used to interlink the png image and the href together so that the image can act as a button
    -Uses "random" package to randomize whether the computer chooses rock, paper, or scissors
    -Uses if else statements to state if the user beats the computer with the option the user picked or if they lost with
     the option they picked
     
-Pong
    
    -When clicking on the png image for Pong, the png image enacts as a direct path to the RNG Game by using
     an href that is set to equal the application route to the function itself (/pong), along with a url_for command
     being used to interlink the png image and the href together so that the image can act as a button    
    -Uses "turtle" package to create shapes of the paddles and ball, and maintain them while they are in motion
    -Uses if and elif statements to keep track of how the ball bounces off of the paddles and how the score is tracked
     when a paddle misses
     
-Pac Man

    -When clicking on the png image for Pac Man, the png image enacts as a direct path to the RNG Game by using
     an href that is set to equal the application route to the function itself (/pacman), along with a url_for command
     being used to interlink the png image and the href together so that the image can act as a button
    -Uses "pygame" and "app_class" to treat the program as an application and a functioning game that uses Python
    -Functions used to control players speed, direction and coin collecting, along with the enemies being used to 
     track the player
    -Uses text files and a png image to form the maze for the player and for them to move around it properly (no breaking
    through walls and cheating)

-Tic Tac Toe

    -When clicking on the png image for Tic Tac Toe, the png image enacts as a direct path to the RNG Game by using
     an href that is set to equal the application route to the function itself (/tics), along with a url_for command
     being used to interlink the png image and the href together so that the image can act as a button
    -Creates a variable for the board to assign naumbers to certain positions on the board
    -Uses if else statements to track both of the users plays on the board to see who gets three in a row first
    -Uses an if else statement to ask if the player wants to play again or quit at the end
    
Snake

    -When clicking on the png image for Snake, the png image enacts as a direct path to the RNG Game by using
     an href that is set to equal the application route to the function itself (/snake), along with a url_for command
     being used to interlink the png image and the href together so that the image can act as a button
    -Uses "curses" and "randit" to randomly place fruits on the board where the snake roams
    -Uses if else statements to increase the size of the snake when fruit is consumed and when the snake hits the wall/
    eats itself

Drop-Down Menus

    -Uses "class = nav-link dropdown-toggle" to establish the navigation bar as a dropdown menu
    -Established as a button using "role=button"
    -Uses "class='dropdown-menu' aria-labelledby='navbarDropdown'" to start the function of what options there are in 
     the dropdown
    -Buttons established from dropdown using "class='dropdown-item'" and then an href to show what the dropdown option
     directs the user to
    -Basis for all dropdowns, what changes is what the href is equivalent to and what each button is titled

        
  
    



