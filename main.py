import streamlit as st
from streamlit_lottie import st_lottie

from utils import load_lottieurl
from widgets import __login__
__login__obj = __login__(auth_token = "你的auth_token",
                    company_name = "Shims",
                    width = 200, height = 250,
                    logout_button_name = 'Logout', hide_menu_bool = False,
                    hide_footer_bool = False,
                    lottie_url = 'https://lottie.host/710526e0-f23c-431b-b552-c5780aef7c1c/nTP95rDIhr.json')

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN:
    # 加载并显示 Lottie 动画
    lottie_json = load_lottieurl('https://lottie.host/36eb93c6-0bbf-46d8-8944-c2de2b53d92b/ITECuXzLB5.json')
    st_lottie(lottie_json, width=300, height=300)
    st.header("登录成功！")
    st.write("在这里你可以管理你的数据")
    st.button("开始使用", key="get_started")





    # 可选：添加一些样式
    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #4CAF50; /* 绿色 */
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border: none;
            border-radius: 8px;
            transition-duration: 0.4s;
        }

        .stButton>button:hover {
            background-color: white;
            color: black;
            border: 2px solid #4CAF50;
        }
        </style>
        """, unsafe_allow_html=True
    )