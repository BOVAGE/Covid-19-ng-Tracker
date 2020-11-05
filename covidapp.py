import requests, json, pprint
import tkinter as tk
from tkinter import ttk

apiUrl = "https://covidnigeria.herokuapp.com/api"
def sendRequest(url: str) -> dict:
    response = requests.get(apiUrl).text
    data = json.loads(response)
    return data
statesInNg = ["Abia", "Adamawa", "AkwaIbom",  "Anambra",  "Bauchi", "Bayelsa",
  "Benue","Borno","Cross River","Delta","Ebonyi","Edo",
  "Ekiti", "Enugu", "FCT", "Gombe", "Imo", "Jigawa",
  "Kaduna","Kano",  "Katsina", "Kebbi",  "Kogi",  "Kwara",  "Lagos",
  "Nasarawa", "Niger",  "Ogun",  "Ondo", "Osun",  "Oyo",
  "Plateau",  "Rivers",  "Sokoto",  "Taraba",  "Yobe",  "Zamfara"
]

def displayData(*event):
    """ displays the covid 19 data to resultText"""
    try:
        data = sendRequest(apiUrl)
    except requests.ConnectionError:
        result.set("Check your internet connection!")
    else:
        statesList = data["data"]["states"]
    #pprint.pprint(statesList)
        for state in statesList:
            if state["state"] == stateSel.get():
                #pprint.pprint(state)
                result.set(f"""
    Covid 19 stats for {stateSel.get()}:
    Cases on Admission: {state["casesOnAdmission"]}
    Death: {state["death"]}
    Number of people Discharged: {state["discharged"]}
    """)
                print(state["state"])
                print(state["casesOnAdmission"])
                print(state["death"])
                print(state["discharged"])

root = tk.Tk()
root.title("Nigeria Covid 19")
root.configure(bg = "#ccffdd")

#frames for combobox and btn
topFrame = tk.Frame(root, bg = "red", bd = "5")
topFrame.place(relx = 0.1, rely = 0.05, relwidth = 0.8, relheight = 0.2)

#frame for label widget
bottomFrame = tk.Frame(root, bg = "white", bd = "5")
bottomFrame.place(relx = 0.1,rely = 0.35, relwidth = 0.8, relheight = 0.6)

statesInNg.insert(0, " ")
stateSel = tk.StringVar()
statesOption = ttk.Combobox(topFrame, textvariable = stateSel)
statesOption["values"] = statesInNg
statesOption.place(relwidth = 0.6, relheight = 1.0)

resultBtn = tk.Button(topFrame, text = "Get Data", bg = "green",
                      relief = "raised", command = displayData)
resultBtn.place(relwidth = 0.3, relheight = 1.0, relx = 0.65)
root.bind("<Return>", displayData)

result = tk.StringVar()
resultText = tk.Label(bottomFrame, textvariable = result, font = ("Helvetica", 16))
resultText.place(relwidth = 1.0, relheight = 1.0)

root.mainloop()
