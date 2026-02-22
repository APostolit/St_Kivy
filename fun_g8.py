import streamlit as st

def run_8_1():
    st.markdown('###### 🐍 Виджет MDBoxLayout 🥝')
    st.image('images_8/img_8_1.png', width="content")

def run_8_2():
    st.markdown('###### 🐍 Виджет MDCircularLayout 🥝')
    st.image('images_8/img_8_2.png', width="content")

def run_8_3():
    st.markdown('###### 🐍 Виджет MDFloat Layout 🥝')
    st.image('images_8/img_8_3.png', width="content")

def run_8_4():
    st.markdown('###### 🐍 Виджет MDGrid Layout 🥝')
    st.image('images_8/img_8_4.png', width="content")

def run_8_5():
    st.markdown('###### 🐍 Виджет RefreshLayout 🥝')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('images_8/img_8_5_1.png', width="content")
    with col2:
        st.image('images_8/img_8_5_2.png', width="content")
    with col3:
        st.image('images_8/img_8_5_3.png', width="content")

def run_8_6():
    st.markdown('###### 🐍 Виджет MDRelativeLayout 🥝')
    st.image('images_8/img_8_6.png', width="content")

def run_8_7():
    st.markdown('###### 🐍 Виджет MDStackLayout 🥝')
    col1, col2 = st.columns(2)
    with col1:
        st.image('images_8/img_8_7_1.png', width="content")
    with col2:
        st.image('images_8/img_8_7_2.png', width="content")
    col3, col4 = st.columns(2)
    with col3:
        st.image('images_8/img_8_7_3.png', width="content")
    with col4:
        st.image('images_8/img_8_7_4.png', width="content")

def run_8_8():
    st.markdown('###### 🐍 Виджет MDStackLayout 🥝')
    st.image('images_8/img_8_8_1.png', width="content")

def run_8_9():
    st.markdown('###### 🐍 Виджет MDCarousel 🥝')
    col1, col2 = st.columns(2)
    with col1:
        st.image('images_8/img_8_9_1.png', width="content")
    with col2:
        st.image('images_8/img_8_9_2.png', width="content")
    col3, col4 = st.columns(2)
    with col3:
        st.image('images_8/img_8_9_3.png', width="content")
    with col4:
        st.image('images_8/img_8_9_4.png', width="content")

def run_8_10():
    st.markdown('###### 🐍 Виджет MDCarousel 🥝')
    col1, col2 = st.columns(2)
    with col1:
        st.image('images_8/img_8_10_1.png', width="content")
    with col2:
        st.image('images_8/img_8_10_2.png', width="content")
    col3, col4 = st.columns(2)
    with col3:
        st.image('images_8/img_8_10_3.png', width="content")
    with col4:
        st.image('images_8/img_8_10_4.png', width="content")

if __name__ == '__main__':
    run_8_1()