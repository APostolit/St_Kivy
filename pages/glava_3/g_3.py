import streamlit as st
import fun_g3

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 3", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 3")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 3",
        ("Листинг 3.1", "Листинг 3.2", "Листинг 3.3", "Листинг 3.4", "Листинг 3.5",
         "Листинг 3.6", "Листинг 3.7", "Листинг 3.8", "Листинг 3.9", "Листинг 3.10",
         "Листинг 3.11", "Листинг 3.12", "Листинг 3.13", "Листинг 3.14", "Листинг 3.15",
         "Листинг 3.16", "Листинг 3.17", "Листинг 3.18", "Листинг 3.19", "Листинг 3.20",
         "Листинг 3.21", "Листинг 3.22", "Листинг 3.23", "Листинг 3.24", "Листинг 3.25",
         "Листинг 3.26", "Листинг 3.27",
         ),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container(width=800)
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 3.1":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-anchor-layout.htm', label='🛠️ Свойства AnchorLayout')
        path = 'pages/glava_3/Listing_3_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=610)
        with st.expander("🔍 Показать результат", width=420):
            fun_g3.run_3_1()

    elif options == "Листинг 3.2":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-anchor-layout.htm', label='🛠️ Свойства AnchorLayout')
        path = 'pages/glava_3/Listing_3_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=420)
        with st.expander("🔍 Показать результат", width=400):
            fun_g3.run_3_2()

    elif options == "Листинг 3.3":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-anchor-layout.htm', label='🛠️ Свойства AnchorLayout')
        path = 'pages/glava_3/Listing_3_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=420)
        with st.expander("🔍 Показать результат", width=400):
            fun_g3.run_3_3()

    elif options == "Листинг 3.4":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-box-layouts.htm', label='🛠️ Свойства BoxLayout')
        path = 'pages/glava_3/Listing_3_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=510)
        with st.expander("🔍 Показать результат", width=400):
            fun_g3.run_3_4()

    elif options == "Листинг 3.5":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-box-layouts.htm', label='🛠️ Свойства BoxLayout')
        path = 'pages/glava_3/Listing_3_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=400):
            fun_g3.run_3_5()

    elif options == "Листинг 3.6":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-box-layouts.htm', label='🛠️ Свойства BoxLayout')
        path = 'pages/glava_3/Listing_3_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=320):
            fun_g3.run_3_6()

    elif options == "Листинг 3.7":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-float-layout.htm', label='🛠️ Свойства FloatLayout')
        path = 'pages/glava_3/Listing_3_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=420)
        with st.expander("🔍 Показать результат", width=400):
            fun_g3.run_3_7()

    elif options == "Листинг 3.8":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-float-layout.htm', label='🛠️ Свойства FloatLayout')
        path = 'pages/glava_3/Listing_3_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=370):
            fun_g3.run_3_8()

    elif options == "Листинг 3.9":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-float-layout.htm', label='🛠️ Свойства FloatLayout')
        path = 'pages/glava_3/Listing_3_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=370):
            fun_g3.run_3_9()

    elif options == "Листинг 3.10":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-grid-layouts.htm', label='🛠️ Свойства GridLayout')
        path = 'pages/glava_3/Listing_3_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=430)
        with st.expander("🔍 Показать результат", width=390):
            fun_g3.run_3_10()

    elif options == "Листинг 3.11":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-grid-layouts.htm', label='🛠️ Свойства GridLayout')
        path = 'pages/glava_3/Listing_3_11.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=390):
            fun_g3.run_3_11()

    elif options == "Листинг 3.12":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-grid-layouts.htm', label='🛠️ Свойства GridLayout')
        path = 'pages/glava_3/Listing_3_12.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=390):
            fun_g3.run_3_12()

    elif options == "Листинг 3.13":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-page-layout.htm', label='🛠️ Свойства PageLayout')
        path = 'pages/glava_3/Listing_3_13.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=420)
        with st.expander("🔍 Показать результат", width=600):
            fun_g3.run_3_13()

    elif options == "Листинг 3.14":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-page-layout.htm', label='🛠️ Свойства PageLayout')
        path = 'pages/glava_3/Listing_3_14.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=600):
            fun_g3.run_3_14()

    elif options == "Листинг 3.15":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-relative-layout.htm', label='🛠️ Свойства RelativeLayout')
        path = 'pages/glava_3/Listing_3_15.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=430):
            fun_g3.run_3_15()

    elif options == "Листинг 3.16":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-relative-layout.htm', label='🛠️ Свойства RelativeLayout')
        path = 'pages/glava_3/Listing_3_16.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=300):
            fun_g3.run_3_16()

    elif options == "Листинг 3.17":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-scatter.htm', label='🛠️ Свойства Scatter')
        path = 'pages/glava_3/Listing_3_17.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=600):
            fun_g3.run_3_17()

    elif options == "Листинг 3.18":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-scatter.htm', label='🛠️ Свойства Scatter')
        path = 'pages/glava_3/Listing_3_18.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=400):
            fun_g3.run_3_18()

    elif options == "Листинг 3.19":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-scatter.htm', label='🛠️ Свойства Scatter')
        path = 'pages/glava_3/Listing_3_19.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=500):
            fun_g3.run_3_19()

    elif options == "Листинг 3.20":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-scatter.htm', label='🛠️ Свойства Scatter')
        path = 'pages/glava_3/Listing_3_20.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=500):
            fun_g3.run_3_20()

    elif options == "Листинг 3.21":
        st.page_link('https://kivy.org/doc/stable/api-kivy.uix.scatterlayout.html', label='🛠️ Свойства ScatterLayout')
        path = 'pages/glava_3/Listing_3_21.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=500):
            fun_g3.run_3_21()

    elif options == "Листинг 3.22":
        st.page_link('https://kivy.org/doc/stable/api-kivy.uix.scatterlayout.html', label='🛠️ Свойства ScatterLayout')
        path = 'pages/glava_3/Listing_3_22.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=500):
            fun_g3.run_3_22()

    elif options == "Листинг 3.23":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-stack-layout.htm', label='🛠️ Свойства StackLayout')
        path = 'pages/glava_3/Listing_3_23.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=450):
            fun_g3.run_3_23()

    elif options == "Листинг 3.24":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-stack-layout.htm', label='🛠️ Свойства StackLayout')
        path = 'pages/glava_3/Listing_3_24.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=450):
            fun_g3.run_3_24()

    elif options == "Листинг 3.25":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-stack-layout.htm', label='🛠️ Свойства StackLayout')
        path = 'pages/glava_3/Listing_3_25.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=270):
            fun_g3.run_3_25()

    elif options == "Листинг 3.26":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-stencil-view.htm', label='🛠️ Свойства StencilView')
        path = 'pages/glava_3/Listing_3_26.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=400):
            fun_g3.run_3_26()

    elif options == "Листинг 3.27":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-stencil-view.htm', label='🛠️ Свойства StencilView')
        path = 'pages/glava_3/Listing_3_27.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=400):
            fun_g3.run_3_27()

    elif options == "Листинг 3.32":
        path = 'pages/glava_3/Listing_3_32.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=420)
        with st.expander("🔍 Показать результат", width=450):
            fun_g3.run_3_32()

    elif options == "Листинг 3.33":
        path = 'pages/glava_3/Listing_3_33.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=420)
        with st.expander("🔍 Показать результат", width=450):
            fun_g3.run_3_33()

    elif options == "Листинг 3.34":
        path = 'pages/glava_3/Listing_3_34.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=420)
        with st.expander("🔍 Показать результат", width=450):
            fun_g3.run_3_34()

    elif options == "Листинг 3.35":
        path = 'pages/glava_3/Listing_3_35.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=450):
            fun_g3.run_3_35()

    elif options == "Листинг 3.36":
        path = 'pages/glava_3/Listing_3_36.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=400):
            fun_g3.run_3_36()
