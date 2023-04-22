# Python-Projects


************************************ Overview ************************************

This code is a basic implementation of the popular game "Tic Tac Toe". It creates a list with nine elements that represents the game board, and then uses a while loop to iterate through the players' moves until one of them wins or the game ends in a tie.

The print_map() function is used to print the current state of the game board. The first player is represented by "X" and the second player is represented by "O".

After each move, the code checks if any player has won by checking all possible win conditions, such as a row or a column filled with the same symbol. If a win condition is met, the code prints a message indicating which player has won and exits the loop


************************************ Algorithm ***********************************

Create a list l1 containing the integers 1 to 9.

Define a function named "print_map" which prints the current state of the game board using the values in the list l1.

Set a variable i to 0.

Enter a while loop that executes while i is less than 9.

Call the "print_map" function to display the current state of the game board.

If i is even, display a message indicating it's Player 1's move, and prompt the user to enter a position for X. If the user enters a valid input, update the corresponding value in l1 to "X". Otherwise, display a message indicating an incorrect input, and decrement i by 1 to allow for another turn.

If i is odd, display a message indicating it's Player 2's move, and prompt the user to enter a position for O. If the user enters a valid input, update the corresponding value in l1 to "O". Otherwise, display a message indicating an incorrect input, and decrement i by 1 to allow for another turn.

Check if any player has won the game by checking the values in l1 for all possible winning combinations. If a winning combination is found, print a message indicating which player has won, and break out of the while loop.

If no winning combination is found, increment i by 1 to allow for another turn.

End the while loop.


~ Akshat Jain