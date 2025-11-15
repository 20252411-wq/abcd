  python
import streamlit as st
import random

# --- 1. 세션 상태 초기화 ---
# 게임 상태를 유지하기 위해 streamlit.session_state를 사용합니다.
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100) # 1부터 100 사이의 랜덤 숫자 생성
    st.session_state.attempts = 0 # 시도 횟수 초기화
    st.session_state.game_over = False # 게임 종료 여부

# --- 2. 앱 제목 및 설명 ---
st.title("🔢 업앤다운(Up & Down) 게임")
st.write("1부터 100 사이의 숫자를 맞춰보세요!")

# --- 3. 게임 로직 처리 함수 ---
def check_guess():
    if st.session_state.game_over:
        return

    try:
        # 사용자 입력 가져오기
        user_guess = int(st.session_input)

        st.session_state.attempts += 1

        if user_guess < st.session_state.secret_number:
            st.warning("⬆️ 업(Up)! 더 큰 숫자를 입력하세요.")
        elif user_guess > st.session_state.secret_number:
            st.warning("⬇️ 다운(Down)! 더 작은 숫자를 입력하세요.")
        else:
            st.success(f"🎉 정답입니다! {st.session_state.attempts}번 만에 맞히셨어요!")
            st.session_state.game_over = True
    except ValueError:
        st.error("유효한 숫자를 입력해주세요.")

# --- 4. 게임 인터페이스 ---
if not st.session_state.game_over:     
    # 텍스트 입력창과 버튼을 만듭니다.
    # key="st_session_input" 으로 입력 위젯의 상태를 세션 스테이트에 저장합니다.
    st.number_input("숫자를 입력하세요:", min_value=1, max_value=100, step=1, key="st_session_input")
    
    # 버튼을 누르면 check_guess 함수가 실행됩니다.
    st.button("제출", on_click=check_guess)

else:
    # 게임이 종료되면 다시 시작 버튼을 보여줍니다.
    if st.button("다시 시작하기"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.experimental_rerun() # 앱을 새로고침하여 게임을 재시작합니다.

# --- 5. 현재 시도 횟수 표시 ---
st.sidebar.info(f"현재 시도 횟수: {st.session_state.attempts}회")
