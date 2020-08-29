from tkinter import *
from math import *
from functools import partial
   

def esconder(identificador, k, ak, bk, fAk, fBk, Xm, fXm, e, lbResultadoFinal, lbRF, lbIteracoes, lbErro):
    linhas = len(ak)-1
    global hidden
    if identificador == "rf":
        if hidden:
            for i in range(len(ak)):
                k[i].grid(row=7+i, column = 0)
                ak[i].grid(row=7+i, column = 1)
                bk[i].grid(row=7+i, column = 2)
                fAk[i].grid(row=7+i, column = 3)
                fBk[i].grid(row=7+i, column = 4)
                Xm[i].grid(row=7+i, column = 5)
                fXm[i].grid(row=7+i, column = 6)
                e[i].grid(row=7+i, column = 7)
        else:
            for i in range(len(ak)):
                k[i].grid_forget()
                ak[i].grid_forget()
                bk[i].grid_forget()
                fAk[i].grid_forget()
                fBk[i].grid_forget()
                Xm[i].grid_forget()
                fXm[i].grid_forget()
                e[i].grid_forget()
    else:
        if hidden:
            for i in range(len(ak)):
                if i == identificador:
                    pass
                else:
                    k[i].grid(row=7+i, column = 0)
                    ak[i].grid(row=7+i, column = 1)
                    bk[i].grid(row=7+i, column = 2)
                    fAk[i].grid(row=7+i, column = 3)
                    fBk[i].grid(row=7+i, column = 4)
                    Xm[i].grid(row=7+i, column = 5)
                    fXm[i].grid(row=7+i, column = 6)
                    e[i].grid(row=7+i, column = 7)
            lbResultadoFinal.grid(row=linhas+8, column = 0)
            lbRF.grid(row=linhas+8, column = 1)
            lbIteracoes.grid(row=linhas+8, column = 2)
            lbErro.grid(row=linhas+8, column = 3)

        else:
            for i in range(len(ak)):
                if i == identificador:
                    pass
                else:
                    k[i].grid_forget()
                    ak[i].grid_forget()
                    bk[i].grid_forget()
                    fAk[i].grid_forget()
                    fBk[i].grid_forget()
                    Xm[i].grid_forget()
                    fXm[i].grid_forget()
                    e[i].grid_forget()
            lbResultadoFinal.grid_forget()
            lbRF.grid_forget()
            lbIteracoes.grid_forget()
            lbErro.grid_forget()

    hidden = not hidden

