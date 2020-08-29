from tkinter import *
from math import *
from functools import partial

def esconder(identificador, k, xk, fxk, dfxk, e, lbResultadoFinal, lbRF, lbIteracoes, lbErro):
    linhas = len(k)-1
    global hidden
    if identificador == "rf":
        if hidden:
            for i in range(len(k)):
                k[i].grid(row=8+i, column = 0)
                xk[i].grid(row=8+i, column = 1)
                fxk[i].grid(row=8+i, column = 2)
                dfxk[i].grid(row = 8+i, column = 3)
                e[i].grid(row=8+i, column = 4)
        else:
            for i in range(len(k)):
                k[i].grid_forget()
                xk[i].grid_forget()
                fxk[i].grid_forget()
                dfxk[i].grid_forget()
                e[i].grid_forget()
    else:
        if hidden:
            for i in range(len(k)):
                if i == identificador:
                    pass
                else:
                    k[i].grid(row=8+i, column = 0)
                    xk[i].grid(row=8+i, column = 1)
                    fxk[i].grid(row=8+i, column = 2)
                    dfxk[i].grid(row=8+i, column = 3)
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
                    fxk[i].grid_forget()
                    dfxk[i].grid_forget()
                    e[i].grid_forget()
            lbResultadoFinal.grid_forget()
            lbRF.grid_forget()
            lbIteracoes.grid_forget()
            lbErro.grid_forget()
    hidden = not hidden

def guardar_parametros(tfEntradaF, tfEntradaD, tfInicioIntervalo, tfFinalIntervalo, tfErro, tfPrecisao):
    
    global hidden
    hidden = False
    funcao = lambda x : eval(tfEntradaF.get())
    funcaoderivada = lambda x : eval(tfEntradaD.get())
    a = float(tfInicioIntervalo.get())
    b = float(tfFinalIntervalo.get())
    erro = float(tfErro.get())
    precisao = tfPrecisao.get()

    p = ''
    p+="{"
    p+=":"
    p+="."
    p+=precisao
    p+="f"
    p+="}"

    if funcao(a)*funcao(b)>=0:
        lbErro = Label(janela, text = "Erro no método de Newton-Raphson")
        lbErro.grid(row = 6, column = 1)
    else:
        lbKv = []
        lbxkv = []
        lbfxkv = []
        lbdfxkv = []
        lbEv = []
        
        a_n = a
        b_n = b
        m_n = (a_n+b_n)/2
        aux = 0
        auxx =0
        linhas = 0
        i=-1
        iteracoes = 0
        
        while True:
            iteracoes+=1
            lbKv.append(Button(janela, width = 12))
            lbxkv.append(Label(janela))
            lbfxkv.append(Label(janela))
            lbdfxkv.append(Label(janela))
            lbEv.append(Label(janela))
            
            i+=1
            linhas = i

            lbKv[i]["text"] = (str(i))
            lbxkv[i]["text"] = p.format(m_n)
            lbfxkv[i]["text"] = p.format(funcao(m_n))
            lbdfxkv[i]["text"] = p.format(funcaoderivada(m_n))

            lbKv[i].grid(row = 8+i, column = 0)
            lbxkv[i].grid(row = 8+i, column = 1)
            lbfxkv[i].grid(row = 8+i, column = 2)
            lbdfxkv[i].grid(row = 8+i, column = 3)

            if i == 0:
                lbEv[i]["text"] = ("-")
                lbEv[i].grid(row = 8+i, column = 4)
            else:
                if abs((m_n-aux_erro)/m_n)<=erro:
                    aux = abs((m_n-aux_erro)/m_n)
                    lbEv[i]["text"] = p.format(aux)
                    lbEv[i].grid(row = 8+i, column = 4)
                    break
                else:
                    aux = abs((m_n-aux_erro)/m_n)
                    lbEv[i]["text"] = p.format(aux)
                    lbEv[i].grid(row = 8+i, column = 4)
            aux_erro = m_n
            auxx = m_n-funcao(m_n)/funcaoderivada(m_n)
            m_n = auxx
            
        lbResultadoFinal = Button(janela, text = "Resultado final", width = 12)
        lbRF = Label(janela, text = "Raiz = "+p.format(m_n))
        lbIteracoes = Label(janela, text = "Número de iterações = "+str(iteracoes-1))
        lbErro = Label(janela, text = "Erro = "+p.format(aux))
        lbResultadoFinal.grid(row = 9+linhas, column = 0)
        lbRF.grid(row = 9+linhas, column = 1)
        lbIteracoes.grid(row = 9+linhas, column = 2)
        lbErro.grid(row = 9+linhas, column = 3)
        for i in range(iteracoes):
            lbKv[i]["command"] = partial(esconder, i, lbKv, lbxkv, lbfxkv, lbdfxkv, lbEv, lbResultadoFinal, lbRF, lbIteracoes, lbErro)
        lbResultadoFinal["command"] = partial(esconder, "rf", lbKv, lbxkv, lbfxkv, lbdfxkv, lbEv, lbResultadoFinal, lbRF, lbIteracoes, lbErro)
janela = Tk()

lbEntradaF = Label(janela, text = "Função")
tfEntradaF = Entry(janela)
lbEntradaD = Label(janela, text = "Derivada primeira")
tfEntradaD = Entry(janela)
lbInicioIntervalo = Label(janela, text = "Inicio do intervalo")
tfInicioIntervalo = Entry(janela)
lbFinalIntervalo = Label(janela, text = "Final do intervalo")
tfFinalIntervalo = Entry(janela)
lbErro = Label(janela, text = "Erro")
tfErro = Entry(janela)

lbPrecisao = Label(janela, text = "Precisão")
tfPrecisao = Entry(janela)

lbK = Label(janela, text = "k")
lbxk = Label(janela, text = "xk")
lbfxk = Label(janela, text = "f(xk)")
lbdfxk = Label(janela, text = "f'(xk)")
lbE = Label(janela, text = "e")

btCalcular = Button(janela, text = "Calcular", width = 10)
btCalcular["command"] = partial(guardar_parametros, tfEntradaF, tfEntradaD, tfInicioIntervalo, tfFinalIntervalo, tfErro, tfPrecisao)

lbEntradaF.grid(row = 0, column = 0)
tfEntradaF.grid(row = 0, column = 1)

lbEntradaD.grid(row = 1, column = 0)
tfEntradaD.grid(row = 1, column = 1)

lbInicioIntervalo.grid(row = 2, column = 0)
tfInicioIntervalo.grid(row = 2, column = 1)
lbFinalIntervalo.grid(row = 3, column = 0)
tfFinalIntervalo.grid(row = 3, column = 1)
lbErro.grid(row = 4, column = 0)
tfErro.grid(row = 4, column = 1)
lbPrecisao.grid(row = 5, column = 0)
tfPrecisao.grid(row = 5, column = 1)
btCalcular.grid(row = 6, column = 0)

lbK.grid(row = 7, column = 0)
lbxk.grid(row = 7, column = 1)
lbfxk.grid(row = 7, column = 2, padx = 50)
lbdfxk.grid(row = 7, column = 3, padx = 50)
lbE.grid(row = 7, column = 4, padx = 50)

janela.mainloop()
