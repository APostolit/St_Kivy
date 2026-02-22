import streamlit as st
import fun_g9

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 9", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 9")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 9",
        ("Листинг 9.1", "Листинг 9.2", "Листинг 9.3",
         "Листинг 9.6", "Листинг 9.7", "Листинг 9.8", "Листинг 9.9", "Листинг 9.10",
         "Листинг 9.11", "Листинг 9.12", "Листинг 9.13", "Листинг 9.14", "Листинг 9.15",
         "Листинг 9.16", "Листинг 9.17", "Листинг 9.18", "Листинг 9.19", "Листинг 9.20",
         "Листинг 9.21", "Листинг 9.22", "Листинг 9.23", "Листинг 9.24", "Листинг 9.25",
         "Листинг 9.26", "Листинг 9.27"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container(width=800)
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 9.1":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/backdrop/', label='🛠️ Виджет MDBackdrop')
        path = 'pages/glava_9/Listing_9_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=500):
            fun_g9.run_9_1()

    elif options == "Листинг 9.2":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/banner/', label='🛠️ Виджет MDBanner')
        path = 'pages/glava_9/Listing_9_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=570):
            fun_g9.run_9_2()

    elif options == "Листинг 9.3":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/bottom-navigation/',
                     label='🛠️ Виджет MDBottom Navigation')
        path = 'pages/glava_9/Listing_9_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=570):
            fun_g9.run_9_3()

    elif options == "Листинг 9.6":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/button/#mdiconbutton',
                     label='🛠️ Виджет MDIconButton')
        path = 'pages/glava_9/Listing_9_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=500):
            fun_g9.run_9_6()

    elif options == "Листинг 9.7":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/button/#mdfloatingactionbutton',
                     label='🛠️ Виджет MDFloatingActionButton')
        path = 'pages/glava_9/Listing_9_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=600):
            fun_g9.run_9_7()

    elif options == "Листинг 9.8":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/button/#mdflatbutton',
                     label='🛠️ Виджет MDFlatButton')
        path = 'pages/glava_9/Listing_9_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=500):
            fun_g9.run_9_8()

    elif options == "Листинг 9.9":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/button/#mdraisedbutton',
                     label='🛠️ Виджет MDRaisedButton')
        path = 'pages/glava_9/Listing_9_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=500):
            fun_g9.run_9_9()

    elif options == "Листинг 9.10":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/button/#mdrectangleflatbutton',
                     label='🛠️ Виджет MDRectangleFlatButton')
        path = 'pages/glava_9/Listing_9_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=500):
            fun_g9.run_9_10()

    elif options == "Листинг 9.11":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/button/#mdrectangleflaticonbutton',
                     label='🛠️ Виджет MMDRectangleFlatIconButton')
        path = 'pages/glava_9/Listing_9_11.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=500):
            fun_g9.run_9_11()

    elif options == "Листинг 9.12":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/button/#mdroundflatbutton',
                     label='🛠️ Виджет MDRoundFlatButton')
        path = 'pages/glava_9/Listing_9_12.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=500):
            fun_g9.run_9_12()

    elif options == "Листинг 9.13":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/button/#mdrectangleflaticonbutton',
                     label='🛠️ Виджет MDRectangleFlatIconButton')
        path = 'pages/glava_9/Listing_9_13.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=500):
            fun_g9.run_9_13()

    elif options == "Листинг 9.14":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/button/#mdfillroundflatbutton',
                     label='🛠️ Виджет MDFillRoundFlatButton')
        path = 'pages/glava_9/Listing_9_14.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=500):
            fun_g9.run_9_14()

    elif options == "Листинг 9.15":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/button/#mdtextbutton',
                     label='🛠️ Виджет MDTextButton')
        path = 'pages/glava_9/Listing_9_15.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=500):
            fun_g9.run_9_15()

    elif options == "Листинг 9.16":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/button/#mdfloatingactionbuttonspeeddial',
                     label='🛠️ Виджет MDFloatingActionButtonSpeedDial')
        path = 'pages/glava_9/Listing_9_16.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=750)
        with st.expander("🔍 Показать результат", width=750):
            fun_g9.run_9_16()

    elif options == "Листинг 9.17":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/card/#mdcard',
                     label='🛠️ Виджет MDCard')
        path = 'pages/glava_9/Listing_9_17.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=500):
            fun_g9.run_9_17()

    elif options == "Листинг 9.18":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/card/#mdcard',
                     label='🛠️ Виджет MDCard')
        path = 'pages/glava_9/Listing_9_18.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=500):
            fun_g9.run_9_18()

    elif options == "Листинг 9.19":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/card/#mdcardswipe',
                     label='🛠️ Виджет MDCardSwipe')
        path = 'pages/glava_9/Listing_9_19.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=750)
        with st.expander("🔍 Показать результат", width=750):
            fun_g9.run_9_19()

    elif options == "Листинг 9.20":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/chip/',
                     label='🛠️ Виджет MDChip')
        path = 'pages/glava_9/Listing_9_20.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=550):
            fun_g9.run_9_20()

    elif options == "Листинг 9.21":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/datatables/',
                     label='🛠️ Виджет MDDataTables')
        path = 'pages/glava_9/Listing_9_21.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=600):
            fun_g9.run_9_21()

    elif options == "Листинг 9.22":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/datatables/',
                     label='🛠️ Виджет MDDataTables')
        path = 'pages/glava_9/Listing_9_22.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=700)
        with st.expander("🔍 Показать результат", width=700):
            fun_g9.run_9_22()

    elif options == "Листинг 9.23":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/datatables/',
                     label='🛠️ Виджет MDDataTables')
        path = 'pages/glava_9/Listing_9_23.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=750)
        with st.expander("🔍 Показать результат", width=700):
            fun_g9.run_9_23()

    elif options == "Листинг 9.24":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/dialog/',
                     label='🛠️ Виджет MDDialog')
        path = 'pages/glava_9/Listing_9_24.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=750)
        with st.expander("🔍 Показать результат", width=700):
            fun_g9.run_9_24()

    elif options == "Листинг 9.25":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/dialog/',
                     label='🛠️ Виджет MDDialog')
        path = 'pages/glava_9/Listing_9_25.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=750)
        with st.expander("🔍 Показать результат", width=750):
            fun_g9.run_9_25()

    elif options == "Листинг 9.26":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/dialog/',
                     label='🛠️ Виджет MDDialog')
        path = 'pages/glava_9/Listing_9_26.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=750)
        with st.expander("🔍 Показать результат", width=800):
            fun_g9.run_9_26()

    elif options == "Листинг 9.27":
        st.page_link('https://kivymd.readthedocs.io/en/0.104.2/components/dialog/',
                     label='🛠️ Виджет MDDialog')
        path = 'pages/glava_9/Listing_9_27.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=700)
        with st.expander("🔍 Показать результат", width=800):
            fun_g9.run_9_27()