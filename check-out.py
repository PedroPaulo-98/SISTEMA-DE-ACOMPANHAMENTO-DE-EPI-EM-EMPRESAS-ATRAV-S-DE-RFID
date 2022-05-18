import tkinter
from tkinter import *
import sqlite3
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


def Janela_eng():

    def btn_capacete():
        GPIO.setwarnings(False)
        rfid = SimpleMFRC522()

        id, text = rfid.read()
        idcap = str(id)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sqlcap = ('SELECT nome_cap FROM Capacete_EPI WHERE id_cap_EPI =' + idcap)
        cur.execute(sqlcap)
        nomecap = cur.fetchall()
        for nome_capacete in nomecap:
            nome_cap = str(nome_capacete[0])
        con.commit()
        con.close()

        print(nome_cap)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()

        sql = 'INSERT INTO saida_cap_epi(id_cap, nome_epi_cap, nome_fun_cap, func_cap) VALUES (?, ?, ?, ?)'

        cur.execute(sql, (idcap, nome_cap, nome_f, m))
        con.commit()
        con.close()


        canvas.create_text(
            157.0, 350.5,
            text="OK",
            fill="#000000",
            font=("None", int(25.0)))


    def btn_finalizar():
        janela_eng.destroy()


    def btn_colete():
        GPIO.setwarnings(False)
        rfid = SimpleMFRC522()

        id,text = rfid.read()
        idcol = str(id)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sqlcol = ('SELECT nome_col FROM Colete_EPI WHERE id_col_EPI =' + idcol)
        cur.execute(sqlcol)
        nomecol = cur.fetchall()
        for nome_colete in nomecol:
            nome_col = str(nome_colete[0])
        con.commit()
        con.close()

        print(nome_col)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()

        sql = 'INSERT INTO saida_col_epi(id_col, nome_epi_col, nome_fun_col, func_col) VALUES (?, ?, ?, ?)'

        cur.execute(sql, (idcol, nome_col, nome_f, m))
        con.commit()
        con.close()


        canvas.create_text(
            357.0, 350.5,
            text="OK",
            fill="#000000",
            font=("None", int(25.0)))


    def btn_oculos():
        GPIO.setwarnings(False)
        rfid = SimpleMFRC522()

        id, text = rfid.read()
        idocu = str(id)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sqlocu = ('SELECT nome_ocu FROM Oculos_EPI WHERE id_ocu_EPI =' + idocu)
        cur.execute(sqlocu)
        nomeocu = cur.fetchall()
        for nome_oculos in nomeocu:
            nome_ocu = str(nome_oculos[0])
        con.commit()
        con.close()

        print(nome_ocu)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()

        sql = 'INSERT INTO saida_ocu_epi(id_ocu, nome_epi_ocu, nome_fun_ocu, func_ocu) VALUES (?, ?, ?, ?)'

        cur.execute(sql, (idocu, nome_ocu, nome_f, m))
        con.commit()
        con.close()

        print("entrou")

        canvas.create_text(
            577.0, 350.5,
            text="OK",
            fill="#000000",
            font=("None", int(25.0)))


    def btn_luva():
        GPIO.setwarnings(False)
        rfid = SimpleMFRC522()

        id, text = rfid.read()
        idluv = str(id)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sqlluv = ('SELECT nome_luva FROM Luva_EPI WHERE id_luva_EPI =' + idluv)
        cur.execute(sqlluv)
        nomeluva = cur.fetchall()
        for nome_luvas in nomeluva:
            nome_luva = str(nome_luvas[0])
        con.commit()
        con.close()

        print(nome_luva)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()

        sql = 'INSERT INTO saida_luva_epi(id_luva, nome_epi_luva, nome_fun_luva, func_luva) VALUES (?, ?, ?, ?)'

        cur.execute(sql, (idluv, nome_luva, nome_f, m))
        con.commit()
        con.close()


        canvas.create_text(
            797.0, 350.5,
            text="OK",
            fill="#000000",
            font=("None", int(25.0)))


    janela_eng = tkinter.Toplevel()

    janela_eng.geometry("950x534")
    janela_eng.configure(bg = "#ffffff")
    canvas = Canvas(
        janela_eng,
        bg = "#ffffff",
        height = 534,
        width = 950,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_eng = PhotoImage(file = f"Imagens/check-out/eng/background.png")
    background = canvas.create_image(
        475.0, 267.0,
        image=background_eng)

    img0 = PhotoImage(file = f"Imagens/check-out/eng/img0.png")
    b0 = Button(janela_eng,
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_capacete,
        relief = "flat")

    b0.place(
        x = 51, y = 112,
        width = 198,
        height = 220)

    img1 = PhotoImage( file = f"Imagens/check-out/eng/img1.png")
    b1 = Button(janela_eng,
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_finalizar,
        relief = "flat")

    b1.place(
        x = 673, y = 442,
        width = 224,
        height = 79)

    img2 = PhotoImage( file = f"Imagens/check-out/eng/img2.png")
    b2 = Button(janela_eng,
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_colete,
        relief = "flat")

    b2.place(
        x = 267, y = 112,
        width = 198,
        height = 220)

    img3 = PhotoImage( file = f"Imagens/check-out/eng/img3.png")
    b3 = Button(janela_eng,
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_oculos,
        relief = "flat")

    b3.place(
        x = 483, y = 112,
        width = 198,
        height = 220)

    img4 = PhotoImage( file = f"Imagens/check-out/eng/img4.png")
    b4 = Button(janela_eng,
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_luva,
        relief = "flat")

    b4.place(
        x = 699, y = 112,
        width = 198,
        height = 220)

    janela_eng.resizable(False, False)
    janela_eng.title("Engenheiro")
    janela_eng.mainloop()


def Janela_ele():

    def btn_capacete():
        GPIO.setwarnings(False)
        rfid = SimpleMFRC522()

        id, text = rfid.read()
        idcap = str(id)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sqlcap = ('SELECT nome_cap FROM Capacete_EPI WHERE id_cap_EPI =' + idcap)
        cur.execute(sqlcap)
        nomecap = cur.fetchall()
        for nome_capacete in nomecap:
            nome_cap = str(nome_capacete[0])
        con.commit()
        con.close()

        print(nome_cap)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()

        sql = 'INSERT INTO saida_cap_epi(id_cap, nome_epi_cap, nome_fun_cap, func_cap) VALUES (?, ?, ?, ?)'

        cur.execute(sql, (idcap, nome_cap, nome_f, m))
        con.commit()
        con.close()


        canvas.create_text(
            157.0, 350.5,
            text="OK",
            fill="#000000",
            font=("None", int(25.0)))


    def btn_finalizar():
        Janela_ele.destroy()


    def btn_colete():
        GPIO.setwarnings(False)
        rfid = SimpleMFRC522()

        id, text = rfid.read()
        idcol = str(id)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sqlcol = ('SELECT nome_col FROM Colete_EPI WHERE id_col_EPI =' + idcol)
        cur.execute(sqlcol)
        nomecol = cur.fetchall()
        for nome_colete in nomecol:
            nome_col = str(nome_colete[0])
        con.commit()
        con.close()

        print(nome_col)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()

        sql = 'INSERT INTO saida_col_epi(id_col, nome_epi_col, nome_fun_col, func_col) VALUES (?, ?, ?, ?)'

        cur.execute(sql, (idcol, nome_col, nome_f, m))
        con.commit()
        con.close()


        canvas.create_text(
            357.0, 320.5,
            text="OK",
            fill="#000000",
            font=("None", int(25.0)))


    def btn_oculos():
        GPIO.setwarnings(False)
        rfid = SimpleMFRC522()

        id, text = rfid.read()
        idocu = str(id)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sqlocu = ('SELECT nome_ocu FROM Oculos_EPI WHERE id_ocu_EPI =' + idocu)
        cur.execute(sqlocu)
        nomeocu = cur.fetchall()
        for nome_oculos in nomeocu:
            nome_ocu = str(nome_oculos[0])
        con.commit()
        con.close()

        print(nome_ocu)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()

        sql = 'INSERT INTO saida_ocu_epi(id_ocu, nome_epi_ocu, nome_fun_ocu, func_ocu) VALUES (?, ?, ?, ?)'

        cur.execute(sql, (idocu, nome_ocu, nome_f, m))
        con.commit()
        con.close()


        canvas.create_text(
            587.0, 320.5,
            text="OK",
            fill="#000000",
            font=("None", int(25.0)))


    def btn_cinturao():
        GPIO.setwarnings(False)
        rfid = SimpleMFRC522()

        id, text = rfid.read()
        idcin = str(id)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sqlcin = ('SELECT nome_cin FROM Cinturao_EPI WHERE id_cin_EPI =' + idcin)
        cur.execute(sqlcin)
        nomecin = cur.fetchall()
        for nome_cint in nomecin:
            nome_cin = str(nome_cint[0])
        con.commit()
        con.close()


        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sql = 'INSERT INTO saida_cin_epi(id_cin, nome_epi_cin, nome_fun_cin, func_cin) VALUES (?, ?, ?, ?)'
        cur.execute(sql, (idcin, nome_cin, nome_f, m))
        con.commit()
        con.close()


        canvas.create_text(
            307.0, 450.5,
            text="OK",
            fill="#000000",
            font=("None", int(25.0)))


    def btn_luva():
        GPIO.setwarnings(False)
        rfid = SimpleMFRC522()

        id, text = rfid.read()
        idluv = str(id)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sqlluv = ('SELECT nome_luva FROM Luva_EPI WHERE id_luva_EPI =' + idluv)
        cur.execute(sqlluv)
        nomeluva = cur.fetchall()
        for nome_luvas in nomeluva:
            nome_luva = str(nome_luvas[0])
        con.commit()
        con.close()

        print(nome_luva)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()

        sql = 'INSERT INTO saida_luva_epi(id_luva, nome_epi_luva, nome_fun_luva, func_luva) VALUES (?, ?, ?, ?)'

        cur.execute(sql, (idluv, nome_luva, nome_f, m))
        con.commit()
        con.close()


        canvas.create_text(
            787.0, 320.5,
            text="OK",
            fill="#000000",
            font=("None", int(25.0)))



    Janela_ele = tkinter.Toplevel()

    Janela_ele.geometry("950x534")
    Janela_ele.configure(bg = "#ffffff")
    canvas = Canvas(
        Janela_ele,
        bg = "#ffffff",
        height = 534,
        width = 950,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Imagens/check-out/ele/background.png")
    background = canvas.create_image(
        475.0, 267.0,
        image=background_img)

    img0 = PhotoImage(file = f"Imagens/check-out/ele/img0.png")
    b0 = Button(Janela_ele,
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_capacete,
        relief = "flat")

    b0.place(
        x = 70, y = 112,
        width = 198,
        height = 191)

    img1 = PhotoImage(file = f"Imagens/check-out/ele/img1.png")
    b1 = Button(Janela_ele,
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_colete,
        relief = "flat")

    b1.place(
        x = 277, y = 112,
        width = 198,
        height = 191)

    img2 = PhotoImage(file = f"Imagens/check-out/ele/img2.png")
    b2 = Button(Janela_ele,
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_oculos,
        relief = "flat")

    b2.place(
        x = 484, y = 112,
        width = 198,
        height = 191)

    img3 = PhotoImage(file = f"Imagens/check-out/ele/img3.png")
    b3 = Button(Janela_ele,
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_luva,
        relief = "flat")

    b3.place(
        x = 690, y = 112,
        width = 198,
        height = 191)

    img4 = PhotoImage(file = f"Imagens/check-out/ele/img4.png")
    b4 = Button(Janela_ele,
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_cinturao,
        relief = "flat")

    b4.place(
        x = 70, y = 339,
        width = 198,
        height = 191)

    img5 = PhotoImage(file = f"Imagens/check-out/ele/img5.png")
    b5 = Button(Janela_ele,
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_finalizar,
        relief = "flat")

    b5.place(
        x = 673, y = 442,
        width = 224,
        height = 79)

    Janela_ele.resizable(False, False)
    Janela_ele.title("Eletricista")
    Janela_ele.mainloop()


def Janela_ped():

    def btn_capacete():
        GPIO.setwarnings(False)
        rfid = SimpleMFRC522()

        id, text = rfid.read()
        idcap = str(id)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sqlcap = ('SELECT nome_cap FROM Capacete_EPI WHERE id_cap_EPI =' + idcap)
        cur.execute(sqlcap)
        nomecap = cur.fetchall()
        for nome_capacete in nomecap:
            nome_cap = str(nome_capacete[0])
        con.commit()
        con.close()

        print(nome_cap)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()

        sql = 'INSERT INTO saida_cap_epi(id_cap, nome_epi_cap, nome_fun_cap, func_cap) VALUES (?, ?, ?, ?)'

        cur.execute(sql, (idcap, nome_cap, nome_f, m))
        con.commit()
        con.close()


        canvas.create_text(
            157.0, 350.5,
            text="OK",
            fill="#000000",
            font=("None", int(25.0)))


    def btn_finalizar():
        janela_ped.destroy()


    def btn_colete():
        GPIO.setwarnings(False)
        rfid = SimpleMFRC522()

        id, text = rfid.read()
        idcol = str(id)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sqlcol = ('SELECT nome_col FROM Colete_EPI WHERE id_col_EPI =' + idcol)
        cur.execute(sqlcol)
        nomecol = cur.fetchall()
        for nome_colete in nomecol:
            nome_col = str(nome_colete[0])
        con.commit()
        con.close()

        print(nome_col)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()

        sql = 'INSERT INTO saida_col_epi(id_col, nome_epi_col, nome_fun_col, func_col) VALUES (?, ?, ?, ?)'

        cur.execute(sql, (idcol, nome_col, nome_f, m))
        con.commit()
        con.close()


        canvas.create_text(
            357.0, 350.5,
            text="OK",
            fill="#000000",
            font=("None", int(25.0)))


    def btn_oculos():
        GPIO.setwarnings(False)
        rfid = SimpleMFRC522()

        id, text = rfid.read()
        idocu = str(id)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sqlocu = ('SELECT nome_ocu FROM Oculos_EPI WHERE id_ocu_EPI =' + idocu)
        cur.execute(sqlocu)
        nomeocu = cur.fetchall()
        for nome_oculos in nomeocu:
            nome_ocu = str(nome_oculos[0])
        con.commit()
        con.close()

        print(nome_ocu)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()

        sql = 'INSERT INTO saida_ocu_epi(id_ocu, nome_epi_ocu, nome_fun_ocu, func_ocu) VALUES (?, ?, ?, ?)'

        cur.execute(sql, (idocu, nome_ocu, nome_f, m))
        con.commit()
        con.close()


        canvas.create_text(
            577.0, 350.5,
            text="OK",
            fill="#000000",
            font=("None", int(25.0)))


    def btn_luva():
        GPIO.setwarnings(False)
        rfid = SimpleMFRC522()

        id, text = rfid.read()
        idluv = str(id)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sqlluv = ('SELECT nome_luva FROM Luva_EPI WHERE id_luva_EPI =' + idluv)
        cur.execute(sqlluv)
        nomeluva = cur.fetchall()
        for nome_luvas in nomeluva:
            nome_luva = str(nome_luvas[0])
        con.commit()
        con.close()

        print(nome_luva)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()

        sql = 'INSERT INTO saida_luva_epi(id_luva, nome_epi_luva, nome_fun_luva, func_luva) VALUES (?, ?, ?, ?)'

        cur.execute(sql, (idluv, nome_luva, nome_f, m))
        con.commit()
        con.close()


        canvas.create_text(
            797.0, 350.5,
            text="OK",
            fill="#000000",
            font=("None", int(25.0)))


    janela_ped = tkinter.Toplevel()

    janela_ped.geometry("950x534")
    janela_ped.configure(bg = "#ffffff")
    canvas = Canvas(
        janela_ped,
        bg = "#ffffff",
        height = 534,
        width = 950,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage( file = f"Imagens/check-out/ped/background.png")
    background = canvas.create_image(
        475.0, 267.0,
        image=background_img)

    img0 = PhotoImage(file = f"Imagens/check-out/ped/img0.png")
    b0 = Button(janela_ped,
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_capacete,
        relief = "flat")

    b0.place(
        x = 51, y = 112,
        width = 198,
        height = 220)

    img1 = PhotoImage( file = f"Imagens/check-out/ped/img1.png")
    b1 = Button(janela_ped,
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_finalizar,
        relief = "flat")

    b1.place(
        x = 673, y = 442,
        width = 224,
        height = 79)

    img2 = PhotoImage( file = f"Imagens/check-out/ped/img2.png")
    b2 = Button(janela_ped,
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_colete,
        relief = "flat")

    b2.place(
        x = 267, y = 112,
        width = 198,
        height = 220)

    img3 = PhotoImage( file = f"Imagens/check-out/ped/img3.png")
    b3 = Button(janela_ped,
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_oculos,
        relief = "flat")

    b3.place(
        x = 483, y = 112,
        width = 198,
        height = 220)

    img4 = PhotoImage( file = f"Imagens/check-out/ped/img4.png")
    b4 = Button(janela_ped,
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_luva,
        relief = "flat")

    b4.place(
        x = 699, y = 112,
        width = 198,
        height = 220)

    janela_ped.resizable(False, False)
    janela_ped.title("Pedreiro")
    janela_ped.mainloop()


def Janela_pin():
    def btn_capacete():
        GPIO.setwarnings(False)
        rfid = SimpleMFRC522()

        id, text = rfid.read()
        idcap = str(id)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sqlcap = ('SELECT nome_cap FROM Capacete_EPI WHERE id_cap_EPI =' + idcap)
        cur.execute(sqlcap)
        nomecap = cur.fetchall()
        for nome_capacete in nomecap:
            nome_cap = str(nome_capacete[0])
        con.commit()
        con.close()

        print(nome_cap)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()

        sql = 'INSERT INTO saida_cap_epi(id_cap, nome_epi_cap, nome_fun_cap, func_cap) VALUES (?, ?, ?, ?)'

        cur.execute(sql, (idcap, nome_cap, nome_f, m))
        con.commit()
        con.close()


        canvas.create_text(
            157.0, 320.5,
            text="OK",
            fill="#000000",
            font=("None", int(25.0)))


    def btn_finalizar():
        Janela_pin.destroy()


    def btn_colete():
        GPIO.setwarnings(False)
        rfid = SimpleMFRC522()

        id, text = rfid.read()
        idcol = str(id)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sqlcol = ('SELECT nome_col FROM Colete_EPI WHERE id_col_EPI =' + idcol)
        cur.execute(sqlcol)
        nomecol = cur.fetchall()
        for nome_colete in nomecol:
            nome_col = str(nome_colete[0])
        con.commit()
        con.close()

        print(nome_col)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()

        sql = 'INSERT INTO saida_col_epi(id_col, nome_epi_col, nome_fun_col, func_col) VALUES (?, ?, ?, ?)'

        cur.execute(sql, (idcol, nome_col, nome_f, m))
        con.commit()
        con.close()


        canvas.create_text(
            357.0, 320.5,
            text="OK",
            fill="#000000",
            font=("None", int(25.0)))


    def btn_oculos():
        GPIO.setwarnings(False)
        rfid = SimpleMFRC522()

        id, text = rfid.read()
        idocu = str(id)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sqlocu = ('SELECT nome_ocu FROM Oculos_EPI WHERE id_ocu_EPI =' + idocu)
        cur.execute(sqlocu)
        nomeocu = cur.fetchall()
        for nome_oculos in nomeocu:
            nome_ocu = str(nome_oculos[0])
        con.commit()
        con.close()

        print(nome_ocu)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()

        sql = 'INSERT INTO saida_ocu_epi(id_ocu, nome_epi_ocu, nome_fun_ocu, func_ocu) VALUES (?, ?, ?, ?)'

        cur.execute(sql, (idocu, nome_ocu, nome_f, m))
        con.commit()
        con.close()


        canvas.create_text(
            587.0, 320.5,
            text="OK",
            fill="#000000",
            font=("None", int(25.0)))


    def btn_mascara():
        GPIO.setwarnings(False)
        rfid = SimpleMFRC522()

        id, text = rfid.read()
        idmasc = str(id)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sqlmasc = ('SELECT nome_masc FROM Mascara_EPI WHERE id_masc_EPI =' + idmasc)
        cur.execute(sqlmasc)
        nomemasc = cur.fetchall()
        for nome_mascara in nomemasc:
            nome_masc = str(nome_mascara[0])
        con.commit()
        con.close()


        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sql = 'INSERT INTO saida_masc_epi(id_masc, nome_epi_masc, nome_fun_masc, func_masc) VALUES (?, ?, ?, ?)'
        cur.execute(sql, (idmasc, nome_masc, nome_f, m))
        con.commit()
        con.close()

        canvas.create_text(
            307.0, 450.5,
            text="OK",
            fill="#000000",
            font=("None", int(25.0)))

    def btn_luva():
        GPIO.setwarnings(False)
        rfid = SimpleMFRC522()

        id, text = rfid.read()
        idluv = str(id)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()
        sqlluv = ('SELECT nome_luva FROM Luva_EPI WHERE id_luva_EPI =' + idluv)
        cur.execute(sqlluv)
        nomeluva = cur.fetchall()
        for nome_luvas in nomeluva:
            nome_luva = str(nome_luvas[0])
        con.commit()
        con.close()

        print(nome_luva)

        con = sqlite3.connect('banco.sqlite')
        cur = con.cursor()

        sql = 'INSERT INTO saida_luva_epi(id_luva, nome_epi_luva, nome_fun_luva, func_luva) VALUES (?, ?, ?, ?)'

        cur.execute(sql, (idluv, nome_luva, nome_f, m))
        con.commit()
        con.close()


        canvas.create_text(
            787.0, 320.5,
            text="OK",
            fill="#000000",
            font=("None", int(25.0)))



    Janela_pin = tkinter.Toplevel()

    Janela_pin.geometry("950x534")
    Janela_pin.configure(bg = "#ffffff")
    canvas = Canvas(
        Janela_pin,
        bg = "#ffffff",
        height = 534,
        width = 950,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Imagens/check-out/pin/background.png")
    background = canvas.create_image(
        475.0, 267.0,
        image=background_img)

    img0 = PhotoImage(file = f"Imagens/check-out/pin/img0.png")
    b0 = Button(Janela_pin,
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_capacete,
        relief = "flat")

    b0.place(
        x = 70, y = 112,
        width = 198,
        height = 191)

    img1 = PhotoImage(file = f"Imagens/check-out/pin/img1.png")
    b1 = Button(Janela_pin,
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_colete,
        relief = "flat")

    b1.place(
        x = 277, y = 112,
        width = 198,
        height = 191)

    img2 = PhotoImage(file = f"Imagens/check-out/pin/img2.png")
    b2 = Button(Janela_pin,
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_oculos,
        relief = "flat")

    b2.place(
        x = 484, y = 112,
        width = 198,
        height = 191)

    img3 = PhotoImage(file = f"Imagens/check-out/pin/img3.png")
    b3 = Button(Janela_pin,
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_luva,
        relief = "flat")

    b3.place(
        x = 690, y = 112,
        width = 198,
        height = 191)

    img4 = PhotoImage(file = f"Imagens/check-out/pin/img4.png")
    b4 = Button(Janela_pin,
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_mascara,
        relief = "flat")

    b4.place(
        x = 70, y = 339,
        width = 198,
        height = 191)

    img5 = PhotoImage(file = f"Imagens/check-out/pin/img5.png")
    b5 = Button(Janela_pin,
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_finalizar,
        relief = "flat")

    b5.place(
        x = 673, y = 442,
        width = 224,
        height = 79)

    Janela_pin.resizable(False, False)
    Janela_pin.title("Pintor")
    Janela_pin.mainloop()



def check():
    GPIO.setwarnings(False)
    rfid = SimpleMFRC522()

    id, text = rfid.read()
    id_fun = str(id)
    global nome_f


    con = sqlite3.connect('banco.sqlite')
    cur = con.cursor()
    sqlid = ('SELECT nome FROM funcionario WHERE id_funcionario =' + id_fun)
    cur.execute(sqlid)
    nomefuncionario = cur.fetchall()
    for nome_fun in nomefuncionario:
        nome_f = str(nome_fun[0])
    con.commit()
    con.close()

    global m

    con = sqlite3.connect('banco.sqlite')
    cur = con.cursor()
    sqlnome = (f'SELECT funcao FROM funcionario WHERE id_funcionario = {id_fun}')
    cur.execute(sqlnome)
    funcionario = cur.fetchall()
    for entradas in funcionario:
        m = entradas[0]
    con.commit()
    con.close()


    con = sqlite3.connect('banco.sqlite')
    cur = con.cursor()
    sql = 'INSERT INTO saida_fun(id_fun, nome_fun, func_fun) VALUES (?,?,?)'
    cur.execute(sql, (id_fun, nome_f, m))
    con.commit()
    con.close()


    while m:
        if (m == "engenheiro"):
            Janela_eng()
            break
        if (m == "pedreiro"):
            Janela_ped()
            break
        if (m == "pintor"):
            Janela_pin()
            break
        if (m == "eletricista"):
            Janela_ele()
            break


def btn_entrada():
    check()



window = Tk()

window.geometry("950x534")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 534,
    width = 950,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Imagens/check-out/checkout/background.png")
background = canvas.create_image(
    475.0, 267.0,
    image=background_img)

img0 = PhotoImage(file = f"Imagens/check-out/checkout/img.ck.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_entrada,
    relief = "flat")

b0.place(
    x = 134, y = 64,
    width = 681,
    height = 406)

window.resizable(False, False)
window.title("Check-out")
window.mainloop()
