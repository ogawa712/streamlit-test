import streamlit as st
import time

st.title("Stream")

st.write("プレグレスバーの表示")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

# f:f文字列 文字列内に式を埋め込む

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右からむ")

expander = st.expander("問い合わせ")
expander.write("問い合わせの回答")

# text = st.text_input("あなたの趣味を教えてください")
# condition = st.slider("あなたの今の調子は？",0,100,50)


# "あなたの趣味は",text,"です"
# "コンディション:",condition


# if st.checkbox("Show Image"):
#     img=Image.open("130190.jpg")
#     st.image(img,caption="OgawaTetsuji",use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=["lat","lon"]
# )

# st.map(df)

# arr1 = np.array([[1,2,3],[11,12,13]])
# pd.DataFrame(data=arr1)

# st.dataframe(df.style.highlight_max(axis=1))

# st.write(arr1)