from tkinter import *
import tkinter.messagebox


#4x4 Tic Tac Toe Game
click=1
def Tic_4x4():
    global click
    win = Tk()
    win.title("Tic Tac Toe 4x4")
    win.geometry("488x535")
    win.resizable(width=False,height=False)
    win.configure(background="black")
    label = Label(win, text="Tic Tac Toe Game 4x4", font="times 30 bold", fg="white", bg="black")
    label.pack(fill=X)
    btn = Button(win, text="Main Menu", bg="white", fg="black", font=("Italic",), padx=50, pady=5, command=win.destroy)
    btn.pack()
    click =1    ### resets value of counter to 1 when main menu button is pressed!
    frame = Frame(win)
    frame.pack()


    def check(buttons):
        global click
        click = click + 1
        if (click % 2 == 0):
            if buttons["text"] == " ":
                buttons["text"] = "X"
            else:
                click=click-1
                tkinter.messagebox.showinfo("Attention","This Box is Already Taken,Please Choose Another!!")
        else:
            if buttons["text"] == " ":
                buttons["text"] = "O"
            else:
                click = click - 1
                tkinter.messagebox.showinfo("Attention", "This Box is Already Taken,Please Choose Another!!")
       # print(click)

        if button_1["text"] == "X" and button_2["text"] == "X" and button_3["text"] == "X" and button_4["text"] == "X":
            tkinter.messagebox.showinfo("Winner X ", " You Won The Match !")
            win.destroy()

        if button_5["text"] == "X" and button_6["text"] == "X" and button_7["text"] == "X" and button_8["text"] == "X":
            tkinter.messagebox.showinfo("Winner X ", " You Won The Match !")
            win.destroy()

        if button_9["text"] == "X" and button_10["text"] == "X" and button_11["text"] == "X" and button_12[
            "text"] == "X":
            tkinter.messagebox.showinfo("Winner X ", " You Won The Match !")
            win.destroy()

        if button_13["text"] == "X" and button_14["text"] == "X" and button_15["text"] == "X" and button_16[
            "text"] == "X":
            tkinter.messagebox.showinfo("Winner X ", " You Won The Match !")
            win.destroy()

        if button_1["text"] == "X" and button_5["text"] == "X" and button_9["text"] == "X" and button_13["text"] == "X":
            tkinter.messagebox.showinfo("Winner X ", " You Won The Match !")
            win.destroy()

        if button_2["text"] == "X" and button_6["text"] == "X" and button_10["text"] == "X" and button_14[
            "text"] == "X":
            tkinter.messagebox.showinfo("Winner X ", " You Won The Match !")
            win.destroy()

        if button_3["text"] == "X" and button_7["text"] == "X" and button_11["text"] == "X" and button_15[
            "text"] == "X":
            tkinter.messagebox.showinfo("Winner X ", " You Won The Match !")
            win.destroy()

        if button_4["text"] == "X" and button_8["text"] == "X" and button_12["text"] == "X" and button_16[
            "text"] == "X":
            tkinter.messagebox.showinfo("Winner X ", " You Won The Match !")
            win.destroy()

        if button_1["text"] == "X" and button_6["text"] == "X" and button_11["text"] == "X" and button_16[
            "text"] == "X":
            tkinter.messagebox.showinfo("Winner X ", " You Won The Match !")
            win.destroy()

        if button_4["text"] == "X" and button_7["text"] == "X" and button_10["text"] == "X" and button_13[
            "text"] == "X":
            tkinter.messagebox.showinfo("Winner X ", " You Won The Match !")
            win.destroy()



        if button_1["text"] == "O" and button_2["text"] == "O" and button_3["text"] == "O" and button_4["text"] == "O":
            tkinter.messagebox.showinfo("Winner O ", " You Won The Match !")
            win.destroy()

        if button_5["text"] == "O" and button_6["text"] == "O" and button_7["text"] == "O" and button_8["text"] == "O":
            tkinter.messagebox.showinfo("Winner O ", " You Won The Match !")
            win.destroy()

        if button_9["text"] == "O" and button_10["text"] == "O" and button_11["text"] == "O" and button_12[
            "text"] == "O":
            tkinter.messagebox.showinfo("Winner O ", " You Won The Match !")
            win.destroy()

        if button_13["text"] == "O" and button_14["text"] == "O" and button_15["text"] == "O" and button_16[
            "text"] == "O":
            tkinter.messagebox.showinfo("Winner O ", " You Won The Match !")
            win.destroy()

        if button_1["text"] == "O" and button_5["text"] == "O" and button_9["text"] == "O" and button_13["text"] == "O":
            tkinter.messagebox.showinfo("Winner O ", " You Won The Match !")
            win.destroy()

        if button_2["text"] == "O" and button_6["text"] == "O" and button_10["text"] == "O" and button_14[
            "text"] == "O":
            tkinter.messagebox.showinfo("Winner O ", " You Won The Match !")
            win.destroy()

        if button_3["text"] == "O" and button_7["text"] == "O" and button_11["text"] == "O" and button_15[
            "text"] == "O":
            tkinter.messagebox.showinfo("Winner O ", " You Won The Match !")
            win.destroy()

        if button_4["text"] == "O" and button_8["text"] == "O" and button_12["text"] == "O" and button_16[
            "text"] == "O":
            tkinter.messagebox.showinfo("Winner O ", " You Won The Match !")
            win.destroy()

        if button_1["text"] == "O" and button_6["text"] == "O" and button_11["text"] == "O" and button_16[
            "text"] == "O":
            tkinter.messagebox.showinfo("Winner O ", " You Won The Match !")
            win.destroy()

        if button_4["text"] == "O" and button_7["text"] == "O" and button_10["text"] == "O" and button_13[
            "text"] == "O":
            tkinter.messagebox.showinfo("Winner O ", " You Won The Match !")
            win.destroy()

        if click==17: #For Match Drawn
            tkinter.messagebox.showinfo("Oops", "Match Drawn!")
            win.destroy()


    button_1 = Button(frame, text=" ", borderwidth=3, width=10, height=5, bg="black", fg="white", font="bold",
                      command=lambda: check(button_1))
    button_1.grid(row=1, column=0)

    button_2 = Button(frame, text=" ", borderwidth=3, width=10, height=5, bg="black", fg="white", font="bold",
                      command=lambda: check(button_2))
    button_2.grid(row=1, column=1)

    button_3 = Button(frame, text=" ", borderwidth=3, width=10, height=5, bg="black", fg="white", font="bold",
                      command=lambda: check(button_3))
    button_3.grid(row=1, column=2)

    button_4 = Button(frame, text=" ", borderwidth=3, width=10, height=5, bg="black", fg="white", font="bold",
                      command=lambda: check(button_4))
    button_4.grid(row=1, column=3)

    button_5 = Button(frame, text=" ", borderwidth=3, width=10, height=5, bg="black", fg="white", font="bold",
                      command=lambda: check(button_5))
    button_5.grid(row=2, column=0)

    button_6 = Button(frame, text=" ", borderwidth=3, width=10, height=5, bg="black", fg="white", font="bold",
                      command=lambda: check(button_6))
    button_6.grid(row=2, column=1)

    button_7 = Button(frame, text=" ", borderwidth=3, width=10, height=5, bg="black", fg="white", font="bold",
                      command=lambda: check(button_7))
    button_7.grid(row=2, column=2)

    button_8 = Button(frame, text=" ", borderwidth=3, width=10, height=5, bg="black", fg="white", font="bold",
                      command=lambda: check(button_8))
    button_8.grid(row=2, column=3)

    button_9 = Button(frame, text=" ", borderwidth=3, width=10, height=5, bg="black", fg="white", font="bold",
                      command=lambda: check(button_9))
    button_9.grid(row=3, column=0)

    button_10 = Button(frame, text=" ", borderwidth=3, width=10, height=5, bg="black", fg="white", font="bold",
                       command=lambda: check(button_10))
    button_10.grid(row=3, column=1)

    button_11 = Button(frame, text=" ", borderwidth=3, width=10, height=5, bg="black", fg="white", font="bold",
                       command=lambda: check(button_11))
    button_11.grid(row=3, column=2)

    button_12 = Button(frame, text=" ", borderwidth=3, width=10, height=5, bg="black", fg="white", font="bold",
                       command=lambda: check(button_12))
    button_12.grid(row=3, column=3)

    button_13 = Button(frame, text=" ", borderwidth=3, width=10, height=5, bg="black", fg="white", font="bold",
                       command=lambda: check(button_13))
    button_13.grid(row=4, column=0)

    button_14 = Button(frame, text=" ", borderwidth=3, width=10, height=5, bg="black", fg="white", font="bold",
                       command=lambda: check(button_14))
    button_14.grid(row=4, column=1)

    button_15 = Button(frame, text=" ", borderwidth=3, width=10, height=5, bg="black", fg="white", font="bold",
                       command=lambda: check(button_15))
    button_15.grid(row=4, column=2)

    button_16 = Button(frame, text=" ", borderwidth=3, width=10, height=5, bg="black", fg="white", font="bold",
                       command=lambda: check(button_16))
    button_16.grid(row=4, column=3)

    win.mainloop()

