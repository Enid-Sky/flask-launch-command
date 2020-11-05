"""Server for launch command app"""

from jinja2 import StrictUndefined
import crud
from model import connect_to_db
from flask import (Flask, render_template, request, flash, session,
                   redirect)
