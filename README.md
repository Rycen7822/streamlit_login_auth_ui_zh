# 介绍
这个插件是一个用户友好的 Streamlit 登录/注册系统，基于[streamlit_login_auth_ui](https://github.com/GauriSP10/streamlit_login_auth_ui)库改写构建，
文本修改为了中文版，同时支持兼容更高版本的streamlit，修复了部分Bug。
它为开发者提供了一种简单的方法，以便在其 Streamlit 应用程序中实现安全的用户身份注册和验证。
## streamlit版本需求
streamlit>=1.12.0
## 主要功能

1. **用户登录与注册**：允许用户使用用户名和密码安全地登录和注册新帐户。
   
2. **密码重置功能**：用户可以通过点击“忘记密码？”链接，接收一封包含临时密码的电子邮件，方便重置密码。

3. **输入验证**：在注册过程中，系统会验证用户名和邮箱的有效性及唯一性，确保用户输入的信息符合标准。

4. **加密存储**：所有用户密码都经过加密处理，增强了安全性。

5. **自动登录**：使用加密的 Cookie 记住用户的登录状态，避免每次都输入密码。

6. **用户界面**：提供一个可定制的登录/注册页面，用户可以通过修改参数来更改界面的外观和行为。

## 使用说明

1. **依赖项安装**：确保在使用之前安装了相关依赖项，包括 `streamlit`, `argon2-cffi`, `trycourier` 等。

2. **初始化和配置**：创建 `__login__` 类的实例时，传入必要的参数，如认证token和公司名称。

3. **界面集成**：使用 `build_login_ui()` 方法整合所有功能，构建完整的用户界面。


## 作者:
[Rycen7822](kristinharrison7826@gmail.com)

## PyPi链接：

( https://pypi.org/project/streamlit-login-auth-ui-zh/0.1.0/)
## The UI:
[The UI](https://github.com/user-attachments/assets/d430963f-9148-4999-a2e3-772ba52f5561)


## 下载库

```python
pip install streamlit_login_auth_ui_zh
```

要导入该库，只需在代码开头粘贴以下内容：
```python
from streamlit_login_auth_ui_zh.widgets import __login__
```

您只需要为 ```__login__``` 类创建一个对象，并传入以下参数：
### 主要参数说明：
1. **auth_token**：从 [Courier](https://www.courier.com/email-api/) 获取的唯一授权token，用于安全地发送电子邮件。
2. **company_name**：发送密码重置邮件的个人或组织的名称，例如 "Shims"。
3. **width**：登录页面上动画的宽度，单位为像素（例如 200 像素）。
4. **height**：登录页面上动画的高度，单位为像素（例如 250 像素）。
5. **logout_button_name**：设置注销按钮的名称（例如 'Logout'）。
6. **hide_menu_bool**：传入 `True` 以隐藏 Streamlit 菜单，传入 `False` 则显示菜单。
7. **hide_footer_bool**：传入 `True` 以隐藏“由 Streamlit 制作”的页脚，传入 `False` 则显示页脚。
8. **lottie_url**：希望在登录页面使用的 Lottie 动画 URL，可以从 [LottieFiles](https://lottiefiles.com/featured) 上找到适合的动画。

# __login__ 类构造函数参数说明

## 必需参数 (Mandatory Arguments)

1. **auth_token**：  
   从 [Courier](https://www.courier.com/email-api/) 获取的token

2. **company_name**：  
   发送密码重置邮件的个人或组织的名称。

3. **width**：  
   登录页面上动画的宽度。

4. **height**：  
   登录页面上动画的高度。

## 非必需参数 (Non Mandatory Arguments)

1. **logout_button_name** [默认值 = '退出登录']：  
   注销按钮的名称。如果不提供，默认为 '退出登录'。

2. **hide_menu_bool** [默认值 = False]：  
   传入 `True` 以隐藏 Streamlit 菜单，默认为 `False`，表示菜单将显示。

3. **hide_footer_bool** [默认值 = False]：  
   传入 `True` 以隐藏“由 Streamlit 制作”的页脚，默认为 `False`，表示页脚将显示。

4. **lottie_url**   
   希望在登录页面使用的 Lottie 动画的 URL。

在创建 __login__ 类的对象之后，你需要调用该对象的 build_login_ui() 方法。这个方法将用于生成和展示登录用户界面。调用该方法的结果可以存储在一个变量中，方便后续操作。


# 使用 __login__ 类构建登录用户界面的示例

本示例演示如何使用 `__login__` 类构造对象并调用 `build_login_ui()` 方法来构建登录用户界面。

## 示例代码
    # 引入需要的库和模块
    import streamlit as st
    from streamlit_login_auth_ui_zh.widgets import __login__
    
    # 创建 __login__ 类的对象
    login_ui = __login__(
        auth_token="courier_auth_token",  # 从 Courier 获取的授权令牌
        company_name="MyCompany",  # 发送密码重置邮件的公司名称
        width=300,  # 动画宽度
        height=400,  # 动画高度
    )
    
    # 调用 build_login_ui() 方法并存储返回值
    user_logged_in = login_ui.build_login_ui()
    
    # 根据返回值执行后续操作
    if user_logged_in:
        st.success("用户已成功登录!")
    else:
       st.warning("请登录以继续.")
    
    def main():
       # your app
       
    if user_logged_in == True:
       main()

# 注意事项
  
请确保将你的应用程序逻辑缩进在 `if st.session_state['LOGGED_IN'] == True:` 语句下，这样可以保证只有在用户安全登录后，应用程序才会运行。
## 说明

### 登录页面
登录页面，用于验证用户身份。
![image](https://github.com/user-attachments/assets/e24003af-6ede-425c-81f4-103aea9ddfd5)
### 创建账户页面
以安全的方式将用户信息存储在 ```_secret_auth_.json``` 文件中。
![image](https://github.com/user-attachments/assets/a456993d-46b2-4df6-a545-0a684652752e)
### 忘记密码页面
在用户身份验证（电子邮件）后，触发一封包含随机密码的电子邮件发送给用户。
![image](https://github.com/user-attachments/assets/2c6bb1b7-0691-45f6-a15b-de2e76976c8e)
### 重置密码页面
在用户身份验证（电子邮件和通过电子邮件共享的密码）后，重置密码并更新到 ```_secret_auth_.json``` 文件中。  
![image](https://github.com/user-attachments/assets/01fe4b6d-9e51-4885-be42-da1729b9ea09)
### 退出按钮
仅在用户已登录时在侧边栏生成，允许用户退出。
![image](https://github.com/user-attachments/assets/39886c88-7a46-458c-b038-7981fc81750b)


## 版本
v0.1.0


## 许可

本项目使用 MIT 许可证。有关详细信息，请查看 [LICENSE](LICENSE) 文件。
