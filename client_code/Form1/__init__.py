from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.media
import time

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    app_tables.table_1.add_row(naam=file.name)
    anvil.server.call("edit_pdf", file, file.name)
    # would like to create the below get() based on row id
    row = app_tables.table_1.get(naam=file.name)
    anvil.media.download(row['media_obj'])

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