#3x3 Tic Tac Toe Game
play=1
def Tic_3x3():
    global play
    window = Tk()
    window.title("Tic Tac Toe 3x3")
    window.geometry("488x535")
    window.resizable(width=False, height=False)
    window.configure(background="black")
    label = Label(window, text="Multiplayer", font="times 30 bold", fg="white", bg="black")
    label.pack(fill=X)
    btnn = Button(window, text="Main Menu", bg="white", fg="black", font=("Italic",), padx=50, pady=5,
                  command=window.destroy)
    btnn.pack()
    play = 1
    frame = Frame(window)
    frame.pack()


    def checked(click):
        global play
        play = play + 1
        if (play % 2 == 0):
            if click["text"] == " ":
                click["text"] = "X"
            else:
                play = play - 1
                tkinter.messagebox.showinfo("Attention", " This Box is Already Taken,ChOose Another Box")
        else:
            if click["text"] == " ":
                click["text"] = "O"
            else:
                play = play - 1
                tkinter.messagebox.showinfo("Attention", " This Box is Already Taken,ChOose Another Box")

        #print(play)



        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
            tkinter.messagebox.showinfo("Winner X", " You Won The Match !")
            window.destroy()

        if b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
            tkinter.messagebox.showinfo("Winner X", " You Won The Match !")
            window.destroy()

        if b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
            tkinter.messagebox.showinfo("Winner X", " You Won The Match !")
            window.destroy()

        if b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
            tkinter.messagebox.showinfo("Winner X", " You Won The Match !")
            window.destroy()

        if b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
            tkinter.messagebox.showinfo("Winner X", " You Won The Match !")
            window.destroy()

        if b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
            tkinter.messagebox.showinfo("Winner X", " You Won The Match !")
            window.destroy()

        if b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
            tkinter.messagebox.showinfo("Winner X", " You Won The Match !")
            window.destroy()

        if b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
            tkinter.messagebox.showinfo("Winner X", " You Won The Match !")
            window.destroy()

        if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
            tkinter.messagebox.showinfo("Winner O", " You Won The Match !")
            window.destroy()

        if b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            tkinter.messagebox.showinfo("Winner O", " You Won The Match !")
            window.destroy()

        if b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            tkinter.messagebox.showinfo("Winner O", " You Won The Match !")
            window.destroy()

        if b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            tkinter.messagebox.showinfo("Winner O", " You Won The Match !")
            window.destroy()

        if b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            tkinter.messagebox.showinfo("Winner O", " You Won The Match !")
            window.destroy()

        if b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            tkinter.messagebox.showinfo("Winner O", " You Won The Match !")
            window.destroy()

        if b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
            tkinter.messagebox.showinfo("Winner O", " You Won The Match !")
            window.destroy()

        if b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            tkinter.messagebox.showinfo("Winner O", " You Won The Match !")
            window.destroy()

        if play == 10:
            tkinter.messagebox.showinfo("Draw", "Match Drawn")
            window.destroy()

    b1 = Button(frame, text=" ", borderwidth=3, width=10, height=6, bg="black", fg="white", font="bold",
                command=lambda: checked(b1))
    b1.grid(row=1, column=0)

    b2 = Button(frame, text=" ", borderwidth=3, width=10, height=6, bg="black", fg="white", font="bold",
                command=lambda: checked(b2))
    b2.grid(row=1, column=1)

    b3 = Button(frame, text=" ", borderwidth=3, width=10, height=6, bg="black", fg="white", font="bold",
                command=lambda: checked(b3))
    b3.grid(row=1, column=2)

    b4 = Button(frame, text=" ", borderwidth=3, width=10, height=6, bg="black", fg="white", font="bold",
                command=lambda: checked(b4))
    b4.grid(row=2, column=0)

    b5 = Button(frame, text=" ", borderwidth=3, width=10, height=6, bg="black", fg="white", font="bold",
                command=lambda: checked(b5))
    b5.grid(row=2, column=1)

    b6 = Button(frame, text=" ", borderwidth=3, width=10, height=6, bg="black", fg="white", font="bold",
                command=lambda: checked(b6))
    b6.grid(row=2, column=2)

    b7 = Button(frame, text=" ", borderwidth=3, width=10, height=6, bg="black", fg="white", font="bold",
                command=lambda: checked(b7))
    b7.grid(row=3, column=0)

    b8 = Button(frame, text=" ", borderwidth=3, width=10, height=6, bg="black", fg="white", font="bold",
                command=lambda: checked(b8))
    b8.grid(row=3, column=1)

    b9 = Button(frame, text=" ", borderwidth=3, width=10, height=6, bg="black", fg="white", font="bold",
                command=lambda: checked(b9))
    b9.grid(row=3, column=2)

    window.mainloop()


