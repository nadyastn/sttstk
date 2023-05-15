import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.sidebar.header("Menu Navigasi")
    task = st.sidebar.selectbox("Pilih Task", ("Apa itu Pengolahan Data Tunggal dalam Statistika?", "Kalkulator Pengolahan Data Tunggal Statistika"))

    if task == "Apa itu Pengolahan Data Tunggal dalam Statistika?":
        penjelasan_materi()
    elif task == "Kalkulator Pengolahan Data Tunggal Statistika":
        masukkan_dan_pengolahan_data()

def masukkan_dan_pengolahan_data():
    st.header(":green[Aplikasi Pengolahan Data Tunggal dalam Statistika]")
    st.subheader("Kalkulator Pengolahan Data Tunggal Statistika")

    # Masukkan Data
    st.subheader("Masukkan Data!")
    rows = st.number_input("Jumlah Data:", min_value=1, value=1)

    data = []
    for i in range(rows):
        value = st.number_input(f"Data {i+1}", value=0.00)
        data.append(value)

    df = pd.DataFrame(data)
    st.write("Data yang Dimasukkan:")
    st.write(df)

    # Pengolahan Data
    st.subheader("Hasil Pengolahan Data:memo:")
    st.write("Rata-rata: ", np.mean(data))
    st.write("Median: ", np.median(data))
    st.write("Range/Jangkauan: ", np.round(np.max(data) - np.min(data), 2))
    st.write("Simpangan Rata-rata: ", np.round(np.mean(np.abs(data - np.mean(data))), 2))
    st.write("Ragam/Variasi: ", np.round(np.var(data), 2))
    st.write("Simpangan Baku/Standar Deviasi: ", np.round(np.std(data), 2))

def penjelasan_materi():
    st.header(":green[Aplikasi Pengolahan Data Tunggal dalam Statistika]")
    st.subheader("Apa itu Pengolahan Data Tunggal dalam Statistika?")
    st.write("Pengolahan data tunggal adalah proses pengumpulan, pengorganisasian, dan analisis data tunggal untuk memahami karakteristik dan informasi yang terkandung dalam data tersebut.")
    st.write("Dalam statistika, terdapat beberapa metode pengolahan data tunggal yang umum digunakan seperti menghitung nilai rata-rata, median, modus, simpangan baku, dan lain sebagainya. Tapi, dalam aplikasi ini hanya tersedia 6 output pengolahan data tunggal yang akan ditampilkan yaitu rata-rata, median, range/jangkauan, simpangan rata-rata, ragam/variasi, dan simpangan baku/standar deviasi. Untuk informasi lebih lengkapnya akan dijelaskan dalam power point dibawah.")
    
    st.subheader("Slide PPT")
    st.markdown("[Buka PPT](https://docs.google.com/presentation/d/1JAiM2lxYhoIuAX0b6yUN6gEb12r-_jBB/edit?usp=drive_web&ouid=109375233677945429292&rtpof=true)")

if __name__ == '__main__':
    main()
