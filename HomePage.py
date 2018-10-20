from tkinter import filedialog
import tkinter as tk


# (tk.Tk) is not a parameter. It's inheritance of Tk class within Tkinter
# why we need this? - Because this class is the baseline code/parent for all other. We can directly
#  create other pages and functions and keep in the window we create once
class ProjectApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        tk.Tk.title = "Gesture Control Image Processing (GCIP)"

        # expand beyond the range you give if available
        container.pack(side="top", fill="both", expand=True)

        # 0 is min size
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for newFrame in (MainPage, HelpPage):
            frame = newFrame(container, self)
            self.frames[newFrame] = frame

            # nsew is north south east west - just stick to all side
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    # main function to display a page
    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()

    def select_image(self):

        global selected_image
        filename = filedialog.askopenfilename(initialdir="~/Pictures", title="Select file",
                                              filetypes=(
                                              ("png files", "*.png"), ("all files", "*.*")))
        # selected_image = tk.PhotoImage(file=filename)
        print(filename)

        img = tk.PhotoImage(filename)

        panel = tk.Label(self, image=img)
        panel.pack()


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Just a page!")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="quit", command=quit)
        button1.pack()

        button2 = tk.Button(self, text="Select Image", command=controller.select_image)
        button2.pack()

        # referencing back to ProjectApp show_frame method
        # why lambda? because we can't pass arguments in functions in tkinter.
        # we need to pass page arg so this seems to work
        button3 = tk.Button(self, text="Help", command=lambda: controller.show_frame(HelpPage))
        button3.pack()


class HelpPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Help Page!")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Go Back to Main Page",
                            command=lambda: controller.show_frame(MainPage))
        button1.pack()


app = ProjectApp()
app.mainloop()
