import customtkinter as ctk


def add_tools():
    tools=type.get()
    label=ctk.CTkLabel(scroll,text=tools)
    label.pack()
    type.delete(0,ctk.END)



root=ctk.CTk()
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
root.geometry("750x500")
root.title('Daily Task')

title_label=ctk.CTkLabel(root,text='Daily Task',font=ctk.CTkFont(size=30,weight='bold'))
title_label.pack(padx=10,pady=(40,20))

scroll=ctk.CTkScrollableFrame(root,width=500,height=200)
scroll.pack()

type=ctk.CTkEntry(scroll,placeholder_text='Add To Note')
type.pack(fill='x')

add_button=ctk.CTkButton(root,text='Add',width=500,command=add_tools)
add_button.pack(padx=5,pady=(40,20))

# delete_button=ctk.CTkButton(root,text='Add',width=200,fg_color='red',command=add_tools)
# delete_button.pack(padx=10,pady=(10,20))

root.mainloop()