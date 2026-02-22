import streamlit as st
import fun_g8

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 8", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 8")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 8",
        ("Листинг 8.1", "Листинг 8.2", "Листинг 8.3", "Листинг 8.4", "Листинг 8.5",
         "Листинг 8.6", "Листинг 8.7", "Листинг 8.8", "Листинг 8.9", "Листинг 8.10",
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

    elif options == "Листинг 8.1":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/box-layout/', label='🛠️ Виджет MDBoxLayout')
        path = 'pages/glava_8/Listing_8_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=260):
            fun_g8.run_8_1()

    elif options == "Листинг 8.2":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/circularlayout/',
                     label='🛠️ Виджет MDCircularLayout')
        path = 'pages/glava_8/Listing_8_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=520)
        with st.expander("🔍 Показать результат", width=400):
            fun_g8.run_8_2()

    elif options == "Листинг 8.3":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/float-layout/',
                     label='🛠️ Виджет MDFloat Layout')
        path = 'pages/glava_8/Listing_8_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=520)
        with st.expander("🔍 Показать результат", width=280):
            fun_g8.run_8_3()

    elif options == "Листинг 8.4":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/grid-layout/',
                     label='🛠️ Виджет MDGrid Layout')
        path = 'pages/glava_8/Listing_8_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=640)
        with st.expander("🔍 Показать результат", width=280):
            fun_g8.run_8_4()

    elif options == "Листинг 8.5":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/refresh-layout/',
                     label='🛠️ Виджет RefreshLayout')
        path = 'pages/glava_8/Listing_8_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=640)
        with st.expander("🔍 Показать результат", width=600):
            fun_g8.run_8_5()

    elif options == "Листинг 8.6":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/relative-layout/',
                     label='🛠️ Виджет MDRelativeLayout')
        path = 'pages/glava_8/Listing_8_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=520)
        with st.expander("🔍 Показать результат", width=380):
            fun_g8.run_8_6()

    elif options == "Листинг 8.7":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/stacklayout/',
                     label='🛠️ Виджет MDStackLayout')
        path = 'pages/glava_8/Listing_8_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=450):
            fun_g8.run_8_7()

    elif options == "Листинг 8.8":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/stacklayout/',
                     label='🛠️ Виджет MDStackLayout')
        path = 'pages/glava_8/Listing_8_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=440):
            fun_g8.run_8_8()

    elif options == "Листинг 8.9":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/carousel/',
                     label='🛠️ Виджет MDCarousel')
        path = 'pages/glava_8/Listing_8_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=450):
            fun_g8.run_8_9()

    elif options == "Листинг 8.10":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/carousel/',
                     label='🛠️ Виджет MDCarousel')
        path = 'pages/glava_8/Listing_8_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=600):
            fun_g8.run_8_10()

