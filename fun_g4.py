import streamlit as st

def run_4_1():
    st.markdown('###### 🐍 Виджет Accordion 🥝')
    tab1, tab2, tab3 = st.tabs(['Вкладка 1', 'Вкладка 2', 'Вкладка 3'])
    with tab1:
        st.image('images_4/img_4_1_1.png', width="content")
    with tab2:
        st.image('images_4/img_4_1_2.png', width="content")
    with tab3:
        st.image('images_4/img_4_1_3.png', width="content")

def run_4_2():
    st.markdown('###### 🐍 Виджет Accordion с KV 🥝')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('images_4/img_4_2_1.png', width="content")
    with col2:
        st.image('images_4/img_4_2_2.png', width="content")
    with col3:
        st.image('images_4/img_4_2_3.png', width="content")

def run_4_3():
    st.markdown('###### 🐍 Виджет ActionBar 🥝')
    tab1, tab2, tab3, tab4 = st.tabs(['ActionBar', 'Нажата иконка',
                                      'Нажатиа Кнопка 1', 'Группа кнопок'])
    with tab1:
        st.image('images_4/img_4_3_1.png', width="content")
    with tab2:
        st.image('images_4/img_4_3_2.png', width="content")
    with tab3:
        st.image('images_4/img_4_3_3.png', width="content")
    with tab4:
        st.image('images_4/img_4_3_4.png', width="content")

def run_4_4():
    st.markdown('###### 🐍 Виджет ActionBar с KV 🥝')
    tab1, tab2, tab3 = st.tabs(['ActionBar', 'Нажатиа Кнопка 1',
                                'Группа кнопок'])
    with tab1:
        st.image('images_4/img_4_4_1.png', width="content")
    with tab2:
        st.image('images_4/img_4_4_2.png', width="content")
    with tab3:
        st.image('images_4/img_4_4_3.png', width="content")

def run_4_5():
    st.markdown('###### 🐍 Виджет Bubble 🥝')
    tab1, tab2, tab3 = st.tabs(['Приложение', 'Меню',
                                'Выбрана опция'])
    with tab1:
        st.image('images_4/img_4_5_1.png', width="content")
    with tab2:
        st.image('images_4/img_4_5_2.png', width="content")
    with tab3:
        st.image('images_4/img_4_5_3.png', width="content")

def run_4_6():
    st.markdown('###### 🐍 Виджет Bubble 🥝')
    tab1, tab2, tab3 = st.tabs(['Приложение', 'Меню',
                                'Выбрана опция'])
    with tab1:
        st.image('images_4/img_4_6_1.png', width="content")
    with tab2:
        st.image('images_4/img_4_6_2.png', width="content")
    with tab3:
        st.image('images_4/img_4_6_3.png', width="content")

def run_4_7():
    st.markdown('###### 🐍 Виджет Button 🥝')
    tab1, tab2 = st.tabs(['Приложение', 'Кнопка нажата'])
    with tab1:
        st.image('images_4/img_4_7_1.png', width="content")
    with tab2:
        st.image('images_4/img_4_7_2.png', width="content")

def run_4_8():
    st.markdown('###### 🐍 Виджет Button 🥝')
    tab1, tab2 = st.tabs(['Приложение', 'Кнопка нажата'])
    with tab1:
        st.image('images_4/img_4_8_1.png', width="content")
    with tab2:
        st.image('images_4/img_4_8_2.png', width="content")

def run_4_9():
    st.markdown('###### 🐍 Виджет Camera 🥝')
    tab1, tab2 = st.tabs(['Приложение', 'Камера активирована'])
    with tab1:
        st.image('images_4/img_4_9_1.png', width="content")
    with tab2:
        st.image('images_4/img_4_9_2.png', width="content")

def run_4_10():
    st.markdown('###### 🐍 Виджет Camera (с KV) 🥝')
    tab1, tab2 = st.tabs(['Приложение', 'Камера активирована'])
    with tab1:
        st.image('images_4/img_4_9_1.png', width="content")
    with tab2:
        st.image('images_4/img_4_9_2.png', width="content")

def run_4_11():
    st.markdown('###### 🐍 Виджет Canvas 🥝')
    st.image('images_4/img_4_11.png', width="content")

def run_4_12():
    st.markdown('###### 🐍 Виджет Canvas (с KV) 🥝')
    st.image('images_4/img_4_12.png', width="content")

def run_4_13():
    st.markdown('###### 🐍 Виджет Carousel (листание слайдов) 🥝')
    col1, col2 = st.columns(2)
    with col1:
        st.image('images_4/img_4_13_1.png', width="content")
    with col2:
        st.image('images_4/img_4_13_2.png', width="content")
    col3, col4 = st.columns(2)
    with col3:
        st.image('images_4/img_4_13_3.png', width="content")
    with col4:
        st.image('images_4/img_4_13_4.png', width="content")

