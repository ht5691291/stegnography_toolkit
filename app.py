from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import stepic  # For steganography (install it via `pip install stepic`)


class IMG_Stegno:
    def __init__(self):
        pass

    def main(self, root):
        root.title("Steganography Toolkit ")
        root.geometry("600x700")
        root.resizable(width=False, height=False)
        root.config(bg="#2a2a72")
        frame = Frame(root, bg="#2a2a72")
        frame.grid()

        title = Label(
            frame,
            text="🔒 Steganography Toolkit 🔍",
            font=("Helvetica", 28, "bold"),
            fg="#f4d03f",
            bg="#2a2a72",
        )
        title.grid(pady=20)
        title.grid(row=0)

    

        encode_btn = Button(
            frame,
            text="Encode Message",
            command=lambda: self.encode_frame1(frame),
            padx=14,
            pady=10,
            bg="#5bc0be",
            fg="white",
            font=("Helvetica", 16, "bold"),
            relief=GROOVE,
        )
        encode_btn.grid(row=1, pady=10)

        decode_btn = Button(
            frame,
            text="Decode Message",
            command=lambda: self.decode_frame1(frame),
            padx=14,
            pady=10,
            bg="#5bc0be",
            fg="white",
            font=("Helvetica", 16, "bold"),
            relief=GROOVE,
        )
        decode_btn.grid(row=2, pady=10)

        subtitle = Label(
        frame,
        text="Project Made by Harsh Tiwari",
        font=("Helvetica", 20),
        fg="Red",
        bg="#2a2a72",
        )
        subtitle.grid(row=3, pady=20)

    def encode_frame1(self, parent_frame):
        parent_frame.destroy()
        encode_frame = Frame(root, bg="#2a2a72")
        encode_frame.grid()

        label1 = Label(
            encode_frame,
            text="🖼️ Select Image to Hide Message",
            font=("Helvetica", 20, "bold"),
            fg="#ff6768",
            bg="#2a2a72",
        )
        label1.grid(row=0)

        select_btn = Button(
            encode_frame,
            text="Select Image",
            command=lambda: self.select_image(encode_frame, True),
            bg="#3aafa9",
            fg="white",
            font=("Helvetica", 16, "bold"),
            relief=GROOVE,
        )
        select_btn.grid(row=1, pady=20)

        back_btn = Button(
            encode_frame,
            text="Go Back",
            command=lambda: self.back(encode_frame),
            bg="#d92027",
            fg="white",
            font=("Helvetica", 16, "bold"),
            relief=GROOVE,
        )
        back_btn.grid(row=2, pady=20)

    def decode_frame1(self, parent_frame):
        parent_frame.destroy()
        decode_frame = Frame(root, bg="#2a2a72")
        decode_frame.grid()

        label1 = Label(
            decode_frame,
            text="🖼️ Select Encoded Image",
            font=("Helvetica", 20, "bold"),
            fg="#ff6768",
            bg="#2a2a72",
        )
        label1.grid(row=0)

        select_btn = Button(
            decode_frame,
            text="Select Image",
            command=lambda: self.select_image(decode_frame, False),
            bg="#3aafa9",
            fg="white",
            font=("Helvetica", 16, "bold"),
            relief=GROOVE,
        )
        select_btn.grid(row=1, pady=20)

        back_btn = Button(
            decode_frame,
            text="Go Back",
            command=lambda: self.back(decode_frame),
            bg="#d92027",
            fg="white",
            font=("Helvetica", 16, "bold"),
            relief=GROOVE,
        )
        back_btn.grid(row=2, pady=20)

    def select_image(self, frame, is_encode):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
        )
        if not file_path:
            return

        img = Image.open(file_path)
        img = img.resize((300, 300))
        img = ImageTk.PhotoImage(img)

        panel = Label(frame, image=img)
        panel.image = img
        panel.grid(row=2, pady=20)

        if is_encode:
            entry_label = Label(
                frame,
                text="Enter the Message to Encode:",
                font=("Helvetica", 14),
                fg="white",
                bg="#2a2a72",
            )
            entry_label.grid(row=3, pady=10)

            message_entry = Entry(frame, width=40, font=("Helvetica", 14))
            message_entry.grid(row=4, pady=10)

            encode_btn = Button(
                frame,
                text="Encode",
                command=lambda: self.encode_message(file_path, message_entry.get()),
                bg="#5bc0be",
                fg="white",
                font=("Helvetica", 16, "bold"),
                relief=GROOVE,
            )
            encode_btn.grid(row=5, pady=20)
        else:
            decode_btn = Button(
                frame,
                text="Decode",
                command=lambda: self.decode_message(file_path),
                bg="#5bc0be",
                fg="white",
                font=("Helvetica", 16, "bold"),
                relief=GROOVE,
            )
            decode_btn.grid(row=3, pady=20)

        back_btn = Button(
            frame,
            text="Go Back",
            command=lambda: self.back(frame),
            bg="#d92027",
            fg="white",
            font=("Helvetica", 16, "bold"),
            relief=GROOVE,
        )
        back_btn.grid(row=6, pady=20)

    def encode_message(self, file_path, message):
        if not message.strip():
            messagebox.showerror("Error", "Please enter a message to encode.")
            return

        try:
            img = Image.open(file_path)
            encoded_img = stepic.encode(img, bytes(message, "utf-8"))
            save_path = filedialog.asksaveasfilename(
                defaultextension=".png", filetypes=[("PNG files", "*.png")]
            )
            if save_path:
                encoded_img.save(save_path)
                messagebox.showinfo("Success", "Message encoded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to encode message. {str(e)}")

    def decode_message(self, file_path):
        try:
            img = Image.open(file_path)
            # Directly retrieve the decoded message
            message = stepic.decode(img)  # Returns a string
            messagebox.showinfo("Decoded Message", message)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decode message. {str(e)}")


    def back(self, frame):
        frame.destroy()
        self.main(root)


# Launch GUI
root = Tk()
stegano_app = IMG_Stegno()
stegano_app.main(root)
root.mainloop()
