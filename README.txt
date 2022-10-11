PySimpleGUI Template
--------------------

This template is a starting point for PySimpleGUI projects

The template includes starting code for the 3 main components of any PySimpleGUI application

These components are:
1) The Layout
2) The Window
3) The Event Loop

--------------------

FOR MORE INFORMATION ON PYSIMPLEGUI, PLEASE SEE THEIR WEBSITE:
https://pysimplegui.readthedocs.io/

For information on how to use elements (and their parameters), see the "Call Reference":
https://pysimplegui.readthedocs.io/en/latest/call%20reference/

Find some example programs in the "Cookbook":
https://www.pysimplegui.org/en/latest/cookbook/


--------------------

The Layout is a list-of-lists.

Each inner list can store PySimpleGUI element(s)
Inner lists function as rows

Elements in rows are rendered horizontally, left-to-right
Rows in the layout are rendered vertically, top-to-bottom

--------------------

The Window stores the code to construct a new sg.Window object

The Window constructor takes in:
a) Title
b) Layout

The "finalize = True" parameter of the Window will build the window on that line

Once the Window is built, it is maximized using the window.maximize() method

--------------------

The event loop holds code for when the application is running
At the heart of the event loop is the window.read() method.

The window.read() method:

1) Waits for an event to occur
2) Returns the event that occured
3) Returns a dictionary of values


Events are keys of elements interacted with
Each element is assigned a key as a unique identifier
Keys can be assigned using the "key = <KEY>" parameter in each element's constructor

Values is a dictionary, where the keys are the keys of each element. The values are the information the element is storing.
For example, an sg.Input() element may hold information a user typed in. 

The key of the Input element, and the value currently typed into the element are stored in the values dictionary.


If the event is either "Exit" or None, the loop will break and the program will exit. 
Without this, you may get an error "You have tried 100 times to read a closed window"

--------------------