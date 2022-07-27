import streamlit as st
import time

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

st.write('''
# The Timer Application

Let's do some focus work. The default timer is 25 mins with a follow 5 mins break!

''')
mod_timer = int(st.sidebar.number_input('Enter desired timer'))*60
mod_break = int(st.sidebar.number_input('Enter desired break'))*60
sidebar_button_clicked = st.sidebar.button('Start the cumtom')
button_clicked = st.button("Start")

t1 = 1500
t2 = 300

if button_clicked:
    with st.empty():
        while t1:
            mins, secs = divmod(t1, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"⏳ {timer}")
            time.sleep(1)
            t1 -= 1
            st.success("🔔 25 minutes is over! Time for a break!")

    with st.empty():
        while t2:
            # Start the break
            mins2, secs2 = divmod(t2, 60)
            timer2 = '{:02d}:{:02d}'.format(mins2, secs2)
            st.header(f"⏳ {timer2}")
            time.sleep(1)
            t2 -= 1
            st.error("⏰ 5 minute break is over!")

if sidebar_button_clicked:
    with st.empty():
        while mod_timer:
            selected_mod_timer = mod_timer
            mins, secs = divmod(mod_timer, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"⏳ {timer}")
            time.sleep(1)
            mod_timer -= 1
            st.balloons()
            st.success("🔔 " + str(selected_mod_timer) + " minute(s) dedicated work is over! Time for a break!")

    with st.empty():
        while mod_break:
            # Start the break
            selected_mod_break = mod_break
            mins2, secs2 = divmod(mod_break, 60)
            timer2 = '{:02d}:{:02d}'.format(mins2, secs2)
            st.header(f"⏳ {timer2}")
            time.sleep(1)
            mod_break -= 1
            st.snow()
            st.error("⏰ " + str(selected_mod_break) + " minute(s) break is over!")
