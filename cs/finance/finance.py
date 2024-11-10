
import tkinter as tk

#Class to load all functions easily.
class start:
    def __init__(self, root):
        self.root = root #defined in the main
        self.root.title('Finance manager') #Header
        self.root.geometry('600x600') #Size of the screen


        self.sign_in = tk.Frame(root, bg = "#737070") #Sign in screen
        self.sign_up = tk.Frame(root, bg = "#737070") #Sign up screen
        self.tracking_frame = tk.Frame(root, bg ="#737070") #Options

        self.USERNAME = "" #User input

        self.create_sign_in() 
        self.create_sign_up()
        self.ask_tracker()

        self.sign_in.pack(fill = "both", expand = True) #To initially show the sign in screen

    def create_sign_in(self): #Details in sign in screen

        signin_label = tk.Label(self.sign_in, text = "Welcome back! Sign In.",bg= "#737070", fg = "Black", font=('Arrus BT', 30 ))
        signin_label.pack(pady=40)

        signin_user = tk.Label(self.sign_in, text = "Username:",bg= "#737070", fg = "Black",font=('Arrus BT',20))
        signin_user.pack(pady=15)
        self.signin_user_entry = tk.Entry(self.sign_in, bg= "Black", fg = "White")
        self.signin_user_entry.pack(pady = 5)

        signin_pass = tk.Label(self.sign_in, text = "Password:",bg= "#737070", fg = "Black", font=('Arrus BT', 20))
        signin_pass.pack(pady=15)
        self.signin_pass_entry = tk.Entry(self.sign_in, bg= "Black", fg = "White",show = '*')
        self.signin_pass_entry.pack(pady=5)

        sign_in_button = tk.Button(self.sign_in, text="Sign In", bg= "#737070", fg = "Black", command=self.sign_in_get)
        sign_in_button.pack(pady=30)

        self.switch_to_sign_up = tk.Button(self.sign_in, text = "Don't have an account? Sign up!", bg= "#737070", fg = "Black", command = self.show_sign_up)
        self.switch_to_sign_up.pack()

    def create_sign_up(self): #Details in sign up screen

        signup_label = tk.Label(self.sign_up, text = "Hi! Sign up.",bg= "#737070", fg = "Black", font=('Arrus BT', 30 ))
        signup_label.pack(pady=40)

        signup_user = tk.Label(self.sign_up, text = "Username:",bg= "#737070", fg = "Black",font=('Arrus BT',20))
        signup_user.pack(pady=15)
        self.signup_user_entry = tk.Entry(self.sign_up, bg= "Black", fg = "White")
        self.signup_user_entry.pack(pady = 5)

        signup_mail = tk.Label(self.sign_up, text = "Email:",bg= "#737070", fg = "Black",font=('Arrus BT',20))
        signup_mail.pack(pady=15)
        self.signup_mail_entry = tk.Entry(self.sign_up, bg= "Black", fg = "White")
        self.signup_mail_entry.pack(pady = 5)

        signup_pass = tk.Label(self.sign_up, text = "Password:",bg= "#737070", fg = "Black", font=('Arrus BT',20) )
        signup_pass.pack(pady=15)
        self.signup_pass_entry = tk.Entry(self.sign_up, bg= "Black", fg = "White", show = '*')
        self.signup_pass_entry.pack(pady = 5)

        sign_up_button = tk.Button(self.sign_up, text="Sign In", bg= "#737070", fg = "Black", command=self.sign_up_get)
        sign_up_button.pack(pady=30)

        self.switch_to_sign_in = tk.Button(self.sign_up, text = "Already have an account? Sign in!", bg= "#737070", fg = "Black", command = self.show_sign_in)
        self.switch_to_sign_in.pack()

    def ask_tracker(self): #Details in tracking screen
        self.track_label = tk.Label(self.tracking_frame, text = "", bg= "#737070", fg = "Black", font=('Arrus BT',20))
        self.track_label.pack(pady = 40)

        track_expenses_button = tk.Button(self.tracking_frame, text = "Track Expenses", bg= "#737070", fg = "Black" , command = self.track_expenses)
        track_expenses_button.pack(pady=15)

        track_income_button = tk.Button(self.tracking_frame, text = "Track Income", bg= "#737070", fg = "Black", command = self.track_income)
        track_income_button.pack(pady=15)

   # def expenses_frame(self):


    def show_sign_in(self): #To show the sign in screen if they click dont have acc
        self.sign_up.pack_forget()
        self.tracking_frame.pack_forget()
        self.sign_in.pack(fill = 'both', expand = True)
    
    def show_sign_up(self):
        self.sign_in.pack_forget()
        self.tracking_frame.pack_forget()
        self.sign_up.pack(fill = 'both', expand = True)

    def show_tracking(self):
        self.sign_up.pack_forget()
        self.sign_in.pack_forget()
        self.tracking_frame.pack(fill = 'both', expand = True)
        self.track_label.config(text=f"Welcome, {self.USERNAME}! What would you like to do today?")

    def sign_in_get(self):
        username = self.signin_user_entry.get()
        password = self.signin_pass_entry.get()
        print("Sign In - Name: ", username, "Password: ", password)
        self.USERNAME = username
        self.show_tracking()
        
    
    def sign_up_get(self):
        name = self.signup_user_entry.get()
        email = self.signup_mail_entry.get()
        Password = self.signup_pass_entry.get()
        print("Sign Up - Name: ", name, "Email: ", email, "Password: ", Password)
        self.USERNAME = name
        self.show_tracking()

    def track_income(self):
        print("Tracking Income")

    def track_expenses(self):
        print("Tracking Expenses")


if __name__ == "__main__":
    root = tk.Tk()
    Start = start(root)
    root.mainloop()