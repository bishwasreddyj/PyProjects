# #
# # import tkinter as tk
# # import time
# #
# # class DigitalClock:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("Digital Clock")
# #         self.label_time = tk.Label(root, font=('Times New Roman', 40, 'bold'), background='black', foreground='white')
# #         self.label_time.pack(anchor='center', expand=True)
# #         self.update_time()
# #
# #     def update_time(self):
# #         current_time = time.strftime('%H:%M:%S')
# #
# #         self.label_time.config(text=current_time)
# #         self.root.after(1000, self.update_time)
# #
# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     clock = DigitalClock(root)
# #     root.mainloop()
#
# import tkinter as tk
import time
#
# class DigitalClock:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Digital Clock")
#         self.label_time = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
#         self.label_time.pack(anchor='center', expand=True)
#         self.label_name = tk.Label(root, text="Yadagiri Reddy Jonnalagadda", font=('calibri', 14))
#         self.label_name.pack()
#
#         self.update_time()
#
#     def update_time(self):
#         current_time = time.strftime('%H:%M:%S')
#         self.label_time.config(text=current_time)
#         self.root.after(1000, self.update_time)
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     clock = DigitalClock(root)
#     root.mainloop()
import tkinter as tk
import time
class ScrollingLabel(tk.Label):
    def __init__(self, master, text, width=20, scroll_delay=100):
        super().__init__(master, text=text, width=width)
        self.scroll_delay = scroll_delay
        self.start_scroll()

    def start_scroll(self):
        self.after(self.scroll_delay, self.scroll)

    def scroll(self):
        text = self.cget("text")
        text = text[1:] + text[0]
        self.config(text=text)
        self.start_scroll()

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        # self.label_time = ScrollingLabel(root, text="", width=8, scroll_delay=500)
        self.label_time = tk.Label(root, font=('calibri', 100, 'bold'), background='black', foreground='white')

        self.label_time.config(font=('calibri', 100, 'bold'), background='black', foreground='white')
        self.label_time.pack(anchor='center', expand=True)
        self.label_name = ScrollingLabel(root, text="        Yadagiri Reddy Jonnalagadda           ", width=50, scroll_delay=200)
        self.label_name.config(font=('calibri', 32))
        self.label_name.pack()

        self.update_time()

    def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        self.label_time.config(text=current_time)
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()
