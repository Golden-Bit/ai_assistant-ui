########################################################################################################################
########################################################################################################################
import os

import requests
import streamlit as st

########################################################################################################################
########################################################################################################################


#def get_stream(url, json_input):
#
#    s = requests.Session()
#    full_response = ""
#    non_decoded_chunk = b''
#    with s.post(url, json=json_input, headers=None, stream=True) as resp:
#        for chunk in resp.iter_content():
#            if chunk:
#                non_decoded_chunk += chunk
#                try:
#                    full_response += non_decoded_chunk.decode()
#                    message_placeholder.markdown(full_response + "▌")
#                    non_decoded_chunk = b''
#                except UnicodeDecodeError:
#                    pass

url = st.secrets["url"]

########################################################################################################################
########################################################################################################################

########################################################################################################################
########################################################################################################################


#def get_stream(url, json_input):
#
#    s = requests.Session()
#    full_response = ""
#    non_decoded_chunk = b''
#    with s.post(url, json=json_input, headers=None, stream=True) as resp:
#        for chunk in resp.iter_content():
#            if chunk:
#                non_decoded_chunk += chunk
#                try:
#                    full_response += non_decoded_chunk.decode()
#                    message_placeholder.markdown(full_response + "▌")
#                    non_decoded_chunk = b''
#                except UnicodeDecodeError:
#                    pass

#url = "http://127.0.0.1:8080/chat"

system_message = "qa_on_knowledge_bank"


system_message_kwargs = {"you_are": "You are an expert AI assistant",
                         "argument": "Helo products and other information about Helo company.",
                         "you_can_only_answer": "about everything",
                         "if_other_topics": "don't worry.",
                         "more_info": "try to be as cut as possible. when possible provide URLs for the user to visit sites where they can find useful information on helo. You have a search tool that allows you to obtain information from documents related to Helo and its products. Use the tool to the best of your ability!"
                                      "Use the search tool, each time carrying out a different query but"#
                                      " always related to the question (so as to obtain the most heterogeneous results "#
                                      "possible).",
                                      #"If the answer contains mathematical formulas or equations write them in a format "
                                      #"that makes them similar to the format generated by Latex, but in such a way that "
                                      #"it is visible in markdown."
                         "language": 'user language'}


#system_message_kwargs = {"you_are": "an agent designed to write and execute python code to answer questions.",
#                         "argument": "AI and python language",
#                         "more_info": #"Use the Google search tool 4 times, each time carrying out a different query but"#
                                      #" always related to the question (so as to obtain the most heterogeneous results "#
                                      #"possible). Therefore, use the search tool in the photovoltaic knowledge base to "#
                                      #"better analyze the technical content of the searches carried out on Google.\n"
#                                      "You have access to a python REPL, which you can use to execute python code."
#                                      "If you get an error, debug your code and try again."
#                                      "Use the output of your code to answer the question. "
#                                      "You might know the answer without running any code, but you should still run the code to get the answer."
#                                      "If it does not seem like you can write code to answer the question, just answer the question without produce code."
#                                      "Find the relevant entities and concepts within the query, then use the 'search tool' for each entity to get as much "
#                                      "useful information as possible. You use this information to generate the response to the user's query. "
#                                      "If there are some useful links in put them inside output response."
#                                      "Use the code contained in the repositories, examples and documentation to the "
#                                      "best of your ability. ",}
                                      #"If the answer contains mathematical formulas or equations write them in a format "
                                      #"that makes them similar to the format generated by Latex, but in such a way that "
                                      #"it is visible in markdown."
                         #"language": 'ITALIAN'}

