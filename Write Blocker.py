import winreg as reg
import ctypes
import tkinter as tk
from tkinter import messagebox

def set_write_protection(enable=True):
    try:
        access_registry = reg.ConnectRegistry(None, reg.HKEY_LOCAL_MACHINE)
        storage_policy_key = r'SYSTEM\CurrentControlSet\Control\StorageDevicePolicies' # path in which we have to modify the policies
        
    
        with reg.CreateKey(access_registry, storage_policy_key) as key:
            reg.SetValueEx(key, 'WriteProtect', 0, reg.REG_DWORD, 1 if enable else 0)
        
    
        messagebox.showinfo("Notification", "Write Protection Enabled" if enable else "Write Protection Disabled")
    
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

def enable_protection():
    set_write_protection(True)

def disable_protection():
    set_write_protection(False)


root = tk.Tk()
root.title("Write Protection App")
root.geometry("400x200")  
root.configure(bg="black")  


enable_button = tk.Button(
    root, text="Enable Write Protection", command=enable_protection,
    bg="red", fg="yellow", font=("Helvetica", 14, "bold")
)
enable_button.pack(pady=20)

disable_button = tk.Button(
    root, text="Disable Write Protection", command=disable_protection,
    bg="blue", fg="yellow", font=("Helvetica", 14, "bold")
)
disable_button.pack(pady=20)


root.mainloop()
