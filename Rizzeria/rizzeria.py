from tkinter import *

root=Tk()

root.title('Rizzeria')

root.maxsize(800,1000)
root.minsize(800,1000)


logo_img = PhotoImage(file='C:\\Users\\Admin\\Desktop\\Rizzeria\\logo.png')


logo_label = Label(root,image=logo_img, borderwidth=0, highlightthickness=0)
logo_label.pack(pady=10)


root.configure(background='#1C1C1C')


nav_frame = Frame(root, bg="#1C1C1C")
nav_frame.pack(side=TOP, fill=X)


home_button = Button(nav_frame, text="Home", fg="white", bg="#1C1C1C", font=("Arial", 12, "bold"), padx=60)
home_button.pack(side=LEFT, padx=10)

menu_button = Button(nav_frame, text="Menu", fg="white", bg="#1C1C1C", font=("Arial", 12, "bold"), padx=60)
menu_button.pack(side=LEFT, padx=10)

about_button = Button(nav_frame, text="About", fg="white", bg="#1C1C1C", font=("Arial", 12, "bold"), padx=60)
about_button.pack(side=LEFT, padx=10)

contact_button = Button(nav_frame, text="Contact", fg="white", bg="#1C1C1C", font=("Arial", 12, "bold"), padx=60)
contact_button.pack(side=LEFT, padx=10)


hero_frame = Frame(root, bg="#1C1C1C")
hero_frame.pack(fill=X)

hero_text = Label(hero_frame, text="Rizz-ify your taste buds with our signature pizzas", fg="white", bg="#1C1C1C", font=("Arial", 24, "bold"), pady=30)
hero_text.pack()

search_frame = Frame(root, bg="#1C1C1C")
search_frame.pack(pady=20)

search_label = Label(search_frame, text="Search:", fg="white", bg="#1C1C1C", font=("Arial", 16, "bold"))
search_label.pack(side=LEFT, padx=10)

search_entry = Entry(search_frame, width=50, font=("Arial", 14))
search_entry.pack(side=LEFT)

menu_frame = Frame(root, bg="#1C1C1C")
menu_frame.pack(pady=20)

menu_label = Label(menu_frame, text="Menu:", fg="white", bg="#1C1C1C", font=("Arial", 20, "bold"))
menu_label.pack()

menu_list = Listbox(menu_frame, width=50,height=5, font=("Arial", 20),bg="Crimson",fg="white", justify=CENTER)
menu_list.pack(pady=10)

menu_items = ['Rizz-tastic Pizza', 'Rizzi-licious Pizza', 'Rizz-otto Pizza', 'Rizz-oni Pizza', 'Rizz and Cheese', 'Rizz-a-lotta']
for item in menu_items:
    menu_list.insert(END, item)

cta_frame = Frame(root, bg="#1C1C1C")
cta_frame.pack(fill=X, pady=30)

order_button = Button(cta_frame, text="Order Now", fg="white", bg="crimson", font=("Arial", 16, "bold"), padx=20, pady=10)
order_button.pack(side=LEFT, padx=50)

coupon_button = Button(cta_frame, text="Get Coupons", fg="white", bg="crimson", font=("Arial", 16, "bold"), padx=20, pady=10)
coupon_button.pack(side=LEFT, padx=50)

gift_button = Button(cta_frame, text="Gift Cards", fg="white", bg="crimson", font=("Arial", 16, "bold"), padx=20, pady=10)
gift_button.pack(side=LEFT, padx=50)


root.mainloop()



