import tkinter as tk
from tkinter import ttk
import requests
import motion_sensor as motion_sensor
from utils import BASE_URL

# Global variables

current_frame = 0

class User:
    '''
    Class that contains methods for checking user credentials and registering them.
    '''
    @staticmethod
    def registerUser(name, email, password):
        '''
        Register an user on database.
        '''
        user = {'name': name, 'email': email, 'password': password}
        response = requests.post(BASE_URL + 'signup', json=user)
        return True if response.status_code == 200 else False


    @staticmethod
    def loginUser(email, password):
        '''
        Check login credentials.
        '''
        user = {'email': email, 'password': password}
        response = requests.post(BASE_URL + 'login', json=user)
        return True if response.status_code == 200 else False


class InitialFrame(ttk.Frame):
    '''
    Class that represents the initial page of the program.
    '''
    def __init__(self, container, control):
        super().__init__(container)
        self.control = control

        s = ttk.Style()
        s.configure('my.TButton', font=('Segoe UI', 12))

        welcomeMessage = ttk.Label(self, text='Welcome to Smart Alarm', font=('Segoe UI', 14))
        welcomeMessage.grid(column=0, row=0, padx=5, pady=10)

        help = ttk.Label(self, text='Select one of the options below', font=('Segoe UI', 12))
        help.grid(column=0, row=1, padx=5, pady=10)

        buttonLogin = ttk.Button(self, text='Log in', command=self.goToLogin, style='my.TButton')
        buttonLogin.grid(column=0, row=2, padx=5, pady=20, ipadx=20, ipady=10)

        buttonSignUp = ttk.Button(self, text='Sign up', command=self.goToSignUp, style='my.TButton')
        buttonSignUp.config()
        buttonSignUp.grid(column=0, row=3, padx=5, pady=20, ipadx=20, ipady=10)

        self.grid(column=0, row=0, padx=5, pady=5)

    
    def goToLogin(self):
        '''
        Go to login page.
        '''
        global current_frame
        current_frame = 1
        self.control.change_frame()


    def goToSignUp(self):
        '''
        Go to sign up page.
        '''
        global current_frame
        current_frame = 2
        self.control.change_frame()


class LoginFrame(ttk.Frame):
    '''
    Class that represents the login page.
    '''
    def __init__(self, container, control):
        super().__init__(container)
        self.control = control
        self.login = User.loginUser

        s = ttk.Style()
        s.configure('my.TButton', font=('Segoe UI', 12))

        self.message = ttk.Label(self)
        self.message.grid(column=0, row=5, padx=5, pady=5)

        login = ttk.Label(self, text='Email', font=('Segoe UI', 12))
        login.grid(column=0, row=0, padx=5, pady=5)

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        usernameField = ttk.Entry(self, textvariable=self.username, font=('Segoe UI', 12))
        usernameField.grid(column=0, row=1, padx=5, pady=5)

        login = ttk.Label(self, text='Password', font=('Segoe UI', 12))
        login.grid(column=0, row=2, padx=5, pady=5)

        passField = ttk.Entry(self, textvariable=self.password, show='*', font=('Segoe UI', 12))
        passField.grid(column=0, row=3, padx=5, pady=5)

        buttonLogin = ttk.Button(self, text='Log in', command=self.loginUser, style='my.TButton')
        buttonLogin.grid(column=0, row=4, padx=5, pady=20, ipadx=20, ipady=10)

        signupMessage = ttk.Label(self, text='Do not have an account?', font=('Segoe UI', 12))
        signupMessage.grid(column=0, row=6, padx=5, pady=25)

        buttonSignUp = ttk.Button(self, text='Sign up', command=self.goToSignUp, style='my.TButton')
        buttonSignUp.grid(column=0, row=7, padx=5, pady=0, ipadx=20, ipady=10)

        self.grid(column=0, row=0, padx=5, pady=5)


    def goToSignUp(self):
        '''
        Go to sign up page.
        '''
        global current_frame
        current_frame = 2
        self.control.change_frame()


    def loginUser(self):
        '''
        Validate login credentials.
        '''
        global current_frame
        self.message.destroy()

        username = self.username.get()
        password = self.password.get()

        if self.login(username, password):
            current_frame = 3
            self.control.change_frame()
        else:
            response = 'Invalid credentials.'
            self.message = ttk.Label(self, text=response)
            self.message.grid(column=0, row=5, padx=5, pady=5)


