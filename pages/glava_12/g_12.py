import streamlit as st
import fun_g12

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 12", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 12")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 12",
        ("Листинг 12.1", "Листинг 12.2", "Листинг 12.3", "Листинг 12.4", "Листинг 12.5",
         "Листинг 12.6", "Листинг 12.7", "Листинг 12.8", "Листинг 12.9", "Листинг 12.10",
         "Листинг 12.11", "Листинг 12.12", "Листинг 12.13", "Листинг 12.14", "Листинг 12.15",
         "Листинг 12.16", "Листинг 12.17", "Листинг 12.18", "Листинг 12.19", "Листинг 12.20",
         "Листинг 12.21"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container(width=800)
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 12.1":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/',
                     label='🛠️ Виджет MDSeparator')
        path = 'pages/glava_12/Listing_12_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=380)
        with st.expander("🔍 Показать результат", width=300):
            fun_g12.run_12_1()

    elif options == "Листинг 12.2":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/slider/',
                     label='🛠️ Виджет MDSlider')
        path = 'pages/glava_12/Listing_12_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=500):
            fun_g12.run_12_2()

    elif options == "Листинг 12.3":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/slider/',
                     label='🛠️ Виджет MDSlider')
        path = 'pages/glava_12/Listing_12_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=300):
            fun_g12.run_12_3()

    elif options == "Листинг 12.4":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/snackbar/',
                     label='🛠️ Виджет Snackbar')
        path = 'pages/glava_12/Listing_12_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=600):
            fun_g12.run_12_4()

    elif options == "Листинг 12.5":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/snackbar/',
                     label='🛠️ Виджет Snackbar')
        path = 'pages/glava_12/Listing_12_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=500):
            fun_g12.run_12_5()

    elif options == "Листинг 12.6":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/snackbar/',
                     label='🛠️ Виджет Snackbar')
        path = 'pages/glava_12/Listing_12_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=600):
            fun_g12.run_12_6()

    elif options == "Листинг 12.8":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/tabs/',
                     label='🛠️ Виджет MDTabs')
        path = 'pages/glava_12/Listing_12_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=500):
            fun_g12.run_12_8()

    elif options == "Листинг 12.9":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/tabs/',
                     label='🛠️ Виджет MDTabs')
        path = 'pages/glava_12/Listing_12_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=680)
        with st.expander("🔍 Показать результат", width=500):
            fun_g12.run_12_9()

    elif options == "Листинг 12.10":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/tabs/',
                     label='🛠️ Виджет MDTabs')
        path = 'pages/glava_12/Listing_12_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=500):
            fun_g12.run_12_10()

    elif options == "Листинг 12.11":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/taptargetview/',
                     label='🛠️ Виджет MDTapTargetView')
        path = 'pages/glava_12/Listing_12_11.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=570)
        with st.expander("🔍 Показать результат", width=500):
            fun_g12.run_12_11()

    elif options == "Листинг 12.12":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/text-field/',
                     label='🛠️ Виджет MDTextField')
        path = 'pages/glava_12/Listing_12_12.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=300):
            fun_g12.run_12_12()

    elif options == "Листинг 12.13":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/text-field/',
                     label='🛠️ Виджет MDTextField')
        path = 'pages/glava_12/Listing_12_13.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=300):
            fun_g12.run_12_13()

    elif options == "Листинг 12.14":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/text-field/',
                     label='🛠️ Виджет MDTextField')
        path = 'pages/glava_12/Listing_12_14.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=400):
            fun_g12.run_12_14()

    elif options == "Листинг 12.15":
        st.page_link('https://kivymd.readthedocs.io/en/1.0.0/components/toolbar/#top',
                     label='🛠️ Виджет MDToopAppBar')
        path = 'pages/glava_12/Listing_12_15.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=300):
            fun_g12.run_12_15()

    elif options == "Листинг 12.16":
        st.page_link('https://kivymd.readthedocs.io/en/1.0.0/components/toolbar/#top',
                     label='🛠️ Виджет MDToopAppBar')
        path = 'pages/glava_12/Listing_12_16.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=500):
            fun_g12.run_12_16()

    elif options == "Листинг 12.17":
        st.page_link('https://kivymd.readthedocs.io/en/1.0.0/components/toolbar/#top',
                     label='🛠️ Виджет MDToopAppBar')
        path = 'pages/glava_12/Listing_12_17.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=700)
        with st.expander("🔍 Показать результат", width=800):
            fun_g12.run_12_17()

    elif options == "Листинг 12.18":
        st.page_link('https://kivymd.readthedocs.io/en/1.0.0/components/toolbar/#top',
                     label='🛠️ Виджет MDToopAppBar')
        path = 'pages/glava_12/Listing_12_18.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=800)
        with st.expander("🔍 Показать результат", width=800):
            fun_g12.run_12_18()

    elif options == "Листинг 12.19":
        st.page_link('https://kivymd.readthedocs.io/en/1.0.0/components/toolbar/#top',
                     label='🛠️ Виджет MDToopAppBar')
        path = 'pages/glava_12/Listing_12_19.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=700)
        with st.expander("🔍 Показать результат", width=600):
            fun_g12.run_12_19()

    elif options == "Листинг 12.20":
        st.page_link('https://kivymd.readthedocs.io/en/1.0.0/components/tooltip/',
                     label='🛠️ Виджет MDTooltip')
        path = 'pages/glava_12/Listing_12_20.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=500):
            fun_g12.run_12_20()

    elif options == "Листинг 12.21":
        st.page_link('https://kivymd.readthedocs.io/en/1.0.0/components/tooltip/',
                     label='🛠️ Виджет MDTooltip')
        path = 'pages/glava_12/Listing_12_21.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=500):
            fun_g12.run_12_21()