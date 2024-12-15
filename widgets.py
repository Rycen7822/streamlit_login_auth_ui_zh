# -*- coding: utf-8 -*-
import streamlit as st
import json
import os
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_cookies_manager import EncryptedCookieManager
from .utils import check_usr_pass
from .utils import load_lottieurl
from .utils import check_valid_name
from .utils import check_valid_email
from .utils import check_unique_email
from .utils import check_unique_usr
from .utils import register_new_usr
from .utils import check_email_exists
from .utils import generate_random_passwd
from .utils import send_passwd_in_email
from .utils import change_passwd
from .utils import check_current_passwd


class __login__:
    """
    Builds the UI for the Login/ Sign Up page.
    """

    def __init__(self, auth_token: str, company_name: str, width, height, logout_button_name: str = '退出登录', hide_menu_bool: bool = False, hide_footer_bool: bool = False, lottie_url: str = "https://assets8.lottiefiles.com/packages/lf20_ktwnwv5m.json" ):
        """
        Arguments:
        -----------
        1. self
        2. auth_token : The unique authorization token received from - https://www.courier.com/email-api/
        3. company_name : This is the name of the person/ organization which will send the password reset email.
        4. width : Width of the animation on the login page.
        5. height : Height of the animation on the login page.
        6. logout_button_name : The logout button name.
        7. hide_menu_bool : Pass True if the streamlit menu should be hidden.
        8. hide_footer_bool : Pass True if the 'made with streamlit' footer should be hidden.
        9. lottie_url : The lottie animation you would like to use on the login page. Explore animations at - https://lottiefiles.com/featured
        """
        self.auth_token = auth_token
        self.company_name = company_name
        self.width = width
        self.height = height
        self.logout_button_name = '退出登录'
        self.hide_menu_bool = hide_menu_bool
        self.hide_footer_bool = hide_footer_bool
        self.lottie_url = lottie_url

        self.cookies = EncryptedCookieManager(
        prefix="streamlit_login_ui_yummy_cookies",
        password='9d68d6f2-4258-45c9-96eb-2d6bc74ddbb5-d8f49cab-edbb-404a-94d0-b25b1d4a564b')

        if not self.cookies.ready():
            st.stop()   


    def check_auth_json_file_exists(self, auth_filename: str) -> bool:
        """
        Checks if the auth file (where the user info is stored) already exists.
        """
        file_names = []
        for path in os.listdir('./'):
            if os.path.isfile(os.path.join('./', path)):
                file_names.append(path)

        present_files = []
        for file_name in file_names:
            if auth_filename in file_name:
                present_files.append(file_name)
                    
            present_files = sorted(present_files)
            if len(present_files) > 0:
                return True
        return False


    def login_widget(self) -> None:
        """
        Creates the login widget, checks and sets cookies, authenticates the users.
        """
        # Checks if cookie exists.
        if st.session_state['LOGGED_IN'] == False:
            if st.session_state['LOGOUT_BUTTON_HIT'] == False:
                fetched_cookies = self.cookies
                if '__streamlit_login_signup_ui_username__' in fetched_cookies.keys():
                    if fetched_cookies['__streamlit_login_signup_ui_username__'] != '1c9a923f-fb21-4a91-b3f3-5f18e3f01182':
                        st.session_state['LOGGED_IN'] = True

        if st.session_state['LOGGED_IN'] == False:
            st.session_state['LOGOUT_BUTTON_HIT'] = False 

            del_login = st.empty()
            with del_login.form("Login Form"):
                username = st.text_input("用户名", placeholder = '请输入你的用户名')
                password = st.text_input("密码", placeholder = '请输入你的密码', type = 'password')

                st.markdown("###")
                login_submit_button = st.form_submit_button(label = '登录')

                if login_submit_button == True:
                    authenticate_user_check = check_usr_pass(username, password)

                    if authenticate_user_check == False:
                        st.error("无效的用户名或密码!")

                    else:
                        st.session_state['LOGGED_IN'] = True
                        self.cookies['__streamlit_login_signup_ui_username__'] = username
                        self.cookies.save()
                        del_login.empty()
                        st.experimental_rerun()


    def animation(self) -> None:
        """
        Renders the lottie animation.
        """
        lottie_json = load_lottieurl(self.lottie_url)
        st_lottie(lottie_json, width = self.width, height = self.height)


    def sign_up_widget(self) -> None:
        """
        Creates the sign-up widget and stores the user info in a secure way in the _secret_auth_.json file.
        """
        with st.form("Sign Up Form"):
            name_sign_up = st.text_input("昵称", placeholder = '请输入你的昵称')
            valid_name_check = check_valid_name(name_sign_up)

            email_sign_up = st.text_input("邮箱", placeholder = '请输入你的邮箱')
            valid_email_check = check_valid_email(email_sign_up)
            unique_email_check = check_unique_email(email_sign_up)
            
            username_sign_up = st.text_input("用户名", placeholder = '请输入用户名')
            unique_username_check = check_unique_usr(username_sign_up)

            password_sign_up = st.text_input("密码", placeholder = '请输入密码', type = 'password')

            st.markdown("###")
            sign_up_submit_button = st.form_submit_button(label = '注册')

            if sign_up_submit_button:
                if valid_name_check == False:
                    st.error("请输入一个有效的昵称!")

                elif valid_email_check == False:
                    st.error("请输入一个有效的邮箱!")
                
                elif unique_email_check == False:
                    st.error("邮箱已被注册!")
                
                elif unique_username_check == False:
                    st.error(f'抱歉, 用户名 {username_sign_up} 已经被使用!')
                
                elif unique_username_check == None:
                    st.error('未输入用户名!')

                if valid_name_check == True:
                    if valid_email_check == True:
                        if unique_email_check == True:
                            if unique_username_check == True:
                                register_new_usr(name_sign_up, email_sign_up, username_sign_up, password_sign_up)
                                st.success("注册成功!")


    def forgot_password(self) -> None:
        """
        Creates the forgot password widget and after user authentication (email), triggers an email to the user 
        containing a random password.
        """
        with st.form("Forgot Password Form"):
            email_forgot_passwd = st.text_input("邮箱", placeholder= '请输入你的邮箱')
            email_exists_check, username_forgot_passwd = check_email_exists(email_forgot_passwd)

            st.markdown("###")
            forgot_passwd_submit_button = st.form_submit_button(label = '获取临时密码')

            if forgot_passwd_submit_button:
                if email_exists_check == False:
                    st.error("该邮箱未注册!")

                if email_exists_check == True:
                    random_password = generate_random_passwd()
                    send_passwd_in_email(self.auth_token, username_forgot_passwd, email_forgot_passwd, self.company_name, random_password)
                    change_passwd(email_forgot_passwd, random_password)
                    st.success("临时密码发送成功!")


    def reset_password(self) -> None:
        """
        Creates the reset password widget and after user authentication (email and the password shared over that email), 
        resets the password and updates the same in the _secret_auth_.json file.
        """
        with st.form("Reset Password Form"):
            email_reset_passwd = st.text_input("邮箱", placeholder= '请输入你的邮箱')
            email_exists_check, username_reset_passwd = check_email_exists(email_reset_passwd)

            current_passwd = st.text_input("临时密码", placeholder= '请输入你在邮箱收到的临时密码')
            current_passwd_check = check_current_passwd(email_reset_passwd, current_passwd)

            new_passwd = st.text_input("新密码", placeholder= '请输入新密码', type = 'password')

            new_passwd_1 = st.text_input("重复输入新密码", placeholder= '请重复输入新密码', type = 'password')

            st.markdown("###")
            reset_passwd_submit_button = st.form_submit_button(label = '重置密码')

            if reset_passwd_submit_button:
                if email_exists_check == False:
                    st.error("该邮箱不存在!")

                elif current_passwd_check == False:
                    st.error("临时密码错误!")

                elif new_passwd != new_passwd_1:
                    st.error("两次输入的密码不一致!")
            
                if email_exists_check == True:
                    if current_passwd_check == True:
                        change_passwd(email_reset_passwd, new_passwd)
                        st.success("密码重置成功!")
                

    def logout_widget(self) -> None:
        """
        Creates the logout widget in the sidebar only if the user is logged in.
        """
        if st.session_state['LOGGED_IN'] == True:
            del_logout = st.sidebar.empty()
            del_logout.markdown("#")
            logout_click_check = del_logout.button(self.logout_button_name)

            if logout_click_check == True:
                st.session_state['LOGOUT_BUTTON_HIT'] = True
                st.session_state['LOGGED_IN'] = False
                self.cookies['__streamlit_login_signup_ui_username__'] = '1c9a923f-fb21-4a91-b3f3-5f18e3f01182'
                del_logout.empty()
                st.experimental_rerun()
        

    def nav_sidebar(self):
        """
        Creates the side navigaton bar
        """
        main_page_sidebar = st.sidebar.empty()

        with main_page_sidebar:
            selected_option = option_menu(
                menu_title = '选项',
                menu_icon = 'list-columns-reverse',
                icons = ['box-arrow-in-right', 'person-plus', 'x-circle','arrow-counterclockwise'],
                options = ['登录', '创建账户', '忘记密码?', '重置密码'],
                styles = {
                    "container": {"padding": "5px"},
                    "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px"}} )
        return main_page_sidebar, selected_option
    

    def hide_menu(self) -> None:
        """
        Hides the streamlit menu situated in the top right.
        """
        st.markdown(""" <style>
        #MainMenu {visibility: hidden;}
        </style> """, unsafe_allow_html=True)
    

    def hide_footer(self) -> None:
        """
        Hides the 'made with streamlit' footer.
        """
        st.markdown(""" <style>
        footer {visibility: hidden;}
        </style> """, unsafe_allow_html=True)


    def build_login_ui(self):
        """
        Brings everything together, calls important functions.
        """
        
        # 插入logo
        def add_logo(url2, url1):
            st.markdown(
                f"""
                <style>
                .logo1 {{
                    position: absolute;
                    top: 0;
                    left: 0;
                    height: 50px;
                    margin-left: 0px;
                    margin-top: -88px;
                }}
                .logo2 {{
                    position: absolute;
                    top: 0;
                    left: 0;
                    height: 50px;
                    margin-left: 280px;
                    margin-top: -90px;
                }}
                </style>
                <img src='{url1}' class='logo1'>
                <img src='{url2}' class='logo2'>
                """,
                unsafe_allow_html=True
            )

        if 'LOGGED_IN' not in st.session_state:
            st.session_state['LOGGED_IN'] = False

        if 'LOGOUT_BUTTON_HIT' not in st.session_state:
            st.session_state['LOGOUT_BUTTON_HIT'] = False

        auth_json_exists_bool = self.check_auth_json_file_exists('_secret_auth_.json')

        if auth_json_exists_bool == False:
            with open("_secret_auth_.json", "w") as auth_json:
                json.dump([], auth_json)

        main_page_sidebar, selected_option = self.nav_sidebar()

        if selected_option == '登录':
            c1, c2 = st.columns([7,3])
            with c1:
                self.login_widget()
            with c2:
                if st.session_state['LOGGED_IN'] == False:
                    self.animation()
        
        if selected_option == '创建账户':
            self.sign_up_widget()

        if selected_option == '忘记密码?':
            self.forgot_password()

        if selected_option == '重置密码':
            self.reset_password()
        
        self.logout_widget()

        if st.session_state['LOGGED_IN'] == True:
            main_page_sidebar.empty()
        
        if self.hide_menu_bool == True:
            self.hide_menu()
        
        if self.hide_footer_bool == True:
            self.hide_footer()
        
        return st.session_state['LOGGED_IN']