# Final Project Report

* Student Name: Peihao Li
* Github Username: peihao2  
* Semester: Fall 2023
* Course: CS 5001



## Description 
General overview of the project, what you did, why you did it, etc. 

For this project, I created a text-based adventure game based on Python. I like to watch movies and TV shows in the detective-solving genre, and I also like to study the process of detectives solving cases through various details and props. As a kid, I used to play some text-based adventure games. These games don't have vivid graphics, but you can feel the tension and the interesting flow of the game through text descriptions. Now I want to create a simple text-based adventure game using the coding knowledge I've learned this semester.


## Key Features
Highlight some key features of this project that you want to show off/talk about/focus on. 

I was inspired by the animated movie Conan. The story is about Conan and his team going to a park to ride a roller coaster, where they witness some suspicious dealings between the Men in Black. Later, while riding the roller coaster, a passenger is killed. This is a murder. Players need to collect evidence and use the props they find and their inference to expose the murderer who utilized the roller coaster. 
Game Overview:
Players take on the role of Conan, who must solve a mysterious murder in the park. The game is played through text descriptions, choices, and puzzle elements.
1. Introduce the park scene. Introduce the main characters: Conan and Ran. As well as a few supporting characters.
2. Text description of the roller coaster accident. Discovery of the murder. Initial reaction of passengers and confusion.
3. Investigation Stage: Allow players to select different areas or clues to examine (e.g., seating arrangements, bodies, roller coaster contraptions). Interviewing Witnesses: Choose to talk to different characters to gather information. Gathering Clues: Look for items or observations that are vital to solving the case (e.g. dropped items, strange markings).
4. Reasoning: Ask the player puzzles or logical questions based on the clues collected. Accusing the Criminal: Confront the murderer after collecting enough evidence. Depending on the player's choices and the evidence collected, this part may have multiple outcomes. Finally, explain how the roller coaster was used to commit the murder. If the player makes choices according to the normal storyline, I'll end with an explanation of the entire crime, which is like a conclusion drawn by the player's reasoning.
If the player chooses the wrong murderer, it leads to a different outcome and then the storyline ends.


Game Mechanics:
CHOICES: The player will make choices at key moments that will affect the direction and end of the story.
CLUE LIBRARY: players can collect clues by talking to characters, clues are only available if the player chooses to talk to the appropriate character, if certain scenes are missed, no clues will be available.TIME LIMIT: Perhaps a time limit for this program could be added to give the game a greater sense of urgency. 
MULTIPLE ENDINGS: Depending on the player's reasoning and decisions, the game will have different endings.

Set up a basic game loop where the game progresses through scenarios and player choices.
Define variables to track player progress, inventory, and key decisions.
Use functions to handle different scenarios and interactions, making the code modular and more manageable.
Use dictionaries or lists to manage inventory and clues.



## Guide
How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features. 

I will be submitting my Github repository where I will upload the full game code. You only need to follow the game's prompts to play.

## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

Download the Python script for the game and run it. The project requires no additional dependencies or API keys.

## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 

Each part of the game is encapsulated in a function. The game uses the global dictionary clues to manage the clues collected during the game.

### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.

The main challenge was that I needed to reorganize the anime's plots and translate them into a first-person puzzle game, and I also needed to translate the flow of the plot and the dialog and clues in it into code that could be interacted with by the player. Keep the code organized and readable. Implementing time-limit features (setup_time_limit and check_time_limit_exceeded) also added complexity to the game logic.


## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

Each function has a descriptive documentation string to explain its use. The player simply follows the code's prompts to play.

## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_
>
> Since my code has a lot of human interaction and different choices can result in different endings. I tested the code manually by running the script many times and navigating different paths and choices. Due to the interactive nature of the game, no automated tests were implemented.


## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

In the future, I would like to add a graphical user interface to my code to enhance the human-computer interaction experience.
More complex puzzles and multiple storylines.
Automated testing of non-interactive parts of the code.

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.

This is my first time developing a text-based adventure game. I encountered very many difficulties and challenges, and the interesting part was that I could guide the player to deduce and decipher a crime scene.
Designing the flow of the game and managing the global state of the threads required careful planning and consideration of how players would interact with the game at different stages.
An important learning point is to build code in a way that balances readability and functionality. Creating different functions for different parts of the game, such as intro, roller_coaster_choice, and final_judgment, helped maintain clarity and modularity. This approach makes the code easier to manage.
Even more challenging was implementing the time limit feature, which added a layer of complexity to the game logic. It forced me to consider how the different components of the game would interact over time. This would give the player an immersive experience; after all, real-life detectives often need to reason through crimes and make judgments as quickly as possible.
With this game, I realize there are multiple avenues for enhancement and expansion. The current version lacks a graphical user interface. I hope to add more interaction in the future to make the game more interactive and visually appealing.
I also need to introduce more complex puzzles and branching storylines. This will not only add depth to the gameplay, but also increase replayability as players can explore different paths and outcomes.
In the future I would also like to develop a set of automated tests, especially for non-interactive components, that will enhance the reliability and robustness of the game.
In conclusion, developing a text-based adventure game has been a rewarding experience and the project has enabled me to gain a lot of experience. In the future, when faced with more complex programming, I will start with each small problem and gradually improve my code.

