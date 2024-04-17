from tkinter import *
from tkinter import ttk,messagebox


class buton_komutlari():
    def odunc_al_btn():
        def odunc_sistemi():
            kisi_isim = kisi_ismi_al.get()
            kitap_isim = kitap_ismi_al.get()
            verilis_tarihi = veriliş_tarihi_al.get()
            

            with open("kutuphane_kitap_list.txt", "r") as dosya:
                kitap_listesi = dosya.readlines()

            kitap_bulundu = False
            for kitap in kitap_listesi:
                if kitap_isim.lower() in kitap.lower():
                    kitap_bulundu = True
                    break

            if kitap_bulundu:
                with open("ödünç_alanlar.txt", "r") as odunc_dosya:
                    odunc_alanlar = odunc_dosya.readlines()
                    for odunc_alan in odunc_alanlar:
                        if kitap_isim.lower() in odunc_alan.lower():
                            messagebox.showerror("Hata", f"{kitap_isim} kitabı zaten ödünç alınmış.")
                            return

                with open("ödünç_alanlar.txt", "a") as odunc_dosya:
                    odunc_dosya.write(f"Kitap ismi: {kitap_isim}\n")
                    odunc_dosya.write(f"Ödünç alan kişi: {kisi_isim}\n")
                    odunc_dosya.write(f"Veriliş tarihi: {verilis_tarihi}\n")
                    

                messagebox.showinfo("Başarılı", f"{kitap_isim} kitabı {kisi_isim} adlı kişiye ödünç verildi.")
            else:
                messagebox.showerror("Hata", f"{kitap_isim} kitabı bulunamadı.")
        frame_sag5=Frame(ana_ekran, bg='#383E42')
        frame_sag5.place(relx=0.22, rely=0.10, relheight=0.9, relwidth=0.8)
        Label(frame_sag5,text="isim ve soyisim:",).pack()
        kisi_ismi_al=Entry(frame_sag5)
        kisi_ismi_al.pack()

        Label(frame_sag5,text="kitap:",).pack()
        kitap_ismi_al=Entry(frame_sag5)
        kitap_ismi_al.pack()

        Label(frame_sag5,text="tarih:",).pack()
        veriliş_tarihi_al=Entry(frame_sag5)
        veriliş_tarihi_al.pack()

        odunc_ver_btn=Button(frame_sag5,text="ÖDÜNÇ VER",bg="#29903B")
        odunc_ver_btn.pack()



    def liste_butonu():
        frame_sag3=Frame(ana_ekran, bg='#383E42')
        frame_sag3.place(relx=0.22, rely=0.10, relheight=0.9, relwidth=0.8)

        scrolbar=ttk.Scrollbar(frame_sag3,orient="vertical",command= canvas.yview)
        canvas.configure(yscrollcommand= scrolbar.set)
        scrolbar.place(relx=1,rely=0,relheight=1,anchor="ne")
        canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta /60),"units"))
        
        
        
        with open("kutuphane_kitap_list.txt") as dosya:
           for satır in dosya:
               Label(frame_sag3,text=satır,font="verdana,12").pack(fill=BOTH,expand=True)


    
    def kitap_sil_btn():
        def silme_btn_tikla():
            kitap_adi = silmeye_giris.get()
            found = False

            # dosyayı oku kullanıcının yazdığı kitabı sil
            with open("kutuphane_kitap_list.txt", "r") as dosya:
                lines = dosya.readlines()
            with open("kutuphane_kitap_list.txt", "w") as dosya:
                for line in lines:
                    if kitap_adi.lower() not in line.lower():
                        dosya.write(line)
                    else:
                        found = True

            if found:
                bildiri=Label(frame_sag4,text="kitap başarıyla silindi",fg="green",)
                bildiri.after(5000,lambda: bildiri.config(text=""))
                bildiri.pack()
            else:
                bildiri=Label(frame_sag4,text="kitap bulunamadı",)
                bildiri.after(5000,lambda: bildiri.config(text=""))
                bildiri.pack()
            silmeye_giris.delete(0,END)

        frame_sag4=Frame(ana_ekran, bg='#383E42')
        frame_sag4.place(relx=0.22, rely=0.10, relheight=0.9, relwidth=0.8)

        silme_etiketi = Label(frame_sag4,bg='#383E42', text="Silmek istediğiniz kitap adını giriniz:")
        silme_etiketi.pack()

        silmeye_giris = Entry(frame_sag4)
        silmeye_giris.pack()

        silme_buton = Button(frame_sag4, text="Sil", command=silme_btn_tikla)
        silme_buton.pack()
        
    def ekle_butonu():
       frame_sag2=Frame(ana_ekran, bg='#383E42')
       frame_sag2.place(relx=0.22, rely=0.10, relheight=0.9, relwidth=0.8)
       Label(frame_sag2,bg='#383E42',text="kitap adı").pack()
       kitap_ad_al=Entry(frame_sag2)
       kitap_ad_al.pack(padx=12,pady=5)

       Label(frame_sag2,bg='#383E42',text="yazar adı").pack()
       yazar_ad_al=Entry(frame_sag2)
       yazar_ad_al.pack(padx=12,pady=5)

       Label(frame_sag2,bg='#383E42',text="ISBN NO").pack()
       isbn_al=Entry(frame_sag2)
       isbn_al.pack(padx=12,pady=5)

       Label(frame_sag2,bg='#383E42',text="yayın evi").pack()
       yayin_evi_al=Entry(frame_sag2)
       yayin_evi_al.pack(padx=12,pady=5)

       Label(frame_sag2,bg='#383E42',text="tür").pack()
       tür_al=Entry(frame_sag2)
       tür_al.pack(padx=12,pady=5)

      
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
           kitap_ad_al.delete(0,END)
           yazar_ad_al.delete(0,END)
           isbn_al.delete(0,END)
           yayin_evi_al.delete(0,END)
           tür_al.delete(0,END)
           

       kaydet=Button(frame_sag2,text="EKLE",command=kaydet_butonu,activebackground="yellow",bg="#29903B",width=16)
       kaydet.pack(pady=5)
           
           
    


    def kitap_ara():
        frame_sag1=Frame(ana_ekran, bg='#383E42')
        frame_sag1.place(relx=0.22, rely=0.10, relheight=0.9, relwidth=0.8)
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
ana_ekran.configure(bg="black")