def guardar_parametros(tfEntrada, tfInicioIntervalo, tfFinalIntervalo, tfErro, tfPrecisao):
    
    global hidden
    hidden = False
    funcao = lambda x : eval(tfEntrada.get())
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

    k = ceil((log10(b-a)-log10(erro)-log10(2))/log10(2))

    if funcao(a)*funcao(b)>=0:
        lbErro = Label(janela, text = "Erro no método da bissecção")
        lbErro.grid(row = 5, column = 1)
    else:
        lbKv = []
        lbAkv = []
        lbBkv = []
        lbfAkv = []
        lbfBkv = []
        lbXmv = []
        lbfXmv = []
        lbEv = []

        for i in range(k+1):
            lbAkv.append(Label(janela))
            lbBkv.append(Label(janela))
            lbfAkv.append(Label(janela))
            lbfBkv.append(Label(janela))
            lbXmv.append(Label(janela))
            lbfXmv.append(Label(janela))
            lbEv.append(Label(janela))
            lbKv.append(Button(janela, width = 12))

        a_n = a
        b_n = b
        aux = 0
        linhas = 0
        for i in range(k+1):
            linhas = i
            lbAkv[i]["text"] = p.format(a_n)
            lbBkv[i]["text"] = p.format(b_n)
            lbfAkv[i]["text"] = p.format(funcao(a_n))
            lbfBkv[i]["text"] = p.format(funcao(b_n))
            lbKv[i]["text"] = (str(i))
            m_n = (a_n+b_n)/2
            lbXmv[i]["text"] = p.format(m_n)
            lbfXmv[i]["text"] = p.format(funcao(m_n))
            lbKv[i].grid(row = 7+i, column = 0)
            lbAkv[i].grid(row = 7+i, column = 1)
            lbBkv[i].grid(row = 7+i, column = 2)
            lbfAkv[i].grid(row = 7+i, column = 3)
            lbfBkv[i].grid(row = 7+i, column = 4)
            lbXmv[i].grid(row = 7+i, column = 5)
            lbfXmv[i].grid(row = 7+i, column = 6)
            if i == 0:
                lbEv[i]["text"] = ("-")
                lbEv[i].grid(row = 7+i, column = 7)
            else:
                aux = abs((m_n-aux_erro)/m_n)
                lbEv[i]["text"] = p.format(aux)
                lbEv[i].grid(row = 7+i, column = 7)
            aux_erro = m_n
            if funcao(a_n)*funcao(m_n)<0:
                a_n = a_n
                b_n = m_n
            elif funcao(b_n)*funcao(m_n)<0:
                a_n = m_n
                b_n = b_n
            elif funcao(m_n) == 0:
                break
            else:
                lbFalha = Label(janela, text = "O método da bissecção falhou")
                lbFalha.grid(row = 8+i, column = 0)
        lbResultadoFinal = Button(janela, text = "Resultado final", width = 12)
        lbRF = Label(janela, text = "Raiz = "+p.format(m_n))
        lbIteracoes = Label(janela, text = "Número de iterações = "+str(k))
        lbErro = Label(janela, text = "Erro = "+p.format(aux))
        lbResultadoFinal.grid(row = 8+linhas, column = 0)
        lbRF.grid(row = 8+linhas, column = 1)
        lbIteracoes.grid(row = 8+linhas, column = 2)
        lbErro.grid(row = 8+linhas, column = 3)
        for i in range(k+1):
            lbKv[i]["command"] = partial(esconder, i, lbKv, lbAkv, lbBkv, lbfAkv, lbfBkv, lbXmv, lbfXmv, lbEv, lbResultadoFinal, lbRF, lbIteracoes, lbErro)
        lbResultadoFinal["command"] = partial(esconder, "rf", lbKv, lbAkv, lbBkv, lbfAkv, lbfBkv, lbXmv, lbfXmv, lbEv, lbResultadoFinal, lbRF, lbIteracoes, lbErro)
janela = Tk()

lbEntrada = Label(janela, text = "Função")
tfEntrada = Entry(janela)
lbInicioIntervalo = Label(janela, text = "Inicio do intervalo")
tfInicioIntervalo = Entry(janela)
lbFinalIntervalo = Label(janela, text = "Final do intervalo")
tfFinalIntervalo = Entry(janela)
lbErro = Label(janela, text = "Erro")
tfErro = Entry(janela)

lbPrecisao = Label(janela, text = "Precisão")
tfPrecisao = Entry(janela)

lbK = Label(janela, text = "k")
lbAk = Label(janela, text = "ak")
lbBk = Label(janela, text = "bk")
lbfAk = Label(janela, text = "f(ak)")
lbfBk = Label(janela, text = "f(bk)")
lbXm = Label(janela, text = "Xm")
lbfXm = Label(janela, text = "f(Xm)")
lbE = Label(janela, text = "e")

btCalcular = Button(janela, text = "Calcular", width = 10)
btCalcular["command"] = partial(guardar_parametros, tfEntrada, tfInicioIntervalo, tfFinalIntervalo, tfErro, tfPrecisao)

lbEntrada.grid(row = 0, column = 0)
tfEntrada.grid(row = 0, column = 1)

lbInicioIntervalo.grid(row = 1, column = 0)
tfInicioIntervalo.grid(row = 1, column = 1)
lbFinalIntervalo.grid(row = 2, column = 0)
tfFinalIntervalo.grid(row = 2, column = 1)
lbErro.grid(row = 3, column = 0)
tfErro.grid(row = 3, column = 1)
lbPrecisao.grid(row = 4, column = 0)
tfPrecisao.grid(row = 4, column = 1)
btCalcular.grid(row = 5, column = 0)

lbK.grid(row = 6, column = 0)
lbAk.grid(row = 6, column = 1)
lbBk.grid(row = 6, column = 2, padx = 50)
lbfAk.grid(row = 6, column = 3, padx = 50)
lbfBk.grid(row = 6, column = 4, padx = 50)
lbXm.grid(row = 6, column = 5, padx = 50)
lbfXm.grid(row = 6, column = 6, padx = 50)
lbE.grid(row = 6, column = 7, padx = 50)


janela.mainloop()
