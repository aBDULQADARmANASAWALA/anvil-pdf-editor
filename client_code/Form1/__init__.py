from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import pymupdf


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    doc = pymupdf.open(file)
    for pg_no in range(len(doc)):
      doc[pg_no].insert_image(pymupdf.Rect(353, 87, 560, 106), filename = "_/theme/Picture1.png")
    # doc.save("edited_file.pdf")

