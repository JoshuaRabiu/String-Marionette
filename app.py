from tkinter import *

root = Tk()
#Creates Title
title = Label(root, text="String Marionette", bg="#336E7B", fg="white")
title.pack(side=TOP)
#Creates Input Field & Sets Cursor Focus inside the field
usr_input = Entry(root)
usr_input.pack()
usr_input.focus_set()
#Creates Output Frame
outputFrame = Frame(root)
outputFrame.pack()

def print_reversed(event):
	string = usr_input.get()
	global reversedText
	reversedText = Label(outputFrame, text= string+ " reversed is: " + string[::-1])
	reversedText.pack()
def run_piglatin(event):
	string = usr_input.get()
	piglatinText = Label(outputFrame, text= string + " converted to Pig Latin is: " +string[1:] + string[0] +"ay")
	piglatinText.pack() 
def palindrome_check(event):
	string = usr_input.get()
	if string[::-1] == string:
		isPalindrome = Label(outputFrame, text= string + " is indeed a palindrome!")
		isPalindrome.pack()
	else:
		notPalindrome = Label(outputFrame, text = string + " is not a palindrome...")
		notPalindrome.pack()
def count_vowels(event):
	count = 0
	string = usr_input.get()
	for char in string:
		if char.lower() in 'aeiou':
			count += 1
	vowelCount = Label(outputFrame, text= string + " contains %d vowel(s)" % count)
	vowelCount.pack()
#Function for clearing output text
def text_clear(event):
	for child in outputFrame.winfo_children():
		child.destroy()
#Creates Button Frame
buttonFrame = Frame(root)
buttonFrame.pack(side=BOTTOM)
#Button Creation and binding
b = Button(buttonFrame, text="Reverse!")
b.bind('<Button-1>', print_reversed)
b.pack(side = LEFT)

b2 = Button(buttonFrame, text="Convert to Pig Latin")
b2.bind('<Button-1>', run_piglatin)
b2.pack(side=LEFT)

b3 = Button(buttonFrame, text = "Check if Palindrome")
b3.bind('<Button-1>', palindrome_check)
b3.pack(side=LEFT)

b4 = Button(buttonFrame, text = "Count Vowels")
b4.bind('<Button-1>', count_vowels)
b4.pack(side=LEFT)

b5 = Button(buttonFrame, text="Clear")
b5.bind('<Button-1>', text_clear)
b5.pack(side=LEFT)

root.mainloop()
