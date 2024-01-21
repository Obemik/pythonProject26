import tkinter
from tkinter import *

root = Tk()

root.config(bg="#86F4FF")
root.title("Hello world!")
root.geometry('500x600+900+300')

btn1 = Button(root, text="New Label", command= lambda: Label(root, text="*********\n   *******\n    ******\n      ****\n         *", bg="#86F4FF").pack(), bg="pink")
btn1.pack()
btn2 = Button(root, text="New Label", command= lambda: Label(root, text="*********\n"
                                                                        "*******  \n"
                                                                        "******   \n"
                                                                        "****     \n"
                                                                        "*         ", bg="#86F4FF").pack(), bg="pink")
btn2.pack()
btn3 = Button(root, text="New Label", command= lambda: Label(root, text="********\n******\n***\n*", bg="#86F4FF").pack(), bg="pink")
btn3.pack()
btn4 = Button(root, text="New Label", command= lambda: Label(root, text="*\n****\n******\n********", bg="#86F4FF").pack(), bg="pink")
btn4.pack()
btn5 = Button(root, text="New Label", command= lambda: Label(root, text="******\n***\n*\n***\n******", bg="#86F4FF").pack(), bg="pink")
btn5.pack()
btn6 = Button(root, text="New Label", command= lambda: Label(root, text="*        *\n"
                                                                        "***    ***\n"
                                                                        "***** ****\n"
                                                                        "***    ***\n"
                                                                        "*        *", bg="#86F4FF").pack(), bg="pink")
btn6.pack()
btn7 = Button(root, text="New Label", command= lambda: Label(root, text="*      \n"
                                                                        "***    \n"
                                                                        "****   \n"
                                                                        "***    \n"
                                                                        "*        ", bg="#86F4FF").pack(), bg="pink")
btn7.pack()
btn8 = Button(root, text="New Label", command= lambda: Label(root, text="       *\n"
                                                                        "     ***\n"
                                                                        "    ****\n"
                                                                        "     ***\n"
                                                                        "       *", bg="#86F4FF").pack(), bg="pink")
btn8.pack()
btn9 = Button(root, text="New Label", command= lambda: Label(root, text="        *\n"
                                                                        "     ****\n"
                                                                        "    *****\n"
                                                                        "   ******\n"
                                                                        " ********", bg="#86F4FF").pack(), bg="pink")
btn9.pack()
btn10 = Button(root, text="New Label", command= lambda: Label(root, text="***** \n"
                                                                        " ****  \n"
                                                                        " ***   \n"
                                                                        " **    \n"
                                                                        " *     ", bg="#86F4FF").pack(), bg="pink")
btn10.pack()

root.mainloop()