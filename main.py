from tkinter import *


class buton_komutlari():
    def liste_butonu():
        
        frame_sag3=Frame(ana_ekran, bg='light blue')
        frame_sag3.place(relx=0.22, rely=0.10, relheight=1.6, relwidth=1)
        buton_komutlari.ekle_butonu
        with open("kutuphane_kitap_list.txt") as dosya:
           for satır in dosya:
               Label(frame_sag3,text=satır,font="verdana,12").pack()


    
    def odunc_butonu():
        print("a")
    def ekle_butonu():
       frame_sag2=Frame(ana_ekran, bg='light blue')
       frame_sag2.place(relx=0.22, rely=0.10, relheight=1.6, relwidth=1)
       Label(frame_sag2,text="kitap adı").pack()
       kitap_ad_al=Entry(frame_sag2)
       kitap_ad_al.pack()

       Label(frame_sag2,text="yazar adı").pack()
       yazar_ad_al=Entry(frame_sag2)
       yazar_ad_al.pack()

       Label(frame_sag2,text="ISBN NO").pack()
       isbn_al=Entry(frame_sag2)
       isbn_al.pack()

       Label(frame_sag2,text="yayın evi").pack()
       yayin_evi_al=Entry(frame_sag2)
       yayin_evi_al.pack()

       Label(frame_sag2,text="tür").pack()
       tür_al=Entry(frame_sag2)
       tür_al.pack()

       Button(frame_sag2,text="ekle",command=kaydet_butonu).pack()
       def kaydet_butonu():
           kitap_adi=kitap_ad_al.get()
           yazar_ad=yazar_ad_al.get()
           isbn=isbn_al.get()
           yayinevi=yayin_evi_al.get()
           tür=tür_al.get()
           with open("kutuphane_kitap_list.txt","w") as dosya:
                dosya.write(f"{kitap_adi}:\n")
                dosya.write(f"Yazar: {yazar_ad}\n")
                dosya.write(f"ISBN: {isbn}\n")
                dosya.write(f"Yayınevi: {yayinevi}\n")
                dosya.write(f"Tür:{tür}")

           
           
    


    def kitap_ara():
        frame_sag1=Frame(ana_ekran, bg='light blue')
        frame_sag1.place(relx=0.22, rely=0.10, relheight=1.6, relwidth=1)
        Label(frame_sag1, text="aramak istediğiniz kitabın adını yazınız",font="verdana, 10").pack()

        arama_giris = Entry(frame_sag1)
        arama_giris.pack()

        def kitap_ara_buton():
            kitap_ara = arama_giris.get()
            found = False
            with open("kutuphane_kitap_list.txt", "r") as dosya:
                for satir in dosya:
                    if kitap_ara in satir.lower():
                        sonuc = f"{satir.strip()} kitap kütüphanede mevcut"
                        found = True
                        break
                if not found:
                    sonuc = f"'{kitap_ara}' kitabı kütüphanede bulunamadı"
            Label(frame_sag1,text=sonuc)
        Button(frame_sag1,text="ara",font="verdana,11",command=kitap_ara_buton()).pack()    
        

        
    

    
    


ana_ekran = Tk()
ana_ekran.title("kütüphane arayüzüne hoşgeldiniz")

canvas=Canvas(ana_ekran, width=700,height=450)
canvas.pack()

frame_ust=Frame(ana_ekran, bg='light blue')
frame_ust.place(relx=0.01, rely=0.01, relheight=0.08, relwidth=1)

frame_sol=Frame(ana_ekran, bg='black')
frame_sol.place(relx=0.01, rely=0.10, relheight=1.7, relwidth=0.2)



#üst frame tasarım
Label(frame_ust,text="KÜTÜPHANE SİSTEMİ",font="verdana,23,bold",bg="light blue",fg="black").pack()

#sol frame tasarım

odunc_alma_btn= Button(frame_sol, bg="dark grey",fg="black",text="ödünç verme",font="verdana, 10",command=buton_komutlari.odunc_butonu,width=25)
odunc_alma_btn.pack(padx=11,pady=12)

liste_butonu=Button(frame_sol, bg="green",fg="black",text="kitap listesi",font="verdana, 10",command=buton_komutlari.liste_butonu,width=25)
liste_butonu.pack(padx=11,pady=12)

kitap_ekle=Button(frame_sol, bg="green",fg="black",text="kitap ekle",font="verdana, 10",command=buton_komutlari.ekle_butonu,width=25)
kitap_ekle.pack(padx=11,pady=12)

kitap_ara_btn=Button(frame_sol, bg="green",fg="black",text="KİTAP ARA",font="verdana, 10",command=buton_komutlari.kitap_ara,width=25)
kitap_ara_btn.pack(padx=11,pady=12)










ana_ekran.mainloop()