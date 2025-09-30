import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 1학년 학생 비만/저체중 분포 분석")

# 파일 업로드
uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요", type=["xlsx"])
if uploaded_file:
    # 데이터 불러오기
    df = pd.read_excel(uploaded_file, sheet_name="데이터 엑셀다운")

    # 필요한 열만 추출
    df_bmi = df[["학년", "반", "성별", "체질량지수_학생", "비만도_학생"]].copy()

    # ==============================
    # 전체 분포 그래프
    # ==============================
    st.subheader("전체 학생 분포")
    counts = df_bmi["비만도_학생"].value_counts()

    fig, ax = plt.subplots(figsize=(6,4))
    counts.plot(kind="bar", ax=ax)
    ax.set_title("1학년 학생 비만/저체중 분포")
    ax.set_xlabel("구분")
    ax.set_ylabel("학생 수")
    st.pyplot(fig)

    # ==============================
    # 학급별 분포 그래프
    # ==============================
    st.subheader("학급별 분포 비교")

    # 학급별 비만도 집계
    class_counts = df_bmi.groupby(["반", "비만도_학생"]).size().unstack(fill_value=0)

    fig2, ax2 = plt.subplots(figsize=(10,6))
    class_counts.plot(kind="bar", stacked=True, ax=ax2)
    ax2.set_title("1학년 학급별 비만/저체중 분포")
    ax2.set_xlabel("학급(반)")
    ax2.set_ylabel("학생 수")
    st.pyplot(fig2)

    # ==============================
    # 원시 데이터 미리보기
    # ==============================
    with st.expander("📑 원본 데이터 미리보기"):
        st.dataframe(df_bmi.head(20))
else:
    st.info("왼쪽에 있는 '엑셀 파일 업로드' 버튼을 이용해 데이터를 불러오세요.")
