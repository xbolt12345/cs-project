import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Welcome')
        self.root.geometry('400x300')
        self.root.configure(bg='lightblue')

        # Create frames for Sign In, Sign Up, and Tracking
        self.sign_in_frame = tk.Frame(root, bg='lightblue')
        self.sign_up_frame = tk.Frame(root, bg='lightblue')
        self.tracking_frame = tk.Frame(root, bg='lightblue')

        self.create_sign_in_frame()
        self.create_sign_up_frame()
        self.create_tracking_frame()

        # Initialize the user's name
        self.user_name = ""

        # Show the sign-in frame initially
        self.show_sign_in_frame()

    def create_sign_in_frame(self):
        label = tk.Label(self.sign_in_frame, text="Sign In", font=('Arial', 24), bg='lightblue')
        label.pack(pady=20)

        username_label = tk.Label(self.sign_in_frame, text="Username:", bg='lightblue')
        username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.sign_in_frame)
        self.username_entry.pack(pady=5)

        password_label = tk.Label(self.sign_in_frame, text="Password:", bg='lightblue')
        password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.sign_in_frame, show='*')
        self.password_entry.pack(pady=5)

        sign_in_button = tk.Button(self.sign_in_frame, text="Sign In", command=self.sign_in)
        sign_in_button.pack(pady=20)

        switch_to_sign_up_button = tk.Button(self.sign_in_frame, text="Don't have an account? Sign Up", command=self.show_sign_up_frame)
        switch_to_sign_up_button.pack()

    def create_sign_up_frame(self):
        label = tk.Label(self.sign_up_frame, text="Sign Up", font=('Arial', 24), bg='lightblue')
        label.pack(pady=20)

        name_label = tk.Label(self.sign_up_frame, text="Name:", bg='lightblue')
        name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.sign_up_frame)
        self.name_entry.pack(pady=5)

        id_label = tk.Label(self.sign_up_frame, text="ID:", bg='lightblue')
        id_label.pack(pady=5)
        self.id_entry = tk.Entry(self.sign_up_frame)
        self.id_entry.pack(pady=5)

        details_label = tk.Label(self.sign_up_frame, text="Details:", bg='lightblue')
        details_label.pack(pady=5)
        self.details_entry = tk.Entry(self.sign_up_frame)
        self.details_entry.pack(pady=5)

        sign_up_button = tk.Button(self.sign_up_frame, text="Sign Up", command=self.sign_up)
        sign_up_button.pack(pady=20)

        switch_to_sign_in_button = tk.Button(self.sign_up_frame, text="Already have an account? Sign In", command=self.show_sign_in_frame)
        switch_to_sign_in_button.pack()

    def create_tracking_frame(self):
        self.tracking_label = tk.Label(self.tracking_frame, text="", font=('Arial', 24), bg='lightblue')
        self.tracking_label.pack(pady=20)

        track_income_button = tk.Button(self.tracking_frame, text="Track Income", command=self.track_income)
        track_income_button.pack(pady=10)

        track_expenses_button = tk.Button(self.tracking_frame, text="Track Expenses", command=self.track_expenses)
        track_expenses_button.pack(pady=10)

    def show_sign_in_frame(self):
        self.sign_up_frame.pack_forget()  # Hide the sign-up frame
        self.tracking_frame.pack_forget()  # Hide the tracking frame
        self.sign_in_frame.pack(fill='both', expand=True)  # Show the sign-in frame

    def show_sign_up_frame(self):
        self.sign_in_frame.pack_forget()  # Hide the sign-in frame
        self.tracking_frame.pack_forget()  # Hide the tracking frame
        self.sign_up_frame.pack(fill='both', expand=True)  # Show the sign-up frame

    def show_tracking_frame(self):
        self.sign_in_frame.pack_forget()  # Hide the sign-in frame
        self.sign_up_frame.pack_forget()  # Hide the sign-up frame
        self.tracking_frame.pack(fill='both', expand=True)  # Show the tracking frame

        # Update the tracking label with the user's name
        self.tracking_label.config(text=f"Welcome, {self.user_name}! Choose an option:")

    def sign_in(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # For demonstration, assume sign-in is always successful
        print(f"Sign In - Username: {username}, Password: {password}")
        self.user_name = username  # Store the username
        self.show_tracking_frame()  # Show the tracking frame after sign-in

    def sign_up(self):
        name = self.name_entry.get()
        user_id = self.id_entry.get()
        details = self.details_entry.get()
        print(f"Sign Up - Name: {name}, ID: {user_id}, Details: {details}")
        self.user_name = name  # Store the user's name
        self.show_tracking_frame()  # Show the tracking frame after sign-up

    def track_income(self):
        print("Tracking Income...")  # Placeholder for tracking income logic

    def track_expenses(self):
        print("Tracking Expenses...")  # Placeholder for tracking expenses logic

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
