import streamlit as st
import fun_g6

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 6", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 6")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 6",
        ("Листинг 6.1", "Листинг 6.2", "Листинг 6.3", "Листинг 6.4", "Листинг 6.5",
         "Листинг 6.6", "Листинг 6.7", "Листинг 6.8", "Листинг 6.9", "Листинг 6.10",
         "Листинг 6.12", "Листинг 6.14", "Листинг 6.15", "Листинг 6.16"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container(width=800)
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 6.1":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-splitter.htm', label='🛠️ Свойства Splitter')
        path = 'pages/glava_6/Listing_6_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=600):
            fun_g6.run_6_1()

    elif options == "Листинг 6.2":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-splitter.htm', label='🛠️ Свойства Splitter')
        path = 'pages/glava_6/Listing_6_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=400):
            fun_g6.run_6_2()

    elif options == "Листинг 6.3":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-stencil-view.htm', label='🛠️ Свойства StencilView')
        path = 'pages/glava_6/Listing_6_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=610)
        with st.expander("🔍 Показать результат", width=500):
            fun_g6.run_6_3()

    elif options == "Листинг 6.4":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-stencil-view.htm', label='🛠️ Свойства StencilView')
        path = 'pages/glava_6/Listing_6_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=620)
        with st.expander("🔍 Показать результат", width=500):
            fun_g6.run_6_4()

    elif options == "Листинг 6.5":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-switch.htm', label='🛠️ Свойства Switch')
        path = 'pages/glava_6/Listing_6_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=500):
            fun_g6.run_6_5()

    elif options == "Листинг 6.6":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-text.htm', label='🛠️ Свойства Text')
        path = 'pages/glava_6/Listing_6_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=500):
            fun_g6.run_6_6()

    elif options == "Листинг 6.7":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-text-markup.htm', label='🛠️ Свойства markup')
        path = 'pages/glava_6/Listing_6_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=450):
            fun_g6.run_6_7()

    elif options == "Листинг 6.8":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-text-input.htm', label='🛠️ Виджет TextInput')
        path = 'pages/glava_6/Listing_6_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=450):
            fun_g6.run_6_8()

    elif options == "Листинг 6.9":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-toggle-button.htm', label='🛠️ Виджет ToggleButton')
        path = 'pages/glava_6/Listing_6_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=620)
        with st.expander("🔍 Показать результат", width=430):
            fun_g6.run_6_9()

    elif options == "Листинг 6.10":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-toggle-button.htm', label='🛠️ Виджет ToggleButton')
        tab1, tab2 = st.tabs(['Код на Python', 'Код на Kivy'])
        with tab1:
            path = 'pages/glava_6/Listing_6_10.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True, width=430)
        with tab2:
            path = 'pages/glava_6/Listing_6_11.kv'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True, width=490)
        with st.expander("🔍 Показать результат", width=380):
            fun_g6.run_6_10()

    elif options == "Листинг 6.12":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-touch-ripple.htm',
                     label='🛠️ Элемент TouchRippleBehavior')
        tab1, tab2 = st.tabs(['Код на Python', 'Код на Kivy'])
        with tab1:
            path = 'pages/glava_6/Listing_6_12.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True, width=580)
        with tab2:
            path = 'pages/glava_6/Listing_6_13.kv'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True, width=490)
        with st.expander("🔍 Показать результат", width=600):
            fun_g6.run_6_12()

    elif options == "Листинг 6.14":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-tree-view.htm', label='🛠️ Виджет TreeView')
        path = 'pages/glava_6/Listing_6_14.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=680)
        with st.expander("🔍 Показать результат", width=680):
            fun_g6.run_6_14()

    elif options == "Листинг 6.15":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-videos.htm', label='🛠️ Виджет Video')
        path = 'pages/glava_6/Listing_6_15.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=480)
        with st.expander("🔍 Показать результат", width=570):
            fun_g6.run_6_15()

    elif options == "Листинг 6.16":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-video-player.htm', label='🛠️ Виджет VideoPlayer')
        tab1, tab2 = st.tabs(['Код на Python', 'Файл - Dictor.jsa'])
        with tab1:
            path = 'pages/glava_6/Listing_6_16.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True, width=450)
        with tab2:
            path = 'pages/glava_6/Dictor.jsa'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=600):
            fun_g6.run_6_16()

    elif options == "Листинг 6.17":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-windows.htm', label='🛠️ Виджет Window')
        path = 'pages/glava_6/Listing_6_17.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=570):
            fun_g6.run_6_17()

    elif options == "Листинг 6.18":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-carousel.htm', label='🛠️ Виджет Carousel')
        path = 'pages/glava_6/Listing_6_18.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=470):
            fun_g6.run_6_18()

    elif options == "Листинг 6.19":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-carousel.htm', label='🛠️ Виджет Carousel')
        path = 'pages/glava_6/Listing_6_19.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=470):
            fun_g6.run_6_19()

    elif options == "Листинг 6.20":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-buttons.htm', label='🛠️ Виджет Button')
        path = 'pages/glava_6/Listing_6_20.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=470):
            fun_g6.run_6_20()

    elif options == "Листинг 6.21":
        st.page_link('https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html', label='🛠️ Элемент Screen Manager')
        path = 'pages/glava_6/Listing_6_21.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=400):
            fun_g6.run_6_21()