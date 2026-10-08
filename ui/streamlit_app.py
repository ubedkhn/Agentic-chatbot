# # import os

# # import requests
# # import streamlit as st
# # from dotenv import load_dotenv

# # load_dotenv()

# # BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:8000').rstrip('/')

# # st.set_page_config(
# #     page_title='Agentic Chatbot',
# #     page_icon='🤖',
# #     layout='centered',
# # )

# # st.title('🤖 Agentic Chatbot')
# # st.caption('Streamlit UI -> FastAPI -> LangGraph Agent -> Tools -> Response')

# # with st.sidebar:
# #     st.subheader('Backend')
# #     st.code(BACKEND_URL)
# #     st.write('Tools: calculator, current time, weather')
# #     if st.button('Clear chat'):
# #         st.session_state.messages = []
# #         st.rerun()

# # if 'messages' not in st.session_state:
# #     st.session_state.messages = []

# # for message in st.session_state.messages:
# #     with st.chat_message(message['role']):
# #         st.markdown(message['content'])

# # prompt = st.chat_input('Ask something...')

# # if prompt:
# #     with st.chat_message('user'):
# #         st.markdown(prompt)

# #     history = st.session_state.messages.copy()
# #     st.session_state.messages.append({'role': 'user', 'content': prompt})

# #     with st.chat_message('assistant'):
# #         with st.spinner('Agent is working...'):
# #             try:
# #                 response = requests.post(
# #                     f'{BACKEND_URL}/chat',
# #                     json={'message': prompt, 'history': history},
# #                     timeout=120,
# #                 )
# #                 response.raise_for_status()
# #                 data = response.json()
# #                 answer = data['answer']
# #                 tool_calls = data.get('tool_calls', [])

# #                 st.markdown(answer)
# #                 if tool_calls:
# #                     st.caption('Tools used: ' + ', '.join(tool_calls))

# #                 st.session_state.messages.append(
# #                     {'role': 'assistant', 'content': answer}
# #                 )
# #             except requests.RequestException as exc:
# #                 st.error(f'Backend connection failed: {exc}')
# #             except Exception as exc:
# #                 st.error(f'Unexpected error: {exc}')
# #-----------------------------------------------------------------------------
# import os
# import textwrap

# import requests
# import streamlit as st
# from dotenv import load_dotenv

# load_dotenv()

# BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:8000').rstrip('/')

# st.set_page_config(
#     page_title='J.A.R.V.I.S | Agentic AI',
#     page_icon='🤖',
#     layout='wide',
# )

