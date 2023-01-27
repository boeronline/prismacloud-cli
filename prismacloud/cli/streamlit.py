import streamlit as st


import logging
import os
import sys
import warnings
import re
import textwrap
import json
import ast


import click
import click_completion
import coloredlogs
import pandas as pd
from click_help_colors import HelpColorsMultiCommand
from pydantic import BaseSettings
from tabulate import tabulate
from update_checker import UpdateChecker

import prismacloud.cli.version as cli_version
from prismacloud.cli import cli_output, pass_environment
from prismacloud.cli.api import pc_api

from __init__ import *


def intro():
    import streamlit as st

    st.write("# Welcome to Streamlit! 👋")
    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.

        **👈 Select a demo from the dropdown on the left** to see some examples
        of what Streamlit can do!

        ### Want to learn more?

        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)

        ### See more complex demos

        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


def defenders_demo():
    import streamlit as st
    import pandas as pd

    result = pc_api.get_endpoint("defenders/summary")
    df = pd.json_normalize(result)
    st.write(df)

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.json(result)


def registry():
    import streamlit as st
    import pandas as pd

    result = pc_api.get_endpoint("registry")
    df = pd.json_normalize(result)
    st.write(df)

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.json(result)


page_names_to_funcs = {
    "—": intro,
    "Defenders": defenders_demo,
    "Registry": registry
}


demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
