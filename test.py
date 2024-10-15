import customtkinter as ctk

if __name__ == "__main__":
    window = ctk.CTk()
    window.title("BIG CIRCLE")
    progressbar = ctk.CTkProgressBar(window,
                                     width = 300,
                                     height = 300,
                                     corner_radius= 150,
                                     )
    progressbar.grid(row=0, column=0,padx=100, pady=100)
    progressbar.start()
    
    window.mainloop()