# # ----------------------------------------------------------------------------
# # GLASSMORPHISM / JARVIS THEME
# # (CSS must have no blank lines and no leading indentation inside st.markdown)
# # ----------------------------------------------------------------------------
# CSS = """
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Inter:wght@300;400;500;600&display=swap');
# :root {
#   --cyan: #00e5ff;
#   --blue: #3b82f6;
#   --violet: #8b5cf6;
#   --glass: rgba(255, 255, 255, 0.06);
#   --glass-strong: rgba(255, 255, 255, 0.10);
#   --border: rgba(255, 255, 255, 0.16);
# }
# html, body, [class*="css"], .stApp { font-family: 'Inter', sans-serif; }
# .stApp {
#   background: radial-gradient(circle at 15% 20%, #0b1a3a 0%, transparent 45%),
#               radial-gradient(circle at 85% 80%, #2a0f4a 0%, transparent 45%),
#               linear-gradient(135deg, #04060f 0%, #070b1c 50%, #05030d 100%);
#   background-attachment: fixed;
#   color: #e6f1ff;
# }
# .stApp::before {
#   content: ''; position: fixed; inset: 0; pointer-events: none; z-index: 0;
#   background-image: linear-gradient(rgba(0,229,255,0.04) 1px, transparent 1px),
#                     linear-gradient(90deg, rgba(0,229,255,0.04) 1px, transparent 1px);
#   background-size: 48px 48px;
#   mask-image: radial-gradient(circle at center, black 30%, transparent 80%);
# }
# .orb { position: fixed; border-radius: 50%; filter: blur(90px); opacity: 0.35; z-index: 0; pointer-events: none; animation: float 14s ease-in-out infinite; }
# .orb.o1 { width: 380px; height: 380px; background: var(--cyan); top: -80px; left: -80px; }
# .orb.o2 { width: 420px; height: 420px; background: var(--violet); bottom: -120px; right: -100px; animation-delay: -6s; }
# .orb.o3 { width: 260px; height: 260px; background: var(--blue); top: 45%; left: 55%; animation-delay: -3s; opacity: 0.2; }
# @keyframes float { 0%,100% { transform: translate(0,0) scale(1); } 50% { transform: translate(40px,-50px) scale(1.15); } }
# header[data-testid="stHeader"] { background: transparent; }
# #MainMenu, footer { visibility: hidden; }
# .block-container { max-width: 980px; padding-top: 1.5rem; padding-bottom: 7rem; position: relative; z-index: 1; }
# section[data-testid="stSidebar"] {
#   background: rgba(8, 12, 30, 0.55) !important;
#   backdrop-filter: blur(22px) saturate(160%);
#   -webkit-backdrop-filter: blur(22px) saturate(160%);
#   border-right: 1px solid var(--border);
# }
# section[data-testid="stSidebar"] * { color: #d6e6ff; }
# .glass {
#   background: var(--glass);
#   backdrop-filter: blur(18px) saturate(170%);
#   -webkit-backdrop-filter: blur(18px) saturate(170%);
#   border: 1px solid var(--border);
#   border-radius: 20px;
#   box-shadow: 0 8px 32px rgba(0,0,0,0.45), inset 0 1px 0 rgba(255,255,255,0.12);
# }
# .hero { display: flex; align-items: center; gap: 22px; padding: 20px 26px; margin-bottom: 18px; }
# .reactor { position: relative; width: 78px; height: 78px; flex: 0 0 78px; }
# .reactor .ring { position: absolute; inset: 0; border-radius: 50%; border: 2px solid transparent; }
# .reactor .r1 { border-top-color: var(--cyan); border-bottom-color: var(--cyan); animation: spin 3s linear infinite; }
# .reactor .r2 { inset: 9px; border-left-color: var(--blue); border-right-color: var(--blue); animation: spin 2s linear infinite reverse; }
# .reactor .r3 { inset: 18px; border-top-color: var(--violet); border-bottom-color: var(--violet); animation: spin 1.4s linear infinite; }
# .reactor .core { position: absolute; inset: 28px; border-radius: 50%; background: radial-gradient(circle, #fff 0%, var(--cyan) 45%, transparent 75%); box-shadow: 0 0 25px var(--cyan), 0 0 55px rgba(0,229,255,0.6); animation: pulse 2s ease-in-out infinite; }
# @keyframes spin { to { transform: rotate(360deg); } }
# @keyframes pulse { 0%,100% { transform: scale(0.85); opacity: 0.8; } 50% { transform: scale(1.15); opacity: 1; } }
# .hero h1 { font-family: 'Orbitron', sans-serif; font-weight: 900; font-size: 1.9rem; letter-spacing: 0.18em; margin: 0; background: linear-gradient(90deg, #fff, var(--cyan), var(--violet)); -webkit-background-clip: text; background-clip: text; color: transparent; }
# .hero p { margin: 4px 0 0 0; color: #8fb2d9; font-size: 0.85rem; letter-spacing: 0.06em; }
# .pill { display: inline-flex; align-items: center; gap: 8px; padding: 5px 14px; border-radius: 999px; font-size: 0.75rem; font-weight: 500; letter-spacing: 0.08em; background: var(--glass); border: 1px solid var(--border); }
# .dot { width: 8px; height: 8px; border-radius: 50%; animation: blink 1.6s infinite; }
# .dot.on { background: #22ff9c; box-shadow: 0 0 10px #22ff9c; }
# .dot.off { background: #ff4d6d; box-shadow: 0 0 10px #ff4d6d; }
# @keyframes blink { 50% { opacity: 0.35; } }
# .hero .status { margin-left: auto; }
# div[data-testid="stChatMessage"] {
#   background: var(--glass);
#   backdrop-filter: blur(16px) saturate(160%);
#   -webkit-backdrop-filter: blur(16px) saturate(160%);
#   border: 1px solid var(--border);
#   border-radius: 18px;
#   padding: 14px 18px;
#   margin-bottom: 14px;
#   box-shadow: 0 6px 24px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.10);
#   animation: slideIn 0.45s cubic-bezier(.2,.8,.2,1);
# }
# div[data-testid="stChatMessage"]:has(img[alt="user avatar"]),
# div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
#   background: linear-gradient(135deg, rgba(59,130,246,0.22), rgba(139,92,246,0.18));
#   border-color: rgba(139,180,255,0.35);
# }
# div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {
#   border-left: 3px solid var(--cyan);
# }
# @keyframes slideIn { from { opacity: 0; transform: translateY(14px) scale(0.98); } to { opacity: 1; transform: none; } }
# div[data-testid="stChatMessage"] p, div[data-testid="stChatMessage"] li { color: #e6f1ff; line-height: 1.65; }
# div[data-testid="stChatMessage"] code { background: rgba(0,0,0,0.4); color: var(--cyan); border-radius: 6px; padding: 2px 6px; }
# div[data-testid="stBottom"] > div, div[data-testid="stBottomBlockContainer"] { background: transparent !important; }
# div[data-testid="stChatInput"] {
#   background: rgba(255,255,255,0.07) !important;
#   backdrop-filter: blur(20px) saturate(170%);
#   -webkit-backdrop-filter: blur(20px) saturate(170%);
#   border: 1px solid rgba(0,229,255,0.35) !important;
#   border-radius: 999px !important;
#   box-shadow: 0 0 24px rgba(0,229,255,0.18), inset 0 1px 0 rgba(255,255,255,0.12);
#   transition: box-shadow .3s, border-color .3s;
# }
# div[data-testid="stChatInput"]:focus-within { border-color: var(--cyan) !important; box-shadow: 0 0 34px rgba(0,229,255,0.45); }
# div[data-testid="stChatInput"] textarea { color: #e6f1ff !important; background: transparent !important; }
# div[data-testid="stChatInput"] textarea::placeholder { color: #7f9cc0 !important; }
# .stButton > button {
#   background: var(--glass) !important;
#   color: #dff3ff !important;
#   border: 1px solid var(--border) !important;
#   border-radius: 14px !important;
#   backdrop-filter: blur(14px);
#   transition: all .25s ease;
#   font-weight: 500;
# }
# .stButton > button:hover { transform: translateY(-2px); border-color: var(--cyan) !important; box-shadow: 0 0 20px rgba(0,229,255,0.35); color: #fff !important; }
# .tool-badge { display: inline-block; margin: 8px 6px 0 0; padding: 4px 12px; font-size: 0.72rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--cyan); background: rgba(0,229,255,0.10); border: 1px solid rgba(0,229,255,0.4); border-radius: 999px; box-shadow: 0 0 12px rgba(0,229,255,0.2); }
# .thinking { display: flex; align-items: center; gap: 12px; color: #8fdcff; font-size: 0.9rem; letter-spacing: 0.08em; }
# .thinking .bars { display: flex; gap: 4px; align-items: flex-end; height: 22px; }
# .thinking .bars span { width: 4px; background: linear-gradient(var(--cyan), var(--violet)); border-radius: 2px; animation: eq 1s ease-in-out infinite; }
# .thinking .bars span:nth-child(2) { animation-delay: .12s; }
# .thinking .bars span:nth-child(3) { animation-delay: .24s; }
# .thinking .bars span:nth-child(4) { animation-delay: .36s; }
# .thinking .bars span:nth-child(5) { animation-delay: .48s; }
# @keyframes eq { 0%,100% { height: 5px; } 50% { height: 22px; } }
# .welcome { padding: 34px; text-align: center; margin-bottom: 18px; }
# .welcome h3 { font-family: 'Orbitron', sans-serif; letter-spacing: 0.12em; color: #fff; margin-bottom: 6px; }
# .welcome p { color: #8fb2d9; margin: 0; }
# .sb-title { font-family: 'Orbitron', sans-serif; font-size: 0.8rem; letter-spacing: 0.2em; color: var(--cyan); margin: 14px 0 8px 0; }
# .sb-card { padding: 12px 14px; margin-bottom: 10px; font-size: 0.85rem; }
# .sb-card code { color: var(--cyan) !important; background: rgba(0,0,0,0.35) !important; font-size: 0.75rem; word-break: break-all; }
# .stat { display: flex; justify-content: space-between; padding: 4px 0; }
# .stat b { color: var(--cyan); font-family: 'Orbitron', sans-serif; }
# ::-webkit-scrollbar { width: 8px; }
# ::-webkit-scrollbar-thumb { background: rgba(0,229,255,0.35); border-radius: 8px; }
# </style>
# <div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div>
# """
# st.markdown(CSS, unsafe_allow_html=True)


