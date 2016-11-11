# HAG-Quick-Search-Tool
This search tool was created for myself, Having slow internet it took way too long for me to check if our site had a certain game on it..
So by creating this tool i sped everything up by just a little bit , its not the greatest tool as some games may have the same name.. but all in all it has helped me quite alot..

# How does it work?
This tool works by taking in the user input of a game such as "Hello World" then it swaps out every space it finds with a "+" Sign..
The reason it does that is because when you search for something on HAG thats what the Web Url turns out to be something along the lines of "search.php?&name=Hello+World" once it takes in the user input it will then send a request to HAG to search for the game.. once the pages contents are all loaded it will then scrape every game name on the page and display them in your terminal.. The good thing about HAG is that every result for whatever you may have searched is displayed on one page making it easier for this tool to work im guessing the only way to do this on a site that has multiple pages for Example 1-600 pages.. you may need to use a while condition that increases the page number after each web scrape and push each result into an array?.. Might look into a project like this as well

# How do i use it?
Well running the script sort of answers this questions itself.. its easy once it is loaded up type in a game name.. it will then present you with all the results for that search and then prompt you if you would like to perform another search you may answer with "Y" or "N" The input for this prompt is not case sensitive so you can use capital letters or lower case
