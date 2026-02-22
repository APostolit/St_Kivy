import streamlit as st
import fun_g4

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 4", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 4")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 4",
        ("Листинг 4.1", "Листинг 4.2", "Листинг 4.3", "Листинг 4.4", "Листинг 4.5",
         "Листинг 4.6", "Листинг 4.7", "Листинг 4.8", "Листинг 4.9", "Листинг 4.10",
         "Листинг 4.11", "Листинг 4.12", "Листинг 4.13", "Листинг 4.14", "Листинг 4.15",
         "Листинг 4.16", "Листинг 4.17", "Листинг 4.18", "Листинг 4.19", "Листинг 4.20",
         "Листинг 4.21", "Листинг 4.23", "Листинг 4.24", "Листинг 4.25", "Листинг 4.26",
         "Листинг 4.27", "Листинг 4.28", "Листинг 4.29", "Листинг 4.30", "Листинг 4.31",
         "Листинг 4.32"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container(width=800)
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 4.1":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-accordion.htm', label='🛠️ Свойства Accordion')
        path = 'pages/glava_4/Listing_4_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=410):
            fun_g4.run_4_1()

    elif options == "Листинг 4.2":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-accordion.htm', label='🛠️ Свойства Accordion')
        path = 'pages/glava_4/Listing_4_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=700):
            fun_g4.run_4_2()

    elif options == "Листинг 4.3":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-action-bar.htm', label='🛠️ Свойства ActionBar')
        path = 'pages/glava_4/Listing_4_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=550):
            fun_g4.run_4_3()

    elif options == "Листинг 4.4":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-action-bar.htm', label='🛠️ Свойства ActionBar')
        path = 'pages/glava_4/Listing_4_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=550):
            fun_g4.run_4_4()

    elif options == "Листинг 4.5":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-bubble.htm', label='🛠️ Свойства Bubble')
        path = 'pages/glava_4/Listing_4_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=620)
        with st.expander("🔍 Показать результат", width=350):
            fun_g4.run_4_5()

    elif options == "Листинг 4.6":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-bubble.htm', label='🛠️ Свойства Bubble')
        path = 'pages/glava_4/Listing_4_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=530)
        with st.expander("🔍 Показать результат", width=350):
            fun_g4.run_4_6()

    elif options == "Листинг 4.7":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-buttons.htm', label='🛠️ Свойства Button')
        path = 'pages/glava_4/Listing_4_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=350):
            fun_g4.run_4_7()

    elif options == "Листинг 4.8":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-buttons.htm', label='🛠️ Свойства Button')
        path = 'pages/glava_4/Listing_4_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=350):
            fun_g4.run_4_8()

    elif options == "Листинг 4.9":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-camera.htm', label='🛠️ Свойства Camera')
        path = 'pages/glava_4/Listing_4_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=560)
        with st.expander("🔍 Показать результат", width=350):
            fun_g4.run_4_9()

    elif options == "Листинг 4.10":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-camera.htm', label='🛠️ Свойства Camera')
        path = 'pages/glava_4/Listing_4_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=540)
        with st.expander("🔍 Показать результат", width=350):
            fun_g4.run_4_10()

    elif options == "Листинг 4.11":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-canvas.htm', label='🛠️ Свойства Canvas')
        path = 'pages/glava_4/Listing_4_11.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=570)
        with st.expander("🔍 Показать результат", width=450):
            fun_g4.run_4_11()

    elif options == "Листинг 4.12":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-canvas.htm', label='🛠️ Свойства Canvas')
        path = 'pages/glava_4/Listing_4_12.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=380)
        with st.expander("🔍 Показать результат", width=450):
            fun_g4.run_4_12()

    elif options == "Листинг 4.13":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-carousel.htm', label='🛠️ Свойства Carousel')
        path = 'pages/glava_4/Listing_4_13.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=470)
        with st.expander("🔍 Показать результат", width=450):
            fun_g4.run_4_13()

    elif options == "Листинг 4.14":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-carousel.htm', label='🛠️ Свойства Carousel')
        path = 'pages/glava_4/Listing_4_14.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=470)
        with st.expander("🔍 Показать результат", width=450):
            fun_g4.run_4_14()

    elif options == "Листинг 4.15":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-checkbox.htm', label='🛠️ Свойства Checkbox')
        path = 'pages/glava_4/Listing_4_15.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=600):
            fun_g4.run_4_15()

    elif options == "Листинг 4.16":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-checkbox.htm', label='🛠️ Свойства Checkbox')
        path = 'pages/glava_4/Listing_4_16.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=600):
            fun_g4.run_4_16()

    elif options == "Листинг 4.17":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-code-input.htm', label='🛠️ Свойства CodeInput')
        path = 'pages/glava_4/Listing_4_17.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=510)
        with st.expander("🔍 Показать результат", width=600):
            fun_g4.run_4_17()

    elif options == "Листинг 4.18":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-color-picker.htm', label='🛠️ Свойства ColorPicker')
        path = 'pages/glava_4/Listing_4_18.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=520)
        with st.expander("🔍 Показать результат", width=500):
            fun_g4.run_4_18()

    elif options == "Листинг 4.19":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-dropdown-list.htm', label='🛠️ Свойства DropDown')
        path = 'pages/glava_4/Listing_4_19.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=700)
        with st.expander("🔍 Показать результат", width=700):
            fun_g4.run_4_19()

    elif options == "Листинг 4.20":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-dropdown-list.htm', label='🛠️ Свойства DropDown')
        path = 'pages/glava_4/Listing_4_20.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=700):
            fun_g4.run_4_20()

    elif options == "Листинг 4.21":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-file-chooser.htm', label='🛠️ Свойства Filechooser')
        tab1, tab2 = st.tabs(['Код на Python', 'Код на Kivy'])
        with tab1:
            path = 'pages/glava_4/Listing_4_21.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True, width=430)
        with tab2:
            path = 'pages/glava_4/Listing_4_22.kv'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True, width=490)
        with st.expander("🔍 Показать результат", width=600):
            fun_g4.run_4_21()

    elif options == "Листинг 4.23":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-images.htm', label='🛠️ Свойства Image')
        path = 'pages/glava_4/Listing_4_23.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=600):
            fun_g4.run_4_23()

    elif options == "Листинг 4.24":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-label.htm', label='🛠️ Свойства Label')
        path = 'pages/glava_4/Listing_4_24.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=510)
        with st.expander("🔍 Показать результат", width=380):
            fun_g4.run_4_24()

    elif options == "Листинг 4.25":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-label.htm', label='🛠️ Свойства Label')
        path = 'pages/glava_4/Listing_4_25.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=380):
            fun_g4.run_4_25()

    elif options == "Листинг 4.26":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-scrollview.htm', label='🛠️ Свойства ScrollView')
        path = 'pages/glava_4/Listing_4_26.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=350):
            fun_g4.run_4_26()

    elif options == "Листинг 4.27":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-scrollview.htm', label='🛠️ Свойства ScrollView')
        path = 'pages/glava_4/Listing_4_27.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=300):
            fun_g4.run_4_27()

    elif options == "Листинг 4.28":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-carousel.htm', label='🛠️ Свойства Carousel')
        path = 'pages/glava_4/Listing_4_28.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=600):
            fun_g4.run_4_28()

    elif options == "Листинг 4.29":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-carousel.htm', label='🛠️ Свойства Carousel')
        path = 'pages/glava_4/Listing_4_29.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=600):
            fun_g4.run_4_29()

    elif options == "Листинг 4.30":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-buttons.htm', label='🛠️ Свойства Button')
        path = 'pages/glava_4/Listing_4_30.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=500):
            fun_g4.run_4_30()

    elif options == "Листинг 4.31":
        st.page_link('https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html', label='🛠️ Свойства Screen')
        path = 'pages/glava_4/Listing_4_31.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=400):
            fun_g4.run_4_31()

    elif options == "Листинг 4.32":
        st.page_link('https://kivy.org/doc/stable/api-kivy.core.window.html', label='🛠️ Свойства Window ')
        path = 'pages/glava_4/Listing_4_32.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=500):
            fun_g4.run_4_32()


