# mkdir -p ~/.streamlit/

# echo "\
# [general]\n\
# email = \"prateekg045@gmail.com\"\n\
# " > ~/.streamlit/credentials.toml

# echo "\
# [server]\n\
# headless = true\n\
# enableCORS=false\n\
# port = $PORT\n\
# " > ~/.streamlit/config.toml


# # mkdir -p ~/.streamlit/
# # echo "
# # [server]\n
# # headless = true\n
# # enableCORS=false\n
# # port = $PORT\n
# # \n
# # " > ~/.streamlit/config.toml


# mkdir -p ~/.streamlit

# echo "[server]
# headless = true
# port = $PORT
# enableCORS = false
# " > ~/.streamlit/config.toml

mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml