from tkinter import *
from math import *
from functools import partial
   

def esconder(identificador, k, xk, gxk, fxk, e, lbResultadoFinal, lbRF, lbIteracoes, lbErro):
    linhas = len(k)
    global hidden
    if identificador == "rf":
        if hidden:
            for i in range(len(k)):
                k[i].grid(row=8+i, column = 0)
                xk[i].grid(row=8+i, column = 1)
                gxk[i].grid(row=8+i, column = 2)
                fxk[i].grid(row=8+i, column = 3)
                e[i].grid(row=8+i, column = 4)
        else:
            for i in range(len(k)):
                k[i].grid_forget()
                xk[i].grid_forget()
                gxk[i].grid_forget()
                fxk[i].grid_forget()
                e[i].grid_forget()
    else:
        if hidden:
            for i in range(len(k)):
                if i == identificador:
                    pass
                else:
                    k[i].grid(row=8+i, column = 0)
                    xk[i].grid(row=8+i, column = 1)
                    gxk[i].grid(row=8+i, column = 2)
                    fxk[i].grid(row=8+i, column = 3)
                    e[i].grid(row=8+i, column = 4)
            lbResultadoFinal.grid(row=linhas+9, column = 0)
            lbRF.grid(row=linhas+9, column = 1)
            lbIteracoes.grid(row=linhas+9, column = 2)
            lbErro.grid(row=linhas+9, column = 3)

        else:
            for i in range(len(k)):
                if i == identificador:
                    pass
                else:
                    k[i].grid_forget()
                    xk[i].grid_forget()
                    gxk[i].grid_forget()
                    fxk[i].grid_forget()
                    e[i].grid_forget()
            lbResultadoFinal.grid_forget()
            lbRF.grid_forget()
            lbIteracoes.grid_forget()
            lbErro.grid_forget()

    hidden = not hidden

def guardar_parametros(tfEntradaF, tfEntradaG, tfx0, tfErro, tfPrecisao):
    global hidden
    hidden = False
    funcaoF = lambda x : eval(tfEntradaF.get())
    funcaoG = lambda x : eval(tfEntradaG.get())
    x0 = float(tfx0.get())
    erro = float(tfErro.get())
    precisao = tfPrecisao.get()

    p = ''
    p+="{"
    p+=":"
    p+="."
    p+=precisao
    p+="f"
    p+="}"

    lbKv = []
    lbxkv = []
    lbfxkv = []
    lbgxkv = []
    lbEv = []
    
    linhas = 0
    i = -1
    contar = 0
    y0 = x0
    while True:
        contar+=1
        if contar == 200:
            break
        else:
            if abs(funcaoF(y0))<=erro:
                break
            else:
                y0 = funcaoG(y0)
    if contar<200:
        iteracoes = 0
        while True:
            iteracoes+=1
            lbKv.append(Button(janela, width = 12))
            lbxkv.append(Label(janela))
            lbfxkv.append(Label(janela))
            lbgxkv.append(Label(janela))
            lbEv.append(Label(janela))

            i += 1
            linhas = i

            lbKv[i]["text"] = (str(i))
            lbxkv[i]["text"] = p.format(x0)
            lbfxkv[i]["text"] = p.format(funcaoF(x0))
            lbgxkv[i]["text"] = p.format(funcaoG(x0))
            lbEv[i]["text"] = p.format(funcaoF(x0))

            lbKv[i].grid(row = 8+i, column = 0)
            lbxkv[i].grid(row = 8+i, column = 1)
            lbgxkv[i].grid(row = 8+i, column = 2)
            lbfxkv[i].grid(row = 8+i, column = 3)
            lbEv[i].grid(row = 8+i, column = 4)

            if abs(funcaoF(x0))<=erro:
                break
            else:
                x0 = funcaoG(x0)
                    
        lbResultadoFinal = Button(janela, text = "Final result", width = 12)
        lbRF = Label(janela, text = "Root = "+p.format(x0))
        lbIteracoes = Label(janela, text = "Iterations number = "+str(iteracoes))
        lbErro = Label(janela, text = "Error = "+p.format(abs(funcaoF(x0))))
        lbResultadoFinal.grid(row = 9+linhas, column = 0)
        lbRF.grid(row = 9+linhas, column = 1)
        lbIteracoes.grid(row = 9+linhas, column = 2)
        lbErro.grid(row = 9+linhas, column = 3)
        for i in range(linhas+1):
            lbKv[i]["command"] = partial(esconder, i, lbKv, lbxkv, lbgxkv, lbfxkv, lbEv, lbResultadoFinal, lbRF, lbIteracoes, lbErro)
        lbResultadoFinal["command"] = partial(esconder, "rf", lbKv, lbxkv, lbgxkv, lbfxkv, lbEv, lbResultadoFinal, lbRF, lbIteracoes, lbErro)
    else:
        lbe = Label(janela, text = "The function g does not converge to the fixed point")
        lbe.grid(row = 5, column = 1)
        
        
janela = Tk()

lbEntradaF = Label(janela, text = "Function f")
lbEntradaG = Label(janela, text = "Function g")
tfEntradaF = Entry(janela)
tfEntradaG = Entry(janela)
lbx0 = Label(janela, text = "x0")
tfx0 = Entry(janela)
lbErro = Label(janela, text = "Error")
tfErro = Entry(janela)

lbPrecisao = Label(janela, text = "Precision")
tfPrecisao = Entry(janela)

lbK = Label(janela, text = "k")
lbXk = Label(janela, text = "xk")
lbfXk = Label(janela, text = "f(xk)")
lbgXk = Label(janela, text = "g(xk)")
lbE = Label(janela, text = "e")

btCalcular = Button(janela, text = "Calculate", width = 10)
btCalcular["command"] = partial(guardar_parametros, tfEntradaF, tfEntradaG, tfx0, tfErro, tfPrecisao)

lbEntradaF.grid(row = 0, column = 0)
tfEntradaF.grid(row = 0, column = 1)

lbEntradaG.grid(row = 1, column = 0)
tfEntradaG.grid(row = 1, column = 1)
lbx0.grid(row = 2, column = 0)
tfx0.grid(row = 2, column = 1)
lbErro.grid(row = 3, column = 0)
tfErro.grid(row = 3, column = 1)
lbPrecisao.grid(row = 4, column = 0)
tfPrecisao.grid(row = 4, column = 1)
btCalcular.grid(row = 5, column = 0)

lbK.grid(row = 6, column = 0)
lbXk.grid(row = 6, column = 1)
lbgXk.grid(row = 6, column = 2, padx = 50)
lbfXk.grid(row = 6, column = 3, padx = 50)
lbE.grid(row = 6, column = 4, padx = 50)

janela.mainloop()