tools = [{"tool_name": "PVlib_readthedocs_knowledge_base",
          "function_name": "search_on_vector_store",
          "func_init_kwargs": {"user_id": "PV",
                               "vector_store_id": "PVlib_readthedocs_knowledge_vector_store",
                               "vector_store_kwargs": {
                                   "collection_name": "PVlib_readthedocs",
                               },
                               "search_kwargs": {"k": 4},
                               "embedding_function_type": "OpenAIEmbeddings",
                               "embedding_function_kwargs": {"chunk_size": 200},
                               },
          "tool_description": "useful for when you need to refer to PVlib documentations to produce the code/solution.",
          },
         {"tool_name": "PVlib_github_repositories_knowledge_base",
          "function_name": "search_on_vector_store",
          "func_init_kwargs": {"user_id": "PV",
                               "vector_store_id": "PVlib_repositories_knowledge_vector_store",
                               "vector_store_kwargs": {
                                   "collection_name": "PVlib_repositories",
                               },
                               "search_kwargs": {"k": 4},
                               "embedding_function_type": "OpenAIEmbeddings",
                               "embedding_function_kwargs": {"chunk_size": 200},
                               },
          "tool_description": "useful for when you need to refer to PVlib examples and documentation to produce the code/solution.",
          },
         {"tool_name": "PVlib_programming_tutorials_knowledge_base",
          "function_name": "search_on_vector_store",
          "func_init_kwargs": {"user_id": "PV",
                               "vector_store_id": "PVlib_tutorials_knowledge_vector_store",
                               "vector_store_kwargs": {
                                   "collection_name": "PVlib_tutorials",
                               },
                               "search_kwargs": {"k": 4},
                               "embedding_function_type": "OpenAIEmbeddings",
                               "embedding_function_kwargs": {"chunk_size": 200},
                               },
          "tool_description": "useful for when you need to refer to PVlib tutorials and documentation to produce the code/solution.",
          },
         {"tool_name": "PVlib_programming_tutorials_knowledge_base",
          "function_name": "search_on_vector_store",
          "func_init_kwargs": {"user_id": "PV",
                               "vector_store_id": "photovoltaic_knowledge_vector_store",
                               "vector_store_kwargs": {
                                   "collection_name": "photovoltaic",
                               },
                               "search_kwargs": {"k": 4},
                               "embedding_function_type": "OpenAIEmbeddings",
                               "embedding_function_kwargs": {"chunk_size": 200},
                               },
          "tool_description": "Useful for when you need to refer to photovoltaic technical information to produce the answer/solution.",
          },
         #{"function_name": "search_on_google",
          #},
         ]


tools = [
    {"tool_name": "search_about_helo",
     "function_name": "search_on_vector_store",
     "func_init_kwargs": {"user_id": "test_user_0",
                           "vector_store_id": "vector_store_1",
                           "vector_store_kwargs": {
                               #"collection_name": "helo_guides",
                           },
                           "search_kwargs": {"k": 5},
                           "embedding_function_type": "OpenAIEmbeddings",
                           "embedding_function_kwargs": {"chunk_size": 200},
                           },
      "tool_description": "Useful for when you need to refer to helo information to produce the answer/solution.",
          },
         ]

########################################################################################################################
########################################################################################################################

st.set_page_config(page_title="AI Assistant",
                   page_icon="https://static.wixstatic.com/media/"
                             "63b1fb_347ecbd8db7d415fa3bf7b420a22b3f5~mv2.png",
                   layout="centered",
                   initial_sidebar_state="auto",
                   menu_items=None)

#left_co, cent_co,last_co = st.columns(3)
#with cent_co:
#    st.image("https://static.wixstatic.com/media/63b1fb_4fb8962f303f4686822b59a8c284690a~mv2.png",
#             caption=None, width=None, use_column_width=True,
#             clamp=False, channels="RGB", output_format="auto")

#st.markdown("<h1 style='text-align: center; color: white;'>Assistente Fotovoltaico </h1>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant",
                                  "result": "Sono un assistente virtuale specializzato su informazioni relative " 
                                            "ai prodotti dell'azienda Helo."
                                            #"perchè dalla qualità delle risposte che ti fornirò dipende il futuro climatico "
                                            #"della terra e di tutto l'ecosistema, devo fare del mio meglio a tutti i costi!"
                                            "\n\n Come posso esserti utile ?"
                                  }]

if "ai_avatar_url" not in st.session_state:

    st.session_state.ai_avatar_url = ("https://static.wixstatic.com/media/"
                                      "63b1fb_347ecbd8db7d415fa3bf7b420a22b3f5~mv2.png")

if "user_avatar_url" not in st.session_state:

    st.session_state.user_avatar_url = ("https://encrypted-tbn0.gstatic.com/"
                                        "images?q=tbn:ANd9GcQiBwY_zfAf9K1OBN1"
                                        "eVu660SqIr6TliAKeAhAaWG5mxrLmsva8XPO"
                                        "0xhW2kHwth4D3IWM&usqp=CAU")
    #"https://cdn3.vectorstock.com/i/1000x1000/41/52/man-user-avatar-icon-person-profile-with-chat-vector-29004152.jpg"


