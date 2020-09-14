Python 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import ttk
>>> root = Tk()
>>> button = ttk.Button(root, text= 'Click Me')
>>> button.pack()
>>> btton['text']
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    btton['text']
NameError: name 'btton' is not defined
>>> 
>>> button['text']
'Click Me'
>>> button['text'] = 'Press Me'
>>> button.config(text='Push Me')
>>> button.config()
{'command': ('command', 'command', 'Command', '', ''), 'default': ('default', 'default', 'Default', <string object: 'normal'>, <string object: 'normal'>), 'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', 'ttk::takefocus', 'ttk::takefocus'), 'text': ('text', 'text', 'Text', '', 'Push Me'), 'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''), 'underline': ('underline', 'underline', 'Underline', -1, -1), 'width': ('width', 'width', 'Width', '', ''), 'image': ('image', 'image', 'Image', '', ''), 'compound': ('compound', 'compound', 'Compound', <string object: 'none'>, <string object: 'none'>), 'padding': ('padding', 'padding', 'Pad', '', ''), 'state': ('state', 'state', 'State', <string object: 'normal'>, <string object: 'normal'>), 'cursor': ('cursor', 'cursor', 'Cursor', '', ''), 'style': ('style', 'style', 'Style', '', ''), 'class': ('class', '', '', '', '')}
>>> str(button)
'.!button'
>>> str(root)
'.'
>>> label = ttk.Label(root, text = "Hello, Tkinter!")
>>> label.pack()
>>> label.config(text='Howdy, Tkinter")
	     
SyntaxError: EOL while scanning string literal
>>> label.config(text='Howdy, Tkinter')
>>> label.config(text = 'dklfjakl;jda;lfjdaklfjdklfjadklfjadklfjdklfjdklfjdklfjasdklfjdlkf.')
>>> label.config(wraplength = 150)
>>> label.config(justify = CENTER)
>>> label.config(foreground = 'blue', background = 'yellow')
>>> label.config(font= ('Courier', 18, 'bold'))
>>> label.config(text = 'Howdy, Tkinter!')
>>> logo = PhotoImage(file = 'C:\\Users\\jon\Documents\\Python\\PythonGUI_Tkinter\\Exercise Files\\Ch03\\python_logo.gif')
>>> label.config(image=logo)
>>> label.config(compound = 'left')
>>> label.img = logo
>>> label.config(image = label.img)
>>> button.config(text='Click Me')
>>> def callback():
	print('Clicked!')

	
>>> button.config(command = callback)
>>> Clicked!
Clicked!
Clicked!
Clicked!
Clicked!

>>> button.config(image = logo, compound = LEFT)
>>> small_logo = logo.subsample(5,5)
>>> button.config(image = small_logo)
>>> checkbutton = ttk.Checkbutton(root, text = 'SPAM?')
>>> checkbutton.pack()
>>> spam = StringVar()
>>> spam.set('SPAM')
>>> spam.get()
'SPAM'
>>> 
>>> 
>>> 


>>> 















>>> clear
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> checkbutton.config(variable = spam, onvalue = 'SPAM Please', offvalue='Book Spam')
>>> spam.get()
'SPAM'
>>> spam.get()
'Book Spam'
>>> spam.get()
'SPAM Please'
>>> breakfast = StringVar()
>>> ttk.Radiobutton(root, text='SPAM', variable = breakfast, value='SPAM').pack()
>>> ttk.Radiobutton(root, text='Eggs', variable = breakfast, value='Eggs').pack()
>>> ttk.Radiobutton(root, text='Sausage', variable = breakfast, value='Sausage').pack()
>>> checkbutton.config(textvariable = breakfast)
>>> entry = ttk.Entry(root, width = 30)
>>> entry.pack()
>>> entry.get()
''
>>> entry.get()
'dafd'
>>> entry.delete(0,1)
>>> entry.delete(0, END)
>>> entry.insert(0, 'Enter your password')
>>> entry.config(show='*')
>>> month = StringVar()
>>> combobox = ttk.Combobox(root, textvariable = month)
>>> combobox.pack()
>>> combobox.config(values = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
>>> month.get()
''
>>> month.set('Dec')
>>> year = StringVar()
>>> Spinbox(root, from_ = 1990, to = 2014, texvariable=year).pack()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    Spinbox(root, from_ = 1990, to = 2014, texvariable=year).pack()
  File "C:\Users\jon\anaconda3\lib\tkinter\__init__.py", line 3646, in __init__
    Widget.__init__(self, master, 'spinbox', cnf, kw)
  File "C:\Users\jon\anaconda3\lib\tkinter\__init__.py", line 2299, in __init__
    (widgetName, self._w) + extra + self._options(cnf))
_tkinter.TclError: unknown option "-texvariable"
>>> Spinbox(root, from_ = 1990, to = 2014, textvariable=year).pack()
>>> year.get()
'1991'
>>> 