# # ----------------------------------------------------------------------------
# # HELPERS
# # ----------------------------------------------------------------------------
# @st.cache_data(ttl=15, show_spinner=False)
# def backend_online(url: str) -> bool:
#     """Any HTTP response below 500 means the backend is reachable."""
#     try:
#         return requests.get(f'{url}/health', timeout=2).status_code < 500
#     except requests.RequestException:
#         return False


# def html(block: str) -> None:
#     """Render raw HTML safely (dedent so Markdown doesn't treat it as code)."""
#     st.markdown(textwrap.dedent(block).strip(), unsafe_allow_html=True)


# def tool_badges(tool_calls) -> str:
#     return ''.join(f'<span class="tool-badge">⚙ {t}</span>' for t in tool_calls)


# def render_message(msg: dict) -> None:
#     avatar = '🧑‍💻' if msg['role'] == 'user' else '🤖'
#     with st.chat_message(msg['role'], avatar=avatar):
#         st.markdown(msg['content'])
#         if msg.get('tool_calls'):
#             html(f'<div>{tool_badges(msg["tool_calls"])}</div>')


# THINKING_HTML = (
#     '<div class="thinking"><div class="bars">'
#     '<span></span><span></span><span></span><span></span><span></span>'
#     '</div>AGENT PROCESSING · REASONING · CALLING TOOLS...</div>'
# )

# # ----------------------------------------------------------------------------
# # STATE
# # ----------------------------------------------------------------------------
# if 'messages' not in st.session_state:
#     st.session_state.messages = []
# if 'pending' not in st.session_state:
#     st.session_state.pending = None

# online = backend_online(BACKEND_URL)

# # ----------------------------------------------------------------------------
# # SIDEBAR
# # ----------------------------------------------------------------------------
# with st.sidebar:
#     html('<div class="sb-title">◈ BACKEND LINK</div>')
#     html(f'<div class="glass sb-card"><code>{BACKEND_URL}</code></div>')

#     html('<div class="sb-title">◈ ACTIVE MODULES</div>')
#     html(
#         """
#         <div class="glass sb-card">
#         🧮 Calculator<br>🕒 Current Time<br>🌦️ Weather
#         </div>
#         """
#     )

#     total_tools = sum(len(m.get('tool_calls', [])) for m in st.session_state.messages)
#     html('<div class="sb-title">◈ SESSION TELEMETRY</div>')
#     html(
#         f"""
#         <div class="glass sb-card">
#         <div class="stat"><span>Messages</span><b>{len(st.session_state.messages)}</b></div>
#         <div class="stat"><span>Tool calls</span><b>{total_tools}</b></div>
#         </div>
#         """
#     )

#     if st.button('🗑  Clear chat', use_container_width=True):
#         st.session_state.messages = []
#         st.session_state.pending = None
#         st.rerun()

# # ----------------------------------------------------------------------------
# # HERO HEADER
# # ----------------------------------------------------------------------------
# status_dot = 'on' if online else 'off'
# status_txt = 'SYSTEMS ONLINE' if online else 'BACKEND OFFLINE'
# html(
#     f"""
#     <div class="glass hero">
#       <div class="reactor">
#         <div class="ring r1"></div><div class="ring r2"></div><div class="ring r3"></div>
#         <div class="core"></div>
#       </div>
#       <div>
#         <h1>J.A.R.V.I.S</h1>
#         <p>Streamlit UI → FastAPI → LangGraph Agent → Tools → Response</p>
#       </div>
#       <div class="status"><span class="pill"><span class="dot {status_dot}"></span>{status_txt}</span></div>
#     </div>
#     """
# )

