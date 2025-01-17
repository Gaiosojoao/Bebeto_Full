import streamlit as st

TIPOS_ARQUIVOS_VALIDDOS = [ 
    'Site', 'Youtube', 'Pdf', 'Csv', 'Txt'
]

MENSAGENS_EXEMPLO = [
    ('user', 'Olá, Bebeto!'),    
    ('assistant', 'Tudo bem?'),
    ('user', 'Tudo ótimo'),
]

def pagina_chat():
    st.header('🤖 Bem-vindo ao Bebeto', divider=True)

    mensagens = st.session_state.get('mensagens', MENSAGENS_EXEMPLO)
    for mensagem in mensagens:
        chat = st.chat_message(mensagem[0])
        chat.markdown(mensagem[1])
    input_usuario = st.chat_input('Fale com o Bebeto!')
    if input_usuario:
        mensagens.append(('user', input_usuario))
        st.session_state['mensagens'] = mensagens  
        st.rerun() 

def sidebar():
    tabs = st.tabs(['Upload de Arquivos', 'Seleção de Modelos'])
    with tabs[0]:
        tipo_arquivo = st.selectbox('Tipo de Arquivo', TIPOS_ARQUIVOS_VALIDDOS)
        if tipo_arquivo == 'Site':
            url = st.text_input('Digite a URL do site:')
        if tipo_arquivo == 'Youtube':
            url = st.text_input('Digite a URL do video:')
        if tipo_arquivo == 'Pdf':
           url = st.file_uploader('Faça o upload do arquivo pdf:', type=['pdf'])
        if tipo_arquivo == 'Csv':
           url = st.file_uploader('Faça o upload do arquivo csv:', type=['.csv'])
        if tipo_arquivo == 'Txt':
           url = st.file_uploader('Faça o upload do arquivo txt:', type=['.txt'])
    
    

def main(): 
    pagina_chat()
    with st.sidebar:
        sidebar()


if __name__ == '__main__':
    main()