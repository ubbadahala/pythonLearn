from PySimpleGUI.PySimpleGUI import PopupAnimated
import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg
import math
import time

def welcome():
    layout = [[sg.Text("Welcome to Numerical Differentiation Program!")], [sg.Button("Enter")]+[sg.Button("Close")]]
    window = sg.Window("Numerical Differentiation", layout)

    while True:
        event, values = window.read()
           
        if event == "Enter":
            window.Close()
            system()
            break

        if event == "Close" or event == sg.WIN_CLOSED:
            window.Close()
            break

def system():
    print('\nCompiled by: Muhammad Ubbadah Al Ala\'')
    print('             3210191044 - 2 SPE-B PENS EEPIS')

    print()
    print('='*5, 'NUMERICAL DIFFERENTIATION', '='*5)
    #print('\nP.S: Sorry for the scattering problem that will make your\ndata slightly shifted right at some interval')
    #print('\nStill working on this bug...')

    # defining the function f(x)
    def f(x):
        return eval(fungsi, {'x': x, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'e': math.exp, 'pi': math.pi, 'np': np})

    # defining the analitical differentiation
    def g(x):
        return eval(tur1, {'x': x, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'e': math.exp, 'pi': math.pi, 'np': np})

    # defining the analitical second differentiation
    def h(x):
        return eval(tur2, {'x': x, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'e': math.exp, 'pi': math.pi, 'np': np})


    # function input section
    fungsi = input('\nInput f(x): ')
    tur1 = input("Input analytical f' (x): ")
    tur2 = input("Input analytical f''(x): ")

    # Input Section
    rangeDO = float(input('\nEnter lower range: '))
    rangeUP = float(input('Enter upper range: '))
    hstep = float(input('Enter h value: '))

    def changeplot():
        plt.close()
        plot = input("\nSelect plotting method:\n1. f  (x) Value\t   4. f' (x) Error\n2. f' (x) Value\t   5. f''(x) Error\n3. f''(x) Value\t   6. Without plot\n\nChoose the number: ")


        # Calculation Section
        print("\nStep\tf(x)\t\tf'(x)\t\tf''(x)\t\tf'(x)EX\t\tf''(x)EX\te\t\te2\n")

        def maxmin(rangeDO,rangeUP, hstep):
            condition = True
            start_time = time.time()
            count = int(abs(rangeUP-rangeDO)/hstep)
            while condition:
                def PlotLogic():
                    bobo = np.arange(rangeDO, stepUP)
                    if plot == '1':
                        for i in bobo:
                            plt.xlabel("Range")
                            plt.ylabel("f(x) Value")
                            plt.title("Numerical Differentiation => f(x) = "+fungsi)
                        plt.scatter(i, fungsix, color='red', )
                        plt.pause(0.00001)
                        plt.autoscale(enable=True, axis='both', tight=None)

                    if plot == '2':
                        for i in bobo:
                            plt.xlabel("Range")
                            plt.ylabel("f'(x) Value")
                            plt.title("Numerical Differentiation => f'(x) = "+tur1)
                        G = plt.scatter(i, fungsitur, color = 'green')
                        B = plt.scatter(i, fungsieks, color ='blue')
                        plt.pause(0.00001)
                        plt.autoscale(enable=True, axis='both', tight=None)
                        plt.legend((G, B),
                        ("f'(x)", "f'(x)EX"),
                        scatterpoints=1,
                        loc='lower right',
                        ncol=2,
                        fontsize=8)

                    if plot == '3':
                        for i in bobo:
                            plt.xlabel("Range")
                            plt.ylabel("f''(x) Value")
                            plt.title("Numerical Differentiation => f''(x) = "+tur2)
                        O = plt.scatter(i, fungsitur2, color = 'Orange')
                        T = plt.scatter(i, fungsieks2, color = 'teal' )
                        plt.pause(0.00001)
                        plt.autoscale(enable=True, axis='both', tight=None)
                        plt.legend((O, T),
                        ("f''(x)", "f''(x)EX"),
                        scatterpoints=1,
                        loc='lower right',
                        ncol=2,
                        fontsize=8)

                    if plot == '4':
                        for i in bobo:
                            plt.xlabel("Range")
                            plt.ylabel("f'(x) Error Value")
                            plt.title("Numerical Differentiation => Error f'(x)")
                        plt.scatter(i, err)
                        plt.pause(0.00001)
                        plt.autoscale(enable=True, axis='both', tight=None)

                    if plot == '5':
                        for i in bobo:
                            plt.xlabel("Range")
                            plt.ylabel("f''(x) Error Value")
                            plt.title("Numerical Differentiation => Error f''(x)")
                        plt.scatter(i, err2)
                        plt.pause(0.00001)
                        plt.autoscale(enable=True, axis='both', tight=None)

                    if plot == '6':
                        None
                condition = rangeDO < rangeUP

                fungsix = f(rangeDO)
                stepUP = rangeDO + hstep
                stepDO = rangeDO - hstep 
                fungsitur = (f(stepUP) - f(stepDO))/(2*hstep)
                fungsitur2 = (f(stepUP+hstep) - (2*f(rangeDO))+ f(stepDO-hstep))/(4*(hstep**2))
                fungsieks = g(rangeDO)
                fungsieks2 = h(rangeDO)
                err = abs(fungsitur-fungsieks)
                err2 = abs(fungsitur2-fungsieks2)
                print('%0.3f\t%0.6f\t%0.6f\t%0.6f\t%0.6f\t%0.6f\t%0.6f\t%0.6f\n' %(rangeDO,fungsix,fungsitur,fungsitur2,fungsieks,fungsieks2,err, err2))
                
                
                PlotLogic()
                rangeDO = stepUP
            waktu = time.time()-start_time
            print("Your", count ,"calculations finished in", time.time() - start_time, "seconds")
            print("Approximately:", count/waktu, "calc/s")   

        maxmin(rangeDO, rangeUP, hstep)
        

    def bye():
        layout = [[sg.Text("Thank you for using this program")], [sg.Button("Close program")]]
        window = sg.Window("Numerical Differentiation", layout)

        while True:
            event, values = window.read()

            if event == "Close program" or event == sg.WIN_CLOSED:
                window.Close()
                break

    def dialog():
        layout = [[sg.Text("Do you want to rewrite f(x)?")], [sg.Button("Yes")]+[sg.Button("No")]]
        window = sg.Window("Numerical Differentiation", layout)

        while True:
            event, values = window.read()

            if event == "Yes":
                window.Close()
                system()
                break

            if event == "No" or event == sg.WIN_CLOSED:
                window.Close()
                bye()
                break

    while True:
        changeplot()
        if input("\nChange the plot?\nEvery changes in plot will make the program recalculate differentiation (Y/N): ").strip().upper() != 'Y':
            dialog()
            print()
            break

welcome()