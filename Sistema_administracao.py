from tkinter import *
from tkinter import *
import tkinter
import sqlite3
from datetime import date
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


def menu():
    def btn_menu_CRUD():
        def btn_cad_fun():
            def btn_cad_fun():
                GPIO.setwarnings(False)
                rfid = SimpleMFRC522()

                id, text = rfid.read()
                rfid.write(entry0.get())
                con = sqlite3.connect('banco.sqlite')
                cur = con.cursor()
                sql = 'INSERT INTO funcionario(id_funcionario, nome, CPF, Funcao) VALUES (?, ?, ?, ?)'
                cur.execute(sql, (id, entry0.get(), entry1.get(), entry2.get()))
                con.commit()
                con.close()


                canvas.create_text(
                    327.0, 380.5,
                    text="Usuario cadastrado",
                    fill="#000000",
                    font=("None", int(16.0)))


            ca_fun = tkinter.Toplevel()

            ca_fun.geometry("950x534")
            ca_fun.configure(bg="#ffffff")
            canvas = Canvas(
                ca_fun,
                bg="#ffffff",
                height=534,
                width=950,
                bd=0,
                highlightthickness=0,
                relief="ridge")
            canvas.place(x=0, y=0)

            background_img = PhotoImage(file=f"Imagens/cad_fun/background.png")
            background = canvas.create_image(
                475.0, 267.0,
                image=background_img)

            img0 = PhotoImage(file=f"Imagens/cad_fun/img0.png")
            b0 = Button(ca_fun,
                        image=img0,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_cad_fun,
                        relief="flat")

            b0.place(
                x=322, y=436,
                width=306,
                height=71)

            entry0_img = PhotoImage(file=f"Imagens/cad_fun/img_textBox0.png")
            entry0_bg = canvas.create_image(
                307.0, 188.0,
                image=entry0_img)

            entry0 = Entry(ca_fun,
                           bd=0,
                           bg="#c4c4c4",
                           highlightthickness=0)

            entry0.place(
                x=117, y=169,
                width=380,
                height=36)

            entry1_img = PhotoImage(file=f"Imagens/cad_fun/img_textBox1.png")
            entry1_bg = canvas.create_image(
                307.0, 267.0,
                image=entry1_img)

            entry1 = Entry(ca_fun,
                           bd=0,
                           bg="#c4c4c4",
                           highlightthickness=0)

            entry1.place(
                x=117, y=248,
                width=380,
                height=36)

            entry2_img = PhotoImage(file=f"Imagens/cad_fun/img_textBox2.png")
            entry2_bg = canvas.create_image(
                307.0, 346.0,
                image=entry2_img)

            entry2 = Entry(ca_fun,
                           bd=0,
                           bg="#c4c4c4",
                           highlightthickness=0)

            entry2.place(
                x=117, y=327,
                width=380,
                height=36)

            ca_fun.resizable(False, False)
            ca_fun.title("Cadastro funcionario")
            ca_fun.mainloop()

            print("cadastro funcionario")

        def btn_cad_epi():
            def btn_capacete():
                def btn_cadastro():
                    GPIO.setwarnings(False)
                    rfid = SimpleMFRC522()

                    id, text = rfid.read()
                    rfid.write(entry_equ.get())
                    con = sqlite3.connect('banco.sqlite')
                    cur = con.cursor()
                    sql = 'INSERT INTO Capacete_EPI(id_cap_EPI, CA_cap, nome_cap,fabricante_cap, protecao_cap, funcao_cap, validade_cap ) VALUES (?, ?, ?, ?, ?, ?, ?)'
                    cur.execute(sql, (
                        id, entry_CA.get(), entry_equ.get(), entry_fab.get(), entry_tip.get(), entry_set.get(),
                        entry_val.get()))
                    con.commit()
                    con.close()


                    canvas.create_text(
                        467.0, 470.5,
                        text="EPI cadastrada",
                        fill="#000000",
                        font=("None", int(18.0)))


                cad_epi = tkinter.Toplevel()

                cad_epi.geometry("950x534")
                cad_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    cad_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/cad_epi2/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/cad_epi2/img0.png")
                b0 = Button(cad_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_cadastro,
                            relief="flat")

                b0.place(
                    x=368, y=479,
                    width=214,
                    height=55)

                entry0_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 248.0,
                    image=entry0_img)

                entry_CA = Entry(cad_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_CA.place(
                    x=33, y=229,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    223.0, 352.0,
                    image=entry1_img)

                entry_fab = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_fab.place(
                    x=33, y=333,
                    width=380,
                    height=36)

                entry2_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox2.png")
                entry2_bg = canvas.create_image(
                    223.0, 433.0,
                    image=entry2_img)

                entry_set = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_set.place(
                    x=33, y=414,
                    width=380,
                    height=36)

                entry3_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox3.png")
                entry3_bg = canvas.create_image(
                    721.0, 248.0,
                    image=entry3_img)

                entry_equ = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_equ.place(
                    x=531, y=229,
                    width=380,
                    height=36)

                entry4_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox4.png")
                entry4_bg = canvas.create_image(
                    726.0, 352.0,
                    image=entry4_img)

                entry_tip = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_tip.place(
                    x=536, y=333,
                    width=380,
                    height=36)

                entry5_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox5.png")
                entry5_bg = canvas.create_image(
                    726.0, 441.0,
                    image=entry5_img)

                entry_val = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_val.place(
                    x=536, y=422,
                    width=380,
                    height=36)

                cad_epi.resizable(False, False)
                cad_epi.title("Capacete")
                cad_epi.mainloop()

            def btn_colete():
                def btn_cadastro():
                    GPIO.setwarnings(False)
                    rfid = SimpleMFRC552()


                    id, text = rfid.read()
                    rfid.write(entry_equ.get())
                    con = sqlite3.connect('banco.sqlite')
                    cur = con.cursor()
                    sql = 'INSERT INTO Colete_EPI(id_col_EPI, CA_col, nome_col,fabricante_col, protecao_col, funcao_col, validade_col ) VALUES (?, ?, ?, ?, ?, ?, ?)'
                    cur.execute(sql, (
                        id, entry_CA.get(), entry_equ.get(), entry_fab.get(), entry_tip.get(), entry_set.get(),
                        entry_val.get()))
                    con.commit()
                    con.close()

                    canvas.create_text(
                        467.0, 470.5,
                        text="EPI cadastrada",
                        fill="#000000",
                        font=("None", int(18.0)))


                cad_epi = tkinter.Toplevel()

                cad_epi.geometry("950x534")
                cad_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    cad_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/cad_epi2/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/cad_epi2/img0.png")
                b0 = Button(cad_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_cadastro,
                            relief="flat")

                b0.place(
                    x=368, y=479,
                    width=214,
                    height=55)

                entry0_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 248.0,
                    image=entry0_img)

                entry_CA = Entry(cad_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_CA.place(
                    x=33, y=229,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    223.0, 352.0,
                    image=entry1_img)

                entry_fab = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_fab.place(
                    x=33, y=333,
                    width=380,
                    height=36)

                entry2_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox2.png")
                entry2_bg = canvas.create_image(
                    223.0, 433.0,
                    image=entry2_img)

                entry_set = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_set.place(
                    x=33, y=414,
                    width=380,
                    height=36)

                entry3_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox3.png")
                entry3_bg = canvas.create_image(
                    721.0, 248.0,
                    image=entry3_img)

                entry_equ = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_equ.place(
                    x=531, y=229,
                    width=380,
                    height=36)

                entry4_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox4.png")
                entry4_bg = canvas.create_image(
                    726.0, 352.0,
                    image=entry4_img)

                entry_tip = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_tip.place(
                    x=536, y=333,
                    width=380,
                    height=36)

                entry5_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox5.png")
                entry5_bg = canvas.create_image(
                    726.0, 441.0,
                    image=entry5_img)

                entry_val = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_val.place(
                    x=536, y=422,
                    width=380,
                    height=36)

                cad_epi.resizable(False, False)
                cad_epi.title("Colete")
                cad_epi.mainloop()

            def btn_oculos():
                def btn_cadastro():
                    GPIO.setwarnings(False)
                    rfid = SimpleMFRC552()

                    id, text = rfid.read()
                    rfid.write(entry_equ.get())
                    con = sqlite3.connect('banco.sqlite')
                    cur = con.cursor()
                    sql = 'INSERT INTO Oculos_EPI(id_ocu_EPI, CA_ocu, nome_ocu,fabricante_ocu, protecao_ocu, funcao_ocu, validade_ocu ) VALUES (?, ?, ?, ?, ?, ?, ?)'
                    cur.execute(sql, (
                        id, entry_CA.get(), entry_equ.get(), entry_fab.get(), entry_tip.get(), entry_set.get(),
                        entry_val.get()))
                    con.commit()
                    con.close()

                    canvas.create_text(
                        467.0, 470.5,
                        text="EPI cadastrada",
                        fill="#000000",
                        font=("None", int(18.0)))


                cad_epi = tkinter.Toplevel()

                cad_epi.geometry("950x534")
                cad_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    cad_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/cad_epi2/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/cad_epi2/img0.png")
                b0 = Button(cad_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_cadastro,
                            relief="flat")

                b0.place(
                    x=368, y=479,
                    width=214,
                    height=55)

                entry0_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 248.0,
                    image=entry0_img)

                entry_CA = Entry(cad_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_CA.place(
                    x=33, y=229,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    223.0, 352.0,
                    image=entry1_img)

                entry_fab = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_fab.place(
                    x=33, y=333,
                    width=380,
                    height=36)

                entry2_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox2.png")
                entry2_bg = canvas.create_image(
                    223.0, 433.0,
                    image=entry2_img)

                entry_set = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_set.place(
                    x=33, y=414,
                    width=380,
                    height=36)

                entry3_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox3.png")
                entry3_bg = canvas.create_image(
                    721.0, 248.0,
                    image=entry3_img)

                entry_equ = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_equ.place(
                    x=531, y=229,
                    width=380,
                    height=36)

                entry4_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox4.png")
                entry4_bg = canvas.create_image(
                    726.0, 352.0,
                    image=entry4_img)

                entry_tip = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_tip.place(
                    x=536, y=333,
                    width=380,
                    height=36)

                entry5_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox5.png")
                entry5_bg = canvas.create_image(
                    726.0, 441.0,
                    image=entry5_img)

                entry_val = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_val.place(
                    x=536, y=422,
                    width=380,
                    height=36)

                cad_epi.resizable(False, False)
                cad_epi.title("Oculos")
                cad_epi.mainloop()

            def btn_luva():
                def btn_cadastro():
                    GPIO.setwarnings(False)
                    rfid = SimpleMFRC552()

                    id = rfid.read()
                    rfid.write(entry_equ.get())
                    con = sqlite3.connect('banco.sqlite')
                    cur = con.cursor()
                    sql = 'INSERT INTO Luva_EPI(id_luva_EPI, CA_luva, nome_luva,fabricante_luva, protecao_luva, funcao_luva, validade_luva) VALUES (?, ?, ?, ?, ?, ?, ?)'
                    cur.execute(sql, (
                        id, entry_CA.get(), entry_equ.get(), entry_fab.get(), entry_tip.get(), entry_set.get(),
                        entry_val.get()))
                    con.commit()
                    con.close()

                    canvas.create_text(
                        467.0, 470.5,
                        text="EPI cadastrada",
                        fill="#000000",
                        font=("None", int(18.0)))


                cad_epi = tkinter.Toplevel()

                cad_epi.geometry("950x534")
                cad_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    cad_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/cad_epi2/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/cad_epi2/img0.png")
                b0 = Button(cad_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_cadastro,
                            relief="flat")

                b0.place(
                    x=368, y=479,
                    width=214,
                    height=55)

                entry0_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 248.0,
                    image=entry0_img)

                entry_CA = Entry(cad_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_CA.place(
                    x=33, y=229,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    223.0, 352.0,
                    image=entry1_img)

                entry_fab = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_fab.place(
                    x=33, y=333,
                    width=380,
                    height=36)

                entry2_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox2.png")
                entry2_bg = canvas.create_image(
                    223.0, 433.0,
                    image=entry2_img)

                entry_set = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_set.place(
                    x=33, y=414,
                    width=380,
                    height=36)

                entry3_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox3.png")
                entry3_bg = canvas.create_image(
                    721.0, 248.0,
                    image=entry3_img)

                entry_equ = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_equ.place(
                    x=531, y=229,
                    width=380,
                    height=36)

                entry4_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox4.png")
                entry4_bg = canvas.create_image(
                    726.0, 352.0,
                    image=entry4_img)

                entry_tip = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_tip.place(
                    x=536, y=333,
                    width=380,
                    height=36)

                entry5_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox5.png")
                entry5_bg = canvas.create_image(
                    726.0, 441.0,
                    image=entry5_img)

                entry_val = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_val.place(
                    x=536, y=422,
                    width=380,
                    height=36)

                cad_epi.resizable(False, False)
                cad_epi.title("Luva")
                cad_epi.mainloop()

            def btn_cinturao():
                def btn_cadastro():
                    GPIO.setwarnings(False)
                    rfid = SimpleMFRC552()

                    id, text = rfid.read()
                    rfid.write(entry_equ.get())
                    con = sqlite3.connect('banco.sqlite')
                    cur = con.cursor()
                    sql = 'INSERT INTO Cinturao_EPI(id_cin_EPI, CA_cin, nome_cin,fabricante_cin, protecao_cin, funcao_cin, validade_cin ) VALUES (?, ?, ?, ?, ?, ?, ?)'
                    cur.execute(sql, (
                        id, entry_CA.get(), entry_equ.get(), entry_fab.get(), entry_tip.get(), entry_set.get(),
                        entry_val.get()))
                    con.commit()
                    con.close()

                    canvas.create_text(
                        467.0, 470.5,
                        text="EPI cadastrada",
                        fill="#000000",
                        font=("None", int(18.0)))

                cad_epi = tkinter.Toplevel()

                cad_epi.geometry("950x534")
                cad_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    cad_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/cad_epi2/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/cad_epi2/img0.png")
                b0 = Button(cad_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_cadastro,
                            relief="flat")

                b0.place(
                    x=368, y=479,
                    width=214,
                    height=55)

                entry0_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 248.0,
                    image=entry0_img)

                entry_CA = Entry(cad_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_CA.place(
                    x=33, y=229,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    223.0, 352.0,
                    image=entry1_img)

                entry_fab = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_fab.place(
                    x=33, y=333,
                    width=380,
                    height=36)

                entry2_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox2.png")
                entry2_bg = canvas.create_image(
                    223.0, 433.0,
                    image=entry2_img)

                entry_set = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_set.place(
                    x=33, y=414,
                    width=380,
                    height=36)

                entry3_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox3.png")
                entry3_bg = canvas.create_image(
                    721.0, 248.0,
                    image=entry3_img)

                entry_equ = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_equ.place(
                    x=531, y=229,
                    width=380,
                    height=36)

                entry4_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox4.png")
                entry4_bg = canvas.create_image(
                    726.0, 352.0,
                    image=entry4_img)

                entry_tip = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_tip.place(
                    x=536, y=333,
                    width=380,
                    height=36)

                entry5_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox5.png")
                entry5_bg = canvas.create_image(
                    726.0, 441.0,
                    image=entry5_img)

                entry_val = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_val.place(
                    x=536, y=422,
                    width=380,
                    height=36)

                cad_epi.resizable(False, False)
                cad_epi.title("Cinturao")
                cad_epi.mainloop()

            def btn_mascara():
                def btn_cadastro():
                    GPIO.setwarnings(False)
                    rfid = SimpleMFRC552()

                    id, text = rfid.read()
                    rfid.write(entry_equ.get())
                    con = sqlite3.connect('banco.sqlite')
                    cur = con.cursor()
                    sql = 'INSERT INTO Mascara_EPI(id_masc_EPI, CA_masc, nome_masc,fabricante_masc, protecao_masc, funcao_masc, validade_masc) VALUES (?, ?, ?, ?, ?, ?, ?)'
                    cur.execute(sql, (
                        id, entry_CA.get(), entry_equ.get(), entry_fab.get(), entry_tip.get(), entry_set.get(),
                        entry_val.get()))
                    con.commit()
                    con.close()

                    canvas.create_text(
                        467.0, 470.5,
                        text="EPI cadastrada",
                        fill="#000000",
                        font=("None", int(18.0)))

                cad_epi = tkinter.Toplevel()

                cad_epi.geometry("950x534")
                cad_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    cad_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/cad_epi2/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/cad_epi2/img0.png")
                b0 = Button(cad_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_cadastro,
                            relief="flat")

                b0.place(
                    x=368, y=479,
                    width=214,
                    height=55)

                entry0_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 248.0,
                    image=entry0_img)

                entry_CA = Entry(cad_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_CA.place(
                    x=33, y=229,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    223.0, 352.0,
                    image=entry1_img)

                entry_fab = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_fab.place(
                    x=33, y=333,
                    width=380,
                    height=36)

                entry2_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox2.png")
                entry2_bg = canvas.create_image(
                    223.0, 433.0,
                    image=entry2_img)

                entry_set = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_set.place(
                    x=33, y=414,
                    width=380,
                    height=36)

                entry3_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox3.png")
                entry3_bg = canvas.create_image(
                    721.0, 248.0,
                    image=entry3_img)

                entry_equ = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_equ.place(
                    x=531, y=229,
                    width=380,
                    height=36)

                entry4_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox4.png")
                entry4_bg = canvas.create_image(
                    726.0, 352.0,
                    image=entry4_img)

                entry_tip = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_tip.place(
                    x=536, y=333,
                    width=380,
                    height=36)

                entry5_img = PhotoImage(file=f"Imagens/cad_epi2/img_textBox5.png")
                entry5_bg = canvas.create_image(
                    726.0, 441.0,
                    image=entry5_img)

                entry_val = Entry(cad_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_val.place(
                    x=536, y=422,
                    width=380,
                    height=36)

                cad_epi.resizable(False, False)
                cad_epi.title("Mascara")
                cad_epi.mainloop()

            Cad_epi = tkinter.Toplevel()

            Cad_epi.geometry("950x534")
            Cad_epi.configure(bg="#ffffff")
            canvas = Canvas(
                Cad_epi,
                bg="#ffffff",
                height=534,
                width=950,
                bd=0,
                highlightthickness=0,
                relief="ridge")
            canvas.place(x=0, y=0)

            background_img = PhotoImage(file=f"Imagens/m_cad_epi/background.png")
            background = canvas.create_image(
                475.0, 267.0,
                image=background_img)

            img0 = PhotoImage(file=f"Imagens/m_cad_epi/img0.png")
            b0 = Button(Cad_epi,
                        image=img0,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_capacete,
                        relief="flat")

            b0.place(
                x=587, y=67,
                width=306,
                height=138)

            img1 = PhotoImage(file=f"Imagens/m_cad_epi/img1.png")
            b1 = Button(Cad_epi,
                        image=img1,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_colete,
                        relief="flat")

            b1.place(
                x=61, y=67,
                width=306,
                height=138)

            img2 = PhotoImage(file=f"Imagens/m_cad_epi/img2.png")
            b2 = Button(Cad_epi,
                        image=img2,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_oculos,
                        relief="flat")

            b2.place(
                x=61, y=215,
                width=306,
                height=138)

            img3 = PhotoImage(file=f"Imagens/m_cad_epi/img3.png")
            b3 = Button(Cad_epi,
                        image=img3,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_luva,
                        relief="flat")

            b3.place(
                x=61, y=363,
                width=306,
                height=138)

            img4 = PhotoImage(file=f"Imagens/m_cad_epi/img4.png")
            b4 = Button(Cad_epi,
                        image=img4,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_cinturao,
                        relief="flat")

            b4.place(
                x=587, y=215,
                width=306,
                height=138)

            img5 = PhotoImage(file=f"Imagens/m_cad_epi/img5.png")
            b5 = Button(Cad_epi,
                        image=img5,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_mascara,
                        relief="flat")

            b5.place(
                x=587, y=363,
                width=306,
                height=138)

            Cad_epi.resizable(False, False)
            Cad_epi.title("Cadastro epi")
            Cad_epi.mainloop()
            print("3")

        def btn_ed_fun():
            def btn_att():
                conn = sqlite3.connect('banco.sqlite')
                cursor = conn.cursor()

                cursor.execute(" UPDATE funcionario SET Funcao = ? WHERE CPF = ? ",
                               (entry_fun.get(), int(entry_cpf.get())))

                conn.commit()

                print('Dados atualizados com sucesso.')

                conn.close()


                canvas.create_text(
                    457.0, 430.5,
                    text="Funcionario atualizado",
                    fill="#000000",
                    font=("None", int(18.0)))

            ed_fun = tkinter.Toplevel()

            ed_fun.geometry("950x534")
            ed_fun.configure(bg="#ffffff")
            canvas = Canvas(
                ed_fun,
                bg="#ffffff",
                height=534,
                width=950,
                bd=0,
                highlightthickness=0,
                relief="ridge")
            canvas.place(x=0, y=0)

            background_img = PhotoImage(file=f"Imagens/ed_fun/background.png")
            background = canvas.create_image(
                475.0, 267.0,
                image=background_img)

            img0 = PhotoImage(file=f"Imagens/ed_fun/img0.png")
            b0 = Button(ed_fun,
                        image=img0,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_att,
                        relief="flat")

            b0.place(
                x=344, y=323,
                width=205,
                height=89)

            entry0_img = PhotoImage(file=f"Imagens/ed_fun/img_textBox0.png")
            entry0_bg = canvas.create_image(
                223.0, 267.0,
                image=entry0_img)

            entry_cpf = Entry(ed_fun,
                              bd=0,
                              bg="#c4c4c4",
                              highlightthickness=0)

            entry_cpf.place(
                x=33, y=248,
                width=380,
                height=36)

            entry1_img = PhotoImage(file=f"Imagens/ed_fun/img_textBox1.png")
            entry1_bg = canvas.create_image(
                707.0, 267.0,
                image=entry1_img)

            entry_fun = Entry(ed_fun,
                              bd=0,
                              bg="#c4c4c4",
                              highlightthickness=0)

            entry_fun.place(
                x=517, y=248,
                width=380,
                height=36)

            ed_fun.resizable(False, False)
            ed_fun.mainloop()

        def btn_ed_epi():
            def btn_capacete():
                def btn_clicked():
                    conn = sqlite3.connect('banco.sqlite')
                    cursor = conn.cursor()

                    cursor.execute(" UPDATE Capacete_EPI SET funcao_cap = ? WHERE id_cap_EPI = ? ",
                                   (entry_fun.get(), int(entry_ID.get())))

                    conn.commit()

                    conn.close()

                    canvas.create_text(
                        457.0, 430.5,
                        text="EPI atualizada",
                        fill="#000000",
                        font=("None", int(18.0)))

                ed_epi = tkinter.Toplevel()

                ed_epi.geometry("950x534")
                ed_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    ed_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/ed_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/ed_epi/img0.png")
                b0 = Button(ed_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_clicked,
                            relief="flat")

                b0.place(
                    x=344, y=323,
                    width=205,
                    height=89)

                entry0_img = PhotoImage(file=f"Imagens/ed_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 267.0,
                    image=entry0_img)

                entry_ID = Entry(ed_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_ID.place(
                    x=33, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/ed_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    707.0, 267.0,
                    image=entry1_img)

                entry_fun = Entry(ed_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_fun.place(
                    x=517, y=248,
                    width=380,
                    height=36)

                ed_epi.resizable(False, False)
                ed_epi.mainloop()

            def btn_colete():
                def btn_clicked():
                    conn = sqlite3.connect('banco.sqlite')
                    cursor = conn.cursor()

                    cursor.execute(" UPDATE Colete_EPI SET funcao_col = ? WHERE id_col_EPI = ? ",
                                   (entry_fun.get(), int(entry_ID.get())))

                    conn.commit()

                    conn.close()
                    canvas.create_text(
                        457.0, 430.5,
                        text="EPI atualizada",
                        fill="#000000",
                        font=("None", int(18.0)))

                ed_epi = tkinter.Toplevel()

                ed_epi.geometry("950x534")
                ed_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    ed_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/ed_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/ed_epi/img0.png")
                b0 = Button(ed_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_clicked,
                            relief="flat")

                b0.place(
                    x=344, y=323,
                    width=205,
                    height=89)

                entry0_img = PhotoImage(file=f"Imagens/ed_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 267.0,
                    image=entry0_img)

                entry_ID = Entry(ed_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_ID.place(
                    x=33, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/ed_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    707.0, 267.0,
                    image=entry1_img)

                entry_fun = Entry(ed_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_fun.place(
                    x=517, y=248,
                    width=380,
                    height=36)

                ed_epi.resizable(False, False)
                ed_epi.mainloop()

            def btn_oculos():
                def btn_clicked():
                    conn = sqlite3.connect('banco.sqlite')
                    cursor = conn.cursor()

                    cursor.execute(" UPDATE Oculos_EPI SET funcao_ocu = ? WHERE id_ocu_EPI = ? ",
                                   (entry_fun.get(), int(entry_ID.get())))

                    conn.commit()

                    conn.close()
                    canvas.create_text(
                        457.0, 430.5,
                        text="EPI atualizada",
                        fill="#000000",
                        font=("None", int(18.0)))

                ed_epi = tkinter.Toplevel()

                ed_epi.geometry("950x534")
                ed_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    ed_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/ed_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/ed_epi/img0.png")
                b0 = Button(ed_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_clicked,
                            relief="flat")

                b0.place(
                    x=344, y=323,
                    width=205,
                    height=89)

                entry0_img = PhotoImage(file=f"Imagens/ed_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 267.0,
                    image=entry0_img)

                entry_ID = Entry(ed_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_ID.place(
                    x=33, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/ed_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    707.0, 267.0,
                    image=entry1_img)

                entry_fun = Entry(ed_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_fun.place(
                    x=517, y=248,
                    width=380,
                    height=36)

                ed_epi.resizable(False, False)
                ed_epi.mainloop()

            def btn_luva():
                def btn_clicked():
                    conn = sqlite3.connect('banco.sqlite')
                    cursor = conn.cursor()

                    cursor.execute(" UPDATE Luva_EPI SET funcao_luva = ? WHERE id_luva_EPI = ? ",
                                   (entry_fun.get(), int(entry_ID.get())))

                    conn.commit()

                    conn.close()
                    canvas.create_text(
                        457.0, 430.5,
                        text="EPI atualizada",
                        fill="#000000",
                        font=("None", int(18.0)))

                ed_epi = tkinter.Toplevel()

                ed_epi.geometry("950x534")
                ed_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    ed_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/ed_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/ed_epi/img0.png")
                b0 = Button(ed_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_clicked,
                            relief="flat")

                b0.place(
                    x=344, y=323,
                    width=205,
                    height=89)

                entry0_img = PhotoImage(file=f"Imagens/ed_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 267.0,
                    image=entry0_img)

                entry_ID = Entry(ed_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_ID.place(
                    x=33, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/ed_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    707.0, 267.0,
                    image=entry1_img)

                entry_fun = Entry(ed_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_fun.place(
                    x=517, y=248,
                    width=380,
                    height=36)

                ed_epi.resizable(False, False)
                ed_epi.mainloop()

            def btn_cinturao():
                def btn_clicked():
                    conn = sqlite3.connect('banco.sqlite')
                    cursor = conn.cursor()

                    cursor.execute(" UPDATE Cinturao_EPI SET funcao_cin = ? WHERE id_cin_EPI = ? ",
                                   (entry_fun.get(), int(entry_ID.get())))

                    conn.commit()

                    conn.close()
                    canvas.create_text(
                        457.0, 430.5,
                        text="EPI atualizada",
                        fill="#000000",
                        font=("None", int(18.0)))

                ed_epi = tkinter.Toplevel()

                ed_epi.geometry("950x534")
                ed_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    ed_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/ed_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/ed_epi/img0.png")
                b0 = Button(ed_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_clicked,
                            relief="flat")

                b0.place(
                    x=344, y=323,
                    width=205,
                    height=89)

                entry0_img = PhotoImage(file=f"Imagens/ed_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 267.0,
                    image=entry0_img)

                entry_ID = Entry(ed_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_ID.place(
                    x=33, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/ed_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    707.0, 267.0,
                    image=entry1_img)

                entry_fun = Entry(ed_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_fun.place(
                    x=517, y=248,
                    width=380,
                    height=36)

                ed_epi.resizable(False, False)
                ed_epi.mainloop()

            def btn_mascara():
                def btn_clicked():
                    conn = sqlite3.connect('banco.sqlite')
                    cursor = conn.cursor()

                    cursor.execute(" UPDATE Mascara_EPI SET funcao_masc = ? WHERE id_masc_EPI = ? ",
                                   (entry_fun.get(), int(entry_ID.get())))

                    conn.commit()

                    conn.close()
                    canvas.create_text(
                        457.0, 430.5,
                        text="EPI atualizada",
                        fill="#000000",
                        font=("None", int(18.0)))

                ed_epi = tkinter.Toplevel()

                ed_epi.geometry("950x534")
                ed_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    ed_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/ed_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/ed_epi/img0.png")
                b0 = Button(ed_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_clicked,
                            relief="flat")

                b0.place(
                    x=344, y=323,
                    width=205,
                    height=89)

                entry0_img = PhotoImage(file=f"Imagens/ed_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 267.0,
                    image=entry0_img)

                entry_ID = Entry(ed_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_ID.place(
                    x=33, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/ed_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    707.0, 267.0,
                    image=entry1_img)

                entry_fun = Entry(ed_epi,
                                  bd=0,
                                  bg="#c4c4c4",
                                  highlightthickness=0)

                entry_fun.place(
                    x=517, y=248,
                    width=380,
                    height=36)

                ed_epi.resizable(False, False)
                ed_epi.mainloop()

            Cad_epi = tkinter.Toplevel()

            Cad_epi.geometry("950x534")
            Cad_epi.configure(bg="#ffffff")
            canvas = Canvas(
                Cad_epi,
                bg="#ffffff",
                height=534,
                width=950,
                bd=0,
                highlightthickness=0,
                relief="ridge")
            canvas.place(x=0, y=0)

            background_img = PhotoImage(file=f"Imagens/m_ed_epi/background.png")
            background = canvas.create_image(
                475.0, 267.0,
                image=background_img)

            img0 = PhotoImage(file=f"Imagens/m_ed_epi/img0.png")
            b0 = Button(Cad_epi,
                        image=img0,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_capacete,
                        relief="flat")

            b0.place(
                x=587, y=67,
                width=306,
                height=138)

            img1 = PhotoImage(file=f"Imagens/m_ed_epi/img1.png")
            b1 = Button(Cad_epi,
                        image=img1,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_colete,
                        relief="flat")

            b1.place(
                x=61, y=67,
                width=306,
                height=138)

            img2 = PhotoImage(file=f"Imagens/m_ed_epi/img2.png")
            b2 = Button(Cad_epi,
                        image=img2,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_oculos,
                        relief="flat")

            b2.place(
                x=61, y=215,
                width=306,
                height=138)

            img3 = PhotoImage(file=f"Imagens/m_ed_epi/img3.png")
            b3 = Button(Cad_epi,
                        image=img3,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_luva,
                        relief="flat")

            b3.place(
                x=61, y=363,
                width=306,
                height=138)

            img4 = PhotoImage(file=f"Imagens/m_ed_epi/img4.png")
            b4 = Button(Cad_epi,
                        image=img4,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_cinturao,
                        relief="flat")

            b4.place(
                x=587, y=215,
                width=306,
                height=138)

            img5 = PhotoImage(file=f"Imagens/m_ed_epi/img5.png")
            b5 = Button(Cad_epi,
                        image=img5,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_mascara,
                        relief="flat")

            b5.place(
                x=587, y=363,
                width=306,
                height=138)

            Cad_epi.resizable(False, False)
            Cad_epi.title("Cadastro epi")
            Cad_epi.mainloop()

        def btn_ex_fun():
            def btn_nome():
                conn = sqlite3.connect('banco.sqlite')
                cursor = conn.cursor()

                cursor.execute("""DELETE FROM funcionario WHERE nome = ?""", (entry_nome.get(),))

                conn.commit()

                print('Registro excluido com sucesso.')

                conn.close()


                canvas.create_text(
                    457.0, 430.5,
                    text="funcionario excluido",
                    fill="#000000",
                    font=("None", int(18.0)))

            def btn_CPF():
                conn = sqlite3.connect('banco.sqlite')
                cursor = conn.cursor()

                cpf = entry_cpf.get()

                cursor.execute("DELETE FROM funcionario WHERE CPF = ?", (cpf,))

                conn.commit()

                print('Registro excluido com sucesso.')

                conn.close()

                canvas.create_text(
                    457.0, 430.5,
                    text="funcionario excluido",
                    fill="#000000",
                    font=("None", int(18.0)))

            ex_fun = tkinter.Toplevel()

            ex_fun.geometry("950x534")
            ex_fun.configure(bg="#ffffff")
            canvas = Canvas(
                ex_fun,
                bg="#ffffff",
                height=534,
                width=950,
                bd=0,
                highlightthickness=0,
                relief="ridge")
            canvas.place(x=0, y=0)

            background_img = PhotoImage(file=f"Imagens/ex_fun/background.png")
            background = canvas.create_image(
                475.0, 267.0,
                image=background_img)

            img0 = PhotoImage(file=f"Imagens/ex_fun/img0.png")
            b0 = Button(ex_fun,
                        image=img0,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_CPF,
                        relief="flat")

            b0.place(
                x=562, y=311,
                width=205,
                height=89)

            img1 = PhotoImage(file=f"Imagens/ex_fun/img1.png")
            b1 = Button(ex_fun,
                        image=img1,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_nome,
                        relief="flat")

            b1.place(
                x=120, y=311,
                width=205,
                height=89)

            entry0_img = PhotoImage(file=f"Imagens/ex_fun/img_textBox0.png")
            entry0_bg = canvas.create_image(
                223.0, 267.0,
                image=entry0_img)

            entry_nome = Entry(ex_fun,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

            entry_nome.place(
                x=33, y=248,
                width=380,
                height=36)

            entry1_img = PhotoImage(file=f"Imagens/ex_fun/img_textBox1.png")
            entry1_bg = canvas.create_image(
                665.0, 267.0,
                image=entry1_img)

            entry_cpf = Entry(ex_fun,
                              bd=0,
                              bg="#c4c4c4",
                              highlightthickness=0)

            entry_cpf.place(
                x=475, y=248,
                width=380,
                height=36)

            ex_fun.resizable(False, False)
            ex_fun.title("Excluir Funcionario")
            ex_fun.mainloop()

        def btn_cons_fun():
            def btn_nome():
                con = sqlite3.connect("banco.sqlite")
                cur = con.cursor()


                cur.execute(" SELECT * FROM funcionario WHERE nome = ?", (entry_nome.get(),))

                funcinario = cur.fetchall()

                for funcinari in funcinario:
                    fun = (f"ID: {funcinari[0]}  |  Nome: {funcinari[1]} \nCPF: {funcinari[2]}  |  Funcao: {funcinari[3]}")

                con.close()

                canvas.create_text(
                    380.0, 470.5,
                    text=fun,
                    fill="#000000",
                    font=("None", int(16.0)))

            def btn_cpf():
                con = sqlite3.connect("banco.sqlite")
                cur = con.cursor()


                cur.execute(" SELECT * FROM funcionario WHERE CPF = ?", (entry_cpf.get(),))

                funcinario = cur.fetchall()

                for funcinari in funcinario:
                    fun = (f"ID: {funcinari[0]} Nome: {funcinari[1]} \nCPF: {funcinari[2]} Funcao: {funcinari[3]}")

                con.close()

                canvas.create_text(
                    380.0, 470.5,
                    text=fun,
                    fill="#000000",
                    font=("None", int(16.0)))

            cons_fun = tkinter.Toplevel()

            cons_fun.geometry("950x534")
            cons_fun.configure(bg="#ffffff")
            canvas = Canvas(
                cons_fun,
                bg="#ffffff",
                height=534,
                width=950,
                bd=0,
                highlightthickness=0,
                relief="ridge")
            canvas.place(x=0, y=0)

            background_img = PhotoImage(file=f"Imagens/cons_fun/background.png")
            background = canvas.create_image(
                464.5, 267.0,
                image=background_img)

            img0 = PhotoImage(file=f"Imagens/cons_fun/img0.png")
            b0 = Button(cons_fun,
                        image=img0,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_cpf,
                        relief="flat")

            b0.place(
                x=562, y=311,
                width=205,
                height=89)

            img1 = PhotoImage(file=f"Imagens/cons_fun/img1.png")
            b1 = Button(cons_fun,
                        image=img1,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_nome,
                        relief="flat")

            b1.place(
                x=120, y=311,
                width=205,
                height=89)

            entry0_img = PhotoImage(file=f"Imagens/cons_fun/img_textBox0.png")
            entry0_bg = canvas.create_image(
                223.0, 267.0,
                image=entry0_img)

            entry_nome = Entry(cons_fun,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

            entry_nome.place(
                x=33, y=248,
                width=380,
                height=36)

            entry1_img = PhotoImage(file=f"Imagens/cons_fun/img_textBox1.png")
            entry1_bg = canvas.create_image(
                665.0, 267.0,
                image=entry1_img)

            entry_cpf = Entry(cons_fun,
                              bd=0,
                              bg="#c4c4c4",
                              highlightthickness=0)

            entry_cpf.place(
                x=475, y=248,
                width=380,
                height=36)

            cons_fun.resizable(False, False)
            cons_fun.mainloop()

        def btn_ex_epi():
            def btn_capacete():
                def btn_nome():
                    conn = sqlite3.connect('banco.sqlite')
                    cursor = conn.cursor()

                    cursor.execute("""DELETE FROM Capacete_EPI WHERE nome_cap = ?""", entry_nome.get())

                    conn.commit()
                    conn.close()

                    canvas.create_text(
                        457.0, 430.5,
                        text="EPI excluida",
                        fill="#000000",
                        font=("None", int(18.0)))

                def btn_ID():
                    conn = sqlite3.connect('banco.sqlite')
                    cursor = conn.cursor()

                    id = entry_id.get()

                    cursor.execute("DELETE FROM Capacete_EPI WHERE id_cap_EPI = ?", (id,))

                    conn.commit()

                    conn.close()
                    canvas.create_text(
                        457.0, 430.5,
                        text="EPI excluida",
                        fill="#000000",
                        font=("None", int(18.0)))

                ex_epi = tkinter.Toplevel()

                ex_epi.geometry("950x534")
                ex_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    ex_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/ex_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/ex_epi/img0.png")
                b0 = Button(ex_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_nome,
                            relief="flat")

                b0.place(
                    x=562, y=311,
                    width=205,
                    height=89)

                img1 = PhotoImage(file=f"Imagens/ex_epi/img1.png")
                b1 = Button(ex_epi,
                            image=img1,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_ID,
                            relief="flat")

                b1.place(
                    x=120, y=311,
                    width=205,
                    height=89)

                entry0_img = PhotoImage(file=f"Imagens/ex_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 267.0,
                    image=entry0_img)

                entry_nome = Entry(ex_epi,
                                   bd=0,
                                   bg="#c4c4c4",
                                   highlightthickness=0)

                entry_nome.place(
                    x=33, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/ex_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    665.0, 267.0,
                    image=entry1_img)

                entry_id = Entry(ex_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_id.place(
                    x=475, y=248,
                    width=380,
                    height=36)

                ex_epi.resizable(False, False)
                ex_epi.mainloop()

            def btn_colete():
                def btn_nome():
                    conn = sqlite3.connect('banco.sqlite')
                    cursor = conn.cursor()

                    cursor.execute("""DELETE FROM Colete_EPI WHERE nome_col = ?""", (entry_nome.get(),))

                    conn.commit()

                    conn.close()
                    canvas.create_text(
                        457.0, 430.5,
                        text="EPI excluida",
                        fill="#000000",
                        font=("None", int(18.0)))

                def btn_ID():
                    conn = sqlite3.connect('banco.sqlite')
                    cursor = conn.cursor()

                    id = entry_id.get()

                    cursor.execute("DELETE FROM Colete_EPI WHERE id_col_EPI = ?", (id,))

                    conn.commit()

                    conn.close()
                    canvas.create_text(
                        457.0, 430.5,
                        text="EPI excluida",
                        fill="#000000",
                        font=("None", int(18.0)))

                ex_epi = tkinter.Toplevel()

                ex_epi.geometry("950x534")
                ex_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    ex_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/ex_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/ex_epi/img0.png")
                b0 = Button(ex_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_nome,
                            relief="flat")

                b0.place(
                    x=562, y=311,
                    width=205,
                    height=89)

                img1 = PhotoImage(file=f"Imagens/ex_epi/img1.png")
                b1 = Button(ex_epi,
                            image=img1,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_ID,
                            relief="flat")

                b1.place(
                    x=120, y=311,
                    width=205,
                    height=89)

                entry0_img = PhotoImage(file=f"Imagens/ex_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 267.0,
                    image=entry0_img)

                entry_nome = Entry(ex_epi,
                                   bd=0,
                                   bg="#c4c4c4",
                                   highlightthickness=0)

                entry_nome.place(
                    x=33, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/ex_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    665.0, 267.0,
                    image=entry1_img)

                entry_id = Entry(ex_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_id.place(
                    x=475, y=248,
                    width=380,
                    height=36)

                ex_epi.resizable(False, False)
                ex_epi.mainloop()

            def btn_oculos():
                def btn_nome():
                    conn = sqlite3.connect('banco.sqlite')
                    cursor = conn.cursor()

                    cursor.execute("""DELETE FROM Oculos_EPI WHERE nome_ocu = ?""", (entry_nome.get(),))

                    conn.commit()


                    conn.close()
                    canvas.create_text(
                        457.0, 430.5,
                        text="EPI excluida",
                        fill="#000000",
                        font=("None", int(18.0)))

                def btn_ID():
                    conn = sqlite3.connect('banco.sqlite')
                    cursor = conn.cursor()

                    id = entry_id.get()

                    cursor.execute("DELETE FROM Oculos_EPI WHERE id_ocu_EPI = ?", (id,))

                    conn.commit()


                    conn.close()
                    canvas.create_text(
                        457.0, 430.5,
                        text="EPI excluida",
                        fill="#000000",
                        font=("None", int(18.0)))

                ex_epi = tkinter.Toplevel()

                ex_epi.geometry("950x534")
                ex_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    ex_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/ex_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/ex_epi/img0.png")
                b0 = Button(ex_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_nome,
                            relief="flat")

                b0.place(
                    x=562, y=311,
                    width=205,
                    height=89)

                img1 = PhotoImage(file=f"Imagens/ex_epi/img1.png")
                b1 = Button(ex_epi,
                            image=img1,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_ID,
                            relief="flat")

                b1.place(
                    x=120, y=311,
                    width=205,
                    height=89)

                entry0_img = PhotoImage(file=f"Imagens/ex_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 267.0,
                    image=entry0_img)

                entry_nome = Entry(ex_epi,
                                   bd=0,
                                   bg="#c4c4c4",
                                   highlightthickness=0)

                entry_nome.place(
                    x=33, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/ex_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    665.0, 267.0,
                    image=entry1_img)

                entry_id = Entry(ex_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_id.place(
                    x=475, y=248,
                    width=380,
                    height=36)

                ex_epi.resizable(False, False)
                ex_epi.mainloop()

            def btn_luva():
                def btn_nome():
                    conn = sqlite3.connect('banco.sqlite')
                    cursor = conn.cursor()

                    cursor.execute("""DELETE FROM Luva_EPI WHERE nome_luva = ?""", (entry_nome.get(),))

                    conn.commit()

                    conn.close()
                    canvas.create_text(
                        457.0, 430.5,
                        text="EPI excluida",
                        fill="#000000",
                        font=("None", int(18.0)))

                def btn_ID():
                    conn = sqlite3.connect('banco.sqlite')
                    cursor = conn.cursor()

                    id = entry_id.get()

                    cursor.execute("DELETE FROM Luva_EPI WHERE id_luva_EPI = ?", (id,))

                    conn.commit()

                    conn.close()
                    canvas.create_text(
                        457.0, 430.5,
                        text="EPI excluida",
                        fill="#000000",
                        font=("None", int(18.0)))

                ex_epi = tkinter.Toplevel()

                ex_epi.geometry("950x534")
                ex_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    ex_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/ex_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/ex_epi/img0.png")
                b0 = Button(ex_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_nome,
                            relief="flat")

                b0.place(
                    x=562, y=311,
                    width=205,
                    height=89)

                img1 = PhotoImage(file=f"Imagens/ex_epi/img1.png")
                b1 = Button(ex_epi,
                            image=img1,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_ID,
                            relief="flat")

                b1.place(
                    x=120, y=311,
                    width=205,
                    height=89)

                entry0_img = PhotoImage(file=f"Imagens/ex_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 267.0,
                    image=entry0_img)

                entry_nome = Entry(ex_epi,
                                   bd=0,
                                   bg="#c4c4c4",
                                   highlightthickness=0)

                entry_nome.place(
                    x=33, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/ex_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    665.0, 267.0,
                    image=entry1_img)

                entry_id = Entry(ex_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_id.place(
                    x=475, y=248,
                    width=380,
                    height=36)

                ex_epi.resizable(False, False)
                ex_epi.mainloop()

            def btn_cinturao():
                def btn_nome():
                    conn = sqlite3.connect('banco.sqlite')
                    cursor = conn.cursor()

                    cursor.execute("""DELETE FROM Cinturao_EPI WHERE nome_cin = ?""", (entry_nome.get(),))

                    conn.commit()

                    conn.close()
                    canvas.create_text(
                        457.0, 430.5,
                        text="EPI excluida",
                        fill="#000000",
                        font=("None", int(18.0)))

                def btn_ID():
                    conn = sqlite3.connect('banco.sqlite')
                    cursor = conn.cursor()

                    id = entry_id.get()

                    cursor.execute("DELETE FROM Cinturao_EPI WHERE id_cin_EPI = ?", (id,))

                    conn.commit()

                    conn.close()
                    canvas.create_text(
                        457.0, 430.5,
                        text="EPI excluida",
                        fill="#000000",
                        font=("None", int(18.0)))

                ex_epi = tkinter.Toplevel()

                ex_epi.geometry("950x534")
                ex_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    ex_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/ex_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/ex_epi/img0.png")
                b0 = Button(ex_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_nome,
                            relief="flat")

                b0.place(
                    x=562, y=311,
                    width=205,
                    height=89)

                img1 = PhotoImage(file=f"Imagens/ex_epi/img1.png")
                b1 = Button(ex_epi,
                            image=img1,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_ID,
                            relief="flat")

                b1.place(
                    x=120, y=311,
                    width=205,
                    height=89)

                entry0_img = PhotoImage(file=f"Imagens/ex_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 267.0,
                    image=entry0_img)

                entry_nome = Entry(ex_epi,
                                   bd=0,
                                   bg="#c4c4c4",
                                   highlightthickness=0)

                entry_nome.place(
                    x=33, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/ex_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    665.0, 267.0,
                    image=entry1_img)

                entry_id = Entry(ex_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_id.place(
                    x=475, y=248,
                    width=380,
                    height=36)

                ex_epi.resizable(False, False)
                ex_epi.mainloop()

            def btn_mascara():
                def btn_nome():
                    conn = sqlite3.connect('banco.sqlite')
                    cursor = conn.cursor()

                    cursor.execute("""DELETE FROM Mascara_EPI WHERE nome_masc = ?""", (entry_nome.get(),))

                    conn.commit()


                    conn.close()
                    canvas.create_text(
                        457.0, 430.5,
                        text="EPI excluida",
                        fill="#000000",
                        font=("None", int(18.0)))

                def btn_ID():
                    conn = sqlite3.connect('banco.sqlite')
                    cursor = conn.cursor()

                    id = entry_id.get()

                    cursor.execute("DELETE FROM Mascara_EPI WHERE id_masc_EPI = ?", (id,))

                    conn.commit()


                    conn.close()
                    canvas.create_text(
                        457.0, 430.5,
                        text="EPI excluida",
                        fill="#000000",
                        font=("None", int(18.0)))

                ex_epi = tkinter.Toplevel()

                ex_epi.geometry("950x534")
                ex_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    ex_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/ex_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/ex_epi/img0.png")
                b0 = Button(ex_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_nome,
                            relief="flat")

                b0.place(
                    x=562, y=311,
                    width=205,
                    height=89)

                img1 = PhotoImage(file=f"Imagens/ex_epi/img1.png")
                b1 = Button(ex_epi,
                            image=img1,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_ID,
                            relief="flat")

                b1.place(
                    x=120, y=311,
                    width=205,
                    height=89)

                entry0_img = PhotoImage(file=f"Imagens/ex_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 267.0,
                    image=entry0_img)

                entry_nome = Entry(ex_epi,
                                   bd=0,
                                   bg="#c4c4c4",
                                   highlightthickness=0)

                entry_nome.place(
                    x=33, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/ex_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    665.0, 267.0,
                    image=entry1_img)

                entry_id = Entry(ex_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_id.place(
                    x=475, y=248,
                    width=380,
                    height=36)

                ex_epi.resizable(False, False)
                ex_epi.mainloop()

            m_ex_epi = tkinter.Toplevel()

            m_ex_epi.geometry("950x534")
            m_ex_epi.configure(bg="#ffffff")
            canvas = Canvas(
                m_ex_epi,
                bg="#ffffff",
                height=534,
                width=950,
                bd=0,
                highlightthickness=0,
                relief="ridge")
            canvas.place(x=0, y=0)

            background_img = PhotoImage(file=f"Imagens/m_ex_epi/background.png")
            background = canvas.create_image(
                475.0, 267.0,
                image=background_img)

            img0 = PhotoImage(file=f"Imagens/m_ex_epi/img0.png")
            b0 = Button(m_ex_epi,
                        image=img0,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_capacete,
                        relief="flat")

            b0.place(
                x=587, y=67,
                width=306,
                height=138)

            img1 = PhotoImage(file=f"Imagens/m_ex_epi/img1.png")
            b1 = Button(m_ex_epi,
                        image=img1,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_colete,
                        relief="flat")

            b1.place(
                x=61, y=67,
                width=306,
                height=138)

            img2 = PhotoImage(file=f"Imagens/m_ex_epi/img2.png")
            b2 = Button(m_ex_epi,
                        image=img2,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_oculos,
                        relief="flat")

            b2.place(
                x=61, y=215,
                width=306,
                height=138)

            img3 = PhotoImage(file=f"Imagens/m_ex_epi/img3.png")
            b3 = Button(m_ex_epi,
                        image=img3,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_luva,
                        relief="flat")

            b3.place(
                x=61, y=363,
                width=306,
                height=138)

            img4 = PhotoImage(file=f"Imagens/m_ex_epi/img4.png")
            b4 = Button(m_ex_epi,
                        image=img4,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_cinturao,
                        relief="flat")

            b4.place(
                x=587, y=215,
                width=306,
                height=138)

            img5 = PhotoImage(file=f"Imagens/m_ex_epi/img5.png")
            b5 = Button(m_ex_epi,
                        image=img5,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_mascara,
                        relief="flat")

            b5.place(
                x=587, y=363,
                width=306,
                height=138)

            m_ex_epi.resizable(False, False)
            m_ex_epi.title("Menu excluir epi")
            m_ex_epi.mainloop()

        def btn_cons_epi():
            def btn_capacete():
                def btn_nome():
                    con = sqlite3.connect("banco.sqlite")
                    cur = con.cursor()


                    cur.execute(" SELECT * FROM Capacete_EPI WHERE nome_cap = ?", (entry_nome.get(),))

                    funcinario = cur.fetchall()

                    for epi in funcinario:
                        fun = (f"ID: {epi[0]} | CA: {epi[1]} | Nome: {epi[2]} | Fabricante: {epi[3]}")
                        fun2 = (f"Protecao: {epi[4]} | Funcao: {epi[5]} | Validade: {epi[6]}")

                    con.close()

                    canvas.create_text(
                        420.0, 470.5,
                        text=fun,
                        fill="#000000",
                        font=("None", int(9.0)))

                    canvas.create_text(
                        420.0, 490.5,
                        text=fun2,
                        fill="#000000",
                        font=("None", int(9.0)))

                def btn_id():
                    con = sqlite3.connect("banco.sqlite")
                    cur = con.cursor()


                    cur.execute(" SELECT * FROM Capacete_EPI WHERE id_cap_EPI = ?", (entry_id.get(),))

                    funcinario = cur.fetchall()

                    for epi in funcinario:
                        fun = (f"ID: {epi[0]} | CA: {epi[1]} | Nome: {epi[2]} | Fabricante: {epi[3]}")
                        fun2 = (f"Protecao: {epi[4]} | Funcao: {epi[5]} | Validade: {epi[6]}")

                    con.close()

                    canvas.create_text(
                        420.0, 470.5,
                        text=fun,
                        fill="#000000",
                        font=("None", int(9.0)))

                    canvas.create_text(
                        420.0, 490.5,
                        text=fun2,
                        fill="#000000",
                        font=("None", int(9.0)))

                cons_epi = tkinter.Toplevel()

                cons_epi.geometry("950x534")
                cons_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    cons_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/cons_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/cons_epi/img0.png")
                b0 = Button(cons_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_id,
                            relief="flat")

                b0.place(
                    x=562, y=311,
                    width=205,
                    height=89)

                img1 = PhotoImage(file=f"Imagens/cons_epi/img1.png")
                b1 = Button(cons_epi,
                            image=img1,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_nome,
                            relief="flat")

                b1.place(
                    x=120, y=311,
                    width=205,
                    height=89)

                entry0_img = PhotoImage(file=f"Imagens/cons_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 267.0,
                    image=entry0_img)

                entry_nome = Entry(cons_epi,
                                   bd=0,
                                   bg="#c4c4c4",
                                   highlightthickness=0)

                entry_nome.place(
                    x=33, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/cons_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    665.0, 267.0,
                    image=entry1_img)

                entry_id = Entry(cons_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_id.place(
                    x=475, y=248,
                    width=380,
                    height=36)

                cons_epi.resizable(False, False)
                cons_epi.title("Capacete")
                cons_epi.mainloop()

            def btn_colete():
                def btn_nome():
                    con = sqlite3.connect("banco.sqlite")
                    cur = con.cursor()


                    cur.execute(" SELECT * FROM Colete_EPI WHERE nome_col = ?", (entry_nome.get(),))

                    funcinario = cur.fetchall()

                    for epi in funcinario:
                        fun = (f"ID: {epi[0]} | CA: {epi[1]} | Nome: {epi[2]} | Fabricante: {epi[3]}")
                        fun2 = (f"Protecao: {epi[4]} | Funcao: {epi[5]} | Validade: {epi[6]}")

                    con.close()

                    canvas.create_text(
                        420.0, 470.5,
                        text=fun,
                        fill="#000000",
                        font=("None", int(9.0)))

                    canvas.create_text(
                        420.0, 490.5,
                        text=fun2,
                        fill="#000000",
                        font=("None", int(9.0)))

                def btn_id():
                    con = sqlite3.connect("banco.sqlite")
                    cur = con.cursor()


                    cur.execute(" SELECT * FROM Colete_EPI WHERE id_col_EPI = ?", (entry_id.get(),))

                    funcinario = cur.fetchall()

                    for epi in funcinario:
                        fun = (f"ID: {epi[0]} | CA: {epi[1]} | Nome: {epi[2]} | Fabricante: {epi[3]}")
                        fun2 = (f"Protecao: {epi[4]} | Funcao: {epi[5]} | Validade: {epi[6]}")

                    con.close()

                    canvas.create_text(
                        420.0, 470.5,
                        text=fun,
                        fill="#000000",
                        font=("None", int(9.0)))

                    canvas.create_text(
                        420.0, 490.5,
                        text=fun2,
                        fill="#000000",
                        font=("None", int(9.0)))

                cons_epi = tkinter.Toplevel()

                cons_epi.geometry("950x534")
                cons_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    cons_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/cons_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/cons_epi/img0.png")
                b0 = Button(cons_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_id,
                            relief="flat")

                b0.place(
                    x=562, y=311,
                    width=205,
                    height=89)

                img1 = PhotoImage(file=f"Imagens/cons_epi/img1.png")
                b1 = Button(cons_epi,
                            image=img1,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_nome,
                            relief="flat")

                b1.place(
                    x=120, y=311,
                    width=205,
                    height=89)

                entry0_img = PhotoImage(file=f"Imagens/cons_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 267.0,
                    image=entry0_img)

                entry_nome = Entry(cons_epi,
                                   bd=0,
                                   bg="#c4c4c4",
                                   highlightthickness=0)

                entry_nome.place(
                    x=33, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/cons_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    665.0, 267.0,
                    image=entry1_img)

                entry_id = Entry(cons_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_id.place(
                    x=475, y=248,
                    width=380,
                    height=36)

                cons_epi.resizable(False, False)
                cons_epi.title("Colete")
                cons_epi.mainloop()

            def btn_oculos():
                def btn_nome():
                    con = sqlite3.connect("banco.sqlite")
                    cur = con.cursor()


                    cur.execute(" SELECT * FROM Oculos_EPI WHERE nome_ocu = ?", (entry_nome.get(),))

                    funcinario = cur.fetchall()

                    for epi in funcinario:
                        fun = (f"ID: {epi[0]} | CA: {epi[1]} | Nome: {epi[2]} | Fabricante: {epi[3]}")
                        fun2 = (f"Protecao: {epi[4]} | Funcao: {epi[5]} | Validade: {epi[6]}")

                    con.close()

                    canvas.create_text(
                        420.0, 470.5,
                        text=fun,
                        fill="#000000",
                        font=("None", int(9.0)))

                    canvas.create_text(
                        420.0, 490.5,
                        text=fun2,
                        fill="#000000",
                        font=("None", int(9.0)))

                def btn_id():
                    con = sqlite3.connect("banco.sqlite")
                    cur = con.cursor()


                    cur.execute(" SELECT * FROM Oculos_EPI WHERE id_ocu_EPI = ?", (entry_id.get(),))

                    funcinario = cur.fetchall()

                    for epi in funcinario:
                        fun = (f"ID: {epi[0]} | CA: {epi[1]} | Nome: {epi[2]} | Fabricante: {epi[3]}")
                        fun2 = (f"Protecao: {epi[4]} | Funcao: {epi[5]} | Validade: {epi[6]}")

                    con.close()

                    canvas.create_text(
                        420.0, 470.5,
                        text=fun,
                        fill="#000000",
                        font=("None", int(9.0)))

                    canvas.create_text(
                        420.0, 490.5,
                        text=fun2,
                        fill="#000000",
                        font=("None", int(9.0)))

                cons_epi = tkinter.Toplevel()

                cons_epi.geometry("950x534")
                cons_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    cons_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/cons_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/cons_epi/img0.png")
                b0 = Button(cons_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_id,
                            relief="flat")

                b0.place(
                    x=562, y=311,
                    width=205,
                    height=89)

                img1 = PhotoImage(file=f"Imagens/cons_epi/img1.png")
                b1 = Button(cons_epi,
                            image=img1,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_nome,
                            relief="flat")

                b1.place(
                    x=120, y=311,
                    width=205,
                    height=89)

                entry0_img = PhotoImage(file=f"Imagens/cons_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 267.0,
                    image=entry0_img)

                entry_nome = Entry(cons_epi,
                                   bd=0,
                                   bg="#c4c4c4",
                                   highlightthickness=0)

                entry_nome.place(
                    x=33, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/cons_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    665.0, 267.0,
                    image=entry1_img)

                entry_id = Entry(cons_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_id.place(
                    x=475, y=248,
                    width=380,
                    height=36)

                cons_epi.resizable(False, False)
                cons_epi.title("Oculos")
                cons_epi.mainloop()

            def btn_luva():
                def btn_nome():
                    con = sqlite3.connect("banco.sqlite")
                    cur = con.cursor()


                    cur.execute(" SELECT * FROM Luva_EPI WHERE nome_luva = ?", (entry_nome.get(),))

                    funcinario = cur.fetchall()

                    for epi in funcinario:
                        fun = (f"ID: {epi[0]} | CA: {epi[1]} | Nome: {epi[2]} | Fabricante: {epi[3]}")
                        fun2 = (f"Protecao: {epi[4]} | Funcao: {epi[5]} | Validade: {epi[6]}")

                    con.close()

                    canvas.create_text(
                        420.0, 470.5,
                        text=fun,
                        fill="#000000",
                        font=("None", int(9.0)))

                    canvas.create_text(
                        420.0, 490.5,
                        text=fun2,
                        fill="#000000",
                        font=("None", int(9.0)))

                def btn_id():
                    con = sqlite3.connect("banco.sqlite")
                    cur = con.cursor()


                    cur.execute(" SELECT * FROM Luva_EPI WHERE id_luva_EPI = ?", (entry_id.get(),))

                    funcinario = cur.fetchall()

                    for epi in funcinario:
                        fun = (f"ID: {epi[0]} | CA: {epi[1]} | Nome: {epi[2]} | Fabricante: {epi[3]}")
                        fun2 = (f"Protecao: {epi[4]} | Funcao: {epi[5]} | Validade: {epi[6]}")

                    con.close()

                    canvas.create_text(
                        420.0, 470.5,
                        text=fun,
                        fill="#000000",
                        font=("None", int(9.0)))

                    canvas.create_text(
                        420.0, 490.5,
                        text=fun2,
                        fill="#000000",
                        font=("None", int(9.0)))

                cons_epi = tkinter.Toplevel()

                cons_epi.geometry("950x534")
                cons_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    cons_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/cons_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/cons_epi/img0.png")
                b0 = Button(cons_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_id,
                            relief="flat")

                b0.place(
                    x=562, y=311,
                    width=205,
                    height=89)

                img1 = PhotoImage(file=f"Imagens/cons_epi/img1.png")
                b1 = Button(cons_epi,
                            image=img1,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_nome,
                            relief="flat")

                b1.place(
                    x=120, y=311,
                    width=205,
                    height=89)

                entry0_img = PhotoImage(file=f"Imagens/cons_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 267.0,
                    image=entry0_img)

                entry_nome = Entry(cons_epi,
                                   bd=0,
                                   bg="#c4c4c4",
                                   highlightthickness=0)

                entry_nome.place(
                    x=33, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/cons_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    665.0, 267.0,
                    image=entry1_img)

                entry_id = Entry(cons_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_id.place(
                    x=475, y=248,
                    width=380,
                    height=36)

                cons_epi.resizable(False, False)
                cons_epi.title("Luva")
                cons_epi.mainloop()

            def btn_cinturao():
                def btn_nome():
                    con = sqlite3.connect("banco.sqlite")
                    cur = con.cursor()


                    cur.execute(" SELECT * FROM Cinturao_EPI WHERE nome_cin = ?", (entry_nome.get(),))

                    funcinario = cur.fetchall()

                    for epi in funcinario:
                        fun = (f"ID: {epi[0]} | CA: {epi[1]} | Nome: {epi[2]} | Fabricante: {epi[3]}")
                        fun2 = (f"Protecao: {epi[4]} | Funcao: {epi[5]} | Validade: {epi[6]}")

                    con.close()

                    canvas.create_text(
                        420.0, 470.5,
                        text=fun,
                        fill="#000000",
                        font=("None", int(9.0)))

                    canvas.create_text(
                        420.0, 490.5,
                        text=fun2,
                        fill="#000000",
                        font=("None", int(9.0)))

                def btn_id():
                    con = sqlite3.connect("banco.sqlite")
                    cur = con.cursor()


                    cur.execute(" SELECT * FROM Cinturao_EPI WHERE id_cin_EPI = ?", (entry_id.get(),))

                    funcinario = cur.fetchall()

                    for epi in funcinario:
                        fun = (f"ID: {epi[0]} | CA: {epi[1]} | Nome: {epi[2]} | Fabricante: {epi[3]}")
                        fun2 = (f"Protecao: {epi[4]} | Funcao: {epi[5]} | Validade: {epi[6]}")

                    con.close()

                    canvas.create_text(
                        420.0, 470.5,
                        text=fun,
                        fill="#000000",
                        font=("None", int(9.0)))

                    canvas.create_text(
                        420.0, 490.5,
                        text=fun2,
                        fill="#000000",
                        font=("None", int(9.0)))

                cons_epi = tkinter.Toplevel()

                cons_epi.geometry("950x534")
                cons_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    cons_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/cons_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/cons_epi/img0.png")
                b0 = Button(cons_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_id,
                            relief="flat")

                b0.place(
                    x=562, y=311,
                    width=205,
                    height=89)

                img1 = PhotoImage(file=f"Imagens/cons_epi/img1.png")
                b1 = Button(cons_epi,
                            image=img1,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_nome,
                            relief="flat")

                b1.place(
                    x=120, y=311,
                    width=205,
                    height=89)

                entry0_img = PhotoImage(file=f"Imagens/cons_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 267.0,
                    image=entry0_img)

                entry_nome = Entry(cons_epi,
                                   bd=0,
                                   bg="#c4c4c4",
                                   highlightthickness=0)

                entry_nome.place(
                    x=33, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/cons_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    665.0, 267.0,
                    image=entry1_img)

                entry_id = Entry(cons_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_id.place(
                    x=475, y=248,
                    width=380,
                    height=36)

                cons_epi.resizable(False, False)
                cons_epi.title("Cinturao")
                cons_epi.mainloop()

            def btn_mascara():
                def btn_nome():
                    con = sqlite3.connect("banco.sqlite")
                    cur = con.cursor()

                    cur.execute(" SELECT * FROM Mascara_EPI WHERE nome_masc = ?", (entry_nome.get(),))

                    funcinario = cur.fetchall()

                    for epi in funcinario:
                        fun = (f"ID: {epi[0]} | CA: {epi[1]} | Nome: {epi[2]} | Fabricante: {epi[3]}")
                        fun2 = (f"Protecao: {epi[4]} | Funcao: {epi[5]} | Validade: {epi[6]}")

                    con.close()

                    canvas.create_text(
                        420.0, 470.5,
                        text=fun,
                        fill="#000000",
                        font=("None", int(9.0)))

                    canvas.create_text(
                        420.0, 490.5,
                        text=fun2,
                        fill="#000000",
                        font=("None", int(9.0)))

                def btn_id():
                    con = sqlite3.connect("banco.sqlite")
                    cur = con.cursor()


                    cur.execute(" SELECT * FROM Mascara_EPI WHERE id_masc_EPI = ?", (entry_id.get(),))

                    funcinario = cur.fetchall()

                    for epi in funcinario:
                        fun = (f"ID: {epi[0]} | CA: {epi[1]} | Nome: {epi[2]} | Fabricante: {epi[3]}")
                        fun2 = (f"Protecao: {epi[4]} | Funcao: {epi[5]} | Validade: {epi[6]}")

                    con.close()

                    canvas.create_text(
                        420.0, 470.5,
                        text=fun,
                        fill="#000000",
                        font=("None", int(9.0)))

                    canvas.create_text(
                        420.0, 490.5,
                        text=fun2,
                        fill="#000000",
                        font=("None", int(9.0)))

                cons_epi = tkinter.Toplevel()

                cons_epi.geometry("950x534")
                cons_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    cons_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/cons_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/cons_epi/img0.png")
                b0 = Button(cons_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_id,
                            relief="flat")

                b0.place(
                    x=562, y=311,
                    width=205,
                    height=89)

                img1 = PhotoImage(file=f"Imagens/cons_epi/img1.png")
                b1 = Button(cons_epi,
                            image=img1,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_nome,
                            relief="flat")

                b1.place(
                    x=120, y=311,
                    width=205,
                    height=89)

                entry0_img = PhotoImage(file=f"Imagens/cons_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    223.0, 267.0,
                    image=entry0_img)

                entry_nome = Entry(cons_epi,
                                   bd=0,
                                   bg="#c4c4c4",
                                   highlightthickness=0)

                entry_nome.place(
                    x=33, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/cons_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    665.0, 267.0,
                    image=entry1_img)

                entry_id = Entry(cons_epi,
                                 bd=0,
                                 bg="#c4c4c4",
                                 highlightthickness=0)

                entry_id.place(
                    x=475, y=248,
                    width=380,
                    height=36)

                cons_epi.resizable(False, False)
                cons_epi.title("Mascara")
                cons_epi.mainloop()

            cons_epi = tkinter.Toplevel()

            cons_epi.geometry("950x534")
            cons_epi.configure(bg="#ffffff")
            canvas = Canvas(
                cons_epi,
                bg="#ffffff",
                height=534,
                width=950,
                bd=0,
                highlightthickness=0,
                relief="ridge")
            canvas.place(x=0, y=0)

            background_img = PhotoImage(file=f"Imagens/m_cons_epi/background.png")
            background = canvas.create_image(
                475.0, 267.0,
                image=background_img)

            img0 = PhotoImage(file=f"Imagens/m_cons_epi/img0.png")
            b0 = Button(cons_epi,
                        image=img0,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_capacete,
                        relief="flat")

            b0.place(
                x=587, y=67,
                width=306,
                height=138)

            img1 = PhotoImage(file=f"Imagens/m_cons_epi/img1.png")
            b1 = Button(cons_epi,
                        image=img1,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_colete,
                        relief="flat")

            b1.place(
                x=61, y=67,
                width=306,
                height=138)

            img2 = PhotoImage(file=f"Imagens/m_cons_epi/img2.png")
            b2 = Button(cons_epi,
                        image=img2,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_oculos,
                        relief="flat")

            b2.place(
                x=61, y=215,
                width=306,
                height=138)

            img3 = PhotoImage(file=f"Imagens/m_cons_epi/img3.png")
            b3 = Button(cons_epi,
                        image=img3,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_luva,
                        relief="flat")

            b3.place(
                x=61, y=363,
                width=306,
                height=138)

            img4 = PhotoImage(file=f"Imagens/m_cons_epi/img4.png")
            b4 = Button(cons_epi,
                        image=img4,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_cinturao,
                        relief="flat")

            b4.place(
                x=587, y=215,
                width=306,
                height=138)

            img5 = PhotoImage(file=f"Imagens/m_cons_epi/img5.png")
            b5 = Button(cons_epi,
                        image=img5,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_mascara,
                        relief="flat")

            b5.place(
                x=587, y=363,
                width=306,
                height=138)

            cons_epi.resizable(False, False)
            cons_epi.title("Consultar epi")
            cons_epi.mainloop()

        m_crud = tkinter.Toplevel()

        m_crud.geometry("950x534")
        m_crud.configure(bg="#ffffff")
        canvas = Canvas(
            m_crud,
            bg="#ffffff",
            height=534,
            width=950,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"Imagens/menu_crud/background.png")
        background = canvas.create_image(
            475.0, 262.0,
            image=background_img)

        img0 = PhotoImage(file=f"Imagens/menu_crud/img0.png")
        b0 = Button(m_crud,
                    image=img0,
                    borderwidth=0,
                    highlightthickness=0,
                    command=btn_cad_fun,
                    relief="flat")

        b0.place(
            x=117, y=86,
            width=243,
            height=100)

        img1 = PhotoImage(file=f"Imagens/menu_crud/img1.png")
        b1 = Button(m_crud,
                    image=img1,
                    borderwidth=0,
                    highlightthickness=0,
                    command=btn_cad_epi,
                    relief="flat")

        b1.place(
            x=575, y=86,
            width=243,
            height=100)

        img2 = PhotoImage(file=f"Imagens/menu_crud/img2.png")
        b2 = Button(m_crud,
                    image=img2,
                    borderwidth=0,
                    highlightthickness=0,
                    command=btn_ed_fun,
                    relief="flat")

        b2.place(
            x=117, y=198,
            width=243,
            height=100)

        img3 = PhotoImage(file=f"Imagens/menu_crud/img3.png")
        b3 = Button(m_crud,
                    image=img3,
                    borderwidth=0,
                    highlightthickness=0,
                    command=btn_ed_epi,
                    relief="flat")

        b3.place(
            x=575, y=198,
            width=243,
            height=100)

        img4 = PhotoImage(file=f"Imagens/menu_crud/img4.png")
        b4 = Button(m_crud,
                    image=img4,
                    borderwidth=0,
                    highlightthickness=0,
                    command=btn_ex_fun,
                    relief="flat")

        b4.place(
            x=113, y=310,
            width=243,
            height=100)

        img5 = PhotoImage(file=f"Imagens/menu_crud/img5.png")
        b5 = Button(m_crud,
                    image=img5,
                    borderwidth=0,
                    highlightthickness=0,
                    command=btn_cons_fun,
                    relief="flat")

        b5.place(
            x=113, y=422,
            width=243,
            height=100)

        img6 = PhotoImage(file=f"Imagens/menu_crud/img6.png")
        b6 = Button(m_crud,
                    image=img6,
                    borderwidth=0,
                    highlightthickness=0,
                    command=btn_ex_epi,
                    relief="flat")

        b6.place(
            x=575, y=310,
            width=243,
            height=100)

        img7 = PhotoImage(file=f"Imagens/menu_crud/img7.png")
        b7 = Button(m_crud,
                    image=img7,
                    borderwidth=0,
                    highlightthickness=0,
                    command=btn_cons_epi,
                    relief="flat")

        b7.place(
            x=575, y=422,
            width=243,
            height=100)

        m_crud.resizable(False, False)
        m_crud.title("Menu CRUD")
        m_crud.mainloop()

    def btn_rela():
        def btn_en_fun():
            def btn_clicked():
                data = entry0.get()
                nome = entry1.get()
                nome_arquivo = nome + ".doc"
                con = sqlite3.connect('banco.sqlite')
                cur = con.cursor()
                hoje = date.today()
                sql = f"SELECT * FROM entrada_fun WHERE data_en_fun = '{data}'"
                cur.execute(sql)
                funcionario = cur.fetchall()
                n_fun = (f'\nEntrou ao total de {len(funcionario)} funcionarios no dia {data}\n')
                con.close()
                try:
                    arquivo = open(nome_arquivo, 'r+')
                except FileNotFoundError:
                    arquivo = open(nome_arquivo, 'w+')
                    arquivo.write('Relatorio criado dia ' + str(hoje))
                    arquivo.write(f'\nEste documento e referente a entrada dos funcionarios da empresa de construcao civil no dia {data}, o ponto foi realizado atraves do craha do funcionario que possui a tecnologia RFID')
                    arquivo.write('' + n_fun)
                    arquivo.write('\n \nTabela de entrada dos funcionarios:\n')
                    arquivo.writelines('')
                    for funcionarios in funcionario:
                        funcionarios = str(
                            f"Entrada: {funcionarios[0]} \nID do funcionario: {funcionarios[1]}\nNome: {funcionarios[2]} \nFuncao: {funcionarios[3]} \nData: {funcionarios[4]} \nHora: {funcionarios[5]} \n\n----------------------------------------------------------------")
                        arquivo.write("\n%s\n" % funcionarios)
                    arquivo.write('----------------------------------------------------------------')
                    arquivo.write('                      Assinatura Responsavel                    ')

                    arquivo.close()

            relatorio_en_fun = tkinter.Toplevel()

            relatorio_en_fun.geometry("950x534")
            relatorio_en_fun.configure(bg="#ffffff")
            canvas = Canvas(
                relatorio_en_fun,
                bg="#ffffff",
                height=534,
                width=950,
                bd=0,
                highlightthickness=0,
                relief="ridge")
            canvas.place(x=0, y=0)

            background_img = PhotoImage(file=f"Imagens/rela_en_fun/background.png")
            background = canvas.create_image(
                475.0, 267.0,
                image=background_img)

            img0 = PhotoImage(file=f"Imagens/rela_en_fun/img0.png")
            b0 = Button(relatorio_en_fun,
                        image=img0,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_clicked,
                        relief="flat")

            b0.place(
                x=322, y=436,
                width=306,
                height=71)

            entry0_img = PhotoImage(file=f"Imagens/rela_en_fun/img_textBox0.png")
            entry0_bg = canvas.create_image(
                285.0, 267.0,
                image=entry0_img)

            entry0 = Entry(relatorio_en_fun,
                           bd=0,
                           bg="#c4c4c4",
                           highlightthickness=0)

            entry0.place(
                x=95, y=248,
                width=380,
                height=36)

            entry1_img = PhotoImage(file=f"Imagens/rela_en_fun/img_textBox1.png")
            entry1_bg = canvas.create_image(
                285.0, 368.0,
                image=entry1_img)

            entry1 = Entry(relatorio_en_fun,
                           bd=0,
                           bg="#c4c4c4",
                           highlightthickness=0)

            entry1.place(
                x=95, y=349,
                width=380,
                height=36)

            relatorio_en_fun.resizable(False, False)
            relatorio_en_fun.title("Relatorio entrada funcionario")
            relatorio_en_fun.mainloop()


        def btn_sa_fun():
            def btn_clicked():
                data = entry0.get()
                nome = entry1.get()
                nome_arquivo = nome + ".doc"
                con = sqlite3.connect('banco.sqlite')
                cur = con.cursor()
                hoje = date.today()
                sql = f"SELECT * FROM saida_fun WHERE data_sa_fun = '{data}'"
                cur.execute(sql)
                funcionario = cur.fetchall()
                n_fun = (f'\nSaiu ao total de {len(funcionario)} funcionarios no dia {data}\n')
                con.close()
                try:
                    arquivo = open(nome_arquivo, 'r+')
                except FileNotFoundError:
                    arquivo = open(nome_arquivo, 'w+')
                    arquivo.write('Relatorio criado dia ' + str(hoje))
                    arquivo.write(f'\nEste documento e referente a saida dos funcionarios da empresa de construcao civil no dia {data}, o ponto foi realizado atraves do craha do funcionario que possui a tecnologia RFID')
                    arquivo.write('' + n_fun)
                    arquivo.write('\n \nTabela de saida dos funcionarios:\n')
                    arquivo.writelines('')
                    for funcionarios in funcionario:
                        funcionarios = str(
                            f"Entrada: {funcionarios[0]} \nID do funcionario: {funcionarios[1]}\nNome: {funcionarios[2]} \nFuncao: {funcionarios[3]} \nData: {funcionarios[4]} \nHora: {funcionarios[5]} \n\n----------------------------------------------------------------")
                        arquivo.write("\n%s\n" % funcionarios)
                    arquivo.write('----------------------------------------------------------------')
                    arquivo.write('                      Assinatura Responsavel                    ')

                    arquivo.close()

            relatorio_sa_fun = tkinter.Toplevel()

            relatorio_sa_fun.geometry("950x534")
            relatorio_sa_fun.configure(bg="#ffffff")
            canvas = Canvas(
                relatorio_sa_fun,
                bg="#ffffff",
                height=534,
                width=950,
                bd=0,
                highlightthickness=0,
                relief="ridge")
            canvas.place(x=0, y=0)

            background_img = PhotoImage(file=f"Imagens/rela_sa_fun/background.png")
            background = canvas.create_image(
                475.0, 267.0,
                image=background_img)

            img0 = PhotoImage(file=f"Imagens/rela_sa_fun/img0.png")
            b0 = Button(relatorio_sa_fun,
                        image=img0,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_clicked,
                        relief="flat")

            b0.place(
                x=322, y=436,
                width=306,
                height=71)

            entry0_img = PhotoImage(file=f"Imagens/rela_sa_fun/img_textBox0.png")
            entry0_bg = canvas.create_image(
                285.0, 267.0,
                image=entry0_img)

            entry0 = Entry(relatorio_sa_fun,
                           bd=0,
                           bg="#c4c4c4",
                           highlightthickness=0)

            entry0.place(
                x=95, y=248,
                width=380,
                height=36)

            entry1_img = PhotoImage(file=f"Imagens/rela_sa_fun/img_textBox1.png")
            entry1_bg = canvas.create_image(
                285.0, 368.0,
                image=entry1_img)

            entry1 = Entry(relatorio_sa_fun,
                           bd=0,
                           bg="#c4c4c4",
                           highlightthickness=0)

            entry1.place(
                x=95, y=349,
                width=380,
                height=36)

            relatorio_sa_fun.resizable(False, False)
            relatorio_sa_fun.title("Relatorio saida funcionario")
            relatorio_sa_fun.mainloop()


        def btn_m_en_epi():
            def btn_cap():
                def btn_clicked():
                    data = entry0.get()
                    nome = entry1.get()
                    nome_arquivo = nome + ".doc"
                    con = sqlite3.connect('banco.sqlite')
                    cur = con.cursor()
                    hoje = date.today()
                    sql = f"SELECT * FROM entrada_cap_epi WHERE data_en_cap = '{data}'"
                    cur.execute(sql)
                    epi = cur.fetchall()
                    n_fun = (f'\nEntrou ao total de {len(epi)} capacetes no dia {data}\n')
                    con.close()
                    try:
                        arquivo = open(nome_arquivo, 'r+')
                    except FileNotFoundError:
                        arquivo = open(nome_arquivo, 'w+')
                        arquivo.write('Relatorio criado dia ' + str(hoje))
                        arquivo.write(f'\nEste documento e referente a entrada dos capacetes durante o servico do dia {data} e ira ser utilizado na empresa de construcao civil, neste relatorio informa que devera ser acompanhado o uso corretamente durante o tempo que estiver em uso observando as medidas gerais de disciplina e uso que integra a NR-06 Equipamento de Protecao Individua - EPI- da portaria n, 3.214 de 08 de Jun. de 1970. ponto foi realizado atraves de uma tag embutida no equipamento que possui a tecnologia RFID')
                        arquivo.write('' + n_fun)
                        arquivo.write('\n \nTabela de entrada dos capacetes:\n')
                        arquivo.writelines('')
                        for epis in epi:
                            epis = str(f"Entrada: {epis[0]} \nID do capacete: {epis[1]}\nNome: {epis[2]} \nNome do Funcionario: {epis[3]} \nFuncao: {epis[4]} \nData: {epis[5]} \nHora: {epis[6]} \n\n----------------------------------------------------------------")
                            arquivo.write("\n%s\n" % epis)
                        arquivo.write('----------------------------------------------------------------')
                        arquivo.write('                      Assinatura Responsavel                    ')

                rela_en_epi = tkinter.Toplevel()

                rela_en_epi.geometry("950x534")
                rela_en_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    rela_en_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/rela_en_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/rela_en_epi/img0.png")
                b0 = Button(rela_en_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_clicked,
                            relief="flat")

                b0.place(
                    x=322, y=436,
                    width=306,
                    height=71)

                entry0_img = PhotoImage(file=f"Imagens/rela_en_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    285.0, 267.0,
                    image=entry0_img)

                entry0 = Entry(rela_en_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry0.place(
                    x=95, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/rela_en_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    285.0, 368.0,
                    image=entry1_img)

                entry1 = Entry(rela_en_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry1.place(
                    x=95, y=349,
                    width=380,
                    height=36)

                rela_en_epi.resizable(False, False)
                rela_en_epi.title("Entrada")
                rela_en_epi.mainloop()
                print("1")

            def btn_luv():
                def btn_clicked():
                    data = entry0.get()
                    nome = entry1.get()
                    nome_arquivo = nome + ".doc"
                    con = sqlite3.connect('banco.sqlite')
                    cur = con.cursor()
                    hoje = date.today()
                    sql = f"SELECT * FROM entrada_luva_epi WHERE data_en_luva = '{data}'"
                    cur.execute(sql)
                    epi = cur.fetchall()
                    n_fun = (f'\nEntrou ao total de {len(epi)} Luvas no dia {data}\n')
                    con.close()
                    try:
                        arquivo = open(nome_arquivo, 'r+')
                    except FileNotFoundError:
                        arquivo = open(nome_arquivo, 'w+')
                        arquivo.write('Relatorio criado dia ' + str(hoje))
                        arquivo.write(f'\nEste documento e referente a entrada das luvas durante o servico do dia {data} e ira ser utilizado na empresa de construcao civil, neste relatorio informa que devera ser acompanhado o uso corretamente durante o tempo que estiver em uso observando as medidas gerais de disciplina e uso que integra a NR-06 Equipamento de Protecao Individua - EPI- da portaria n, 3.214 de 08 de Jun. de 1970. ponto foi realizado atraves de uma tag embutida no equipamento que possui a tecnologia RFID')
                        arquivo.write('' + n_fun)
                        arquivo.write('\n \nTabela de entrada das luvas:\n')
                        arquivo.writelines('')
                        for epis in epi:
                            epis = str(
                                f"Entrada: {epis[0]} \nID da luva: {epis[1]}\nNome: {epis[2]} \nNome do Funcionario: {epis[3]} \nFuncao: {epis[4]} \nData: {epis[5]} \nHora: {epis[6]} \n\n----------------------------------------------------------------")
                            arquivo.write("\n%s\n" % epis)

                rela_en_epi = tkinter.Toplevel()

                rela_en_epi.geometry("950x534")
                rela_en_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    rela_en_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/rela_en_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/rela_en_epi/img0.png")
                b0 = Button(rela_en_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_clicked,
                            relief="flat")

                b0.place(
                    x=322, y=436,
                    width=306,
                    height=71)

                entry0_img = PhotoImage(file=f"Imagens/rela_en_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    285.0, 267.0,
                    image=entry0_img)

                entry0 = Entry(rela_en_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry0.place(
                    x=95, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/rela_en_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    285.0, 368.0,
                    image=entry1_img)

                entry1 = Entry(rela_en_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry1.place(
                    x=95, y=349,
                    width=380,
                    height=36)

                rela_en_epi.resizable(False, False)
                rela_en_epi.title("Entrada")
                rela_en_epi.mainloop()
                print("2")

            def btn_col():
                def btn_clicked():
                    data = entry0.get()
                    nome = entry1.get()
                    nome_arquivo = nome + ".doc"
                    con = sqlite3.connect('banco.sqlite')
                    cur = con.cursor()
                    hoje = date.today()
                    sql = f"SELECT * FROM entrada_col_epi WHERE data_en_col = '{data}'"
                    cur.execute(sql)
                    epi = cur.fetchall()
                    n_fun = (f'\nEntrou ao total de {len(epi)} coletes no dia {data}\n')
                    con.close()
                    try:
                        arquivo = open(nome_arquivo, 'r+')
                    except FileNotFoundError:
                        arquivo = open(nome_arquivo, 'w+')
                        arquivo.write('Relatorio criado dia ' + str(hoje))
                        arquivo.write(f'\nEste documento e referente a entrada dos coletes durante o servico do dia {data} e ira ser utilizado na empresa de construcao civil, neste relatorio informa que devera ser acompanhado o uso corretamente durante o tempo que estiver em uso observando as medidas gerais de disciplina e uso que integra a NR-06 Equipamento de Protecao Individua - EPI- da portaria n, 3.214 de 08 de Jun. de 1970. ponto foi realizado atraves de uma tag embutida no equipamento que possui a tecnologia RFID')
                        arquivo.write('' + n_fun)
                        arquivo.write('\n \nTabela de entrada dos coletes:\n')
                        arquivo.writelines('')
                        for epis in epi:
                            epis = str(
                                f"Entrada: {epis[0]} \nID do colete: {epis[1]}\nNome: {epis[2]} \nNome do Funcionario: {epis[3]} \nFuncao: {epis[4]} \nData: {epis[5]} \nHora: {epis[6]} \n\n----------------------------------------------------------------")
                            arquivo.write("\n%s\n" % epis)

                rela_en_epi = tkinter.Toplevel()

                rela_en_epi.geometry("950x534")
                rela_en_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    rela_en_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/rela_en_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/rela_en_epi/img0.png")
                b0 = Button(rela_en_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_clicked,
                            relief="flat")

                b0.place(
                    x=322, y=436,
                    width=306,
                    height=71)

                entry0_img = PhotoImage(file=f"Imagens/rela_en_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    285.0, 267.0,
                    image=entry0_img)

                entry0 = Entry(rela_en_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry0.place(
                    x=95, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/rela_en_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    285.0, 368.0,
                    image=entry1_img)

                entry1 = Entry(rela_en_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry1.place(
                    x=95, y=349,
                    width=380,
                    height=36)

                rela_en_epi.resizable(False, False)
                rela_en_epi.title("Entrada")
                rela_en_epi.mainloop()
                print("3")

            def btn_ocu():
                def btn_clicked():
                    data = entry0.get()
                    nome = entry1.get()
                    nome_arquivo = nome + ".doc"
                    con = sqlite3.connect('banco.sqlite')
                    cur = con.cursor()
                    hoje = date.today()
                    sql = f"SELECT * FROM entrada_ocu_epi WHERE data_en_ocu = '{data}'"
                    cur.execute(sql)
                    epi = cur.fetchall()
                    n_fun = (f'\nEntrou ao total de {len(epi)} oculos no dia {data}\n')
                    con.close()
                    try:
                        arquivo = open(nome_arquivo, 'r+')
                    except FileNotFoundError:
                        arquivo = open(nome_arquivo, 'w+')
                        arquivo.write('Relatorio criado dia ' + str(hoje))
                        arquivo.write(f'\nEste documento e referente a entrada dos oculos durante o servico do dia {data} e ira ser utilizado na empresa de construcao civil, neste relatorio informa que devera ser acompanhado o uso corretamente durante o tempo que estiver em uso observando as medidas gerais de disciplina e uso que integra a NR-06 Equipamento de Protecao Individua - EPI- da portaria n, 3.214 de 08 de Jun. de 1970. ponto foi realizado atraves de uma tag embutida no equipamento que possui a tecnologia RFID')
                        arquivo.write('' + n_fun)
                        arquivo.write('\n \nTabela de entrada dos oculos:\n')
                        arquivo.writelines('')
                        for epis in epi:
                            epis = str(
                                f"Entrada: {epis[0]} \nID do oculos: {epis[1]}\nNome: {epis[2]} \nNome do Funcionario: {epis[3]} \nFuncao: {epis[4]} \nData: {epis[5]} \nHora: {epis[6]} \n\n----------------------------------------------------------------")
                            arquivo.write("\n%s\n" % epis)

                rela_en_epi = tkinter.Toplevel()

                rela_en_epi.geometry("950x534")
                rela_en_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    rela_en_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/rela_en_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/rela_en_epi/img0.png")
                b0 = Button(rela_en_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_clicked,
                            relief="flat")

                b0.place(
                    x=322, y=436,
                    width=306,
                    height=71)

                entry0_img = PhotoImage(file=f"Imagens/rela_en_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    285.0, 267.0,
                    image=entry0_img)

                entry0 = Entry(rela_en_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry0.place(
                    x=95, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/rela_en_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    285.0, 368.0,
                    image=entry1_img)

                entry1 = Entry(rela_en_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry1.place(
                    x=95, y=349,
                    width=380,
                    height=36)

                rela_en_epi.resizable(False, False)
                rela_en_epi.title("Entrada")
                rela_en_epi.mainloop()
                print("4")

            def btn_cin():
                def btn_clicked():
                    data = entry0.get()
                    nome = entry1.get()
                    nome_arquivo = nome + ".doc"
                    con = sqlite3.connect('banco.sqlite')
                    cur = con.cursor()
                    hoje = date.today()
                    sql = f"SELECT * FROM entrada_cin_epi WHERE data_en_cin = '{data}'"
                    cur.execute(sql)
                    epi = cur.fetchall()
                    n_fun = (f'\nEntrou ao total de {len(epi)} cinturao no dia {data}\n')
                    con.close()
                    try:
                        arquivo = open(nome_arquivo, 'r+')
                    except FileNotFoundError:
                        arquivo = open(nome_arquivo, 'w+')
                        arquivo.write('Relatorio criado dia ' + str(hoje))
                        arquivo.write(f'\nEste documento e referente a entrada dos cinturoes durante o servico do dia {data} e ira ser utilizado na empresa de construcao civil, neste relatorio informa que devera ser acompanhado o uso corretamente durante o tempo que estiver em uso observando as medidas gerais de disciplina e uso que integra a NR-06 Equipamento de Protecao Individua - EPI- da portaria n, 3.214 de 08 de Jun. de 1970. ponto foi realizado atraves de uma tag embutida no equipamento que possui a tecnologia RFID')
                        arquivo.write('' + n_fun)
                        arquivo.write('\n \nTabela de entrada dos cinturao:\n')
                        arquivo.writelines('')
                        for epis in epi:
                            epis = str(
                                f"Entrada: {epis[0]} \nID do cinturao: {epis[1]}\nNome: {epis[2]} \nNome do Funcionario: {epis[3]} \nFuncao: {epis[4]} \nData: {epis[5]} \nHora: {epis[6]} \n\n----------------------------------------------------------------")
                            arquivo.write("\n%s\n" % epis)

                rela_en_epi = tkinter.Toplevel()

                rela_en_epi.geometry("950x534")
                rela_en_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    rela_en_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/rela_en_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/rela_en_epi/img0.png")
                b0 = Button(rela_en_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_clicked,
                            relief="flat")

                b0.place(
                    x=322, y=436,
                    width=306,
                    height=71)

                entry0_img = PhotoImage(file=f"Imagens/rela_en_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    285.0, 267.0,
                    image=entry0_img)

                entry0 = Entry(rela_en_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry0.place(
                    x=95, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/rela_en_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    285.0, 368.0,
                    image=entry1_img)

                entry1 = Entry(rela_en_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry1.place(
                    x=95, y=349,
                    width=380,
                    height=36)

                rela_en_epi.resizable(False, False)
                rela_en_epi.title("Entrada")
                rela_en_epi.mainloop()
                print("5")

            def btn_mas():
                def btn_clicked():
                    data = entry0.get()
                    nome = entry1.get()
                    nome_arquivo = nome + ".doc"
                    con = sqlite3.connect('banco.sqlite')
                    cur = con.cursor()
                    hoje = date.today()
                    sql = f"SELECT * FROM entrada_masc_epi WHERE data_en_masc = '{data}'"
                    cur.execute(sql)
                    epi = cur.fetchall()
                    n_fun = (f'\nEntrou ao total de {len(epi)} mascaras no dia {data}\n')
                    con.close()
                    try:
                        arquivo = open(nome_arquivo, 'r+')
                    except FileNotFoundError:
                        arquivo = open(nome_arquivo, 'w+')
                        arquivo.write('Relatorio criado dia ' + str(hoje))
                        arquivo.write(f'\nEste documento e referente a entrada das mascaras durante o servico do dia {data} e ira ser utilizado na empresa de construcao civil, neste relatorio informa que devera ser acompanhado o uso corretamente durante o tempo que estiver em uso observando as medidas gerais de disciplina e uso que integra a NR-06 Equipamento de Protecao Individua - EPI- da portaria n, 3.214 de 08 de Jun. de 1970. ponto foi realizado atraves de uma tag embutida no equipamento que possui a tecnologia RFID')
                        arquivo.write('' + n_fun)
                        arquivo.write('\n \nTabela de entrada dos mascaras:\n')
                        arquivo.writelines('')
                        for epis in epi:
                            epis = str(
                                f"Entrada: {epis[0]} \nID do mascaras: {epis[1]}\nNome: {epis[2]} \nNome do Funcionario: {epis[3]} \nFuncao: {epis[4]} \nData: {epis[5]} \nHora: {epis[6]} \n\n----------------------------------------------------------------")
                            arquivo.write("\n%s\n" % epis)

                rela_en_epi = tkinter.Toplevel()

                rela_en_epi.geometry("950x534")
                rela_en_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    rela_en_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/rela_en_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/rela_en_epi/img0.png")
                b0 = Button(rela_en_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_clicked,
                            relief="flat")

                b0.place(
                    x=322, y=436,
                    width=306,
                    height=71)

                entry0_img = PhotoImage(file=f"Imagens/rela_en_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    285.0, 267.0,
                    image=entry0_img)

                entry0 = Entry(rela_en_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry0.place(
                    x=95, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/rela_en_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    285.0, 368.0,
                    image=entry1_img)

                entry1 = Entry(rela_en_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry1.place(
                    x=95, y=349,
                    width=380,
                    height=36)

                rela_en_epi.resizable(False, False)
                rela_en_epi.title("Entrada")
                rela_en_epi.mainloop()
                print("6")

            m_re_en_epi = tkinter.Toplevel()

            m_re_en_epi.geometry("950x534")
            m_re_en_epi.configure(bg="#ffffff")
            canvas = Canvas(
                m_re_en_epi,
                bg="#ffffff",
                height=534,
                width=950,
                bd=0,
                highlightthickness=0,
                relief="ridge")
            canvas.place(x=0, y=0)

            background_img = PhotoImage(file=f"Imagens/m_rela_en_epi/background.png")
            background = canvas.create_image(
                475.0, 267.0,
                image=background_img)

            img0 = PhotoImage(file=f"Imagens/m_rela_en_epi/img0.png")
            b0 = Button(m_re_en_epi,
                        image=img0,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_cap,
                        relief="flat")

            b0.place(
                x=18, y=136,
                width=243,
                height=100)

            img1 = PhotoImage(file=f"Imagens/m_rela_en_epi/img1.png")
            b1 = Button(m_re_en_epi,
                        image=img1,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_luv,
                        relief="flat")

            b1.place(
                x=315, y=136,
                width=243,
                height=100)

            img2 = PhotoImage(file=f"Imagens/m_rela_en_epi/img2.png")
            b2 = Button(m_re_en_epi,
                        image=img2,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_col,
                        relief="flat")

            b2.place(
                x=18, y=267,
                width=243,
                height=100)

            img3 = PhotoImage(file=f"Imagens/m_rela_en_epi/img3.png")
            b3 = Button(m_re_en_epi,
                        image=img3,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_ocu,
                        relief="flat")

            b3.place(
                x=315, y=267,
                width=243,
                height=100)

            img4 = PhotoImage(file=f"Imagens/m_rela_en_epi/img4.png")
            b4 = Button(m_re_en_epi,
                        image=img4,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_cin,
                        relief="flat")

            b4.place(
                x=18, y=398,
                width=243,
                height=100)

            img5 = PhotoImage(file=f"Imagens/m_rela_en_epi/img5.png")
            b5 = Button(m_re_en_epi,
                        image=img5,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_mas,
                        relief="flat")

            b5.place(
                x=315, y=398,
                width=243,
                height=100)

            m_re_en_epi.resizable(False, False)
            m_re_en_epi.title("Menu entrada EPI")
            m_re_en_epi.mainloop()

        def btn_m_sa_epi():
            def btn_cap():
                def btn_clicked():
                    data = entry0.get()
                    nome = entry1.get()
                    nome_arquivo = nome + ".doc"
                    con = sqlite3.connect('banco.sqlite')
                    cur = con.cursor()
                    hoje = date.today()
                    sql = f"SELECT * FROM saida_cap_epi WHERE data_sa_cap = '{data}'"
                    cur.execute(sql)
                    epi = cur.fetchall()
                    n_fun = (f'\nSaiu ao total de {len(epi)} capacetes no dia {data}\n')
                    con.close()
                    try:
                        arquivo = open(nome_arquivo, 'r+')
                    except FileNotFoundError:
                        arquivo = open(nome_arquivo, 'w+')
                        arquivo.write('Relatorio criado dia ' + str(hoje))
                        arquivo.write(f'Este documento e referente a saida dos capacetes durante o servico do dia {data} e foi utilizado na empresa de construcao civil, neste relatorio informa que foi utilizado corretamente durante o tempo que permaneceu observando as medidas gerais de disciplina e uso que integra a NR-06 Equipamento de Protecao Individua - EPI- da portaria n, 3.214 de 08 de Jun. de 1970. ponto foi realizado atraves de uma tag embutida no equipamento que possui a tecnologia RFID')
                        arquivo.write('' + n_fun)
                        arquivo.write('\n \nTabela de saida dos capacetes:\n')
                        arquivo.writelines('')
                        for epis in epi:
                            epis = str(
                                f"Saida: {epis[0]} \nID do capacete: {epis[1]}\nNome: {epis[2]} \nNome do Funcionario: {epis[3]} \nFuncao: {epis[4]} \nData: {epis[5]} \nHora: {epis[6]} \n\n----------------------------------------------------------------")
                            arquivo.write("\n%s\n" % epis)
                        arquivo.write('----------------------------------------------------------------')
                        arquivo.write('                      Assinatura Responsavel                    ')

                rela_sa_epi = tkinter.Toplevel()

                rela_sa_epi.geometry("950x534")
                rela_sa_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    rela_sa_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/rela_sa_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/rela_sa_epi/img0.png")
                b0 = Button(rela_sa_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_clicked,
                            relief="flat")

                b0.place(
                    x=322, y=436,
                    width=306,
                    height=71)

                entry0_img = PhotoImage(file=f"Imagens/rela_sa_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    285.0, 267.0,
                    image=entry0_img)

                entry0 = Entry(rela_sa_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry0.place(
                    x=95, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/rela_sa_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    285.0, 368.0,
                    image=entry1_img)

                entry1 = Entry(rela_sa_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry1.place(
                    x=95, y=349,
                    width=380,
                    height=36)

                rela_sa_epi.resizable(False, False)
                rela_sa_epi.title("saida de epi")
                rela_sa_epi.mainloop()

            def btn_luv():
                def btn_clicked():
                    data = entry0.get()
                    nome = entry1.get()
                    nome_arquivo = nome + ".doc"
                    con = sqlite3.connect('banco.sqlite')
                    cur = con.cursor()
                    hoje = date.today()
                    sql = f"SELECT * FROM saida_luva_epi WHERE data_sa_luva = '{data}'"
                    cur.execute(sql)
                    epi = cur.fetchall()
                    n_fun = (f'\nSaiu ao total de {len(epi)} Luvas no dia {data}\n')
                    con.close()
                    try:
                        arquivo = open(nome_arquivo, 'r+')
                    except FileNotFoundError:
                        arquivo = open(nome_arquivo, 'w+')
                        arquivo.write('Relatorio criado dia ' + str(hoje))
                        arquivo.write(f'\nEste documento e referente a saida das Luvas durante o servico do dia {data} e foi utilizado na empresa de construcao civil, neste relatorio informa que foi utilizado corretamente durante o tempo que permaneceu observando as medidas gerais de disciplina e uso que integra a NR-06 Equipamento de Protecao Individua - EPI- da portaria n, 3.214 de 08 de Jun. de 1970. ponto foi realizado atraves de uma tag embutida no equipamento que possui a tecnologia RFID')
                        arquivo.write('' + n_fun)
                        arquivo.write('\n \nTabela de saida das luvas:\n')
                        arquivo.writelines('')
                        for epis in epi:
                            epis = str(
                                f"Saida: {epis[0]} \nID da luva: {epis[1]}\nNome: {epis[2]} \nNome do Funcionario: {epis[3]} \nFuncao: {epis[4]} \nData: {epis[5]} \nHora: {epis[6]} \n\n----------------------------------------------------------------")
                            arquivo.write("\n%s\n" % epis)

                rela_sa_epi = tkinter.Toplevel()

                rela_sa_epi.geometry("950x534")
                rela_sa_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    rela_sa_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/rela_sa_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/rela_sa_epi/img0.png")
                b0 = Button(rela_sa_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_clicked,
                            relief="flat")

                b0.place(
                    x=322, y=436,
                    width=306,
                    height=71)

                entry0_img = PhotoImage(file=f"Imagens/rela_sa_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    285.0, 267.0,
                    image=entry0_img)

                entry0 = Entry(rela_sa_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry0.place(
                    x=95, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/rela_sa_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    285.0, 368.0,
                    image=entry1_img)

                entry1 = Entry(rela_sa_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry1.place(
                    x=95, y=349,
                    width=380,
                    height=36)

                rela_sa_epi.resizable(False, False)
                rela_sa_epi.title("saida de epi")
                rela_sa_epi.mainloop()

            def btn_col():
                def btn_clicked():
                    data = entry0.get()
                    nome = entry1.get()
                    nome_arquivo = nome + ".doc"
                    con = sqlite3.connect('banco.sqlite')
                    cur = con.cursor()
                    hoje = date.today()
                    sql = f"SELECT * FROM saida_col_epi WHERE data_sa_col = '{data}'"
                    cur.execute(sql)
                    epi = cur.fetchall()
                    n_fun = (f'\nSaiu ao total de {len(epi)} coletes no dia {data}\n')
                    con.close()
                    try:
                        arquivo = open(nome_arquivo, 'r+')
                    except FileNotFoundError:
                        arquivo = open(nome_arquivo, 'w+')
                        arquivo.write('Relatorio criado dia ' + str(hoje))
                        arquivo.write(f'\nEste documento e referente a saida dos coletes durante o servico do dia {data} e foi utilizado na empresa de construcao civil, neste relatorio informa que foi utilizado corretamente durante o tempo que permaneceu observando as medidas gerais de disciplina e uso que integra a NR-06 Equipamento de Protecao Individua - EPI- da portaria n, 3.214 de 08 de Jun. de 1970. ponto foi realizado atraves de uma tag embutida no equipamento que possui a tecnologia RFID')
                        arquivo.write('' + n_fun)
                        arquivo.write('\n \nTabela de saida dos coletes:\n')
                        arquivo.writelines('')
                        for epis in epi:
                            epis = str(
                                f"Saida: {epis[0]} \nID do colete: {epis[1]}\nNome: {epis[2]} \nNome do Funcionario: {epis[3]} \nFuncao: {epis[4]} \nData: {epis[5]} \nHora: {epis[6]} \n\n----------------------------------------------------------------")
                            arquivo.write("\n%s\n" % epis)

                rela_sa_epi = tkinter.Toplevel()

                rela_sa_epi.geometry("950x534")
                rela_sa_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    rela_sa_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/rela_sa_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/rela_sa_epi/img0.png")
                b0 = Button(rela_sa_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_clicked,
                            relief="flat")

                b0.place(
                    x=322, y=436,
                    width=306,
                    height=71)

                entry0_img = PhotoImage(file=f"Imagens/rela_sa_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    285.0, 267.0,
                    image=entry0_img)

                entry0 = Entry(rela_sa_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry0.place(
                    x=95, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/rela_sa_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    285.0, 368.0,
                    image=entry1_img)

                entry1 = Entry(rela_sa_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry1.place(
                    x=95, y=349,
                    width=380,
                    height=36)

                rela_sa_epi.resizable(False, False)
                rela_sa_epi.title("saida de epi")
                rela_sa_epi.mainloop()

            def btn_ocu():
                def btn_clicked():
                    data = entry0.get()
                    nome = entry1.get()
                    nome_arquivo = nome + ".doc"
                    con = sqlite3.connect('banco.sqlite')
                    cur = con.cursor()
                    hoje = date.today()
                    sql = f"SELECT * FROM saida_ocu_epi WHERE data_sa_ocu = '{data}'"
                    cur.execute(sql)
                    epi = cur.fetchall()
                    n_fun = (f'\nSaiu ao total de {len(epi)} oculos no dia {data}\n')
                    con.close()
                    try:
                        arquivo = open(nome_arquivo, 'r+')
                    except FileNotFoundError:
                        arquivo = open(nome_arquivo, 'w+')
                        arquivo.write('Relatorio criado dia ' + str(hoje))
                        arquivo.write(f'\nEste documento e referente a saida dos oculos durante o servico do dia {data} e foi utilizado na empresa de construcao civil, neste relatorio informa que foi utilizado corretamente durante o tempo que permaneceu observando as medidas gerais de disciplina e uso que integra a NR-06 Equipamento de Protecao Individua - EPI- da portaria n, 3.214 de 08 de Jun. de 1970. ponto foi realizado atraves de uma tag embutida no equipamento que possui a tecnologia RFID')
                        arquivo.write('' + n_fun)
                        arquivo.write('\n \nTabela de saida dos oculos:\n')
                        arquivo.writelines('')
                        for epis in epi:
                            epis = str(
                                f"Saida: {epis[0]} \nID do oculos: {epis[1]}\nNome: {epis[2]} \nNome do Funcionario: {epis[3]} \nFuncao: {epis[4]} \nData: {epis[5]} \nHora: {epis[6]} \n\n----------------------------------------------------------------")
                            arquivo.write("\n%s\n" % epis)

                rela_sa_epi = tkinter.Toplevel()

                rela_sa_epi.geometry("950x534")
                rela_sa_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    rela_sa_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/rela_sa_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/rela_sa_epi/img0.png")
                b0 = Button(rela_sa_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_clicked,
                            relief="flat")

                b0.place(
                    x=322, y=436,
                    width=306,
                    height=71)

                entry0_img = PhotoImage(file=f"Imagens/rela_sa_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    285.0, 267.0,
                    image=entry0_img)

                entry0 = Entry(rela_sa_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry0.place(
                    x=95, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/rela_sa_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    285.0, 368.0,
                    image=entry1_img)

                entry1 = Entry(rela_sa_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry1.place(
                    x=95, y=349,
                    width=380,
                    height=36)

                rela_sa_epi.resizable(False, False)
                rela_sa_epi.title("saida de epi")
                rela_sa_epi.mainloop()

            def btn_cin():
                def btn_clicked():
                    def btn_clicked():
                        data = entry0.get()
                        nome = entry1.get()
                        nome_arquivo = nome + ".doc"
                        con = sqlite3.connect('banco.sqlite')
                        cur = con.cursor()
                        hoje = date.today()
                        sql = f"SELECT * FROM saida_cin_epi WHERE data_sa_cin = '{data}'"
                        cur.execute(sql)
                        epi = cur.fetchall()
                        n_fun = (f'\nSaiu ao total de {len(epi)} cinturao no dia {data}\n')
                        con.close()
                        try:
                            arquivo = open(nome_arquivo, 'r+')
                        except FileNotFoundError:
                            arquivo = open(nome_arquivo, 'w+')
                            arquivo.write('Relatorio criado dia ' + str(hoje))
                            arquivo.write(f'\nEste documento e referente a saida dos cinturao durante o servico do dia {data} e foi utilizado na empresa de construcao civil, neste relatorio informa que foi utilizado corretamente durante o tempo que permaneceu observando as medidas gerais de disciplina e uso que integra a NR-06 Equipamento de Protecao Individua - EPI- da portaria n, 3.214 de 08 de Jun. de 1970. ponto foi realizado atraves de uma tag embutida no equipamento que possui a tecnologia RFID')
                            arquivo.write('' + n_fun)
                            arquivo.write('\n \nTabela de saida dos cinturao:\n')
                            arquivo.writelines('')
                            for epis in epi:
                                epis = str(
                                    f"Saida: {epis[0]} \nID do cinturao: {epis[1]}\nNome: {epis[2]} \nNome do Funcionario: {epis[3]} \nFuncao: {epis[4]} \nData: {epis[5]} \nHora: {epis[6]} \n\n----------------------------------------------------------------")
                                arquivo.write("\n%s\n" % epis)

                rela_sa_epi = tkinter.Toplevel()

                rela_sa_epi.geometry("950x534")
                rela_sa_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    rela_sa_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/rela_sa_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/rela_sa_epi/img0.png")
                b0 = Button(rela_sa_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_clicked,
                            relief="flat")

                b0.place(
                    x=322, y=436,
                    width=306,
                    height=71)

                entry0_img = PhotoImage(file=f"Imagens/rela_sa_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    285.0, 267.0,
                    image=entry0_img)

                entry0 = Entry(rela_sa_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry0.place(
                    x=95, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/rela_sa_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    285.0, 368.0,
                    image=entry1_img)

                entry1 = Entry(rela_sa_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry1.place(
                    x=95, y=349,
                    width=380,
                    height=36)

                rela_sa_epi.resizable(False, False)
                rela_sa_epi.title("saida de epi")
                rela_sa_epi.mainloop()

            def btn_mas():
                def btn_clicked():
                    data = entry0.get()
                    nome = entry1.get()
                    nome_arquivo = nome + ".doc"
                    con = sqlite3.connect('banco.sqlite')
                    cur = con.cursor()
                    hoje = date.today()
                    sql = f"SELECT * FROM saida_masc_epi WHERE data_sa_masc = '{data}'"
                    cur.execute(sql)
                    epi = cur.fetchall()
                    n_fun = (f'\nSaiu ao total de {len(epi)} mascaras no dia {data}\n')
                    con.close()
                    try:
                        arquivo = open(nome_arquivo, 'r+')
                    except FileNotFoundError:
                        arquivo = open(nome_arquivo, 'w+')
                        arquivo.write('Relatorio criado dia ' + str(hoje))
                        arquivo.write(f'\nEste documento e referente a saida das mascaras durante o servico do dia {data} e foi utilizado na empresa de construcao civil, neste relatorio informa que foi utilizado corretamente durante o tempo que permaneceu observando as medidas gerais de disciplina e uso que integra a NR-06 Equipamento de Protecao Individua - EPI- da portaria n, 3.214 de 08 de Jun. de 1970. ponto foi realizado atraves de uma tag embutida no equipamento que possui a tecnologia RFID')
                        arquivo.write('' + n_fun)
                        arquivo.write('\n \nTabela de saida dos mascaras:\n')
                        arquivo.writelines('')
                        for epis in epi:
                            epis = str(
                                f"Saiu: {epis[0]} \nID do mascaras: {epis[1]}\nNome: {epis[2]} \nNome do Funcionario: {epis[3]} \nFuncao: {epis[4]} \nData: {epis[5]} \nHora: {epis[6]} \n\n----------------------------------------------------------------")
                            arquivo.write("\n%s\n" % epis)

                rela_sa_epi = tkinter.Toplevel()

                rela_sa_epi.geometry("950x534")
                rela_sa_epi.configure(bg="#ffffff")
                canvas = Canvas(
                    rela_sa_epi,
                    bg="#ffffff",
                    height=534,
                    width=950,
                    bd=0,
                    highlightthickness=0,
                    relief="ridge")
                canvas.place(x=0, y=0)

                background_img = PhotoImage(file=f"Imagens/rela_sa_epi/background.png")
                background = canvas.create_image(
                    475.0, 267.0,
                    image=background_img)

                img0 = PhotoImage(file=f"Imagens/rela_sa_epi/img0.png")
                b0 = Button(rela_sa_epi,
                            image=img0,
                            borderwidth=0,
                            highlightthickness=0,
                            command=btn_clicked,
                            relief="flat")

                b0.place(
                    x=322, y=436,
                    width=306,
                    height=71)

                entry0_img = PhotoImage(file=f"Imagens/rela_sa_epi/img_textBox0.png")
                entry0_bg = canvas.create_image(
                    285.0, 267.0,
                    image=entry0_img)

                entry0 = Entry(rela_sa_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry0.place(
                    x=95, y=248,
                    width=380,
                    height=36)

                entry1_img = PhotoImage(file=f"Imagens/rela_sa_epi/img_textBox1.png")
                entry1_bg = canvas.create_image(
                    285.0, 368.0,
                    image=entry1_img)

                entry1 = Entry(rela_sa_epi,
                               bd=0,
                               bg="#c4c4c4",
                               highlightthickness=0)

                entry1.place(
                    x=95, y=349,
                    width=380,
                    height=36)

                rela_sa_epi.resizable(False, False)
                rela_sa_epi.title("saida de epi")
                rela_sa_epi.mainloop()

            m_re_sa_epi = tkinter.Toplevel()

            m_re_sa_epi.geometry("950x534")
            m_re_sa_epi.configure(bg="#ffffff")
            canvas = Canvas(
                m_re_sa_epi,
                bg="#ffffff",
                height=534,
                width=950,
                bd=0,
                highlightthickness=0,
                relief="ridge")
            canvas.place(x=0, y=0)

            background_img = PhotoImage(file=f"Imagens/m_rela_sa_epi/background.png")
            background = canvas.create_image(
                475.0, 267.0,
                image=background_img)

            img0 = PhotoImage(file=f"Imagens/m_rela_sa_epi/img0.png")
            b0 = Button(m_re_sa_epi,
                        image=img0,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_cap,
                        relief="flat")

            b0.place(
                x=18, y=136,
                width=243,
                height=100)

            img1 = PhotoImage(file=f"Imagens/m_rela_sa_epi/img1.png")
            b1 = Button(m_re_sa_epi,
                        image=img1,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_luv,
                        relief="flat")

            b1.place(
                x=315, y=136,
                width=243,
                height=100)

            img2 = PhotoImage(file=f"Imagens/m_rela_sa_epi/img2.png")
            b2 = Button(m_re_sa_epi,
                        image=img2,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_col,
                        relief="flat")

            b2.place(
                x=18, y=267,
                width=243,
                height=100)

            img3 = PhotoImage(file=f"Imagens/m_rela_sa_epi/img3.png")
            b3 = Button(m_re_sa_epi,
                        image=img3,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_ocu,
                        relief="flat")

            b3.place(
                x=315, y=267,
                width=243,
                height=100)

            img4 = PhotoImage(file=f"Imagens/m_rela_sa_epi/img4.png")
            b4 = Button(m_re_sa_epi,
                        image=img4,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_cin,
                        relief="flat")

            b4.place(
                x=18, y=398,
                width=243,
                height=100)

            img5 = PhotoImage(file=f"Imagens/m_rela_sa_epi/img5.png")
            b5 = Button(m_re_sa_epi,
                        image=img5,
                        borderwidth=0,
                        highlightthickness=0,
                        command=btn_mas,
                        relief="flat")

            b5.place(
                x=315, y=398,
                width=243,
                height=100)

            m_re_sa_epi.resizable(False, False)
            m_re_sa_epi.title("Menu saida EPI")
            m_re_sa_epi.mainloop()

            print("4")

        m_relatorio = tkinter.Toplevel()

        m_relatorio.geometry("950x534")
        m_relatorio.configure(bg="#ffffff")
        canvas = Canvas(
            m_relatorio,
            bg="#ffffff",
            height=534,
            width=950,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"Imagens/m_rela/background.png")
        background = canvas.create_image(
            475.0, 267.0,
            image=background_img)

        img0 = PhotoImage(file=f"Imagens/m_rela/img0.png")
        b0 = Button(m_relatorio,
                    image=img0,
                    borderwidth=0,
                    highlightthickness=0,
                    command=btn_en_fun,
                    relief="flat")

        b0.place(
            x=51, y=136,
            width=368,
            height=151)

        img1 = PhotoImage(file=f"Imagens/m_rela/img1.png")
        b1 = Button(m_relatorio,
                    image=img1,
                    borderwidth=0,
                    highlightthickness=0,
                    command=btn_sa_fun,
                    relief="flat")

        b1.place(
            x=51, y=336,
            width=368,
            height=151)

        img2 = PhotoImage(file=f"Imagens/m_rela/img2.png")
        b2 = Button(m_relatorio,
                    image=img2,
                    borderwidth=0,
                    highlightthickness=0,
                    command=btn_m_en_epi,
                    relief="flat")

        b2.place(
            x=535, y=136,
            width=368,
            height=151)

        img3 = PhotoImage(file=f"Imagens/m_rela/img3.png")
        b3 = Button(m_relatorio,
                    image=img3,
                    borderwidth=0,
                    highlightthickness=0,
                    command=btn_m_sa_epi,
                    relief="flat")

        b3.place(
            x=535, y=336,
            width=368,
            height=151)

        m_relatorio.resizable(False, False)
        m_relatorio.title("Menu relatorio")
        m_relatorio.mainloop()

    def btn_sistema():
        info_sis = tkinter.Toplevel()

        info_sis.geometry("950x534")
        info_sis.configure(bg="#ffffff")
        canvas = Canvas(
            info_sis,
            bg="#ffffff",
            height=534,
            width=950,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"Imagens/info/background.png")
        background = canvas.create_image(
            475.0, 267.0,
            image=background_img)

        info_sis.resizable(False, False)
        info_sis.title("Informacoes do sistema")
        info_sis.mainloop()

    def btn_cad_adm():

        def salvar():
            con = sqlite3.connect('banco_adm.sqlite')
            cur = con.cursor()
            sql = 'INSERT INTO fun_adm (nome_funcionario, senha_funcionario) VALUES (?, ?)'
            cur.execute(sql, (entry_login.get(), entry_senha.get()))
            con.commit()
            con.close()
            cad_admi.destroy()
            print("cadastrado")

        cad_admi = tkinter.Toplevel()

        cad_admi.geometry("950x534")
        cad_admi.configure(bg="#ffffff")
        canvas = Canvas(
            cad_admi,
            bg="#ffffff",
            height=534,
            width=950,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"Imagens/cad_adm/background.png")
        background = canvas.create_image(
            475.0, 267.0,
            image=background_img)

        img0 = PhotoImage(file=f"Imagens/cad_adm/img0.png")
        b0 = Button(cad_admi,
                    image=img0,
                    borderwidth=0,
                    highlightthickness=0,
                    command=salvar,
                    relief="flat")

        b0.place(
            x=322, y=436,
            width=306,
            height=71)

        entry0_img = PhotoImage(file=f"Imagens/cad_adm/img_textBox0.png")
        entry0_bg = canvas.create_image(
            307.0, 188.0,
            image=entry0_img)

        entry_login = Entry(cad_admi,
                            bd=0,
                            bg="#c4c4c4",
                            highlightthickness=0)

        entry_login.place(
            x=117, y=169,
            width=380,
            height=36)

        entry1_img = PhotoImage(file=f"Imagens/cad_adm/img_textBox1.png")
        entry1_bg = canvas.create_image(
            307.0, 267.0,
            image=entry1_img)

        entry_senha = Entry(cad_admi,
                            bd=0,
                            bg="#c4c4c4",
                            highlightthickness=0)

        entry_senha.place(
            x=117, y=248,
            width=380,
            height=36)

        cad_admi.resizable(False, False)
        cad_admi.title("Cadastro do sistema")
        cad_admi.mainloop()
        print("4")

    def btn_info():

        def btn_fun():
            nome = entry0_fun.get()
            nome_arquivo = nome + ".doc"
            con = sqlite3.connect('banco.sqlite')
            cur = con.cursor()
            hoje = date.today()
            sql = 'SELECT * FROM funcionario'
            cur.execute(sql)
            funcionario = cur.fetchall()
            n_fun = (f'\nA empresa possui o total de {len(funcionario)} funcionarios\n')
            con.close()
            try:
                arquivo = open(nome_arquivo, 'r+')
            except FileNotFoundError:
                arquivo = open(nome_arquivo, 'w+')
                arquivo.write('Relatorio criado dia ' + str(hoje))
                arquivo.write('' + n_fun)
                arquivo.write('\n \nTabela dos funcionarios:')
                arquivo.writelines('')
                for funcionarios in funcionario:
                    funcionarios = str(f"ID: {funcionarios[0]} \nNome: {funcionarios[1]} \nCPF: {funcionarios[2]} \nFuncao: {funcionarios[3]} \n\n----------------------------------------------------------------")
                    arquivo.write("\n%s\n" % funcionarios)

                arquivo.close()

        def btn_epi():
            nome = entry1_epi.get()
            nome_arquivo = nome + ".doc"
            con = sqlite3.connect('banco.sqlite')
            cur = con.cursor()
            hoje = date.today()
            sql1 = 'SELECT * FROM Capacete_EPI'
            cur.execute(sql1)
            Cap = cur.fetchall()
            n_cap = (f'\nA empresa possui o total de {len(Cap)} Capacetes\n')
            con.close()

            con = sqlite3.connect('banco.sqlite')
            cur = con.cursor()
            sql2 = 'SELECT * FROM Colete_EPI'
            cur.execute(sql2)
            Col = cur.fetchall()
            n_col = (f'\nA empresa possui o total de {len(Col)} Coletes\n')
            con.close()

            con = sqlite3.connect('banco.sqlite')
            cur = con.cursor()
            sql3 = 'SELECT * FROM Oculos_EPI'
            cur.execute(sql3)
            Ocu = cur.fetchall()
            n_ocu = (f'\nA empresa possui o total de {len(Ocu)} Oculos\n')
            con.close()

            con = sqlite3.connect('banco.sqlite')
            cur = con.cursor()
            sql3 = 'SELECT * FROM Luva_EPI'
            cur.execute(sql3)
            luva = cur.fetchall()
            n_luva = (f'\nA empresa possui o total de {len(luva)} Luvas\n')
            con.close()

            con = sqlite3.connect('banco.sqlite')
            cur = con.cursor()
            sql3 = 'SELECT * FROM Cinturao_EPI'
            cur.execute(sql3)
            Cin = cur.fetchall()
            n_cin = (f'\nA empresa possui o total de {len(Cin)} Cinturao\n')
            con.close()

            con = sqlite3.connect('banco.sqlite')
            cur = con.cursor()
            sql3 = 'SELECT * FROM Mascara_EPI'
            cur.execute(sql3)
            masc = cur.fetchall()
            n_masc = (f'\nA empresa possui o total de {len(masc)} mascara\n')
            con.close()

            try:
                arquivo = open(nome_arquivo, 'r+')
            except FileNotFoundError:
                arquivo = open(nome_arquivo, 'w+')
                arquivo.write('Relatorio criado dia ' + str(hoje))
                arquivo.write('\n \n' + n_cap)
                arquivo.write('\nTabela dos Capacetes:')
                arquivo.writelines('')
                for capacete in Cap:
                    capacet = str(f"ID:{capacete[0]} \nCA:{capacete[1]} \nNome:{capacete[2]} \nFabricante:{capacete[3]} \nProtecao:{capacete[4]} \nFuncao:{capacete[5]} \nValidade{capacete[6]}\n\n----------------------------------------------------------------")
                    arquivo.write("\n%s\n" % capacet)

                arquivo.write('\n\n\n\n' + n_col)
                arquivo.write('\nTabela dos Coletes:')
                arquivo.writelines('')
                for coletes in Col:
                    colete = str(f"ID:{coletes[0]} \nCA:{coletes[1]} \nNome:{coletes[2]} \nFabricante:{coletes[3]} \nProtecao:{coletes[4]} \nFuncao:{coletes[5]} \nValidade{coletes[6]}\n\n----------------------------------------------------------------")
                    arquivo.write("\n%s\n" % colete)

                arquivo.write('\n\n\n\n' + n_ocu)
                arquivo.write('\nTabela dos Oculos:')
                arquivo.writelines('')
                for oculos in Ocu:
                    oculo = str(f"ID:{oculos[0]} \nCA:{oculos[1]} \nNome:{oculos[2]} \nFabricante:{oculos[3]} \nProtecao:{oculos[4]} \nFuncao:{oculos[5]} \nValidade{oculos[6]}\n\n----------------------------------------------------------------")
                    arquivo.write("\n%s\n" % oculo)

                arquivo.write('\n\n\n\n' + n_luva)
                arquivo.write('\nTabela das Luvas:')
                arquivo.writelines('')
                for luvas in luva:
                    luv = str(f"ID:{luvas[0]} \nCA:{luvas[1]} \nNome:{luvas[2]} \nFabricante:{luvas[3]} \nProtecao:{luvas[4]} \nFuncao:{luvas[5]} \nValidade{luvas[6]}\n\n----------------------------------------------------------------")
                    arquivo.write("\n%s\n" % luv)

                arquivo.write('\n\n\n\n' + n_cin)
                arquivo.write('\nTabela das Cinturoes:')
                arquivo.writelines('')
                for cinturoes in Cin:
                    cinturoe = str(f"ID:{cinturoes[0]} \nCA:{cinturoes[1]} \nNome:{cinturoes[2]} \nFabricante:{cinturoes[3]} \nProtecao:{cinturoes[4]} \nFuncao:{cinturoes[5]} \nValidade{cinturoes[6]}\n\n----------------------------------------------------------------")
                    arquivo.write("\n%s\n" % cinturoe)

                arquivo.write('\n\n\n\n' + n_masc)
                arquivo.write('\nTabela das Mascaras:')
                arquivo.writelines('')
                for mascaras in masc:
                    mascara = str(f"ID:{mascaras[0]} \nCA:{mascaras[1]} \nNome:{mascaras[2]} \nFabricante:{mascaras[3]} \nProtecao:{mascaras[4]} \nFuncao:{mascaras[5]} \nValidade{mascaras[6]}\n\n----------------------------------------------------------------")
                    arquivo.write("\n%s\n" % mascara)

                arquivo.close()

        info_f_e = tkinter.Toplevel()

        info_f_e.geometry("950x534")
        info_f_e.configure(bg="#ffffff")
        canvas = Canvas(
            info_f_e,
            bg="#ffffff",
            height=534,
            width=950,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"Imagens/info_fun_epi/background.png")
        background = canvas.create_image(
            475.0, 267.0,
            image=background_img)

        img0 = PhotoImage(file=f"Imagens/info_fun_epi/img0.png")
        b0 = Button(info_f_e,
                    image=img0,
                    borderwidth=0,
                    highlightthickness=0,
                    command=btn_epi,
                    relief="flat")

        b0.place(
            x=630, y=311,
            width=205,
            height=89)

        img1 = PhotoImage(file=f"Imagens/info_fun_epi/img1.png")
        b1 = Button(info_f_e,
                    image=img1,
                    borderwidth=0,
                    highlightthickness=0,
                    command=btn_fun,
                    relief="flat")

        b1.place(
            x=120, y=311,
            width=205,
            height=89)

        entry0_img = PhotoImage(file=f"Imagens/info_fun_epi/img_textBox0.png")
        entry0_bg = canvas.create_image(
            223.0, 267.0,
            image=entry0_img)

        entry0_fun = Entry(info_f_e,
                           bd=0,
                           bg="#c4c4c4",
                           highlightthickness=0)

        entry0_fun.place(
            x=33, y=248,
            width=380,
            height=36)

        entry1_img = PhotoImage(file=f"Imagens/info_fun_epi/img_textBox1.png")
        entry1_bg = canvas.create_image(
            733.0, 267.0,
            image=entry1_img)

        entry1_epi = Entry(info_f_e,
                           bd=0,
                           bg="#c4c4c4",
                           highlightthickness=0)

        entry1_epi.place(
            x=543, y=248,
            width=380,
            height=36)

        info_f_e.resizable(False, False)
        info_f_e.title("Informacoes")
        info_f_e.mainloop()

    def btn_c_banco():
        def btn_clicked():
            def conexao():
                return sqlite3.connect('banco.sqlite')

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS funcionario 
                (
                    id_funcionario  INTEGER PRIMARY KEY, 
                    nome    TEXT    NOT NULL,
                    CPF     INTEGER NOT NULL, 
                    Funcao  TEXT    NOT NULL
                )
            ''')

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS Capacete_EPI
                (
                    id_cap_EPI  INTEGER PRIMARY KEY,
                    CA_cap   INTEGER   NOT NULL,
                    nome_cap  TEXT    NOT NULL,
                    fabricante_cap   TEXT  NOT NULL,
                    protecao_cap   TEXT  NOT NULL,
                    funcao_cap TEXT    NOT NULL,
                    validade_cap  DATE    NOT NULL
                )
            ''')

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS Colete_EPI
                (
                    id_col_EPI  INTEGER PRIMARY KEY,
                    CA_col   INTEGER   NOT NULL,
                    nome_col  TEXT    NOT NULL,
                    fabricante_col   TEXT  NOT NULL,
                    protecao_col   TEXT  NOT NULL,
                    funcao_col TEXT    NOT NULL,
                    validade_col  DATE    NOT NULL
                )
            ''')

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS Oculos_EPI
                (
                    id_ocu_EPI  INTEGER PRIMARY KEY,
                    CA_ocu   INTEGER   NOT NULL,
                    nome_ocu  TEXT    NOT NULL,
                    fabricante_ocu   TEXT  NOT NULL,
                    protecao_ocu   TEXT  NOT NULL,
                    funcao_ocu TEXT    NOT NULL,
                    validade_ocu  DATE    NOT NULL
                )
            ''')

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS Luva_EPI
                (
                    id_luva_EPI  INTEGER PRIMARY KEY,
                    CA_luva   INTEGER   NOT NULL,
                    nome_luva  TEXT    NOT NULL,
                    fabricante_luva   TEXT  NOT NULL,
                    protecao_luva   TEXT  NOT NULL,
                    funcao_luva TEXT    NOT NULL,
                    validade_luva  DATE    NOT NULL
                )
            ''')

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS Cinturao_EPI
                (
                    id_cin_EPI  INTEGER PRIMARY KEY,
                    CA_cin   INTEGER   NOT NULL,
                    nome_cin  TEXT    NOT NULL,
                    fabricante_cin   TEXT  NOT NULL,
                    protecao_cin   TEXT  NOT NULL,
                    funcao_cin TEXT    NOT NULL,
                    validade_cin  DATE    NOT NULL
                )
            ''')

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS Mascara_EPI
                (
                    id_masc_EPI  INTEGER PRIMARY KEY,
                    CA_masc   INTEGER   NOT NULL,
                    nome_masc  TEXT    NOT NULL,
                    fabricante_masc   TEXT  NOT NULL,
                    protecao_masc   TEXT  NOT NULL,
                    funcao_masc TEXT    NOT NULL,
                    validade_masc  DATE    NOT NULL
                )
            ''')

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS entrada_fun
                (
                    id_en_fun    INTEGER  PRIMARY KEY AUTOINCREMENT,
                    id_fun       INTEGER    NOT NULL,
                    nome_fun     TEXT   NOT NULL,
                    func_fun     TEXT   NOT NULL,
                    data_en_fun  DATE DEFAULT CURRENT_DATE,
                    hora_en_fun  TIME DEFAULT CURRENT_TIME
                )
            ''')

            "data_en_fun  TIMESTAMP DEFAULT CURRENT_TIMESTAMP"

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS entrada_cap_epi
                (
                    id_en_cap    INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cap      INTEGER    NOT NULL,
                    nome_epi_cap    TEXT   NOT NULL,
                    nome_fun_cap    TEXT    NOT NULL,
                    func_cap     TEXT   NOT NULL,
                    data_en_cap  DATE DEFAULT CURRENT_DATE,
                    hora_en_cap  TIME DEFAULT CURRENT_TIME
                )
            ''')

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS entrada_col_epi
                (
                    id_en_col    INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_col      INTEGER    NOT NULL,
                    nome_epi_col    TEXT   NOT NULL,
                    nome_fun_col    TEXT    NOT NULL,
                    func_col     TEXT   NOT NULL,
                    data_en_col  DATE DEFAULT CURRENT_DATE,
                    hora_en_col  TIME DEFAULT CURRENT_TIME
                )
            ''')

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS entrada_ocu_epi
                (
                    id_en_ocu    INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_ocu      INTEGER    NOT NULL,
                    nome_epi_ocu    TEXT   NOT NULL,
                    nome_fun_ocu    TEXT    NOT NULL,
                    func_ocu     TEXT   NOT NULL,
                    data_en_ocu  DATE DEFAULT CURRENT_DATE,
                    hora_en_ocu  TIME DEFAULT CURRENT_TIME
                )
            ''')

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS entrada_luva_epi
                (
                    id_en_luva    INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_luva      INTEGER    NOT NULL,
                    nome_epi_luva    TEXT   NOT NULL,
                    nome_fun_luva    TEXT    NOT NULL,
                    func_luva     TEXT   NOT NULL,
                    data_en_luva  DATE DEFAULT CURRENT_DATE,
                    hora_en_luva  TIME DEFAULT CURRENT_TIME
                )
            ''')

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS entrada_cin_epi
                (
                    id_en_cin    INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cin      INTEGER    NOT NULL,
                    nome_epi_cin    TEXT   NOT NULL,
                    nome_fun_cin    TEXT    NOT NULL,
                    func_cin     TEXT   NOT NULL,
                    data_en_cin  DATE DEFAULT CURRENT_DATE,
                    hora_en_cin  TIME DEFAULT CURRENT_TIME
                )
            ''')

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS entrada_masc_epi
                (
                    id_en_masc    INTEGER PRIMARY KEY AUTOINCREMENT,
                    ID_masc      INTEGER    NOT NULL,
                    nome_epi_masc    TEXT   NOT NULL,
                    nome_fun_masc    TEXT    NOT NULL,
                    func_masc     TEXT   NOT NULL,
                    data_en_masc  DATE DEFAULT CURRENT_DATE,
                    hora_en_masc  TIME DEFAULT CURRENT_TIME
                )
            ''')

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS saida_fun
                (
                    id_sa_fun    INTEGER  PRIMARY KEY AUTOINCREMENT,
                    id_fun       INTEGER    NOT NULL,
                    nome_fun     TEXT   NOT NULL,
                    func_fun     TEXT   NOT NULL,
                    data_sa_fun  DATE DEFAULT CURRENT_DATE,
                    hora_sa_fun  TIME DEFAULT CURRENT_TIME
                )
            ''')

            "data_en_fun  TIMESTAMP DEFAULT CURRENT_TIMESTAMP"

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS saida_cap_epi
                (
                    id_sa_cap    INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cap      INTEGER    NOT NULL,
                    nome_epi_cap    TEXT   NOT NULL,
                    nome_fun_cap    TEXT    NOT NULL,
                    func_cap      TEXT   NOT NULL,
                    data_sa_cap  DATE DEFAULT CURRENT_DATE,
                    hora_sa_cap  TIME DEFAULT CURRENT_TIME
                )
            ''')

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS saida_col_epi
                (
                    id_sa_col    INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_col      INTEGER    NOT NULL,
                    nome_epi_col    TEXT   NOT NULL,
                    nome_fun_col    TEXT    NOT NULL,
                    func_col     TEXT   NOT NULL,
                    data_en_col  DATE DEFAULT CURRENT_DATE,
                    hora_en_col  TIME DEFAULT CURRENT_TIME
                )
            ''')

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS saida_ocu_epi
                (
                    id_sa_ocu    INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_ocu      INTEGER    NOT NULL,
                    nome_epi_ocu    TEXT   NOT NULL,
                    nome_fun_ocu    TEXT    NOT NULL,
                    func_ocu     TEXT   NOT NULL,
                    data_sa_ocu  DATE DEFAULT CURRENT_DATE,
                    hora_sa_ocu  TIME DEFAULT CURRENT_TIME
                )
            ''')

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS saida_luva_epi
                (
                    id_sa_luva    INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_luva      INTEGER    NOT NULL,
                    nome_epi_luva    TEXT   NOT NULL,
                    nome_fun_luva    TEXT    NOT NULL,
                    func_luva     TEXT   NOT NULL,
                    data_sa_luva  DATE DEFAULT CURRENT_DATE,
                    hora_sa_luva  TIME DEFAULT CURRENT_TIME
                )
            ''')

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS saida_cin_epi
                (
                    id_sa_cin    INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cin      INTEGER    NOT NULL,
                    nome_epi_cin    TEXT   NOT NULL,
                    nome_fun_cin    TEXT    NOT NULL,
                    func_cin     TEXT   NOT NULL,
                    data_sa_cin  DATE DEFAULT CURRENT_DATE,
                    hora_sa_cin  TIME DEFAULT CURRENT_TIME
                )
            ''')

            con.commit()
            con.close()

            con = conexao()
            cur = con.cursor()

            cur.execute('''
                CREATE TABLE IF NOT EXISTS saida_masc_epi
                (
                    id_sa_masc    INTEGER PRIMARY KEY AUTOINCREMENT,
                    ID_masc      INTEGER    NOT NULL,
                    nome_epi_masc    TEXT   NOT NULL,
                    nome_fun_masc    TEXT    NOT NULL,
                    func_masc     TEXT   NOT NULL,
                    data_sa_masc  DATE DEFAULT CURRENT_DATE,
                    hora_sa_masc  TIME DEFAULT CURRENT_TIME
                )
            ''')

            con.commit()
            con.close()

        c_banco = tkinter.Toplevel()

        c_banco.geometry("950x534")
        c_banco.configure(bg="#ffffff")
        canvas = Canvas(
            c_banco,
            bg="#ffffff",
            height=534,
            width=950,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"Imagens/cri_banco/background.png")
        background = canvas.create_image(
            475.0, 267.0,
            image=background_img)

        img0 = PhotoImage(file=f"Imagens/cri_banco/img0.png")
        b0 = Button(c_banco,
                    image=img0,
                    borderwidth=0,
                    highlightthickness=0,
                    command=btn_clicked,
                    relief="flat")

        b0.place(
            x=251, y=330,
            width=447,
            height=161)

        c_banco.resizable(False, False)
        c_banco.title("Criar Banco")
        c_banco.mainloop()

    menu = Tk()

    menu.geometry("950x534")
    menu.configure(bg="#ffffff")
    canvas = Canvas(
        menu,
        bg="#ffffff",
        height=534,
        width=950,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=f"Imagens/menu/background.png")
    background = canvas.create_image(
        475.0, 267.0,
        image=background_img)

    img0 = PhotoImage(file=f"Imagens/menu/img0.png")
    b0 = Button(menu,
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=btn_rela,
        relief="flat")

    b0.place(
        x=587, y=67,
        width=306,
        height=138)

    img1 = PhotoImage(file=f"Imagens/menu/img1.png")
    b1 = Button(menu,
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=btn_menu_CRUD,
        relief="flat")

    b1.place(
        x=61, y=67,
        width=306,
        height=138)

    img2 = PhotoImage(file=f"Imagens/menu/img3.png")
    b2 = Button(menu,
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=btn_cad_adm,
        relief="flat")

    b2.place(
        x=61, y=215,
        width=306,
        height=138)

    img3 = PhotoImage(file=f"Imagens/menu/img5.png")
    b3 = Button(menu,
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=btn_c_banco,
        relief="flat")

    b3.place(
        x=61, y=363,
        width=306,
        height=138)

    img4 = PhotoImage(file=f"Imagens/menu/img4.png")
    b4 = Button(menu,
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=btn_info,
        relief="flat")

    b4.place(
        x=587, y=215,
        width=306,
        height=138)

    img5 = PhotoImage(file=f"Imagens/menu/img2.png")
    b5 = Button(menu,
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        command=btn_sistema,
        relief="flat")

    b5.place(
        x=587, y=363,
        width=306,
        height=138)

    menu.resizable(False, False)
    menu.title("Menu")
    menu.mainloop()


import sqlite3 as sql
def logar(usuario, senha):
    con = sql.connect("banco_adm.sqlite")
    cur = con.cursor()
    log = f"SELECT nome_funcionario from fun_adm WHERE nome_funcionario= '{usuario}' AND senha_funcionario = '{senha}';"
    cur.execute(log)
    if not cur.fetchone():
        canvas.create_text(
            307.0, 350.5,
            text="senha incorreta",
            fill="#000000",
            font=("None", int(16.0)))
    else:
        Login.destroy()
        menu()

    con.close()


def btn_clicked():
    logar(entry1.get(), entry0.get())






Login = Tk()

Login.geometry("950x534")
Login.configure(bg = "#ffffff")
canvas = Canvas(
    Login,
    bg = "#ffffff",
    height = 534,
    width = 950,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Imagens/ImagensLogin/background.png")
background = canvas.create_image(
    475.0, 267.0,
    image=background_img)

img0 = PhotoImage(file = f"Imagens/ImagensLogin/img0.png")
b0 = Button(Login,
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 391, y = 328,
    width = 167,
    height = 38)


entry0_img = PhotoImage(file = f"Imagens/ImagensLogin/img_textBox0.png")
entry0_bg = canvas.create_image(
    462.0, 290.5,
    image = entry0_img)

entry0 = Entry(Login,
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry0.place(
    x = 281, y = 273,
    width = 362,
    height = 33)

entry0.config(show="*")

canvas.create_rectangle(
    123, 70, 123+703, 70+393,
    fill = "#ffffff",
    outline = "")

canvas.create_text(
    307.0, 254.5,
    text = "Senha:",
    fill = "#000000",
    font = ("None", int(16.0)))

entry1_img = PhotoImage(file = f"Imagens/ImagensLogin/img_textBox1.png")
entry1_bg = canvas.create_image(
    462.0, 197.5,
    image = entry1_img)

entry1 = Entry(Login,
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry1.place(
    x = 281, y = 180,
    width = 362,
    height = 33)


canvas.create_text(
    312.5, 161.5,
    text = "Usuario:",
    fill = "#000000",
    font = ("None", int(16.0)))



Login.resizable(False, False)
Login.title("Login")
Login.mainloop()