import tkinter as tk
from tkinter import ttk
import sv_ttk

class VirtualAssistantGUI(tk.Tk):
    """
    This class is responsible for handling user input and providing output through the GUI.
    """

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        """
        Initializes the main window, input and output widgets, and event handlers for user input.
        """

        # Adding a title to the window
        self.wm_title("Test Application")

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=400, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (MainPage, SidePage, CompletionScreen):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="Go to the Side Page",
            command=lambda: controller.show_frame(SidePage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

class SidePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the Side Page")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Completion Screen",
            command=lambda: controller.show_frame(CompletionScreen),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

class CompletionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Completion Screen, we did it!")
        label.pack(padx=10, pady=10)
        switch_window_button = ttk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(MainPage)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)














        # self.root = tk.Tk()
        # self.root.geometry("700x900")
        #
        # button = ttk.Button(self.root, text="Click Me")
        # button.pack()
        #
        # sv_ttk.set_theme("dark")
        #
        # self.root.mainloop()




    # def start(self):
    #     """
    #     Starts the GUI event loop and handles user input and output through the GUI.
    #     This method should call the mainloop() method of the Tk object to start the GUI event loop.
    #     """
    #     pass
    #
    # def handle_input(self):
    #     """
    #     This method would handle user input by retrieving the input text from the input widget,
    #     passing it to the virtual assistant to process, and displaying the response in the output widget.
    #     """
    #     pass
    #
    # def display_message(self):
    #     """
    #     This method would display a message in the output widget, such as a greeting or a message
    #     indicating that the virtual assistant is processing the user input.
    #     """
    #     pass
    #
    # def display_response(self):
    #     """
    #     This method would display the response from the virtual assistant in the output widget.
    #     """
    #     pass

# The VirtualAssistantGUI class would also instantiate the other classes in the project,
# such as the IntentClassifier, ActionHandler, TextToSpeech, and SpeechToText classes,
# and use them to handle user input and provide output.

if __name__ == "__main__":
    testObj = VirtualAssistantGUI()
    testObj.mainloop()

