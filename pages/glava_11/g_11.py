import streamlit as st
import fun_g11

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 11", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 11")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 11",
        ("Листинг 11.1", "Листинг 11.2", "Листинг 11.3", "Листинг 11.4", "Листинг 11.5",
         "Листинг 11.6", "Листинг 11.7", "Листинг 11.8", "Листинг 11.9", "Листинг 11.10",
         "Листинг 11.11", "Листинг 11.12", "Листинг 11.13", "Листинг 11.14", "Листинг 11.15",
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

    elif options == "Листинг 11.1":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/navigation-drawer/',
                     label='🛠️ Виджет MDNavigationDrawer')
        path = 'pages/glava_11/Listing_11_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=710)
        with st.expander("🔍 Показать результат", width=600):
            fun_g11.run_11_1()

    elif options == "Листинг 11.2":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/navigation-drawer/',
                     label='🛠️ Виджет MDNavigationDrawer')
        path = 'pages/glava_11/Listing_11_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=710)
        with st.expander("🔍 Показать результат", width=600):
            fun_g11.run_11_2()

    elif options == "Листинг 11.3":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/navigation-drawer/',
                     label='🛠️ Виджет MDNavigationDrawer')
        path = 'pages/glava_11/Listing_11_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=710)
        with st.expander("🔍 Показать результат", width=700):
            fun_g11.run_11_3()

    elif options == "Листинг 11.4":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/navigation-drawer/',
                     label='🛠️ Виджет MDNavigationDrawer')
        path = 'pages/glava_11/Listing_11_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=710)
        with st.expander("🔍 Показать результат", width=700):
            fun_g11.run_11_4()

    elif options == "Листинг 11.5":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/navigation-rail/',
                     label='🛠️ Виджет MDNavigationRail')
        path = 'pages/glava_11/Listing_11_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=500):
            fun_g11.run_11_5()

    elif options == "Листинг 11.6":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/pickers/#mdtimepicker',
                     label='🛠️ Виджет MDTimePicker')
        path = 'pages/glava_11/Listing_11_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=500):
            fun_g11.run_11_6()

    elif options == "Листинг 11.7":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/pickers/#mddatepicker',
                     label='🛠️ Виджет MDDatePicker')
        path = 'pages/glava_11/Listing_11_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=500):
            fun_g11.run_11_7()

    elif options == "Листинг 11.8":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/pickers/#mddatepicker',
                     label='🛠️ Виджет MDDatePicker')
        path = 'pages/glava_11/Listing_11_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=500):
            fun_g11.run_11_8()

    elif options == "Листинг 11.9":
        st.page_link('https://kivymd.readthedocs.io/en/1.1.0/components/colorpicker/index.html',
                     label='🛠️ Виджет MDColorPicker')
        path = 'pages/glava_11/Listing_11_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=500):
            fun_g11.run_11_9()

    elif options == "Листинг 11.10":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/progress-bar/',
                     label='🛠️ Виджет MDProgressBar')
        path = 'pages/glava_11/Listing_11_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=500):
            fun_g11.run_11_10()

    elif options == "Листинг 11.11":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/progress-bar/',
                     label='🛠️ Виджет MDProgressBar')
        path = 'pages/glava_11/Listing_11_11.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=700)
        with st.expander("🔍 Показать результат", width=500):
            fun_g11.run_11_11()

    elif options == "Листинг 11.12":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/screen/',
                     label='🛠️ Виджет MDScreen')
        path = 'pages/glava_11/Listing_11_12.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=250):
            fun_g11.run_11_12()

    elif options == "Листинг 11.13":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/selection-controls/#mdcheckbox',
                     label='🛠️ MDCheckbox')
        path = 'pages/glava_11/Listing_11_13.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=700):
            fun_g11.run_11_13()

    elif options == "Листинг 11.14":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/selection-controls/#mdcheckbox',
                     label='🛠️ MDCheckbox')
        path = 'pages/glava_11/Listing_11_14.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=500):
            fun_g11.run_11_14()

    elif options == "Листинг 11.15":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/selection-controls/#mdswitch',
                     label='🛠️ MDSwitch')
        path = 'pages/glava_11/Listing_11_15.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=700):
            fun_g11.run_11_15()