'''
the interface 
'''

import tkinter
from tkinter import ttk

if __name__ == '__main__':
    form = tkinter.Tk()

    getFld = tkinter.IntVar()

    form.wm_title('GEO spatial tools')

    stepOne = tkinter.LabelFrame(form, text=" 1. configurations: ")
    stepOne.grid(row=0, columnspan=7, sticky='W', \
                 padx=5, pady=5, ipadx=5, ipady=5,)

    helpLf = tkinter.LabelFrame(form, text=" Quick Help ")
    helpLf.grid(row=0, column=13, columnspan=2, rowspan=12, \
                sticky='NS', padx=5, pady=5)
    helpLbl = tkinter.Label(helpLf, text="Help will come - ask for it.")
    helpLbl.grid(row=0)

    stepTwo = tkinter.LabelFrame(form, text=" 2. Choose the operations you need: ")
    stepTwo.grid(row=2, columnspan=7, sticky='W', \
                 padx=5, pady=5, ipadx=5, ipady=5)

    stepThree = tkinter.LabelFrame(form, text=" 3. Choose the calculations you want: ")
    stepThree.grid(row=3, columnspan=7, sticky='W', \
                   padx=5, pady=5, ipadx=5, ipady=5)

    stepFour = tkinter.LabelFrame(form, text=" 4. Double check and GO: ")
    stepFour.grid(row=4, columnspan=7, sticky='W', \
                   padx=5, pady=5, ipadx=5, ipady=5)

    directory_FileLbl = tkinter.Label(stepOne, text="Select arcpy directory:")
    directory_FileLbl.grid(row=0, column=0, sticky='E', padx=5, pady=2)

    directory_FileTxt = tkinter.Entry(stepOne,width=50)
    directory_FileTxt.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)

    directory_FileBtn = tkinter.Button(stepOne, text="Browse ...")
    directory_FileBtn.grid(row=0, column=8, sticky='W', padx=5, pady=2)

    input_FileLbl = tkinter.Label(stepOne, text="Select input data directory")
    input_FileLbl.grid(row=1, column=0, sticky='E', padx=5, pady=2)

    input_FileTxt = tkinter.Entry(stepOne,width=50)
    input_FileTxt.grid(row=1, column=1, columnspan=7, sticky="WE", pady=2)

    input_FileBtn = tkinter.Button(stepOne, text="Browse ...")
    input_FileBtn.grid(row=1, column=8, sticky='W', padx=5, pady=2)

    output_FileLbl = tkinter.Label(stepOne, text="Select output directory")
    output_FileLbl.grid(row=2, column=0, sticky='E', padx=5, pady=2)

    output_FileTxt = tkinter.Entry(stepOne,width=50)
    output_FileTxt.grid(row=2, column=1, columnspan=7, sticky="WE", pady=2)

    output_FileBtn = tkinter.Button(stepOne, text="Browse ...")
    output_FileBtn.grid(row=2, column=8, sticky='W', padx=5, pady=2)

    
    combo_choice = ttk.Combobox(stepTwo, width=70,values=[
                                    "Wind Index", 
                                    "TWE",
                                    "Proximity",
                                    "Landform",
                                    "Soil Dryness"])
    combo_choice.grid(row=1, column=8, sticky='W', padx=5, pady=2)

    
    combo_choice = ttk.Combobox(stepThree, width=70,values=[
                                    "Weighted Sum", 
                                    "Neuro network",
                                    "Wind Rose Plot"])
    combo_choice.grid(row=1, column=8, sticky='W', padx=5, pady=2)
    

    run_button=tkinter.Button(stepFour, text="RUN")
    run_button.grid(row=0, column=0, sticky='E', padx=5, pady=2)
    progress = ttk.Progressbar(stepFour,style='text.Horizontal.TProgressbar', length=200,
                              maximum=100, value=0)

    form.mainloop()