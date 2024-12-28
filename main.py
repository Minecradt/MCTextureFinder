import tkinter as tk
import os,json
from functools import partial
def scanPredicates(jsonfile,pack="pack"):
    assetsFolder = f"{pack}/assets/minecraft/models/item"
    with open(os.path.join(assetsFolder,jsonfile),'r') as f:
        jsondata = json.load(f)
        overrides = jsondata['overrides']
        #overrides is a list
        overridesdict = {}
        print(overrides)
        for i in overrides:
            #make sure that predicate contains custom_model
            if not 'custom_model_data' in i['predicate'].keys():
                continue
            overridesdict[i['model'].replace("minehut:cosmetics/",'').replace('elitecreatures:halloween_cosmetics','')] = i['predicate']['custom_model_data']
        return overridesdict
def scanInPack(pack="pack"):
    assetsFolder = f"{pack}/assets/minecraft/models/item"
    files = os.listdir(assetsFolder)
    #filter out files and folders
    files = [file for file in files if os.path.isfile(os.path.join(assetsFolder,file))]
    print(files)
    return files
# Function to be called when the button is clicked
def on_button_click():
    print("Button was clicked!")

# Create the main window
root = tk.Tk()

# Set the title of the window
root.title("Tkinter Button Example")

# Set the size of the window (optional)
root.geometry("400x300")  # width x height

# Create a button widget


# ADD packs

def remove_all_buttons():
    for widget in root.winfo_children():  # Loop through all child widgets
        if isinstance(widget, tk.Button) or isinstance(widget,tk.Entry):  # Check if it's a Button
            widget.destroy()  # Remove the button from the window
def addButtonsPredicate(json,pack="pack"):
    remove_all_buttons()
    things = scanPredicates(json,pack)
    x,y = 0,0
    for i in things.keys():
        label = tk.Entry(root,width=40)
        label.insert(tk.END, i + ": " + str(things[i]))  # Set default text
        label.config(state="readonly")  # Make it read-only

        label.grid(row=y,column=x)
        x += 1
        if x==5:
            y += 1
            x = 0
    tk.Button(root,text="Back",command=scanAndAdd).grid(row=y,column=x)
        


def scanAndAdd():
    x = 0
    y = 0
    remove_all_buttons()
    for i in scanInPack():
        button = tk.Button(root,text=i.replace('.json',''),command=partial(addButtonsPredicate,i,"pack"))
        button.grid(row=y,column=x)
        x += 1
        if x==5:
            y += 1
            x = 0
scanAndAdd()
# Run the main event loop to keep the window open
root.mainloop()