# # ----------------------------------------------------------------------------
# # WELCOME + QUICK ACTIONS (only when chat is empty)
# # ----------------------------------------------------------------------------
# if not st.session_state.messages:
#     html(
#         """
#         <div class="glass welcome">
#           <h3>AT YOUR SERVICE</h3>
#           <p>Ask me to calculate, check the time, or fetch the weather. Pick a quick command or type below.</p>
#         </div>
#         """
#     )
#     quick = [
#         ('🧮 Calculate', 'What is (1234 * 56) / 7?'),
#         ('🕒 Time now', 'What is the current time?'),
#         ('🌦️ Weather', 'What is the weather in Indore right now?'),
#     ]
#     cols = st.columns(len(quick))
#     for col, (label, text) in zip(cols, quick):
#         if col.button(label, use_container_width=True, key=f'quick_{label}'):
#             st.session_state.pending = text
#             st.rerun()

# # ----------------------------------------------------------------------------
# # CHAT HISTORY
# # ----------------------------------------------------------------------------
# for message in st.session_state.messages:
#     render_message(message)

# # ----------------------------------------------------------------------------
# # INPUT + BACKEND CALL
# # ----------------------------------------------------------------------------
# typed = st.chat_input('Command J.A.R.V.I.S ...')
# prompt = typed or st.session_state.pending
# st.session_state.pending = None

# if prompt:
#     render_message({'role': 'user', 'content': prompt})

#     # Backend only needs role + content (same format as before)
#     history = [
#         {'role': m['role'], 'content': m['content']}
#         for m in st.session_state.messages
#     ]
#     st.session_state.messages.append({'role': 'user', 'content': prompt})

#     with st.chat_message('assistant', avatar='🤖'):
#         placeholder = st.empty()
#         placeholder.markdown(THINKING_HTML, unsafe_allow_html=True)
#         try:
#             response = requests.post(
#                 f'{BACKEND_URL}/chat',
#                 json={'message': prompt, 'history': history},
#                 timeout=120,
#             )
#             response.raise_for_status()
#             data = response.json()
#             answer = data['answer']
#             tool_calls = data.get('tool_calls', [])

#             placeholder.markdown(answer)
#             if tool_calls:
#                 html(f'<div>{tool_badges(tool_calls)}</div>')

#             st.session_state.messages.append(
#                 {'role': 'assistant', 'content': answer, 'tool_calls': tool_calls}
#             )
#         except requests.RequestException as exc:
#             placeholder.empty()
#             st.error(f'Backend connection failed: {exc}')
#         except Exception as exc:
#             placeholder.empty()
#             st.error(f'Unexpected error: {exc}')

import os
import re
import textwrap
import time
from html import escape

import requests
import streamlit as st
import streamlit.components.v1 as components
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:8000').rstrip('/')

st.set_page_config(
    page_title='Agentic AI',
    page_icon='✨',
    layout='wide',
    initial_sidebar_state='expanded',
)

# ----------------------------------------------------------------------------
# THEME TOKENS (dark / light)
# ----------------------------------------------------------------------------
THEMES = {
    'dark': {
        'bg1': '#04060f', 'bg2': '#070b1c', 'bg3': '#05030d',
        'glow1': '#0b1a3a', 'glow2': '#2a0f4a',
        'text': '#e8f1ff', 'muted': '#8fb2d9',
        'glass': 'rgba(255,255,255,0.06)', 'glass2': 'rgba(255,255,255,0.10)',
        'border': 'rgba(255,255,255,0.16)', 'shadow': 'rgba(0,0,0,0.45)',
        'hi': 'rgba(255,255,255,0.12)',
        'a1': '#00e5ff', 'a2': '#3b82f6', 'a3': '#a855f7',
        'grid': 'rgba(0,229,255,0.045)', 'orbop': '0.35',
        'input': 'rgba(255,255,255,0.07)', 'codebg': 'rgba(0,0,0,0.40)',
        'side': 'rgba(8,12,30,0.55)', 'spot': 'rgba(0,229,255,0.08)',
        'user1': 'rgba(59,130,246,0.22)', 'user2': 'rgba(168,85,247,0.18)',
    },
    'light': {
        'bg1': '#eef3ff', 'bg2': '#f6f1ff', 'bg3': '#e9f7fb',
        'glow1': '#cfe0ff', 'glow2': '#e4d3ff',
        'text': '#0f1b3a', 'muted': '#51648a',
        'glass': 'rgba(255,255,255,0.55)', 'glass2': 'rgba(255,255,255,0.80)',
        'border': 'rgba(80,100,160,0.20)', 'shadow': 'rgba(60,80,140,0.18)',
        'hi': 'rgba(255,255,255,0.90)',
        'a1': '#0891b2', 'a2': '#2563eb', 'a3': '#7c3aed',
        'grid': 'rgba(37,99,235,0.06)', 'orbop': '0.30',
        'input': 'rgba(255,255,255,0.75)', 'codebg': 'rgba(15,27,58,0.08)',
        'side': 'rgba(255,255,255,0.60)', 'spot': 'rgba(37,99,235,0.08)',
        'user1': 'rgba(37,99,235,0.14)', 'user2': 'rgba(124,58,237,0.12)',
    },
}

if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'pending' not in st.session_state:
    st.session_state.pending = None

theme_name = 'light' if st.session_state.get('light_mode', False) else 'dark'
ROOT_VARS = ':root{' + ''.join(f'--{k}:{v};' for k, v in THEMES[theme_name].items()) + '}'

