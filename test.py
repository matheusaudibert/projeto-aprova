import streamlit as st
from streamlit_plugins.components.theme_changer import st_theme_changer
from streamlit_plugins.components.theme_changer.entity import ThemeInfo, ThemeInput, ThemeBaseLight, ThemeBaseDark
theme_data = dict(
    light_day=ThemeInput(
        name="Light Day",
        icon=":material/light_mode:", 
        order=0,
        themeInfo=ThemeInfo(
            base=ThemeBaseLight.base,
            primaryColor="#60B4FF",
            backgroundColor="#ffffff",
            secondaryBackgroundColor="#e8e8e8",
            textColor="#000000",
            bodyFont=ThemeBaseLight.bodyFont,
            codeFont=ThemeBaseLight.codeFont,
            fontFaces=ThemeBaseLight.fontFaces,
        )
    ),
    dark_night=ThemeInput(
        name="Dark Night",
        icon=":material/dark_mode:",
        order=1,
        themeInfo=ThemeInfo(
            base=ThemeBaseLight.base,
            primaryColor="#60B4FF",
            backgroundColor="#000000",
            secondaryBackgroundColor="##1e1e1e",
            textColor="#ffffff",

            fontFaces=ThemeBaseLight.fontFaces,
        )
    ),
    github=ThemeInput(
        name="GitHub",
        icon=":material/code:",
        order=2,
        themeInfo=ThemeInfo(
            base=ThemeBaseLight.base,
            primaryColor="#60B4FF",
            backgroundColor="#0D1117",
            secondaryBackgroundColor="#30363D",
            textColor="#ffffff",
            fontFaces=ThemeBaseLight.fontFaces,
        )
    )
)

with st.sidebar:
    st_theme_changer(
        themes_data=theme_data, render_mode="pills",
        rerun_whole_st=True, key="secondary_pills"
    )