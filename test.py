import customtkinter as ctk

class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Create a button and store it as an attribute
        self.widget = ctk.CTkButton(self, text="Click Me", command=self.on_button_click)
        self.widget.pack(pady=10)
        
        # Create a frame and store it as an attribute
        self.frame = ctk.CTkFrame(self, fg_color="gray10")
        self.frame.pack(pady=20)
        #self.frame.pack_propagate(False)

        # Create a button to switch the parent
        self.switch_button = ctk.CTkButton(self, text="Move Button to Frame", command=lambda :self.switchParent(self.widget, self.frame))
        self.switch_button.pack(pady=10)

    def switchParent(self, widget, frame):
        # Unpack the widget from the main window
        self.widget.pack_forget()
        
        # Change the master of the widget to be the frame
        widget.pack(in_=frame, pady=10)
        widget.lift()

    def on_button_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = Window()
    app.mainloop()