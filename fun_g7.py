import streamlit as st

def run_7_1():
    st.markdown('###### 🐍 Базовая структура приложения KivyMD 🥝')
    st.image('images_7/img_7_1.png', width="content")

def run_7_2():
    st.markdown('###### 🐍 Элемент Screen 🥝')
    st.image('images_7/img_7_2.png', width="content")

def run_7_3():
    st.markdown('###### 🐍 Компоненты MDTopAppBar и кнопка с KV 🥝')
    st.image('images_7/img_7_3.png', width="content")

def run_7_4():
    st.markdown('###### 🐍 Менеджер экранов (ScreenManager) 🥝')
    tab1, tab2, tab3 = st.tabs(['Экран 1',
                                'Экран 2',
                                'Экран 3'])
    with tab1:
        st.image('images_7/img_7_4_1.png', width="content")
    with tab2:
        st.image('images_7/img_7_4_2.png', width="content")
    with tab3:
        st.image('images_7/img_7_4_3.png', width="content")

def run_7_5():
    st.markdown('###### 🐍 Стили KivyMD для задания цвета элементам 🥝')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('images_7/img_7_5_1.png', width="content")
    with col2:
        st.image('images_7/img_7_5_2.png', width="content")
    with col3:
        st.image('images_7/img_7_5_3.png', width="content")

def run_7_6():
    st.markdown('###### 🐍 Изменение оттенка цвета элемента 🥝')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('images_7/img_7_6_1.png', width="content")
    with col2:
        st.image('images_7/img_7_6_2.png', width="content")
    with col3:
        st.image('images_7/img_7_6_3.png', width="content")

def run_7_7():
    st.markdown('###### 🐍 Изменение оттенка цвета фона элемента 🥝')
    st.image('images_7/img_7_7.png', width="content")

def run_7_8():
    st.markdown('###### 🐍 Темы и стили 🥝')
    col1, col2 = st.columns(2)
    with col1:
        st.image('images_7/img_7_8_1.png', width="content")
    with col2:
        st.image('images_7/img_7_8_2.png', width="content")

def run_7_9():
    st.markdown('###### 🐍 Темы и стили 🥝')
    st.image('images_7/img_7_9.png', width="content")

def run_7_10():
    st.markdown('###### 🐍 Список иконок 🥝')
    st.image('images_7/img_7_10.png', width="content")

def run_7_11():
    st.markdown('###### 🐍 Виджет TopAppBar 🥝')
    st.image('images_7/img_7_11.png', width="content")

if __name__ == '__main__':
    run_7_1()