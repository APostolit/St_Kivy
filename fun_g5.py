import streamlit as st

def run_5_1():
    st.markdown('###### 🐍 Виджет Line 🥝')
    st.image('images_5/img_5_1.png', width="content")

def run_5_2():
    st.markdown('###### 🐍 Виджет Line 🥝')
    st.image('images_5/img_5_2.png', width="content")

def run_5_3():
    st.markdown('###### 🐍 Виджет ModalView 🥝')
    col1, col2= st.columns(2)
    with col1:
        st.image('images_5/img_5_3_1.png', width="content")
    with col2:
        st.image('images_5/img_5_3_2.png', width="content")

def run_5_4():
    st.markdown('###### 🐍 Виджет ModalView 🥝')
    col1, col2= st.columns(2)
    with col1:
        st.image('images_5/img_5_3_1.png', width="content")
    with col2:
        st.image('images_5/img_5_3_2.png', width="content")

def run_5_5():
    st.markdown('###### 🐍 Виджет ModalView 🥝')
    col1, col2, col3= st.columns(3)
    with col1:
        st.image('images_5/img_5_5_1.png', width="content")
    with col2:
        st.image('images_5/img_5_5_2.png', width="content")
    with col3:
        st.image('images_5/img_5_5_3.png', width="content")

def run_5_6():
    st.markdown('###### 🐍 Виджет ProgressBar 🥝')
    col1, col2 = st.columns(2)
    with col1:
        st.image('images_5/img_5_6_1.png', width="content")
    with col2:
        st.image('images_5/img_5_6_2.png', width="content")

def run_5_7():
    st.markdown('###### 🐍 Виджет ProgressBar 🥝')
    col1, col2 = st.columns(2)
    with col1:
        st.image('images_5/img_5_6_1.png', width="content")
    with col2:
        st.image('images_5/img_5_6_2.png', width="content")

def run_5_8():
    st.markdown('###### 🐍 Виджет RstDocument 🥝')
    st.image('images_5/img_5_8.png', width="content")

def run_5_9():
    st.markdown('###### 🐍 Виджет RstDocument 🥝')
    col1, col2 = st.columns(2)
    with col1:
        st.image('images_5/img_5_9_1.png', width="content")
    with col2:
        st.image('images_5/img_5_9_2.png', width="content")

def run_5_10():
    st.markdown('###### 🐍 Виджет RstDocument 🥝')
    col1, col2 = st.columns(2)
    with col1:
        st.image('images_5/img_5_10_1.png', width="content")
    with col2:
        st.image('images_5/img_5_10_2.png', width="content")

def run_5_11():
    st.markdown('###### 🐍 Виджет ScrollView 🥝')
    st.image('images_5/img_5_11.png', width="content")

def run_5_12():
    st.markdown('###### 🐍 Виджет ScrollView 🥝')
    st.image('images_5/img_5_11.png', width="content")

def run_5_13():
    st.markdown('###### 🐍 Виджет Slider 🥝')
    tab1, tab2, tab3 = st.tabs(['Окно после загрузки',
                                'Задан зеленый цвет',
                                'Задан белый цвет'])
    with tab1:
        st.image('images_5/img_5_13_1.png', width="content")
    with tab2:
        st.image('images_5/img_5_13_2.png', width="content")
    with tab3:
        st.image('images_5/img_5_13_3.png', width="content")

def run_5_14():
    st.markdown('###### 🐍 Виджет Slider 🥝')
    tab1, tab2, tab3 = st.tabs(['Окно после загрузки',
                                'Задан зеленый цвет',
                                'Задан белый цвет'])
    with tab1:
        st.image('images_5/img_5_13_1.png', width="content")
    with tab2:
        st.image('images_5/img_5_13_2.png', width="content")
    with tab3:
        st.image('images_5/img_5_13_3.png', width="content")

def run_5_15():
    st.markdown('###### 🐍 Виджет SoundLoader 🥝')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('images_5/img_5_15_1.png', width="content")
    with col2:
        st.image('images_5/img_5_15_2.png', width="content")
    with col3:
        st.image('images_5/img_5_15_3.png', width="content")

def run_5_16():
    st.markdown('###### 🐍 Виджет Spinner 🥝')
    tab1, tab2, tab3 = st.tabs(['Начальное состояние',
                                'Список раскрыт',
                                'Сделан выбор'])
    with tab1:
        st.image('images_5/img_5_16_1.png', width="content")
    with tab2:
        st.image('images_5/img_5_16_2.png', width="content")
    with tab3:
        st.image('images_5/img_5_16_3.png', width="content")

def run_5_17():
    st.markdown('###### 🐍 Виджет TabbedPanel 🥝')
    tab1, tab2= st.tabs(['Панель - Регистрация',
                         'Панель - Вход',
                         ])
    with tab1:
        st.image('images_5/img_5_17_1.png', width="content")
    with tab2:
        st.image('images_5/img_5_17_2.png', width="content")


if __name__ == '__main__':
    run_5_1()