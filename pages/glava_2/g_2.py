# https://python-code-online.pages.dev/ru/
import streamlit as st
import fun_g2

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 2", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="auto",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 2")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

# Контейнер
with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 2",
        ("Листинг 2.1", "Листинг 2.2", "Листинг 2.3", "Листинг 2.4",
         "Листинг 2.5", "Листинг 2.6", "Листинг 2.7", "Листинг 2.8",
         "Листинг 2.9", "Листинг 2.10", "Листинг 2.11", "Листинг 2.12",
         "Листинг 2.13", "Листинг 2.15", "Листинг 2.16",
         "Листинг 2.18", "Листинг 2.19", "Листинг 2.20",
         "Листинг 2.21", "Листинг 2.22", "Листинг 2.23", "Листинг 2.24",
         "Листинг 2.25", "Листинг 2.26", "Листинг 2.27", "Листинг 2.28",
         "Листинг 2.29", "Листинг 2.30", "Листинг 2.31", "Листинг 2.32",
         "Листинг 2.33", "Листинг 2.34", "Листинг 2.35", "Листинг 2.36",
         "Листинг 2.37", "Листинг 2.38", "Листинг 2.39", "Листинг 2.40",
         "Листинг 2.41", "Листинг 2.42", "Листинг 2.43", "Листинг 2.44",
         "Листинг 2.45", "Листинг 2.46", "Листинг 2.47", "Листинг 2.48",
         "Листинг 2.49", "Листинг 2.50", "Листинг 2.51", "Листинг 2.52",
         "Листинг 2.53", "Листинг 2.54", "Листинг 2.55",
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
    elif options == "Листинг 2.1":
        path = 'pages/glava_2/Listing_2_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=300):
            fun_g2.run_2_1()

    elif options == "Листинг 2.2":
        path = 'pages/glava_2/Listing_2_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=320):
            fun_g2.run_2_2()

    elif options == "Листинг 2.3":
        path = 'pages/glava_2/Listing_2_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=320):
            fun_g2.run_2_3()

    elif options == "Листинг 2.4":
        path = 'pages/glava_2/Listing_2_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=320):
            fun_g2.run_2_4()

    elif options == "Листинг 2.5":
        path = 'pages/glava_2/Listing_2_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=500):
            fun_g2.run_2_5()

    elif options == "Листинг 2.6":
        path = 'pages/glava_2/Listing_2_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=280):
            fun_g2.run_2_6()

    elif options == "Листинг 2.7":
        path = 'pages/glava_2/Listing_2_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=500):
            fun_g2.run_2_7()

    elif options == "Листинг 2.8":
        path = 'pages/glava_2/Listing_2_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=760)
        with st.expander("🔍 Показать результат", width=500):
            fun_g2.run_2_8()

    elif options == "Листинг 2.9":
        path = 'pages/glava_2/Listing_2_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=400):
            fun_g2.run_2_9()

    elif options == "Листинг 2.10":
        path = 'pages/glava_2/Listing_2_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=500):
            fun_g2.run_2_10()

    elif options == "Листинг 2.11":
        path = 'pages/glava_2/Listing_2_11.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=450):
            fun_g2.run_2_11()

    elif options == "Листинг 2.12":
        path = 'pages/glava_2/Listing_2_12.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=450):
            fun_g2.run_2_12()

    elif options == "Листинг 2.13":
        tab1, tab2 = st.tabs(['Python', 'Kivy'])
        with tab1:
            path = 'pages/glava_2/Listing_2_13.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True, width=500)
        with tab2:
            path = 'pages/glava_2/Listing_2_14.kv'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=350):
            fun_g2.run_2_13()

    elif options == "Листинг 2.15":
        tab1, tab2 = st.tabs(['Python', 'Kivy'])
        with tab1:
            path = 'pages/glava_2/Listing_2_15.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True, width=500)
        with tab2:
            path = 'pages/glava_2/Listing_2_14.kv'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=350):
            fun_g2.run_2_15()

    elif options == "Листинг 2.16":
        tab1, tab2 = st.tabs(['Python', 'Kivy'])
        with tab1:
            path = 'pages/glava_2/Listing_2_16.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True, width=550)
        with tab2:
            path = 'pages/glava_2/Listing_2_17.kv'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=350):
            fun_g2.run_2_16()

    elif options == "Листинг 2.18":
        path = 'pages/glava_2/Listing_2_18.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=300):
            fun_g2.run_2_18()

    elif options == "Листинг 2.19":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-label.htm', label='🛠️ Свойства Label')
        path = 'pages/glava_2/Listing_2_19.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=300):
            fun_g2.run_2_19()

    elif options == "Листинг 2.20":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-label.htm', label='🛠️ Свойства Label')
        path = 'pages/glava_2/Listing_2_20.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=300):
            fun_g2.run_2_20()

    elif options == "Листинг 2.21":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-buttons.htm', label='🛠️ Свойства Button')
        path = 'pages/glava_2/Listing_2_21.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=500):
            fun_g2.run_2_21()

    elif options == "Листинг 2.22":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-buttons.htm', label='🛠️ Свойства Button')
        path = 'pages/glava_2/Listing_2_22.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=400):
            fun_g2.run_2_22()

    elif options == "Листинг 2.23":
        st.page_link('https://kivy.org/doc/stable/api-kivy.uix.checkbox.html', label='🛠️ Свойства CheckBox')
        path = 'pages/glava_2/Listing_2_23.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=400):
            fun_g2.run_2_23()

    elif options == "Листинг 2.24":
        st.page_link('https://kivy.org/doc/stable/api-kivy.uix.checkbox.html', label='🛠️ Свойства CheckBox')
        path = 'pages/glava_2/Listing_2_24.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=400):
            fun_g2.run_2_24()

    elif options == "Листинг 2.25":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-images.htm', label='🛠️ Свойства Image')
        path = 'pages/glava_2/Listing_2_25.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=300):
            fun_g2.run_2_25()

    elif options == "Листинг 2.26":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-images.htm', label='🛠️ Свойства Image')
        path = 'pages/glava_2/Listing_2_26.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=300):
            fun_g2.run_2_26()

    elif options == "Листинг 2.27":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-slider.htm', label='🛠️ Свойства Slider')
        path = 'pages/glava_2/Listing_2_27.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=510)
        with st.expander("🔍 Показать результат", width=300):
            fun_g2.run_2_27()

    elif options == "Листинг 2.28":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-slider.htm', label='🛠️ Свойства Slider')
        path = 'pages/glava_2/Listing_2_28.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=260):
            fun_g2.run_2_28()

    elif options == "Листинг 2.29":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-progress-bar.htm', label='🛠️ Свойства ProgressBar')
        path = 'pages/glava_2/Listing_2_29.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=260):
            fun_g2.run_2_29()

    elif options == "Листинг 2.30":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-progress-bar.htm', label='🛠️ Свойства ProgressBar')
        path = 'pages/glava_2/Listing_2_30.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=260):
            fun_g2.run_2_30()

    elif options == "Листинг 2.31":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-text-input.htm', label='🛠️ Свойства TextInput')
        path = 'pages/glava_2/Listing_2_31.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=260):
            fun_g2.run_2_31()

    elif options == "Листинг 2.32":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-text-input.htm', label='🛠️ Свойства TextInput')
        path = 'pages/glava_2/Listing_2_32.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=300):
            fun_g2.run_2_32()

    elif options == "Листинг 2.33":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-toggle-button.htm', label='🛠️ Свойства ToggleButton')
        path = 'pages/glava_2/Listing_2_33.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=450)
        with st.expander("🔍 Показать результат", width=450):
            fun_g2.run_2_33()

    elif options == "Листинг 2.34":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-toggle-button.htm', label='🛠️ Свойства ToggleButton')
        path = 'pages/glava_2/Listing_2_34.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=450):
            fun_g2.run_2_34()

    elif options == "Листинг 2.35":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-toggle-button.htm', label='🛠️ Свойства ToggleButton')
        path = 'pages/glava_2/Listing_2_35.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=550):
            fun_g2.run_2_35()

    elif options == "Листинг 2.36":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-switch.htm', label='🛠️ Свойства Switch')
        path = 'pages/glava_2/Listing_2_36.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=450):
            fun_g2.run_2_36()

    elif options == "Листинг 2.37":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-switch.htm', label='🛠️ Свойства Switch')
        path = 'pages/glava_2/Listing_2_37.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=450):
            fun_g2.run_2_37()

    elif options == "Листинг 2.38":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-videos.htm', label='🛠️ Свойства Video')
        path = 'pages/glava_2/Listing_2_38.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=480):
            fun_g2.run_2_38()

    elif options == "Листинг 2.39":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-videos.htm', label='🛠️ Свойства Video')
        path = 'pages/glava_2/Listing_2_39.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=480):
            fun_g2.run_2_39()

    elif options == "Листинг 2.40":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-widgets.htm', label='🛠️ Свойства Widget')
        path = 'pages/glava_2/Listing_2_40.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=400):
            fun_g2.run_2_40()

    elif options == "Листинг 2.41":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-widgets.htm', label='🛠️ Свойства Widget')
        path = 'pages/glava_2/Listing_2_41.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=400):
            fun_g2.run_2_41()

    elif options == "Листинг 2.42":
        st.page_link('https://www.tutorialspoint.com/kivy/kivy-widgets.htm', label='🛠️ Свойства Widget')
        path = 'pages/glava_2/Listing_2_42.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=400):
            fun_g2.run_2_42()

    elif options == "Листинг 2.43":
        path = 'pages/glava_2/Listing_2_43.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=400):
            fun_g2.run_2_43()

    elif options == "Листинг 2.44":
        path = 'pages/glava_2/Listing_2_44.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=400):
            fun_g2.run_2_44()

    elif options == "Листинг 2.45":
        path = 'pages/glava_2/Listing_2_45.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=500)
        with st.expander("🔍 Показать результат", width=400):
            fun_g2.run_2_45()

    elif options == "Листинг 2.46":
        path = 'pages/glava_2/Listing_2_46.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=400):
            fun_g2.run_2_46()

    elif options == "Листинг 2.47":
        path = 'pages/glava_2/Listing_2_47.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=600):
            fun_g2.run_2_47()

    elif options == "Листинг 2.48":
        path = 'pages/glava_2/Listing_2_48.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=500):
            fun_g2.run_2_48()

    elif options == "Листинг 2.49":
        path = 'pages/glava_2/Listing_2_49.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=600)
        with st.expander("🔍 Показать результат", width=600):
            fun_g2.run_2_49()

    elif options == "Листинг 2.50":
        path = 'pages/glava_2/Listing_2_50.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=600):
            fun_g2.run_2_50()

    elif options == "Листинг 2.51":
        tab1, tab2 = st.tabs(['Python', 'Kivy'])
        with tab1:
            path = 'pages/glava_2/Listing_2_51.py'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True, width=500)
        with tab2:
            path = 'pages/glava_2/Listing_2_52.kv'
            file = open(path, 'r')
            code = file.read()
            st.code(code, language="python", line_numbers=True, width=400)
        with st.expander("🔍 Показать результат", width=500):
            fun_g2.run_2_51()

    elif options == "Листинг 2.53":
        path = 'pages/glava_2/Listing_2_53.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=650)
        with st.expander("🔍 Показать результат", width=400):
            fun_g2.run_2_53()

    elif options == "Листинг 2.54":
        path = 'pages/glava_2/Listing_2_54.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=400):
            fun_g2.run_2_54()

    elif options == "Листинг 2.55":
        path = 'pages/glava_2/Listing_2_55.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True, width=550)
        with st.expander("🔍 Показать результат", width=600):
            fun_g2.run_2_55()


