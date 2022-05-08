import requests, json, pprint
import tkinter as tk
from tkinter import ttk
import threading

apiUrl = "https://covidnigeria.herokuapp.com/api"
def sendRequest(url: str, result=[]) -> dict:
    response = requests.get(apiUrl).text
    data = json.loads(response)
    # use to output result from thread
    result.append(data)
    return data
statesInNg = ["Abia", "Adamawa", "AkwaIbom",  "Anambra",  "Bauchi", "Bayelsa",
  "Benue","Borno","Cross River","Delta","Ebonyi","Edo",
  "Ekiti", "Enugu", "FCT", "Gombe", "Imo", "Jigawa",
  "Kaduna","Kano",  "Katsina", "Kebbi",  "Kogi",  "Kwara",  "Lagos",
  "Nasarawa", "Niger",  "Ogun",  "Ondo", "Osun",  "Oyo",
  "Plateau",  "Rivers",  "Sokoto",  "Taraba",  "Yobe",  "Zamfara"
]

def displayData():
    """ displays the covid 19 data to resultText"""
    response = []
    try:
        t1 = threading.Thread(target=sendRequest, args=(apiUrl,response))
        t1.start()
        t1.join()
        data = response[0]
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

def thread_handler(*event):
    t2 = threading.Thread(target=displayData)
    t2.start()

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
                      relief = "raised", command = thread_handler)
resultBtn.place(relwidth = 0.3, relheight = 1.0, relx = 0.65)
root.bind("<Return>", thread_handler)

result = tk.StringVar()
resultText = tk.Label(bottomFrame, textvariable = result, font = ("Helvetica", 16))
resultText.place(relwidth = 1.0, relheight = 1.0)

root.mainloop()
