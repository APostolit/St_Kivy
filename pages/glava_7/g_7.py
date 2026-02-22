import streamlit as st
import fun_g7

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 7", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 7")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 7",
        ("Листинг 7.1", "Листинг 7.2", "Листинг 7.3", "Листинг 7.4", "Листинг 7.5",
         "Листинг 7.6", "Листинг 7.7", "Листинг 7.8", "Листинг 7.9", "Листинг 7.10",
         "Листинг 7.11"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container(width=800)
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 7.1":
        st.page_link('https://kivymd.readthedocs.io/en/latest/getting-started/', label='🛠️ Приложения с KivyMD')
        path = 'pages/glava_7/Listing_7_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=610)
        with st.expander("🔍 Показать результат", width=390):
            fun_g7.run_7_1()

    elif options == "Листинг 7.2":
        st.page_link('https://kivymd.readthedocs.io/en/latest/components/screen/', label='🛠️ Элемент Screen')
        path = 'pages/glava_7/Listing_7_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=400):
            fun_g7.run_7_2()

    elif options == "Листинг 7.3":
        st.page_link('https://kivymd.readthedocs.io/en/latest/components/appbar/', label='🛠️ Элемент MDTopAppBar с KV')
        path = 'pages/glava_7/Listing_7_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=400):
            fun_g7.run_7_3()

    elif options == "Листинг 7.4":
        st.page_link('https://kivymd.readthedocs.io/en/latest/components/screenmanager/', label='🛠️ ScreenManager')
        path = 'pages/glava_7/Listing_7_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=580)
        with st.expander("🔍 Показать результат", width=400):
            fun_g7.run_7_4()

    elif options == "Листинг 7.5":
        st.page_link('https://kivymd.readthedocs.io/en/latest/themes/theming/', label='🛠️ Темы и стили')
        path = 'pages/glava_7/Listing_7_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=570)
        with st.expander("🔍 Показать результат", width=600):
            fun_g7.run_7_5()

    elif options == "Листинг 7.6":
        st.page_link('https://kivymd.readthedocs.io/en/latest/themes/theming/', label='🛠️ Темы и стили')
        path = 'pages/glava_7/Listing_7_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=570)
        with st.expander("🔍 Показать результат", width=600):
            fun_g7.run_7_6()

    elif options == "Листинг 7.7":
        st.page_link('https://kivymd.readthedocs.io/en/latest/themes/theming/', label='🛠️ Темы и стили')
        path = 'pages/glava_7/Listing_7_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=410):
            fun_g7.run_7_7()

    elif options == "Листинг 7.8":
        st.page_link('https://kivymd.readthedocs.io/en/latest/themes/theming/', label='🛠️ Темы и стили')
        path = 'pages/glava_7/Listing_7_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=460):
            fun_g7.run_7_8()

    elif options == "Листинг 7.9":
        st.page_link('https://kivymd.readthedocs.io/en/latest/themes/theming/', label='🛠️ Темы и стили')
        path = 'pages/glava_7/Listing_7_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=260):
            fun_g7.run_7_9()

    elif options == "Листинг 7.10":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/themes/icon-definitions/', label='🛠️ Список иконок')
        path = 'pages/glava_7/Listing_7_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=350):
            fun_g7.run_7_10()

    elif options == "Листинг 7.11":
        st.page_link('https://kivymd.readthedocs.io/en/latest/components/appbar/', label='🛠️ Виджет TopAppBar')
        path = 'pages/glava_7/Listing_7_11.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=350):
            fun_g7.run_7_11()