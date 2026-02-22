import streamlit as st
import fun_g5

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 5", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 5")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 5",
        ("Листинг 5.1", "Листинг 5.2", "Листинг 5.3", "Листинг 5.4", "Листинг 5.5",
         "Листинг 5.6", "Листинг 5.7", "Листинг 5.8", "Листинг 5.9", "Листинг 5.10",
         "Листинг 5.11", "Листинг 5.12", "Листинг 5.13", "Листинг 5.14", "Листинг 5.15",
         "Листинг 5.16", "Листинг 5.17", ),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container(width=800)
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 5.1":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-line.htm', label='🛠️ Свойства Line')
        path = 'pages/glava_5/Listing_5_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=350):
            fun_g5.run_5_1()

    elif options == "Листинг 5.2":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-line.htm', label='🛠️ Свойства Line')
        path = 'pages/glava_5/Listing_5_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=350):
            fun_g5.run_5_2()

    elif options == "Листинг 5.3":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-modal-view.htm', label='🛠️ Свойства ModalView')
        path = 'pages/glava_5/Listing_5_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=620)
        with st.expander("🔍 Показать результат", width=600):
            fun_g5.run_5_3()

    elif options == "Листинг 5.4":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-modal-view.htm', label='🛠️ Свойства ModalView')
        path = 'pages/glava_5/Listing_5_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=600):
            fun_g5.run_5_4()

    elif options == "Листинг 5.5":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-popup.htm', label='🛠️ Свойства Popup')
        path = 'pages/glava_5/Listing_5_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=700):
            fun_g5.run_5_5()

    elif options == "Листинг 5.6":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-progress-bar.htm', label='🛠️ Свойства ProgressBar')
        path = 'pages/glava_5/Listing_5_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=500):
            fun_g5.run_5_6()

    elif options == "Листинг 5.7":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-progress-bar.htm', label='🛠️ Свойства ProgressBar')
        path = 'pages/glava_5/Listing_5_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=500):
            fun_g5.run_5_7()

    elif options == "Листинг 5.8":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-restructuredtext.htm', label='🛠️ Свойства RstDocument')
        path = 'pages/glava_5/Listing_5_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=600):
            fun_g5.run_5_8()

    elif options == "Листинг 5.9":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-scatter.htm', label='🛠️ Свойства Scatter')
        path = 'pages/glava_5/Listing_5_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=600):
            fun_g5.run_5_9()

    elif options == "Листинг 5.10":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-scatter.htm', label='🛠️ Свойства Scatter')
        path = 'pages/glava_5/Listing_5_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=600):
            fun_g5.run_5_10()

    elif options == "Листинг 5.11":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-scrollview.htm', label='🛠️ Свойства ScrollView')
        path = 'pages/glava_5/Listing_5_11.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=620)
        with st.expander("🔍 Показать результат", width=300):
            fun_g5.run_5_11()

    elif options == "Листинг 5.12":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-scrollview.htm', label='🛠️ Свойства ScrollView')
        path = 'pages/glava_5/Listing_5_12.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=300):
            fun_g5.run_5_12()

    elif options == "Листинг 5.13":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-slider.htm', label='🛠️ Свойства Slider')
        path = 'pages/glava_5/Listing_5_13.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=500):
            fun_g5.run_5_13()

    elif options == "Листинг 5.14":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-slider.htm', label='🛠️ Свойства Slider')
        path = 'pages/glava_5/Listing_5_14.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=500):
            fun_g5.run_5_14()

    elif options == "Листинг 5.15":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-audio.htm', label='🛠️ Свойства SoundLoader')
        path = 'pages/glava_5/Listing_5_15.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=560)
        with st.expander("🔍 Показать результат", width=800):
            fun_g5.run_5_15()

    elif options == "Листинг 5.16":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-spinner.htm', label='🛠️ Свойства Spinner')
        path = 'pages/glava_5/Listing_5_16.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=660)
        with st.expander("🔍 Показать результат", width=390):
            fun_g5.run_5_16()

    elif options == "Листинг 5.17":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-tabbed-panel.htm', label='🛠️ Свойства TabbedPanel')
        path = 'pages/glava_5/Listing_5_17.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=420):
            fun_g5.run_5_17()


