import tkinter as tk
from tkinter import ttk
import sv_ttk
import time
from PIL import Image, ImageTk
from SpeechToText import *
from TextToSpeech import *
from IntentClassifier import *
from ActionHandler import *

#-----------------------------------------------------------------------------------------------------------------------
# GUI CONTAINER


class VirtualAssistantGUI(tk.Tk):
    """
    This class is responsible for handling user input and providing output through the GUI.
    """

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # locks the assistant if busy
        self.lock = 1

        # Adding a title to the window
        self.wm_title("Virtual Assistant")

        # transparency
        # self.wm_attributes('-alpha', 0.9)

        # creates a container to store each page
        container = ttk.Frame(self, height=400, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # creates a dictionary of frames
        # allows access to objects from each page/frame
        self.frames = {}
        for F in (MainPage, HelpPage, SettingsPage):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(MainPage)

        # Binding the click event to the image
        self.frames[MainPage].canvas.tag_bind(self.frames[MainPage].image_id, '<ButtonPress-1>', self.handle_click)

        # Scheduling the animation
        self.angle = 0
        self.rotate_direction = 1  # 1 for clockwise, -1 for counterclockwise
        self.animate_image()

        sv_ttk.set_theme("dark")


# -----------------------------------------------------------------------------------------------------------------------
# GUI METHODS


    # changes frame/page
    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()

    def speak_response(self, response):
        speaker = TextToSpeech()
        speaker.set_voice("female")
        speaker.speak(response)

    # adds the virtual assistant's response to the response_window
    # uses a delay to simulate typing
    def add_response(self, response: str, name: str) -> None:

        self.lock = 0
        response = name + ": " + response
        self.frames[MainPage].response_box.configure(state="normal")

        if name == "assistant":
            color = "#eb5b0b"
        else:
            color = "white"
            response += "?"

        self.frames[MainPage].response_box.tag_configure(name, foreground=color)

        for i, char in enumerate(response):
            self.frames[MainPage].response_box.insert(tk.END, char, name)
            self.frames[MainPage].response_box.see(tk.END)
            self.update()
            time.sleep(0.05)

        self.frames[MainPage].response_box.insert(tk.END, "\n")
        self.frames[MainPage].response_box.insert(tk.END, "\n")
        self.frames[MainPage].response_box.configure(state="disabled")

        self.lock = 1

    # handles when avatar is pressed
    def handle_click(self, event):
        """
        Custom function to handle the click event.
        """

        if self.lock == 1:
            self.lock = 0

            # Get the coordinates of the click event
            x, y = event.x, event.y
            # Get the coordinates of the center of the circle
            cx, cy = self.frames[MainPage].canvas.coords(self.frames[MainPage].image_id)
            # Calculate the distance between the click coordinates and the center of the circle
            distance = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            # Get the radius of the circle
            r = self.assistant_image.width() / 2
            # Check if the distance is less than or equal to the radius of the circle
            if distance <= r:
                print("Assistant clicked")

                # transcribe user speech
                transcription = self.listen_to_user()

                # add user speech to response
                self.add_response(transcription, "user")

                # process assistant response and action
                response = self.handle_request(transcription)
                self.add_response(response, "assistant")


    # animates the avatar to rotate.
    def animate_image(self):
        """
        Function to animate the image by rotating it.
        """
        self.angle += 5 * self.rotate_direction
        if self.angle >= 360:
            self.angle = 0
        elif self.angle < 0:
            self.angle = 359

        # Rotate the image
        img = Image.open("assistant1.png")
        img = img.rotate(self.angle)
        self.assistant_image = ImageTk.PhotoImage(img)

        # Update the canvas image
        self.frames[MainPage].canvas.itemconfig(self.frames[MainPage].image_id, image=self.assistant_image)

        # Call this function again after 50ms
        self.after(50, self.animate_image)

    def listen_to_user(self) -> str:
        speechR = SpeechRecognizer()
        transcription = speechR.listen()
        return transcription

    def handle_request(self, request) -> str:

        ic = IntentClassifier()
        intent, entity = ic.parse_input(request)




        ah = ActionHandler()
        response = ah.handle_action(intent, entity)

        return response



#-----------------------------------------------------------------------------------------------------------------------
# MAIN WINDOW


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating a canvas to place the image
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()

        # Loading the image using PhotoImage
        self.assistant_image = tk.PhotoImage(file="assistant1.png")
        self.image_id = self.canvas.create_image(200, 200, image=self.assistant_image)



        # Adding the text widget to the frame
        # orange: "#eb5b0b"
        # grey: "#5c5b5b"
        self.response_box = tk.Text(self, height=10, width=50, state="disabled", bd=6, fg="#eb5b0b")
        self.response_box.pack(pady=(0, 60), padx=30)

        switch_window_button = ttk.Button(
            self,
            text="Settings",
            command=lambda: controller.show_frame(SettingsPage),
        )
        switch_window_button.pack(side="left", padx=5, pady=5)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = ttk.Button(
            self,
            text="Help",
            command=lambda: controller.show_frame(HelpPage),
        )
        switch_window_button.pack(side="left")



#-----------------------------------------------------------------------------------------------------------------------
# HELP PAGE


class HelpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="This is the Help Page", wraplength=100000)
        label.pack(padx=10, pady=10)

        switch_window_button = ttk.Button(self, text="Return", command=lambda: controller.show_frame(MainPage))
        switch_window_button.pack(side="bottom", fill=tk.X)


#-----------------------------------------------------------------------------------------------------------------------
# OPTIONS PAGE


class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        title_label = ttk.Label(self, text="Settings")
        title_label.pack(padx=10, pady=10)

        separator = ttk.Separator(self, orient='horizontal')
        separator.pack(fill='x')

        gender_label = ttk.Label(self, text="Virtual Assistant Voice")
        gender_label.pack(padx=10, pady=(40, 10))


        self.gender = tk.StringVar()

        self.gender_combobox = ttk.Combobox(self, textvariable=self.gender, width=10, state="readonly")
        self.gender_combobox["values"] = ("Male", "Female")
        self.gender_combobox.current(0)
        self.gender_combobox.config()
        self.gender_combobox.pack()


        switch_window_button = ttk.Button(self, text="Return", command=lambda: controller.show_frame(MainPage))
        switch_window_button.pack(side="bottom", fill=tk.X)


# -----------------------------------------------------------------------------------------------------------------------



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

    testObj.add_response("hello, how may I assist you?", "assistant")

    testObj.mainloop()

