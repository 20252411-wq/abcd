  python
import streamlit as st
import pandas as pd
import numpy as np

# --- 1. 앱 제목 설정 ---
st.title("스트림릿 데이터 시각화 예제")
st.write("간단한 랜덤 데이터를 표와 그래프로 보여줍니다.")

# --- 2. 데이터 생성 (Pandas 사용) ---
# 10행 3열의 랜덤 데이터프레임을 만듭니다.
df = pd.DataFrame(
    np.random.randn(10, 3), # 랜덤 숫자 생성
    columns=['컬럼 A', '컬럼 B', '컬럼 C'] # 컬럼 이름 설정
)

# --- 3. 데이터 표시 (표) ---
st.subheader("데이터프레임 (표 형식)")
st.dataframe(df) # st.dataframe() 함수로 데이터프레임을 웹에 표시

# --- 4. 데이터 시각화 (꺾은선 그래프) ---
st.subheader("꺾은선 그래프")
st.line_chart(df) # st.line_chart() 함수로 꺾은선 그래프를 웹에 표시

# --- 5. 상호작용 위젯 추가 ---
st.sidebar.header("설정")
