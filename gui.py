import tkinter as tk
from tkinter import messagebox

class ErrorCodeApp:
    def __init__(self, master):
        self.master = master
        master.title('رموز أخطاء السيارات')  # "Car Error Codes"
        master.geometry('400x300')
        master.configure(bg='#2E2E2E')  # Dark theme

        self.label = tk.Label(master, text='أدخل رمز الخطأ:', bg='#2E2E2E', fg='white')  # Label in Arabic
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        self.search_button = tk.Button(master, text='بحث', command=self.search_code)
        self.search_button.pack(pady=5)

        self.clear_button = tk.Button(master, text='مسح', command=self.clear_field)
        self.clear_button.pack(pady=5)

        self.copy_button = tk.Button(master, text='نسخ', command=self.copy_result)
        self.copy_button.pack(pady=5)

        self.result_label = tk.Label(master, text='', bg='#2E2E2E', fg='white')
        self.result_label.pack(pady=10)

    def search_code(self):
        error_code = self.entry.get()
        # Normally you would fetch the data from a database
        # Here, a mockup response is provided for demonstration.
        mock_database = {
            'P0010': {'description': 'حساس موضع عمود الكامات', 'solution': 'تحقق من التوصيلات'},
            'P0011': {'description': 'توقيت عمود الكامات غير صحيح', 'solution': 'استبدال الحساس'},
        }
        result = mock_database.get(error_code, None)
        if result:
            self.result_label['text'] = f"{error_code}: {result['description']}\nحل: {result['solution']}"
        else:
            messagebox.showerror('خطأ', 'رمز الخطأ غير موجود.')

    def clear_field(self):
        self.entry.delete(0, tk.END)
        self.result_label['text'] = ''

    def copy_result(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.result_label['text'])

if __name__ == '__main__':
    root = tk.Tk()
    app = ErrorCodeApp(root)
    root.mainloop()