from setuptools import setup, find_packages
setup(
    name='streamlit_login_auth_ui_zh',  # 替换为你的包名
    version='0.1.0',  # 版本号
    packages=find_packages(),  # 自动查找包含的包
    install_requires=[
    ],  # 依赖库
    author='Rycen7822',
    author_email='kristinharrison7826@gmail.com',
    description='这个库是一个用户友好的 Streamlit 登录/注册系统，基于streamlit_login_auth_ui 库改写构建。 它为开发者提供了一种简单的方法，以便在其 Streamlit 应用程序中实现安全的用户身份注册和验证。',  # 描述
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Python 版本要求
)

