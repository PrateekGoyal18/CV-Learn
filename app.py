import streamlit as st
from modules.style import *
from modules.pages import *

code = '''
def hello():
    print("Hello, Streamlit!")
'''
PAGE_NAV_OPTIONS = ('Home', 'Image Options', 'About')
IMAGE_NAV_OPTIONS = ('Image Information', 'Grayscale', 'Color Extraction', 'Shifting', 'Rotation', 'Resize', 'Blurring', 'Histogram')

if __name__ == '__main__':
    st.beta_set_page_config(page_title='CV-Learn', page_icon='None', layout='centered', initial_sidebar_state='expanded')
    st.set_option('deprecation.showfileUploaderEncoding', False)
    st.title('**Welcome to CV-Learn** :sunglasses:')  
    st.sidebar.title('Navigation')
    
    local_css("assets/css/style.css")
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
    # icon("search")

    # """Add this in your streamlit app.py"""
    # GA_JS = """Hello world!"""

    # # Insert the script in the head tag of the static template inside your virtual environement
    # index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    # soup = BeautifulSoup(index_path.read_text(), features="lxml")
    # if not soup.find(id='custom-js'):
    #     script_tag = soup.new_tag("script", id='custom-js')
    #     script_tag.string = GA_JS
    #     soup.head.append(script_tag)
    #     index_path.write_text(str(soup))

    page_name = st.sidebar.radio('Go to', PAGE_NAV_OPTIONS)
    page(page_name)