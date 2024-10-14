#import tkinter as tk
import customtkinter as ctk
#from tkinter import ttk
from PIL import Image, ImageTk

LIGHT_BORDER = "#cce6ff"
DARK_BORDER = "#343638"
DEFAULT_THEME_MODE = "dark"
TASKBAROFFSET = 20
WINDOW_MAX_SIZE = (1150,768)
WINDOW_MIN_SIZE = (855,600)
WINDOW_DEFAULT_COLORS = ("#b3d9ff","#242424")

class Window(ctk.CTk):
    def __init__(self,*, winDim:tuple[int,int], winTitle:str, winDimLim:tuple[int,int] = None, center:bool = True) -> None:
        """
        Object of ctk.CTk is created and displayed on screen.
        params:
            winDim (tuple(int,int)): The dimensions of the window
            winTitle (str): The title of the window
            winDimLim (tuple(int,int)) (optional): The limit of the window dimensions
            center (bool) (optional): Whether to center the window on the screen
        
        returns:
            None
        """
        super().__init__()
        screenHeight = self.winfo_screenheight()
        screenWidth = self.winfo_screenwidth()
        taskbarOffset = TASKBAROFFSET # This will later be grabbed from config file.
        offsetString = f"+{int(screenWidth/2 - winDim[0]/2)}+{int(screenHeight/2 - winDim[1]/2 - taskbarOffset)}" if center else ""
        
        print(f"Screen dimensions: {screenWidth}x{screenHeight}")
        self.windowLimits = winDimLim if winDimLim else WINDOW_MAX_SIZE # This will later be grabbed from config file.
        

        self._set_appearance_mode(DEFAULT_THEME_MODE) # This will later be grabbed from config file.
        self.title(winTitle)
        self.minsize(*WINDOW_MIN_SIZE) # This will later be grabbed from config file.
        self.maxsize(self.windowLimits[0], self.windowLimits[1])
        self.bind("<Configure>", lambda e: self.on_resize(e))
        self.geometry( f"{winDim[0]}x{winDim[1]}" + offsetString)
        self.configure(fg_color = WINDOW_DEFAULT_COLORS)
        
    
    def buildWindow(self, type:str) -> None:
        self._type= type
        match type.lower():
            case "login":	
                self._buildLogin()
            
            case "register":
                self._buildRegister()
            
            case "verify":
                self._buildVerify()
            
            case _:
                print("Invalid window type")

    def _buildLogin(self):        
        

        self.clear()

        fields = [
            ("user", "Enter Username"),
            ("password","Enter Password")
        ]


        self.registerBtn = ctk.CTkButton(self, 
                                        text="Create Account", 
                                        font=("Arial", 16), 
                                        fg_color="transparent",
                                        border_width=0, 
                                        text_color=("gray10", "#DCE4EE"),
                                        hover=False,
                                        command= lambda: self.buildWindow("Register"))
        self.forgotBtn = ctk.CTkButton(self,
                                        text="Forgot password?", 
                                        font=("Arial", 16), 
                                        fg_color="transparent", 
                                        border_width=0, 
                                        text_color=("gray10", "#DCE4EE"),
                                        hover=False,
                                        command= lambda: print("User forgot account!"))

        self.registerBtn.pack(side="left", padx=0)
        self.forgotBtn.pack(side="right", padx=0)


        self.submitBtn = ctk.CTkButton(self,
                                        text="Login", 
                                        font=("Arial", 16), 
                                        fg_color="transparent", 
                                        border_width=3, 
                                        border_color=(LIGHT_BORDER,DARK_BORDER),
                                        corner_radius=5,
                                        text_color=("gray10", "#DCE4EE"),
                                        command= lambda: print("Logging in user..."),
                                        hover_color=(LIGHT_BORDER,DARK_BORDER))
        
        self.submitBtn.pack(side="right", padx=10)

        layoutManager = LayoutManager("layout1", self)
        layoutManager.layout1("Login", fields, (self.registerBtn, self.forgotBtn), self.submitBtn)

        # self.clear()

        # #Configure window layout
        # self.columnconfigure((0,2), weight = 1, uniform="a")
        # self.columnconfigure(1, weight = 5, uniform="a")
        # self.rowconfigure((0,1), weight = 2, uniform = "a")
        # self.rowconfigure((2,3), weight = 1, uniform="a")

        
        # #Title
        # ctk.CTkLabel(self, text="Login", font=("Arial", 62, "bold"),justify="center").grid(row=0, column=1, sticky="nesw", padx=10, pady=10) #font= will later be grabbed from config file.

        
        # #Theme Change
        # self.themeChangeImg = ctk.CTkImage(light_image= Image.open("./assets/themeLight.png"),dark_image= Image.open("./assets/themeDark.png")) #This picture has been designed using resources from Flaticon.com
        # self.themeChangeBtn = ctk.CTkButton(self, 
        #                                     text="", 
        #                                     font=("Arial", 12), 
        #                                     command=self.switchTheme, 
        #                                     image= self.themeChangeImg, 
        #                                     border_width=0,
        #                                     width=16, 
        #                                     fg_color=(LIGHT_BORDER,DARK_BORDER), 
        #                                     hover=False)
        # self.themeChangeBtn.grid(row=0, column=2, sticky="n", padx=10, pady=10) 

        # #Containers
        # fieldsContainer = ctk.CTkFrame(self, fg_color="transparent")
        # registerForgotContainer = ctk.CTkFrame(self, fg_color="transparent")
        # submitContainer = ctk.CTkFrame(self, fg_color="transparent")

        # #Fields
        # self.userField = Field(fieldsContainer, type="user", prompt="Enter Username")
        # self.passwordField = Field(fieldsContainer, type="password", prompt="Enter Password")

        # fieldsContainer.grid(row=1, column=1, sticky="nesw", padx=10, pady=10)

        # #Register/Forgot
        # self.registerBtn = ctk.CTkButton(registerForgotContainer, 
        #                                 text="Create Account", 
        #                                 font=("Arial", 16), 
        #                                 fg_color="transparent",
        #                                 border_width=0, 
        #                                 text_color=("gray10", "#DCE4EE"),
        #                                 hover=False,
        #                                 command= lambda: self.buildWindow("Register"))
        # self.forgotBtn = ctk.CTkButton(registerForgotContainer,
        #                                 text="Forgot password?", 
        #                                 font=("Arial", 16), 
        #                                 fg_color="transparent", 
        #                                 border_width=0, 
        #                                 text_color=("gray10", "#DCE4EE"),
        #                                 hover=False,
        #                                 command= lambda: print("User forgot account!"))
        
        # self.registerBtn.pack(side="left", padx=0)
        # self.forgotBtn.pack(side="right", padx=0)

        # registerForgotContainer.grid(row=2, column=1, sticky="nesw", padx=10, pady=10)

        # #Submit
        # self.submitBtn = ctk.CTkButton(submitContainer,
        #                                 text="Login", 
        #                                 font=("Arial", 16), 
        #                                 fg_color="transparent", 
        #                                 border_width=3, 
        #                                 border_color=(LIGHT_BORDER,DARK_BORDER),
        #                                 corner_radius=5,
        #                                 text_color=("gray10", "#DCE4EE"),
        #                                 command= lambda: print("Logging in user..."),
        #                                 hover_color=(LIGHT_BORDER,DARK_BORDER))
        # self.submitBtn.pack(side="right", padx=10)

        # submitContainer.grid(row=3, column=1, sticky="nesw", padx=10, pady=10)


    def _buildRegister(self):
        
        self.clear()

        fields = [
            ("user","Enter Username"),
            ("email","Enter Email"),
            ("password","Enter Password"),
            ("password","Confirm Password")
        ]

        businessLabel = ctk.CTkLabel(self, text="Here for business?", font=("Arial", 16))
        self.businessCheckbox = ctk.CTkCheckBox(self, text= "", command=lambda: print("Is business?"), border_width=1, width=24) #width = 24 actual checkbox size.
        self.submitBtn = ctk.CTkButton(self, 
                                        text="Submit", 
                                        font=("Arial", 16), 
                                        fg_color="transparent", 
                                        border_width=3,
                                        border_color=(LIGHT_BORDER,DARK_BORDER), 
                                        corner_radius=5,
                                        text_color=("gray10", "#DCE4EE"),
                                        command= lambda: self.buildWindow("Verify"),
                                        hover_color=(LIGHT_BORDER,DARK_BORDER))
        
        self.layoutManager = LayoutManager("layout1", self)
        self.layoutManager.layout1("Register", fields, (businessLabel,self.businessCheckbox), self.submitBtn)
        
        # #configure window layout
        # self.columnconfigure((0,2), weight = 1, uniform="a")
        # self.columnconfigure(1, weight=5, uniform="a")
        # self.rowconfigure((0,1), weight = 3, uniform = "a")
        # self.rowconfigure((3,4), weight= 1, uniform="a")

        # #Title
        # ctk.CTkLabel(self, text="Register", font=("Arial", 62, "bold"), justify="center").grid(row=0, column=1, sticky="nesw", padx=10, pady=10)

        # #Theme Change
        # self.themeChangeImg = ctk.CTkImage(light_image= Image.open("./assets/themeLight.png"),dark_image= Image.open("./assets/themeDark.png")) #This picture has been designed using resources from Flaticon.com
        # self.themeChangeBtn = ctk.CTkButton(self, 
        #                                     text="", 
        #                                     font=("Arial", 12), 
        #                                     command=self.switchTheme, 
        #                                     image= self.themeChangeImg, 
        #                                     border_width=0,
        #                                     width=16, 
        #                                     fg_color=(LIGHT_BORDER,DARK_BORDER), 
        #                                     hover=False)
        # self.themeChangeBtn.grid(row=0, column=2, sticky="n", padx=10, pady=10) 
    
        # #Containers
        # fieldsContainer = ctk.CTkFrame(self, fg_color="transparent")
        # businessContainer = ctk.CTkFrame(self, fg_color="transparent")
        # submitContainer = ctk.CTkFrame(self, fg_color="transparent")

        # #Fields

        # self.userField = Field(fieldsContainer, type="user", prompt="Enter Username")
        # self.emailField = Field(fieldsContainer, type="email", prompt="Enter Email")
        # self.passwordField = Field(fieldsContainer, type="password", prompt="Enter Password")
        # self.confirmPasswordField = Field(fieldsContainer, type="password", prompt="Confirm Password")

        # fieldsContainer.grid(row=1, column=1, sticky="nesw", padx=10, pady=10)

        # #Business
        # businessContainer.grid_columnconfigure((0,1), weight=1)
        # ctk.CTkLabel(businessContainer, text="Here for business?", font=("Arial", 16)).grid(column=0, row=0, sticky="nsw")
        # self.businessCheckbox = ctk.CTkCheckBox(businessContainer,text= "", command=lambda: print("Is business?"), border_width=1, width=24) #width = 24 actual checkbox size.
        # self.businessCheckbox.grid(column= 1, row=0, sticky="nes")
        # businessContainer.grid(row=2, column=1, sticky="nesw", padx=10, pady=10)

        # #Submit
        # self.submitBtn = ctk.CTkButton(submitContainer, 
        #                                 text="Submit", 
        #                                 font=("Arial", 16), 
        #                                 fg_color="transparent", 
        #                                 border_width=3,
        #                                 border_color=(LIGHT_BORDER,DARK_BORDER), 
        #                                 corner_radius=5,
        #                                 text_color=("gray10", "#DCE4EE"),
        #                                 command= lambda: self.buildWindow("Verify"),
        #                                 hover_color=(LIGHT_BORDER,DARK_BORDER))
        # self.submitBtn.pack(side="right", padx=0)

        # submitContainer.grid(row=4, column=1, sticky="nesw", padx=10, pady=10)

    def _buildVerify(self):
        
        self.clear()
        
        #configure window layout
        self.columnconfigure((0,2), weight = 1, uniform="a")
        self.columnconfigure(1, weight=5, uniform="a")
        self.rowconfigure((0,1,2), weight = 2, uniform = "a")
        self.rowconfigure(3, weight= 1, uniform="a")




        #Title
        ctk.CTkLabel(self, text="Verify Your Account", font=("Arial", 62, "bold"), justify="center").grid(row=0, column=1, sticky="nesw", padx=10, pady=10)

        #Theme Change
        self.themeChangeImg = ctk.CTkImage(light_image= Image.open("./assets/themeLight.png"),dark_image= Image.open("./assets/themeDark.png")) #This picture has been designed using resources from Flaticon.com
        self.themeChangeBtn = ctk.CTkButton(self, 
                                            text="", 
                                            font=("Arial", 12), 
                                            command=self.switchTheme, 
                                            image= self.themeChangeImg, 
                                            border_width=0,
                                            width=16, 
                                            fg_color=(LIGHT_BORDER,DARK_BORDER), 
                                            hover=False)
        self.themeChangeBtn.grid(row=0, column=2, sticky="n", padx=10, pady=10) 

        #Containers
        self.explanationTextContainer = ctk.CTkFrame(self, fg_color="transparent")
        fieldsContainer = ctk.CTkFrame(self, fg_color="transparent")
        submitContainer = ctk.CTkFrame(self, fg_color="transparent")
        
        #Explanation
        explanationText = "We sent a verification code to your email, please insert the code to verify your account"

        ctk.CTkLabel(self.explanationTextContainer, text=explanationText, font=("Arial", 32 ), justify="center", wraplength=32*20).pack(padx= 10) # wraplength = fontsize*20
        self.explanationTextContainer.grid(row=1, column=1, sticky="new", padx=10, pady=10)


        #Authenitication Field
        self.authField = Field(fieldsContainer, type="auth", prompt="Enter Code")
        self.authField.input.bind("<KeyRelease>", self.authField.handleCodeInput)
        fieldsContainer.grid(row=2, column=1, sticky="nesw", padx=10, pady=10)


        #Submit
        self.submitBtn = ctk.CTkButton(submitContainer, 
                                        text="Submit", 
                                        font=("Arial", 16), 
                                        fg_color="transparent", 
                                        border_width=3, 
                                        border_color=(LIGHT_BORDER,DARK_BORDER),
                                        corner_radius=5,
                                        text_color=("gray10", "#DCE4EE"),
                                        command= lambda: self.badCode.pack(side="left", padx=0),
                                        hover_color=(LIGHT_BORDER,DARK_BORDER)
                                        )
        self.submitBtn.pack(side="right", padx=0)
        self.badCode = ctk.CTkFrame(submitContainer, fg_color="transparent")
        ctk.CTkLabel(self.badCode, text="Wrong code!", font=("Arial", 16), text_color="red").pack(side="left", padx=0)
        ctk.CTkButton(self.badCode, text="send another", font=("Arial", 16), text_color="red", fg_color="transparent", hover=False, height=16, width=40 ,anchor = "center", command= lambda: print("Send another code")).pack(side="left", padx=0, pady=0)
        

        submitContainer.grid(row=3, column=1, sticky="nesw", padx=10, pady=10)

    def on_resize(self, _):
       
        if self._type.lower() == "verify":
            explanationContext = self.explanationTextContainer.winfo_children()[0]
            wp = explanationContext.cget("wraplength")
            if self.winfo_width() < (wp * 1.5):
                explanationContext.configure(wraplength= wp - 10)
            elif self.winfo_width() > (wp * 1.5):
                explanationContext.configure(wraplength= wp + 10)	

    def switchTheme(self: ctk.CTk):
        current_mode = self._get_appearance_mode()
        new_mode = "dark" if current_mode == "light" else "light"
        ctk.set_appearance_mode(new_mode)
    
    def switchParent(self, widget: ctk.CTkBaseClass, frame: ctk.CTkFrame, pack_options: dict = None):
        widget.pack_forget()
        widget.pack(in_=frame, **pack_options)
        print (widget.pack_info())
        widget.lift()

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()


