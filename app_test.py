
import streamlit as st
from PIL import Image
from openai import OpenAI
import os

# OpenAI APIのキーを環境変数から取得
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

st.title("クロノクエスト")
st.caption("あなたのやりたいことを助けるのじゃ")

# 画像の表示
image = Image.open("クロノス.png")
st.image(image, width=300)

with st.form(key="pro_form"):

    # テキストボックス
    name = st.text_input("名前")

    # セレクトボックス
    todo = st.multiselect(
        "あなたのToDo",
        ("英語", "筋トレ", "ストレッチ", "瞑想", "推し活")
    )

    submit_btn = st.form_submit_button("submit")

    if submit_btn:
        st.text(f"ようこそ!{name}さん！") 
        st.text(f"あなたのToDo: {', '.join(todo)}ですね!")
        st.text("以下にファーストステップとして必要なアクションを提案しますね。ちょっとお待ちください。")

        # ChatGPT-4 APIを使ってアクションを生成
        if todo:
            suggestions = []
            for task in todo:
                # ChatGPT-4に対するプロンプトの作成
                prompt = (
                    f"私は{task}を始めたいですが、初心者です。"
                    "初めの一歩としてできる具体的なアクションを一つ提案してください。"
                )

                try:
                    # OpenAI APIを呼び出して応答を取得
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": "あなたは有益で具体的なアドバイスを提供するアシスタントです。プリキュアのこむぎになりきって"},
                            {"role": "user", "content": prompt}
                        ]
                    )

                    # 応答の抽出
                    suggestion = response.choices[0].message.content.strip()
                    suggestions.append(f"{task}: {suggestion}")
                except Exception as e:
                    suggestions.append(f"{task}: アクションを取得できませんでした (エラー: {e})")

            # 提案を表示
            st.subheader("クロノス（プリキュアver）からの提案")
            for suggestion in suggestions:
                st.text(suggestion)