def run_4_14():
    st.markdown('###### 🐍 Виджет Carousel (с KV) 🥝')
    col1, col2 = st.columns(2)
    with col1:
        st.image('images_4/img_4_14_1.png', width="content")
    with col2:
        st.image('images_4/img_4_14_2.png', width="content")
    col3, col4 = st.columns(2)
    with col3:
        st.image('images_4/img_4_14_3.png', width="content")
    with col4:
        st.image('images_4/img_4_14_4.png', width="content")

def run_4_15():
    st.markdown('###### 🐍 Виджет Checkbox 🥝')
    col1, col2 = st.columns(2)
    with col1:
        st.image('images_4/img_4_15_1.png', width="content")
    with col2:
        st.image('images_4/img_4_15_2.png', width="content")

def run_4_16():
    st.markdown('###### 🐍 Виджет Checkbox (с KV) 🥝')
    col1, col2 = st.columns(2)
    with col1:
        st.image('images_4/img_4_15_1.png', width="content")
    with col2:
        st.image('images_4/img_4_15_2.png', width="content")

def run_4_17():
    st.markdown('###### 🐍 Виджет CodeInput 🥝')
    st.image('images_4/img_4_17.png', width="content")

def run_4_18():
    st.markdown('###### 🐍 Виджет ColorPicker 🥝')
    tab1, tab2, tab3 = st.tabs(['Приложение',
                                'ColorPicker',
                                'Выбран цвет'])
    with tab1:
        st.image('images_4/img_4_18_1.png', width="content")
    with tab2:
        st.image('images_4/img_4_18_2.png', width="content")
    with tab3:
        st.image('images_4/img_4_18_3.png', width="content")

def run_4_19():
    st.markdown('###### 🐍 Виджет DropDown 🥝')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('images_4/img_4_19_1.png', width="content")
    with col2:
        st.image('images_4/img_4_19_2.png', width="content")
    with col3:
        st.image('images_4/img_4_19_3.png', width="content")

def run_4_20():
    st.markdown('###### 🐍 Виджет DropDown 🥝')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('images_4/img_4_20_1.png', width="content")
    with col2:
        st.image('images_4/img_4_20_2.png', width="content")
    with col3:
        st.image('images_4/img_4_20_3.png', width="content")

def run_4_21():
    st.markdown('###### 🐍 Виджет Filechooser 🥝')
    st.image('images_4/img_4_21.png', width="content")

def run_4_23():
    st.markdown('###### 🐍 Виджет Image (с KV) 🥝')
    col1, col2 = st.columns(2)
    with col1:
        st.image('images_4/img_4_23_1.png', width="content")
    with col2:
        st.image('images_4/img_4_23_2.png', width="content")
    col3, col4 = st.columns(2)
    with col3:
        st.image('images_4/img_4_23_3.png', width="content")
    with col4:
        st.image('images_4/img_4_23_4.png', width="content")

def run_4_24():
    st.markdown('###### 🐍 Виджет Label 🥝')
    st.image('images_4/img_4_24.png', width="content")

def run_4_25():
    st.markdown('###### 🐍 Виджет Label 🥝')
    st.image('images_4/img_4_24.png', width="content")

def run_4_26():
    st.markdown('###### 🐍 Виджет ScrollView 🥝')
    st.image('images_4/img_4_26.png', width="content")

def run_4_27():
    st.markdown('###### 🐍 Виджет ScrollView 🥝')
    st.image('images_4/img_4_27.png', width="content")

def run_4_28():
    st.markdown('###### 🐍 Виджет Carousel 🥝')
    col1, col2 = st.columns(2)
    with col1:
        st.image('images_4/img_4_28_1.png', width="content")
    with col2:
        st.image('images_4/img_4_28_2.png', width="content")

def run_4_29():
    st.markdown('###### 🐍 Виджет Carousel 🥝')
    col1, col2 = st.columns(2)
    with col1:
        st.image('images_4/img_4_29_1.png', width="content")
    with col2:
        st.image('images_4/img_4_29_2.png', width="content")

def run_4_30():
    st.markdown('###### 🐍 Виджет Button 🥝')
    col1, col2 = st.columns(2)
    with col1:
        st.image('images_4/img_4_30_1.png', width="content")
    with col2:
        st.image('images_4/img_4_30_2.png', width="content")

def run_4_31():
    st.markdown('###### 🐍 Виджет Screen 🥝')
    tab1, tab2, tab3 = st.tabs(['Экран 1',
                                'Экран 2',
                                'Экран 3'])
    with tab1:
        st.image('images_4/img_4_31_1.png', width="content")
    with tab2:
        st.image('images_4/img_4_31_2.png', width="content")
    with tab3:
        st.image('images_4/img_4_31_3.png', width="content")

def run_4_32():
    st.markdown('###### 🐍 Виджет Window 🥝')
    tab1, tab2, tab3 = st.tabs(['Экран по умолчанию',
                                'Экран 360х600',
                                'Экран 600х360'])
    with tab1:
        st.image('images_4/img_4_32_1.png', width="content")
    with tab2:
        st.image('images_4/img_4_32_2.png', width="content")
    with tab3:
        st.image('images_4/img_4_32_3.png', width="content")


if __name__ == '__main__':
    run_4_1()