canvas=Canvas(ana_ekran, width=700,height=450,bg="black",scrollregion=(0,0,0,5000))
canvas.pack()

frame_ust=Frame(ana_ekran, bg='#2B2D31')
frame_ust.place(relx=0.01, rely=0.01, relheight=0.08, relwidth=1)

frame_sol=Frame(ana_ekran, bg='#2B2D31')
frame_sol.place(relx=0.01, rely=0.10, relheight=0.9, relwidth=0.2)

frame_sag=Frame(ana_ekran, bg='#2B2D31')
frame_sag.place(relx=0.22, rely=0.10, relheight=0.9, relwidth=1)



#üst frame tasarım
Label(frame_ust,text="KÜTÜPHANE SİSTEMİ",font="arial,23,bold",bg="#2B2D31",fg="black").pack()

#sol frame tasarım

odunc_alma_btn= Button(frame_sol, bg="dark grey",fg="black",text="ÖDÜNÇ VERME",font="verdana, 10",command=buton_komutlari.odunc_al_btn,width=25)
odunc_alma_btn.pack(padx=11,pady=12,fill=BOTH,expand=True)

liste_butonu=Button(frame_sol, bg="dark grey",fg="black",text="KİTAP LİSTESİ",font="verdana, 10",command=buton_komutlari.liste_butonu,width=25)
liste_butonu.pack(padx=11,pady=12,fill=BOTH,expand=True)

kitap_ekle=Button(frame_sol, bg="dark grey",fg="black",text="KİTAP EKLE",font="verdana, 10",command=buton_komutlari.ekle_butonu,width=25)
kitap_ekle.pack(padx=11,pady=12,fill=BOTH,expand=True)

kitap_ara_btn=Button(frame_sol, bg="dark grey",fg="black",text="KİTAP ARA",font="verdana, 10",command=buton_komutlari.kitap_ara,width=25)
kitap_ara_btn.pack(padx=11,pady=12,fill=BOTH,expand=True)

kitap_sil_btn=Button(frame_sol, bg="dark grey",fg="black",text="KİTAP SİL",font="verdana, 10",command=buton_komutlari.kitap_sil_btn,width=25)
kitap_sil_btn.pack(padx=11,pady=12,fill=BOTH,expand=True)










ana_ekran.mainloop()