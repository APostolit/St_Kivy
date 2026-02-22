import streamlit as st
import fun_g10

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 10", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 10")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 10",
        ("Листинг 10.1", "Листинг 10.2", "Листинг 10.3", "Листинг 10.4", "Листинг 10.5",
         "Листинг 10.6", "Листинг 10.7", "Листинг 10.8", "Листинг 10.9", "Листинг 10.10",
         "Листинг 10.11", "Листинг 10.12", "Листинг 10.13", "Листинг 10.14", "Листинг 10.15",
         "Листинг 10.16", "Листинг 10.17", "Листинг 10.18", "Листинг 10.19", "Листинг 10.20",
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

    elif options == "Листинг 10.1":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/dropdown-item/',
                     label='🛠️ Виджет DropdownItem')
        path = 'pages/glava_10/Listing_10_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=500):
            fun_g10.run_10_1()

    elif options == "Листинг 10.2":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/expansion-panel/',
                     label='🛠️ MDExpansionPanel')
        path = 'pages/glava_10/Listing_10_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=600):
            fun_g10.run_10_2()

    elif options == "Листинг 10.3":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/file-manager/',
                     label='🛠️ MDFileManager')
        path = 'pages/glava_10/Listing_10_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=700):
            fun_g10.run_10_3()

    elif options == "Листинг 10.4":
        st.page_link('https://kivymd.readthedocs.io/en/latest/components/fitimage/',
                     label='🛠️ FitImage')
        path = 'pages/glava_10/Listing_10_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=300):
            fun_g10.run_10_4()

    elif options == "Листинг 10.5":
        st.page_link('https://kivymd.readthedocs.io/en/latest/components/fitimage/',
                     label='🛠️ FitImage')
        path = 'pages/glava_10/Listing_10_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=300):
            fun_g10.run_10_5()

    elif options == "Листинг 10.6":
        st.page_link('https://kivy.org/doc/stable/api-kivy.uix.image.html',
                     label='🛠️ Image')
        path = 'pages/glava_10/Listing_10_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=300):
            fun_g10.run_10_6()

    elif options == "Листинг 10.7":
        st.page_link('https://kivy.org/doc/stable/api-kivy.uix.image.html',
                     label='🛠️ Image')
        path = 'pages/glava_10/Listing_10_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=250):
            fun_g10.run_10_7()

    elif options == "Листинг 10.8":
        st.page_link('https://kivymd.readthedocs.io/en/latest/components/imagelist/',
                     label='🛠️ ImageList')
        path = 'pages/glava_10/Listing_10_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=700):
            fun_g10.run_10_8()

    elif options == "Листинг 10.9":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/label/',
                     label='🛠️ MDLabel')
        path = 'pages/glava_10/Listing_10_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=300):
            fun_g10.run_10_9()

    elif options == "Листинг 10.10":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/label/',
                     label='🛠️ MDIcon')
        path = 'pages/glava_10/Listing_10_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=300):
            fun_g10.run_10_10()

    elif options == "Листинг 10.11":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/list/',
                     label='🛠️ Виджет MDList')
        path = 'pages/glava_10/Listing_10_11.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=300):
            fun_g10.run_10_11()

    elif options == "Листинг 10.12":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/list/',
                     label='🛠️ Виджет MDList')
        path = 'pages/glava_10/Listing_10_12.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=600):
            fun_g10.run_10_12()

    elif options == "Листинг 10.13":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/list/',
                     label='🛠️ Виджет MDList')
        path = 'pages/glava_10/Listing_10_13.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=600):
            fun_g10.run_10_13()

    elif options == "Листинг 10.14":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/list/',
                     label='🛠️ Виджет MDList')
        path = 'pages/glava_10/Listing_10_14.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=600):
            fun_g10.run_10_14()

    elif options == "Листинг 10.15":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/list/',
                     label='🛠️ Виджет MDList')
        path = 'pages/glava_10/Listing_10_15.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=700):
            fun_g10.run_10_15()

    elif options == "Листинг 10.16":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/menu/',
                     label='🛠️ Виджет MDDropdownMenu')
        path = 'pages/glava_10/Listing_10_16.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=750)
        with st.expander("🔍 Показать результат", width=700):
            fun_g10.run_10_16()

    elif options == "Листинг 10.17":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/menu/',
                     label='🛠️ Виджет MDDropdownMenu')
        path = 'pages/glava_10/Listing_10_17.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=750)
        with st.expander("🔍 Показать результат", width=700):
            fun_g10.run_10_17()

    elif options == "Листинг 10.18":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/menu/',
                     label='🛠️ Виджет MDDropdownMenu')
        path = 'pages/glava_10/Listing_10_18.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=750)
        with st.expander("🔍 Показать результат", width=700):
            fun_g10.run_10_18()

    elif options == "Листинг 10.19":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/menu/',
                     label='🛠️ Виджет MDDropdownMenu')
        path = 'pages/glava_10/Listing_10_19.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=750)
        with st.expander("🔍 Показать результат", width=800):
            fun_g10.run_10_19()

    elif options == "Листинг 10.20":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/menu/',
                     label='🛠️ Виджет MDDropdownMenu')
        path = 'pages/glava_10/Listing_10_20.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=750)
        with st.expander("🔍 Показать результат", width=800):
            fun_g10.run_10_20()