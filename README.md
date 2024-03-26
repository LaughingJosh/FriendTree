# FriendTree
FriendTree is a Python program designed to visualize relationships between different characters, such as friendships, couples, animosities, etc., through an interactive graph.

## Key Features:

- **Import from Excel file:** The program can import relationship data from a structured Excel file, where character names are arranged in rows and columns with corresponding relationship types in the cells.

- **Interactive Visualization:** FriendTree uses the NetworkX library to create an interactive graph representing relationships between characters. Nodes in the graph represent characters, while edges represent relationship types, with different colors for each type.

- **Customization:** Colors and relationship types can be easily customized according to user needs. Additionally, the program provides the option to save the graphical visualization as a PNG image.

## Usage:

1. Prepare an Excel file containing relationship data between characters.
2. Execute the Python program by specifying the path to the Excel file.
3. FriendTree will generate a graphical visualization of the relationships between characters and display it on the screen.
4. You can also save the visualization as a PNG image for future use.

FriendTree offers an intuitive and user-friendly way to visualize relationships between characters in various scenarios, such as literature, movies, games, and more.

## Excel File Format:

The Excel file should be structured with character names arranged in rows and columns. Each cell should contain the relationship type between the corresponding characters. Empty cells indicate no relationship between characters.
************************************************************************
           Alice      Bob      Charlie     David      Eve
Alice     couple    amitié    animosité    crush    amitié
Bob       amitié              amitié      animosité  -
Charlie   animosité amitié                crush    amitié
David     crush    animosité   crush                amitié
Eve       amitié              amitié      amitié      
************************************************************************

## Required Libraries:

- NetworkX
- pandas
- matplotlib
