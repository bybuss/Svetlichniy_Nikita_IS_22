from tkinter import *


def submit():
    print("Submit Button!")


def choose_files():
    print("File Button!")


root = Tk()
root.title("Contact Form")
root.geometry("400x650+300+200")
root.resizable(False, False)

title_label = Label(root, text="Contact Form", font="Arial 16", anchor=W)
title_label.pack(fill='x', padx=10, pady=5)

line = Canvas(root, height=2, bd=0, highlightthickness=0, relief='ridge')
line.create_line(0, 1, 400, 1, fill="grey")
line.pack(fill='x', padx=10)

name_frame = Frame(root)
name_frame.pack(fill='x', padx=10, pady=5)
name_label_text = Label(name_frame, text="Name ", font="Arial 12", fg="black")
name_label_text.pack(side=LEFT)
name_label_star = Label(name_frame, text="*", font="Arial 12", fg="red")
name_label_star.pack(side=LEFT)
name_entry = Entry(root, font="Arial 12")
name_entry.pack(fill='x', padx=10, pady=5)

email_frame = Frame(root)
email_frame.pack(fill='x', padx=10, pady=5)
email_label_text = Label(email_frame, text="Email ", font="Arial 12", fg="black")
email_label_text.pack(side=LEFT)
email_label_star = Label(email_frame, text="*", font="Arial 12", fg="red")
email_label_star.pack(side=LEFT)
email_entry = Entry(root, font="Arial 12")
email_entry.pack(fill='x', padx=10, pady=5)

phone_frame = Frame(root)
phone_frame.pack(fill='x', padx=10, pady=5)
phone_label_text = Label(phone_frame, text="Phone Number ", font="Arial 12", fg="black")
phone_label_text.pack(side=LEFT)
phone_label_star = Label(phone_frame, text="*", font="Arial 12", fg="red")
phone_label_star.pack(side=LEFT)
phone_entry = Entry(root, font="Arial 12")
phone_entry.pack(fill='x', padx=10, pady=5)

subject_frame = Frame(root)
subject_frame.pack(fill='x', padx=10, pady=5)
subject_label_text = Label(subject_frame, text="Subject ", font="Arial 12", fg="black")
subject_label_text.pack(side=LEFT)
subject_label_star = Label(subject_frame, text="*", font="Arial 12", fg="red")
subject_label_star.pack(side=LEFT)
subject_entry = Entry(root, font="Arial 12")
subject_entry.pack(fill='x', padx=10, pady=5)

message_frame = Frame(root)
message_frame.pack(fill='x', padx=10, pady=5)
message_label_text = Label(message_frame, text="Leave us a few words ", font="Arial 12", fg="black")
message_label_text.pack(side=LEFT)
message_label_star = Label(message_frame, text="*", font="Arial 12", fg="red")
message_label_star.pack(side=LEFT)
message_text = Text(root, height=5, font="Arial 12", wrap=WORD)
message_text.pack(fill='x', padx=10, pady=5)

file_frame = Frame(root)
file_frame.pack(anchor="w", padx=10, pady=5)
file_label = Label(file_frame, text="File Attachments", font="Arial 12", anchor=W)
file_label.pack(anchor="w", side=LEFT)

file_frame_inner = Frame(root)
file_frame_inner.pack(anchor="w", padx=10, pady=5)
file_button = Button(file_frame_inner, text="Choose Files", command=choose_files, font="Arial 12")
file_button.pack(side=LEFT)
file_text = Label(file_frame_inner, text="No file chosen", font="Arial 12", fg="gray")
file_text.pack(side=LEFT, padx=10)


captcha_check = Checkbutton(root, text="I'm not a robot", font="Arial 12")
captcha_check.pack(anchor="w", padx=10, pady=5)

submit_button = Button(root, text="Submit", command=submit, font="Arial 12", bg="Blue", fg="white")
submit_button.pack(anchor="w", padx=10, pady=20)

root.mainloop()
