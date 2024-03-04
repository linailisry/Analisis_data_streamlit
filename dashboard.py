import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')


def main():
    st.title('Data Kota Changping')
    st.sidebar.title("Air Pollution Analysis")
    tabs = st.sidebar.radio("Menu", ["Data Wrangling", "Visualisasi Data"])
    
    if tabs == "Data Wrangling":
        data_option = st.sidebar.radio('Pilih Data:', ('Data Asli', 'Data Hasil Preprocessing'))
        
        if data_option == 'Data Asli':
            st.subheader('Data Asli')
            file_path_asli = "D:/MSIB/Bangkit/DIcoding/assignment/data_asli.csv"
            original_data = pd.read_csv(file_path_asli)

            st.write("**Deskripsi Data Asli:**")
            st.write("Jumlah Data:", original_data.shape[0])
            st.write("Jumlah Data Null:", original_data.isna().sum().sum())
            st.write("Jumlah Data Duplikat:", original_data.duplicated().sum())

            st.write(original_data)
        
        elif data_option == 'Data Hasil Preprocessing':
            st.subheader('Data Hasil Preprocessing')
            file_path_hasil = "D:/MSIB/Bangkit/DIcoding/assignment/all_data.csv"
            preprocessed_data = pd.read_csv(file_path_hasil)

            st.write("**Deskripsi Data Hasil Preprocessing:**")
            st.write("Jumlah Data:", preprocessed_data.shape[0])
            st.write("Jumlah Data Null:", preprocessed_data.isna().sum().sum())
            st.write("Jumlah Data Duplikat:", preprocessed_data.duplicated().sum())

            st.write(preprocessed_data)
    
    elif tabs == "Visualisasi Data":
        st.subheader("Visualisasi Data")
        data_option = st.sidebar.radio('Pilih Pertanyaan:', ('Pertanyaan 1', 'Pertanyaan 2'))
        if data_option == 'Pertanyaan 1':
            preprocessed_data = pd.read_csv("D:/MSIB/Bangkit/DIcoding/assignment/all_data.csv")
            st.subheader("Diagram Batang untuk Polutan Udara Paling Umum")
            
            AP = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
            pollutant_counts = preprocessed_data[AP].mode().iloc[0]
            plt.figure(figsize=(10, 6))
            pollutant_counts.plot(kind='bar', color='skyblue')
            plt.title('Polutan Udara Paling Umum dalam Dataset')
            plt.xlabel('Polutan Udara')
            plt.ylabel('Frekuensi Kemunculan')
            plt.xticks(rotation=45)
            st.pyplot(plt)

            st.subheader("Diagram Lingkaran untuk Polutan Udara Paling Umum")
            plt.figure(figsize=(8, 8))
            pollutant_counts.plot(kind='pie', colors=['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightpink', 'lightyellow'], autopct='%1.1f%%')
            plt.title('Polutan Udara Paling Umum dalam Dataset')
            plt.ylabel('')
            st.pyplot(plt)

            st.write("Kesimpulan: Bagaimana keadaan polusi udara di Changping? Terdapat beberapa jenis polutan udara di Changping dengan jenis polutan paling banyak adalah CO (karbon) sebanyak 89,9% diikuti dengan PM10 (partikulat 10) sebanyak 3,9%, dan NO2 (Nitrogen Dioksida) sebanyak 3,6%")

        elif data_option == 'Pertanyaan 2':
            preprocessed_data = pd.read_csv("D:/MSIB/Bangkit/DIcoding/assignment/all_data.csv")
            st.subheader("Tren Polutan Udara di Changping berdasarkan Tahun")

            # Membuat kelompok berdasarkan nilai pada kolom 'year'
            grouped_df = preprocessed_data.groupby('year')
            # Menghitung rata-rata pada kolom variabel untuk setiap kelompok
            result_df = grouped_df['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'].mean().reset_index()
            # Membatasi data hanya untuk rentang nilai 'year' dari 2013-2017
            result_df = result_df[result_df['year'].between(2013, 2017)]

            # Plotting line by year
            AP = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
            plt.figure(figsize=(10, 6))
            for pollutant in AP:
                plt.plot(result_df['year'], result_df[pollutant], label=pollutant)
                
            plt.title('Tren Polutan Udara Berdasarkan Tahun')
            plt.xlabel('Tahun')
            plt.ylabel('Konsentrasi Polutan (µg/m³)')
            plt.legend()
            st.pyplot(plt)


            st.subheader("Tren Polutan Udara di Changping berdasarkan Bulan")
            # Membuat kelompok berdasarkan nilai pada kolom 'month'
            grouped = preprocessed_data.groupby('month')
            # Menghitung rata-rata pada kolom variabel untuk setiap kelompok
            result = grouped['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'].mean().reset_index()
            # Membatasi data hanya untuk rentang nilai 'month' dari 1-12
            result = result[result['month'].between(1, 12)]

            AP = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']

            # plotting line by month
            plt.figure(figsize=(12, 6))
            for column in AP:
                plt.plot(result['month'], result[column], label=column)

            plt.title('Tren Polutan Udara Berdasarkan Bulan')
            plt.xlabel('Bulan')
            plt.ylabel('Konsentrasi Polutan (µg/m³)')
            plt.legend()
            st.pyplot(plt)

            st.write("Kesimpulan: Bagaimana tren jenis polusi udara dalam tahunan dan bulanan di Changping? Berdasarkan analisis tren tahunan dari masing masing polutan, dimana CO berada pada peringkat teratas yang semakin naik tiap tahunnya hingga tahun 2017. berdasarkan analisis tren bulanan, polutan CO berada pada titik tertinggi pada Bulan Januari dan Bulan Desember.")

    st.caption('Copyright © Dicoding 2024')

if __name__ == "__main__":
    main()

