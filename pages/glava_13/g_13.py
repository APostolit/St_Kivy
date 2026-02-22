import streamlit as st
import fun_g13

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 13", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 13")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 13",
        ("Листинг 13.1", "Листинг 13.2", "Листинг 13.3", "Листинг 13.4", "Листинг 13.5",
         "Листинг 13.6", "Листинг 13.7", "Листинг 13.8", "Листинг 13.9", "Листинг 13.10",
         "Листинг 13.11", "Листинг 13.12",),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container(width=800)
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 13.1":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/',
                     label='🛠️ Приложение "Калькулятор"')
        path = 'pages/glava_13/Listing_13_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=800)
        with st.expander("🔍 Показать результат", width=600):
            fun_g13.run_13_1()

    elif options == "Листинг 13.2":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/',
                     label='🛠️ Калькулятор - файл на Python')
        path = 'pages/glava_13/Listing_13_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=550):
            fun_g13.run_13_2()

    elif options == "Листинг 13.3":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/',
                     label='🛠️ Калькулятор - файл на Kivy')
        path = 'pages/glava_13/calculator.kv'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=550):
            fun_g13.run_13_3()

    elif options == "Листинг 13.4":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/',
                     label='🛠️ Магазин "Пицца", Kivy')
        path = 'pages/glava_13/Pizza_Delivery.kv'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=700)
        with st.expander("🔍 Показать результат", width=400):
            fun_g13.run_13_4()

    elif options == "Листинг 13.5":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/',
                     label='🛠️ Магазин "Пицца", Python')
        path = 'pages/glava_13/Listing_13_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=700)
        with st.expander("🔍 Показать результат", width=400):
            fun_g13.run_13_5()

    elif options == "Листинг 13.6":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/',
                     label='🛠️ Магазин "ЭЛЕКТРОН" - Python+Kivy')
        path = 'pages/glava_13/Listing_13_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=560)
        with st.expander("🔍 Показать результат", width=400):
            fun_g13.run_13_6()

    elif options == "Листинг 13.7":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/',
                     label='🛠️ Приложение Sopping, базовый модуль - Python')
        path = 'pages/glava_13/Listing_13_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=780)
        with st.expander("🔍 Показать результат", width=400):
            fun_g13.run_13_7()

    elif options == "Листинг 13.8":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/',
                     label='🛠️ Приложение Sopping, менеджер БД - Python')
        path = 'pages/glava_13/data_manage.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=780)
        with st.expander("🔍 Показать результат", width=400):
            fun_g13.run_13_8()

    elif options == "Листинг 13.9":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/',
                     label='🛠️ Приложение Sopping, модуль разметки на Kivy')
        path = 'pages/glava_13/NotePad.kv'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=350):
            fun_g13.run_13_9()

    elif options == "Листинг 13.10":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/',
                     label='🛠️ Приложение Видеопроигрыватель')
        path = 'pages/glava_13/Listing_13_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=500):
            fun_g13.run_13_10()