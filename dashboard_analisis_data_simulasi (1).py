
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Analisis Nilai Siswa", layout="wide")

st.title("📊 Dashboard Analisis Data Nilai Siswa")

# Load data
file_path = "data_simulasi_50_siswa_20_soal.xlsx"
df = pd.read_excel(file_path)

# Tampilkan data
st.subheader("📋 Data Nilai Siswa")
st.dataframe(df)

# Hitung rata-rata nilai per siswa
df["Rata-rata"] = df.iloc[:, 1:].mean(axis=1)

# Statistik umum
st.subheader("📈 Statistik Umum")
col1, col2, col3 = st.columns(3)

col1.metric("Nilai Tertinggi", round(df.iloc[:, 1:-1].max().max(), 2))
col2.metric("Nilai Terendah", round(df.iloc[:, 1:-1].min().min(), 2))
col3.metric("Rata-rata Kelas", round(df["Rata-rata"].mean(), 2))

# Grafik rata-rata nilai siswa
st.subheader("📊 Rata-rata Nilai per Siswa")
fig, ax = plt.subplots()
ax.bar(df.iloc[:, 0], df["Rata-rata"])
ax.set_xlabel("Siswa")
ax.set_ylabel("Nilai")
ax.tick_params(axis='x', rotation=90)
st.pyplot(fig)

# Rata-rata nilai per soal
st.subheader("📝 Rata-rata Nilai per Soal")
rata_soal = df.iloc[:, 1:-1].mean()

fig2, ax2 = plt.subplots()
ax2.plot(rata_soal.index, rata_soal.values, marker="o")
ax2.set_xlabel("Soal")
ax2.set_ylabel("Nilai Rata-rata")
ax2.grid(True)
st.pyplot(fig2)

# Ranking siswa
st.subheader("🏆 Peringkat Siswa")
ranking = df[[df.columns[0], "Rata-rata"]].sort_values(by="Rata-rata", ascending=False)
ranking.columns = ["Nama Siswa", "Rata-rata"]
st.dataframe(ranking.reset_index(drop=True))