class Field(ctk.CTkFrame):
    def __init__(self, parent, type:str, prompt:str) -> None:
        '''
        This class is used to create a field element.
        the overall width of this element is 176px, and the height is 30px.

        Args:
            parent: The parent frame of the field
            type: The type of the field, either "user" or "password"
            prompt: The prompt to display as placeholder text of the field
        
        Returns:
            None
        '''
        
        super().__init__(parent, height=30,fg_color=("#F9F9FA","#343638"), corner_radius=10)
        self.columnconfigure((0,2), weight = 0, uniform="a")
        self.columnconfigure(1, weight = 3, uniform="a")
        self.rowconfigure(0, weight = 1)
        self._type = type

        if type == "password":
            self.input = ctk.CTkEntry(self, show="•", placeholder_text=prompt, font=("Arial", 16), border_width=0)
            parent.passwordVisible = False
            self.passwordShowImage = ctk.CTkImage(light_image= Image.open("./assets/passwordShowLight.png"),dark_image= Image.open("./assets/passwordShowDark.png")) #This picture has been designed using resources from Flaticon.com
            self.passwordHideImage = ctk.CTkImage(light_image= Image.open("./assets/passwordHideLight.png"),dark_image= Image.open("./assets/passwordHideDark.png")) #This picture has been designed using resources from Flaticon.com
            self.passwordShowImgContainer = ctk.CTkButton(self, 
                                            text="", 
                                            image=self.passwordShowImage, 
                                            command= lambda: self.togglePassword(parent),
                                            width=16,
                                            fg_color="transparent",
                                            bg_color="transparent",	
                                            hover=False,
                                            border_width=0,
                                            font=("Arial", 16)
                                            )
            self.passwordShowImgContainer.grid(row=0, column=2, sticky="nesw", padx=2, pady=2)

        else:
            self.input = ctk.CTkEntry(self, placeholder_text=prompt, font=("Arial", 16), border_width=0)

        if type == "auth":	
            self.input.configure(justify="center",font=("Arial", 42, "bold"))

        self.fieldVal = self.input.get()
        self.img = ctk.CTkImage(light_image= Image.open(f'./assets/{type}Light.png'), dark_image=Image.open(f'./assets/{type}Dark.png')) #This picture has been designed using resources from Flaticon.com
        self.imgContainer = ctk.CTkLabel(self, text="", image=self.img, corner_radius=10)

        self.imgContainer.grid(row=0, column=0, sticky="nesw", padx=2, pady=2)
        self.input.grid(row=0, column=1, sticky="nesw", padx=0, pady=0)
        

        self.pack(pady=5, expand=True, fill="x")

    def getFieldVal(self) -> str:
        self.fieldVal= self.input.get()
        return self.fieldVal

    def togglePassword(self, parent):
        if parent.passwordVisible:
            for widget in parent.winfo_children():
                if isinstance(widget, Field) and widget._type == "password":
                    widget.input.configure(show="•")
                    widget.passwordShowImgContainer.configure(image=widget.passwordShowImage)
            parent.passwordVisible = False
        else:
            for widget in parent.winfo_children():
                if isinstance(widget, Field) and widget._type == "password":
                    widget.input.configure(show="")
                    widget.passwordShowImgContainer.configure(image=widget.passwordHideImage)
            parent.passwordVisible = True
    
    def handleCodeInput(self, event):
        if self._type == "auth":
            
            val = self.input.get()
            valLen= len(val)

            if event.keysym == "BackSpace":
                if len(val) < 6:
                    self.input.delete(valLen-1, ctk.END)
            
            elif event.char:
                if not event.char.isalnum():
                    self.input.delete(valLen-1,ctk.END)
                    
                elif val:
                    self.input.insert(ctk.INSERT, "-")
                    if len(val) >= 7:
                        self.input.delete(7, ctk.END)