def main():

    for message in st.session_state.messages:
        if message["role"] == "user":
            with st.chat_message(message["role"], avatar=st.session_state.user_avatar_url):
                st.markdown(message["question"])
        else:
            with st.chat_message(message["role"], avatar=st.session_state.ai_avatar_url):
                st.markdown(message["result"])

    if prompt := st.chat_input("Say something"):

        st.session_state.messages.append({"role": "user", "question": prompt})

        #####################################################################
        # for secure
        if len(st.session_state.messages) > 30:
            st.session_state.messages = st.session_state.messages[-30:]
        #####################################################################

        with st.chat_message("user", avatar=st.session_state.user_avatar_url):
            st.markdown(prompt)

        with st.chat_message("assistant", avatar=st.session_state.ai_avatar_url):
            message_placeholder = st.empty()
            s = requests.Session()
            full_response = ""
            json_input = {"message": prompt,
                          "system_message": system_message,
                          "system_message_kwargs": system_message_kwargs,
                          "tools": tools,
                          "chat_history": st.session_state.messages[-30:]}

            non_decoded_chunk = b''
            with s.post(url, json=json_input, headers=None, stream=True) as resp:
                for chunk in resp.iter_content():
                    if chunk:
                        non_decoded_chunk += chunk
                        try:
                            full_response += non_decoded_chunk.decode()
                            message_placeholder.markdown(full_response + "▌")
                            non_decoded_chunk = b''
                        except UnicodeDecodeError:
                            pass
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "result": full_response})
########################################################################################################################


def sidebar():
    with st.sidebar:
        #st.image("https://static.wixstatic.com/shapes/63b1fb_be9011a5235c419ca293745311d3af6a.svg",
        #         caption=None, width=None, use_column_width='always',
        #         clamp=False, channels="RGB", output_format="auto")

        #st.markdown("# Helo Virtual assistant")
        st.markdown("<h1 style='text-align: center; color: violet;'>Helo Virtual assistant</h1>",
                    unsafe_allow_html=True)
        st.markdown("--- \n")

        st.markdown("<h3 style='text-align: center;'>About</h3>",
                    unsafe_allow_html=True)
        st.markdown(
            "Il Chatbot basato sul sito di Helo è un assistente virtuale intelligente che utilizza le informazioni ricavate dal sito web di Helo per fornire risposte accurate e tempestive agli utenti. Può fornire dettagli sui prodotti e servizi offerti da Helo, rispondere a domande tecniche e fornire consigli per migliorare il benessere generale. È un modo intuitivo e facile per ottenere informazioni sulle offerte di Helo."
        )

        #st.markdown("<h1 style='text-align: center; color: violet;'>Fonti</h1>",
        #            unsafe_allow_html=True)

        #st.markdown("Di seguito puoi trovare i riferimenti online ai documenti "
        #            "da cui l'assistente ha appreso tutte le sue conoscenze:\n"
        #            " * [Keras](https://keras.io/)\n"
        #            " * [Scikit Learn](https://scikit-learn.org/stable/)\n"
        #            " * [Langchain](https://python.langchain.com/docs/get_started/introduction)\n")

        #st.header("Domande di esempio:")
        #st.markdown(
        #    "1. Qauli incidenti hanno coinvolto i trasformatori instalalti all'interno dei treni ?\n"
        #    "2. Genera uan sintesi dei report (per punti) riguardanti guasti ai trasformatori.\n"
        #    "3. Descrivi le possibili cause del guasto e le contromisure adottate (enumerandole).\n"
        #    "4. Genera uan tabella (avente due colonne) per la rappresentazione dei dati contenuti nel report.\n"
        #    "5. Quali incidenti si sono verificati con il modello di treno 'ETR521 Rock train'?"
        #    "Nel caso in cui si siano riportati incidenti scrivimi una breve descrizione per ognuno di essi. \n"
        #)
        st.markdown("--- \n")

        st.markdown("<p style='text-align: center; color: violet;'>Powered by <a href='https://cyberneid.com/'>Cyberneid</a></p>",
                    unsafe_allow_html=True)

        st.markdown("<h4 style='text-align: center; color: violet;'>© 2024 by Cyberneid s.r.l</h4>",
                    unsafe_allow_html=True)
########################################################################################################################
########################################################################################################################


main()
sidebar()
