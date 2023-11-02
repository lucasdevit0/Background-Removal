from rembg import remove
import streamlit as st
from io import BytesIO
from PIL import Image

st.set_page_config(layout='wide', page_title='Image Background Removal')

st.write('## Remove background from your image :camera:')
st.write('Upload an image and see the background magically removed in just a few seconds! :upside_down_face:')
st.write(':point_left: Full quality image can be downloaded in the sidebar.')
st.write('\n')

st.sidebar.write('Upload and download :arrow_down:')

MAX_FILE_SIZE = 5 * 1024 * 1024 #5MB

col1, col2 = st.columns(2)
upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Download
def download_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im
    
# Remove bg
def remove_bg(upload):
    original = Image.open(upload)
    col1.write('##### Original Image')
    col1.image(original)
    
    col2.write('##### Processed Image')
    nobg = remove(original)
    col2.image(nobg)
    
    st.sidebar.markdown('\n')
    st.sidebar.download_button("Download processed image", download_image(nobg),"no_bg_image.png", "image/png")

st.write('\n')
st.write('# Info:')
st.write('All code is open source and can be found at this [Github repository](https://github.com/lucasdevit0/Background-Removal)')
st.write('Credits to [rembg](https://github.com/danielgatis/rembg)')
st.write('Author: Lucas de Vito, connect with me on [Linkedin](https://www.linkedin.com/in/devitolucas/)')
    
if upload is None:
    remove_bg('img/girafe.jpg')
else:
    if upload.size > MAX_FILE_SIZE:
        st.error('Uploaded file is too large! Select file < 5MB.')
    else:
        remove_bg(upload = upload)

