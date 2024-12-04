
import streamlit as st
from PIL import Image

st.title("クロノクエスト")
st.caption("これはテストです")

#画像
image = Image.open("クロノス.png")
st.image(image, width=300)

with st.form(key="pro_form"):

    #テキストボックス
    name = st.text_input("名前")

    #セレクトボックス
    todo = st.multiselect(
        "あなたのToDo",
        ("英語", "筋トレ", "ストレッチ", "瞑想", "推し活" ))

    submit_btn = st.form_submit_button("submit")
    if submit_btn:
        st.text(f"ようこそ!{name}さん！") 
        st.text(f"あなたのToDo: {', '.join(todo)}ですね!")

