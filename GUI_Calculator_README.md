# Python-Projects

************************************ Overview *************************************

This is a basic calculator app built using the Tkinter module in Python. It has a simple GUI that allows users to perform basic mathematical operations such as addition, subtraction, multiplication, and division. The calculator also has a clear button, delete button, and percentage button.

The calculator app works by listening for events such as button clicks and then updating the display accordingly. The click() function is used to handle these events. The app uses the eval() function to evaluate the mathematical expression and display the result.

Overall, this is a basic calculator app that can be used for simple calculations. However, it does not have advanced features such as scientific calculations or the ability to save and recall previous calculations.

The provided code is for a simple calculator using the tkinter module in Python. When a user clicks on a button, the click() function is called, which takes an event argument containing information about the event, such as which button was clicked. The function then performs a specific operation based on the button clicked.

************************************ Algorithm ************************************

Import the tkinter module.
Define a function named click that takes an event argument.
Declare the screen_value variable as a StringVar and set its value to an empty string.
Create a root object using the Tk class from the tkinter module.
Set the dimensions and title of the window using the geometry() and title() methods of the root object.
Create an Entry widget named screen and pass the textvar argument as screen_value.
Pack the screen widget using the pack() method.
Create a frame object.
Create a Button widget for the number 7 with the text "7", a font size of 18, and a padx of 8.
Pack the b7 widget using the pack() method.
Bind the <Button-1> event to the click function using the bind() method.
Repeat steps 9-11 for the numbers 8 and 9, the "DEL" button, and the "AC" button.
Pack the frame widget using the pack() method.
Repeat steps 8-13 for the next two rows of buttons for numbers 4-6 and 1-3, the multiplication, division, addition, and subtraction buttons.
Create a final frame widget for the decimal point, zero, and equals buttons.
Repeat steps 9-11 for the decimal point and zero buttons.
Create a Button widget for the equals button with the text "=", a font size of 15, and a padx of 10.
Pack the beq widget using the pack() method.
Bind the <Button-1> event to the click function using the bind() method.
Pack the frame widget using the pack() method.
Call the mainloop() method of the root object to start the GUI event loop.

~ Akshat Jain