class LayoutManager():
    def __init__(self, layout: str, window:Window) -> None:
        self.layout = layout
        self.window = window

        
    def layout1(self , title:str, fields:list[tuple[str,str]], checkSection:tuple[ctk.CTkBaseClass,ctk.CTkBaseClass], submitBtm:ctk.CTkButton):
        
        
        #Configure window layout
        self.window.columnconfigure((0,2), weight = 1, uniform="a")
        self.window.columnconfigure(1, weight=5, uniform="a")
        self.window.rowconfigure((0,1), weight = 3, uniform = "a")
        self.window.rowconfigure(2, weight = 2, uniform = "a")
        self.window.rowconfigure(3, weight= 1, uniform="a")
        
        #Title
        labelTitle = ctk.CTkLabel(self.window, text=title, font=("Arial", 62, "bold"),justify="center") #font= will later be grabbed from config file.

        
        #Theme Change
        self.window.themeChangeImg = ctk.CTkImage(light_image= Image.open("./assets/themeLight.png"),dark_image= Image.open("./assets/themeDark.png")) #This picture has been designed using resources from Flaticon.com
        self.window.themeChangeBtn = ctk.CTkButton(self.window, 
                                            text="", 
                                            font=("Arial", 12), 
                                            command= self.window.switchTheme, 
                                            image= self.window.themeChangeImg, 
                                            border_width=0,
                                            width=16, 
                                            fg_color=(LIGHT_BORDER,DARK_BORDER), 
                                            hover=False)

        #Containers
        fieldsContainer = ctk.CTkFrame(self.window, fg_color="transparent")
        checkSectionContainer = ctk.CTkFrame(self.window, fg_color="transparent")
        submitContainer = ctk.CTkFrame(self.window, fg_color="transparent")

        #Fields
        self.window.fields = {}
        for fieldType, fieldPrompt in fields:
            self.window.fields[fieldType] = Field(fieldsContainer, type=fieldType, prompt=fieldPrompt)
        

        #Check Section
      
        self.window.switchParent(checkSection[0], checkSectionContainer, {"side":"left", "padx":10})
        self.window.switchParent(checkSection[1], checkSectionContainer, {"side":"right", "padx":10})
          

        #Submit
        self.window.switchParent(submitBtm, submitContainer, {"side":"right", "padx":10})
        
      
        #Packing 
        self.window.themeChangeBtn.grid(row=0, column=2, sticky="n", padx=10, pady=10)

        labelTitle.grid(row=0, column=1, sticky="nesw", padx=10, pady=10) 
        fieldsContainer.grid(row=1, column=1, sticky="nesw", padx=10, pady=10)
        checkSectionContainer.grid(row=2, column=1, sticky="nesw", padx=10, pady=10)
        submitContainer.grid(row=3, column=1, sticky="nesw", padx=10, pady=10)

def main():
    window = Window(winDim = (1100,600), winTitle= "Login", center= True)
    window.buildWindow("Login")
    window.mainloop()

if __name__ == "__main__":
    main()