def Ins():
    tkinter.messagebox.askokcancel("Instructions", ''' What is Tic Tac Toe ?

        >>> Tic Tac Toe is a Paper And Pencil game for two Players , Who Take turns making the spaces in a 3x3 Or 4x4 grid.One Player is X and the Other player is O.


        How To Play ?

        >>> If a player gets Three Of their marks on the board in a row,column or one of the two diagonals,they win,when the board fills up with the neither Player winning the game ends in a draw. It is depend on you whether your game is 3x3 Or 4x4.''')


def Exit():
    main.destroy()




main= Tk()
main.title("Main Menu")
main.geometry("488x535")
main.resizable(width=False,height=False)
#main.configure(background="black")
canvas = Canvas(main,width=488,height=535)
canvas.pack()
my_image=PhotoImage(file='blob2.png')
canvas.create_image(0,0,anchor=NW,image=my_image)
lbl=Label(main,text="Game Menu",font="times 50 bold",fg="black",bg="white",padx="70")
lbl.place(y=1)
#single=Button(main,text="Single Player",bg="white",fg="black",font="times 12 bold",padx=60,pady=5)
#single.place(x=130,y=100)
Tic_3x3=Button(main,text="Multiplayer",bg="white",fg="black",font="times 12 bold",padx=65,pady=5,command=Tic_3x3)
Tic_3x3.place(x=130,y=140)
Tic_4x4=Button(main,text="Multiplayer 4x4",bg="white",fg="black",font="times 12 bold",padx=51,pady=5,command=Tic_4x4)
Tic_4x4.place(x=130,y=205)
Instructions=Button(main,text="Instructions",bg="white",fg="black",font="times 12 bold",padx=65,pady=5,command=Ins)
Instructions.place(x=130,y=270)
Exit=Button(main,text="Exit",bg="white",fg="black",font="times 12 bold",padx=92,pady=5,command=Exit)
Exit.place(x=130,y=335)

main.mainloop()