# ----------------------------------------------------------------------------
# GLOBAL CSS  (no blank lines inside - Markdown would break the HTML block)
# ----------------------------------------------------------------------------
BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Inter:wght@300;400;500;600&display=swap');
@property --ang { syntax: '<angle>'; inherits: false; initial-value: 0deg; }
html, body, .stApp, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp {
  background: radial-gradient(circle at 12% 18%, var(--glow1) 0%, transparent 45%),
              radial-gradient(circle at 88% 82%, var(--glow2) 0%, transparent 45%),
              linear-gradient(135deg, var(--bg1) 0%, var(--bg2) 50%, var(--bg3) 100%);
  background-attachment: fixed;
  color: var(--text);
}
.stApp::before {
  content: ''; position: fixed; inset: 0; pointer-events: none; z-index: 0;
  background-image: linear-gradient(var(--grid) 1px, transparent 1px), linear-gradient(90deg, var(--grid) 1px, transparent 1px);
  background-size: 52px 52px;
  mask-image: radial-gradient(circle at center, black 25%, transparent 78%);
  -webkit-mask-image: radial-gradient(circle at center, black 25%, transparent 78%);
}
.stApp::after {
  content: ''; position: fixed; inset: 0; pointer-events: none; z-index: 0;
  background: radial-gradient(520px circle at var(--mx, 50%) var(--my, 30%), var(--spot), transparent 60%);
}
.orb { position: fixed; border-radius: 50%; filter: blur(95px); opacity: var(--orbop); z-index: 0; pointer-events: none; animation: float 16s ease-in-out infinite; }
.orb.o1 { width: 400px; height: 400px; background: var(--a1); top: -90px; left: -90px; }
.orb.o2 { width: 440px; height: 440px; background: var(--a3); bottom: -130px; right: -110px; animation-delay: -7s; }
.orb.o3 { width: 280px; height: 280px; background: var(--a2); top: 45%; left: 55%; animation-delay: -3s; opacity: 0.2; }
@keyframes float { 0%,100% { transform: translate(0,0) scale(1); } 50% { transform: translate(45px,-55px) scale(1.15); } }
header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }
[class*="stElementContainer"]:has(iframe[height="0"]), .element-container:has(iframe[height="0"]) { position: absolute; height: 0; width: 0; overflow: hidden; margin: 0; padding: 0; }
.block-container { max-width: 1000px; padding-top: 1.4rem; padding-bottom: 8rem; position: relative; z-index: 1; }
.stApp p, .stApp li, .stApp label, [data-testid="stWidgetLabel"] p { color: var(--text); }
section[data-testid="stSidebar"] { background: var(--side) !important; backdrop-filter: blur(24px) saturate(170%); -webkit-backdrop-filter: blur(24px) saturate(170%); border-right: 1px solid var(--border); }
.glass { background: var(--glass); backdrop-filter: blur(18px) saturate(170%); -webkit-backdrop-filter: blur(18px) saturate(170%); border: 1px solid var(--border); border-radius: 22px; box-shadow: 0 10px 36px var(--shadow), inset 0 1px 0 var(--hi); }
.hero { position: relative; display: flex; align-items: center; gap: 24px; padding: 22px 28px; margin-bottom: 20px; overflow: hidden; }
.hero::before { content: ''; position: absolute; inset: 0; border-radius: inherit; padding: 1.5px; pointer-events: none; background: conic-gradient(from var(--ang), transparent 0%, var(--a1) 12%, transparent 30%, var(--a3) 60%, transparent 80%); -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0); -webkit-mask-composite: xor; mask-composite: exclude; animation: rot 6s linear infinite; }
@keyframes rot { to { --ang: 360deg; } }
.core { position: relative; width: 74px; height: 74px; flex: 0 0 74px; }
.core .ring { position: absolute; inset: 0; border-radius: 50%; border: 2px solid transparent; }
.core .r1 { border-top-color: var(--a1); border-bottom-color: var(--a1); animation: spin 3.2s linear infinite; }
.core .r2 { inset: 9px; border-left-color: var(--a2); border-right-color: var(--a2); animation: spin 2.2s linear infinite reverse; }
.core .r3 { inset: 18px; border-top-color: var(--a3); border-bottom-color: var(--a3); animation: spin 1.5s linear infinite; }
.core .nucleus { position: absolute; inset: 28px; border-radius: 50%; background: conic-gradient(from 0deg, var(--a1), var(--a3), var(--a2), var(--a1)); box-shadow: 0 0 22px var(--a1), 0 0 50px var(--a3); animation: pulse 2.2s ease-in-out infinite, spin 6s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
@keyframes pulse { 0%,100% { filter: brightness(.9); scale: .88; } 50% { filter: brightness(1.3); scale: 1.12; } }
.hero h1 { font-family: 'Sora', sans-serif; font-weight: 800; font-size: 2.1rem; letter-spacing: 0.04em; margin: 0; padding: 0; line-height: 1.1; background: linear-gradient(90deg, var(--text), var(--a1), var(--a3), var(--text)); background-size: 250% 100%; -webkit-background-clip: text; background-clip: text; color: transparent; animation: shimmer 7s linear infinite; }
@keyframes shimmer { to { background-position: 250% 0; } }
.hero p { margin: 6px 0 0 0; color: var(--muted); font-size: 0.86rem; letter-spacing: 0.03em; }
.hero .status { margin-left: auto; }
.pill { display: inline-flex; align-items: center; gap: 8px; padding: 6px 14px; border-radius: 999px; font-size: 0.72rem; font-weight: 600; letter-spacing: 0.1em; background: var(--glass); border: 1px solid var(--border); color: var(--text); white-space: nowrap; }
.dot { width: 8px; height: 8px; border-radius: 50%; animation: blink 1.6s infinite; }
.dot.on { background: #22ff9c; box-shadow: 0 0 10px #22ff9c; }
.dot.off { background: #ff4d6d; box-shadow: 0 0 10px #ff4d6d; }
@keyframes blink { 50% { opacity: .35; } }
div[data-testid="stChatMessage"] { background: var(--glass); backdrop-filter: blur(16px) saturate(160%); -webkit-backdrop-filter: blur(16px) saturate(160%); border: 1px solid var(--border); border-radius: 20px; padding: 14px 18px; margin: 0 6% 14px 0; box-shadow: 0 6px 26px var(--shadow), inset 0 1px 0 var(--hi); animation: slideIn .5s cubic-bezier(.2,.8,.2,1); transition: transform .25s, box-shadow .25s; }
div[data-testid="stChatMessage"]:hover { transform: translateY(-2px); box-shadow: 0 12px 34px var(--shadow), 0 0 0 1px var(--a1) inset; }
div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]), div[data-testid="stChatMessage"]:has(img[alt="user avatar"]) { background: linear-gradient(135deg, var(--user1), var(--user2)); margin: 0 0 14px 14%; }
div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]), div[data-testid="stChatMessage"]:has(img[alt="assistant avatar"]) { border-left: 3px solid var(--a1); }
@keyframes slideIn { from { opacity: 0; transform: translateY(16px) scale(.98); } to { opacity: 1; transform: none; } }
div[data-testid="stChatMessage"] p, div[data-testid="stChatMessage"] li { color: var(--text); line-height: 1.7; }
div[data-testid="stChatMessage"] code { background: var(--codebg); color: var(--a1); border-radius: 6px; padding: 2px 6px; }
div[data-testid="stChatMessage"] pre { background: var(--codebg) !important; border: 1px solid var(--border); border-radius: 14px; }
div[data-testid="stBottom"] > div, div[data-testid="stBottomBlockContainer"] { background: transparent !important; }
div[data-testid="stChatInput"] { position: relative; background: var(--input) !important; backdrop-filter: blur(22px) saturate(170%); -webkit-backdrop-filter: blur(22px) saturate(170%); border: 1px solid var(--border) !important; border-radius: 999px !important; box-shadow: 0 0 26px color-mix(in srgb, var(--a1) 22%, transparent), inset 0 1px 0 var(--hi); transition: box-shadow .3s, border-color .3s; }
div[data-testid="stChatInput"]:focus-within { border-color: var(--a1) !important; box-shadow: 0 0 38px color-mix(in srgb, var(--a1) 45%, transparent); }
div[data-testid="stChatInput"] textarea { color: var(--text) !important; background: transparent !important; padding-right: 96px !important; }
div[data-testid="stChatInput"] textarea::placeholder { color: var(--muted) !important; }
.mic-btn { position: absolute; right: 58px; top: 50%; transform: translateY(-50%); width: 34px; height: 34px; border-radius: 50%; border: 1px solid var(--border); background: var(--glass2); cursor: pointer; font-size: 16px; line-height: 1; z-index: 5; transition: all .25s; }
.mic-btn:hover { border-color: var(--a1); box-shadow: 0 0 16px var(--a1); }
.mic-btn.live { background: rgba(255,77,109,.28); border-color: #ff4d6d; animation: micpulse 1.1s infinite; }
@keyframes micpulse { 0% { box-shadow: 0 0 0 0 rgba(255,77,109,.6); } 100% { box-shadow: 0 0 0 16px rgba(255,77,109,0); } }
.stButton > button, .stDownloadButton > button { background: var(--glass) !important; color: var(--text) !important; border: 1px solid var(--border) !important; border-radius: 16px !important; backdrop-filter: blur(14px); transition: all .25s ease; font-weight: 500; }
.stButton > button:hover, .stDownloadButton > button:hover { transform: translateY(-3px); border-color: var(--a1) !important; box-shadow: 0 8px 26px color-mix(in srgb, var(--a1) 35%, transparent); }
.stButton > button:disabled, .stDownloadButton > button:disabled { opacity: .45; }
.chip { display: inline-block; margin: 10px 6px 0 0; padding: 4px 12px; font-size: .7rem; font-weight: 600; letter-spacing: .08em; text-transform: uppercase; color: var(--a1); background: color-mix(in srgb, var(--a1) 10%, transparent); border: 1px solid color-mix(in srgb, var(--a1) 40%, transparent); border-radius: 999px; }
.chip.lat { color: var(--muted); background: var(--glass); border-color: var(--border); }
.think { display: flex; flex-direction: column; gap: 14px; }
.think-row { display: flex; align-items: center; gap: 12px; color: var(--a1); font-size: .85rem; font-weight: 600; letter-spacing: .1em; }
.bars { display: flex; gap: 4px; align-items: flex-end; height: 22px; }
.bars span { width: 4px; background: linear-gradient(var(--a1), var(--a3)); border-radius: 2px; animation: eq 1s ease-in-out infinite; }
.bars span:nth-child(2) { animation-delay: .12s; }
.bars span:nth-child(3) { animation-delay: .24s; }
.bars span:nth-child(4) { animation-delay: .36s; }
.bars span:nth-child(5) { animation-delay: .48s; }
@keyframes eq { 0%,100% { height: 5px; } 50% { height: 22px; } }
.pipe { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
.node { padding: 5px 12px; border-radius: 10px; font-size: .72rem; font-weight: 600; letter-spacing: .06em; color: var(--muted); border: 1px solid var(--border); background: var(--glass); animation: node 4s infinite; }
.node.n2 { animation-delay: 1s; }
.node.n3 { animation-delay: 2s; }
.node.n4 { animation-delay: 3s; }
.arrow { width: 22px; height: 2px; background: linear-gradient(90deg, var(--a1), var(--a3)); opacity: .6; border-radius: 2px; }
@keyframes node { 0%,24% { color: var(--bg1); background: var(--a1); border-color: var(--a1); box-shadow: 0 0 18px var(--a1); } 30%,100% { color: var(--muted); background: var(--glass); border-color: var(--border); box-shadow: none; } }
.welcome { padding: 38px 30px; text-align: center; margin-bottom: 18px; }
.welcome h3 { font-family: 'Sora', sans-serif; font-weight: 700; font-size: 1.6rem; margin: 0 0 8px 0; color: var(--text); }
.welcome p { color: var(--muted); margin: 0; }
.sb-title { font-family: 'Sora', sans-serif; font-size: .72rem; font-weight: 700; letter-spacing: .22em; color: var(--a1); margin: 16px 0 8px 0; }
.sb-card { padding: 12px 16px; margin-bottom: 10px; font-size: .85rem; color: var(--text); line-height: 1.9; }
.sb-card code { color: var(--a1) !important; background: var(--codebg) !important; font-size: .74rem; word-break: break-all; }
.stat { display: flex; justify-content: space-between; padding: 3px 0; line-height: 1.6; }
.stat b { color: var(--a1); font-family: 'Sora', sans-serif; }
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-thumb { background: color-mix(in srgb, var(--a1) 40%, transparent); border-radius: 8px; }
"""

st.markdown(f'<style>{ROOT_VARS}{BASE_CSS}</style>', unsafe_allow_html=True)
st.markdown(
    '<div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div>',
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# JS: cursor spotlight + voice input (injected into the parent page)
# ----------------------------------------------------------------------------
JS = """
<script>
(function () {
  const P = window.parent, D = P.document;
  const token = String(Math.random());
  if (P.__agMove) D.removeEventListener('mousemove', P.__agMove);
  P.__agMove = function (e) {
    D.documentElement.style.setProperty('--mx', e.clientX + 'px');
    D.documentElement.style.setProperty('--my', e.clientY + 'px');
  };
  D.addEventListener('mousemove', P.__agMove);

  const SR = P.SpeechRecognition || P.webkitSpeechRecognition;
  let rec = null, listening = false, finalText = '';

  function setVal(el, v) {
    const setter = Object.getOwnPropertyDescriptor(P.HTMLTextAreaElement.prototype, 'value').set;
    setter.call(el, v);
    el.dispatchEvent(new P.Event('input', { bubbles: true }));
  }
  function submit() {
    const b = D.querySelector('button[data-testid="stChatInputSubmitButton"]');
    if (b) b.click();
  }
  function toggle() {
    const btn = D.querySelector('.mic-btn');
    const ta = D.querySelector('div[data-testid="stChatInput"] textarea');
    if (!SR) { alert('Voice input is not supported in this browser. Please use Chrome or Edge.'); return; }
    if (listening && rec) { rec.stop(); return; }
    finalText = '';
    rec = new SR();
    rec.lang = 'en-IN';
    rec.interimResults = true;
    rec.continuous = false;
    rec.onstart = function () { listening = true; if (btn) btn.classList.add('live'); };
    rec.onresult = function (e) {
      let t = '';
      for (let i = 0; i < e.results.length; i++) t += e.results[i][0].transcript;
      if (ta) setVal(ta, t);
      if (e.results[e.results.length - 1].isFinal) finalText = t;
    };
    rec.onerror = function () { listening = false; if (btn) btn.classList.remove('live'); };
    rec.onend = function () {
      listening = false;
      if (btn) btn.classList.remove('live');
      if (finalText.trim()) setTimeout(submit, 350);
    };
    rec.start();
  }
  function ensureMic() {
    const box = D.querySelector('div[data-testid="stChatInput"]');
    if (!box) return;
    const old = box.querySelector('.mic-btn');
    if (old && old.dataset.owner === token) return;
    if (old) old.remove();
    const b = D.createElement('button');
    b.type = 'button';
    b.className = 'mic-btn';
    b.title = 'Voice input';
    b.dataset.owner = token;
    b.textContent = '🎙️';
    b.addEventListener('click', toggle);
    box.appendChild(b);
  }
  ensureMic();
  setInterval(ensureMic, 800);
})();
</script>
"""
components.html(JS, height=0)


# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
@st.cache_data(ttl=15, show_spinner=False)
def backend_online(url: str) -> bool:
    """Any HTTP response below 500 means the backend is reachable."""
    try:
        return requests.get(f'{url}/health', timeout=2).status_code < 500
    except requests.RequestException:
        return False


def html(block: str) -> None:
    """Render raw HTML (dedented so Markdown doesn't treat it as a code block)."""
    st.markdown(textwrap.dedent(block).strip(), unsafe_allow_html=True)


def tool_icon(name: str) -> str:
    n = name.lower()
    if 'calc' in n:
        return '🧮'
    if 'time' in n:
        return '🕒'
    if 'weather' in n:
        return '🌦️'
    return '⚙️'


def meta_html(tool_calls, latency) -> str:
    chips = ''.join(
        f'<span class="chip">{tool_icon(t)} {escape(str(t))}</span>' for t in (tool_calls or [])
    )
    if latency:
        chips += f'<span class="chip lat">⏱ {latency:.1f}s</span>'
    return f'<div>{chips}</div>' if chips else ''


def render_message(msg: dict) -> None:
    avatar = '🧑‍💻' if msg['role'] == 'user' else '✨'
    with st.chat_message(msg['role'], avatar=avatar):
        st.markdown(msg['content'])
        meta = meta_html(msg.get('tool_calls'), msg.get('latency'))
        if meta:
            html(meta)


def stream_text(placeholder, text: str) -> None:
    """Typewriter-style streaming (the backend returns the full answer at once)."""
    tokens = re.findall(r'\S+\s*', text)
    step = max(1, len(tokens) // 120)
    buf = ''
    for i in range(0, len(tokens), step):
        buf += ''.join(tokens[i:i + step])
        placeholder.markdown(buf + ' ▌')
        time.sleep(0.02)
    placeholder.markdown(text)


THINKING_HTML = (
    '<div class="think"><div class="think-row"><div class="bars">'
    '<span></span><span></span><span></span><span></span><span></span></div>'
    'AGENT IS THINKING...</div>'
    '<div class="pipe"><span class="node n1">Understand</span><span class="arrow"></span>'
    '<span class="node n2">Plan</span><span class="arrow"></span>'
    '<span class="node n3">Use tools</span><span class="arrow"></span>'
    '<span class="node n4">Respond</span></div></div>'
)

online = backend_online(BACKEND_URL)

# ----------------------------------------------------------------------------
# SIDEBAR
# ----------------------------------------------------------------------------
with st.sidebar:
    html('<div class="sb-title">◈ BACKEND LINK</div>')
    html(f'<div class="glass sb-card"><code>{escape(BACKEND_URL)}</code></div>')

    html('<div class="sb-title">◈ ACTIVE MODULES</div>')
    html(
        """
        <div class="glass sb-card">
        🧮 Calculator<br>🕒 Current Time<br>🌦️ Weather
        </div>
        """
    )

    msgs = st.session_state.messages
    total_tools = sum(len(m.get('tool_calls') or []) for m in msgs)
    lats = [m['latency'] for m in msgs if m.get('latency')]
    avg_lat = f'{sum(lats) / len(lats):.1f}s' if lats else '–'
    html('<div class="sb-title">◈ SESSION TELEMETRY</div>')
    html(
        f"""
        <div class="glass sb-card">
        <div class="stat"><span>Messages</span><b>{len(msgs)}</b></div>
        <div class="stat"><span>Tool calls</span><b>{total_tools}</b></div>
        <div class="stat"><span>Avg latency</span><b>{avg_lat}</b></div>
        </div>
        """
    )

    html('<div class="sb-title">◈ PREFERENCES</div>')
    st.toggle('☀️ Light mode', key='light_mode')
    st.toggle('⚡ Stream responses', value=True, key='stream_on')

    html('<div class="sb-title">◈ ACTIONS</div>')
    export_md = '\n\n'.join(
        f"**{'You' if m['role'] == 'user' else 'Agentic AI'}:** {m['content']}" for m in msgs
    )
    st.download_button(
        '⬇  Export chat',
        data=export_md or ' ',
        file_name='agentic-ai-chat.md',
        mime='text/markdown',
        use_container_width=True,
        disabled=not msgs,
    )
    if st.button('🗑  Clear chat', use_container_width=True):
        st.session_state.messages = []
        st.session_state.pending = None
        st.rerun()

# ----------------------------------------------------------------------------
# HERO HEADER
# ----------------------------------------------------------------------------
status_dot = 'on' if online else 'off'
status_txt = 'SYSTEMS ONLINE' if online else 'BACKEND OFFLINE'
html(
    f"""
    <div class="glass hero">
      <div class="core">
        <div class="ring r1"></div><div class="ring r2"></div><div class="ring r3"></div>
        <div class="nucleus"></div>
      </div>
      <div>
        <h1>Agentic AI</h1>
        <p>Autonomous reasoning · Tool use · Real-time answers</p>
      </div>
      <div class="status"><span class="pill"><span class="dot {status_dot}"></span>{status_txt}</span></div>
    </div>
    """
)

# ----------------------------------------------------------------------------
# WELCOME + SUGGESTIONS (only when chat is empty)
# ----------------------------------------------------------------------------
if not st.session_state.messages:
    html(
        """
        <div class="glass welcome">
          <h3>How can I help you today?</h3>
          <p>I can calculate, tell the time and check live weather. Pick a command, type, or tap the mic.</p>
        </div>
        """
    )
    suggestions = [
        ('🧮  Solve a calculation', 'What is (1234 * 56) / 7?'),
        ('🕒  What time is it?', 'What is the current time?'),
        ('🌦️  Weather in Indore', 'What is the weather in Indore right now?'),
        ('🔗  Combine tools', 'What is the weather in Delhi and what is the time now?'),
    ]
    row1 = st.columns(2)
    row2 = st.columns(2)
    for col, (label, text) in zip(row1 + row2, suggestions):
        if col.button(label, use_container_width=True, key=f'sg_{label}'):
            st.session_state.pending = text
            st.rerun()

# ----------------------------------------------------------------------------
# CHAT HISTORY
# ----------------------------------------------------------------------------
for message in st.session_state.messages:
    render_message(message)

# ----------------------------------------------------------------------------
# INPUT + BACKEND CALL
# ----------------------------------------------------------------------------
typed = st.chat_input('Message Agentic AI ...')
prompt = typed or st.session_state.pending
st.session_state.pending = None

if prompt:
    render_message({'role': 'user', 'content': prompt})

    # Backend only needs role + content (same contract as your original code)
    history = [
        {'role': m['role'], 'content': m['content']}
        for m in st.session_state.messages
    ]
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    with st.chat_message('assistant', avatar='✨'):
        placeholder = st.empty()
        placeholder.markdown(THINKING_HTML, unsafe_allow_html=True)
        started = time.perf_counter()
        try:
            response = requests.post(
                f'{BACKEND_URL}/chat',
                json={'message': prompt, 'history': history},
                timeout=120,
            )
            response.raise_for_status()
            data = response.json()
            answer = data['answer']
            tool_calls = data.get('tool_calls', [])
            latency = time.perf_counter() - started

            if st.session_state.get('stream_on', True):
                stream_text(placeholder, answer)
            else:
                placeholder.markdown(answer)

            meta = meta_html(tool_calls, latency)
            if meta:
                html(meta)

            st.session_state.messages.append(
                {
                    'role': 'assistant',
                    'content': answer,
                    'tool_calls': tool_calls,
                    'latency': latency,
                }
            )
        except requests.RequestException as exc:
            placeholder.empty()
            st.error(f'Backend connection failed: {exc}')
        except Exception as exc:
            placeholder.empty()
            st.error(f'Unexpected error: {exc}')