class SignUpFrame(ttk.Frame):
    '''
    Class that represents the sign up page.
    '''
    def __init__(self, container, control):
        super().__init__(container)
        self.control = control
        self.register = User.registerUser

        s = ttk.Style()
        s.configure('my.TButton', font=('Segoe UI', 12))

        self.message = ttk.Label(self)
        self.message.grid(column=0, row=14, padx=5, pady=5)

        self.name = tk.StringVar()
        self.email = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.address = tk.StringVar()
        self.number = tk.StringVar()

        name = ttk.Label(self, text='Name', font=('Segoe UI', 12))
        name.grid(column=0, row=0, padx=5, pady=5)

        nameField = ttk.Entry(self, textvariable=self.name, font=('Segoe UI', 12))
        nameField.grid(column=0, row=1, padx=5, pady=5)

        email = ttk.Label(self, text='Email', font=('Segoe UI', 12))
        email.grid(column=0, row=3, padx=5, pady=5)

        emailField = ttk.Entry(self, textvariable=self.email, font=('Segoe UI', 12))
        emailField.grid(column=0, row=4, padx=5, pady=5)

        password = ttk.Label(self, text='Password', font=('Segoe UI', 12))
        password.grid(column=0, row=5, padx=5, pady=5)

        passwordField = ttk.Entry(self, textvariable=self.password, show='*', font=('Segoe UI', 12))
        passwordField.grid(column=0, row=6, padx=5, pady=5)
        
        buttonSignUp = ttk.Button(self, text='Sign up', command=self.registerUser, style='my.TButton')
        buttonSignUp.grid(column=0, row=13, padx=5, pady=25, ipadx=20, ipady=10)

        signupMessage = ttk.Label(self, text='Already have an account?', font=('Segoe UI', 12))
        signupMessage.grid(column=0, row=15, padx=5, pady=10)

        buttonLogin = ttk.Button(self, text='Log in', command=self.goToLogin, style='my.TButton')
        buttonLogin.grid(column=0, row=16, padx=5, pady=0, ipadx=20, ipady=10)

        self.grid(column=0, row=0, padx=5, pady=5)


    def goToLogin(self):
        '''
        Go to login page.
        '''
        global current_frame
        current_frame = 1
        self.control.change_frame()
    
    def registerUser(self):
        '''
        Register an user.
        '''
        global current_frame
        self.message.destroy()

        name = self.name.get()
        email = self.email.get()
        password = self.password.get()

        if self.register(name, email, password):
            current_frame = 3
            self.control.change_frame()
        else:
            response = 'Email already in use.'
            self.message = ttk.Label(self, text=response)
            self.message.grid(column=0, row=14, padx=5, pady=5)


class MotionSensorFrame(ttk.Frame):
    '''
    Class that represents the motion sensor page of the program.
    '''
    def __init__(self, container, control):
        super().__init__(container)
        self.control = control

        s = ttk.Style()
        s.configure('my.TButton', font=('Segoe UI', 12))

        welcomeMessage = ttk.Label(self, text='Motion Sensor', font=('Segoe UI', 14))
        welcomeMessage.grid(column=0, row=0, padx=5, pady=10)

        help = ttk.Label(self, text='Select one of the options below', font=('Segoe UI', 12))
        help.grid(column=0, row=1, padx=5, pady=10)

        # Adicionar logica de inserir tempo para começar a gravar

        buttonLogin = ttk.Button(self, text='Open sensor', command=self.openMotionSensor, style='my.TButton')
        buttonLogin.grid(column=0, row=2, padx=5, pady=20, ipadx=20, ipady=10)

        self.grid(column=0, row=0, padx=5, pady=5)

    
    def openMotionSensor(self):
        '''
        Open motion sensor.
        '''
        motion_sensor.run()


    def goToSignUp(self):
        '''
        Go to sign up page.
        '''
        global current_frame
        current_frame = 2
        self.control.change_frame()


class ControlFrame(ttk.LabelFrame):
    '''
    Class to control which page will be shown.
    '''
    def __init__(self, container):
        super().__init__(container)

        self.container = container

        self.frame = InitialFrame(container, self)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.change_frame()
    
    def change_frame(self):
        '''
        Switch pages.
        '''
        global current_frame
        self.frame.destroy()

        if current_frame == 0:
            self.frame = InitialFrame(self.container, self)
        elif current_frame == 1:
            self.frame = LoginFrame(self.container, self)
        elif current_frame == 2:
            self.frame = SignUpFrame(self.container, self)
        else:
            self.frame = MotionSensorFrame(self.container, self)

        self.frame.tkraise()


class App(tk.Tk):
    '''
    Class that represents the root page, i.e., the default screen.
    '''
    def __init__(self):
        super().__init__()

        window_width = 600
        window_height = 700

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int((screen_width - window_width) / 2)
        center_y = int((screen_height - window_height) / 2)

        self.title('Smart Alarm')
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)

# Initialize program

app = App()
ControlFrame(app)
app.mainloop()