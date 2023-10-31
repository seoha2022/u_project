import streamlit as st
import openai
import os

# OpenAI API 키 설정
openai.api_key = os.environ.get("OPENAI_API_KEY")

st.title("OpenAI Chatbot")

# 사용자에게 질문 받기
user_input = st.text_input("질문을 입력하세요:")

if user_input:
    # OpenAI API를 사용하여 답변 생성
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=50,
    )

    answer = response.choices[0].text

    # 답변 표시
    st.write("답변:")
    st.write(answer)
