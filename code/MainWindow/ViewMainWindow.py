import tkinter
import tkinter.ttk

from code.MainWindow import ConstantsMainWindow
from code.MainWindow.IViewMainWindow import IViewMainWindow
from constants import core
from constants import labels_en as labels


class ViewMainWindow(
	tkinter.Frame,
	IViewMainWindow):
	
	def __init__(
		self,
		_presenter):
		
		master = tkinter.Tk()
		
		super().__init__(master)
		
		# Init instance members used throughout the entire class with a default
		# value.
		self.master = None	
		
		# Menu
		self.tkinter_menu = None
		self.tkinter_menu_file = None
		
		# Frames
		self.tkinter_frame = None
		
		# Master
		self.master = master
		self.master.title(
			core.CHAR_SPACE.join((
				core.TEXT_TOOL_TITLE,
				core.TEXT_TOOL_VERSION)))	
		
		# Ablakok
		self.tk_frame_create()
		
		# Pack all controls.
		#self.grid(
		#	row = 0,
		#	column = 0)
		self.pack()
		
		self.presenter = _presenter
		self.presenter.set_view(self)
		
		# Let the presenter init this view.
		self.presenter.init_view()			
			
		self.bind_events()

	
	def tk_frame_create(self):
		self.tk_frame = tkinter.Frame(
			self)
		self.tk_frame.grid(
			row = 0,
			column = 0,
			sticky = "nsew")
			
		# Gyömbér
		self.tk_label_heading = tkinter.Label(
			self.tk_frame,
			text = core.TEXT_TOOL_TITLE,
			font = (
				core.FONT_DEFAULT,
				core.FONT_SIZE_HEADING))
		self.tk_label_heading.grid(
			row = 0,
			column = 0,
			columnspan = 9)
		
		# Subheading
		self.tk_label_subheading = tkinter.Label(
			self.tk_frame,
			text = core.TEXT_TOOL_DESCRIPTION,
			font = (
				core.FONT_DEFAULT,
				core.FONT_SIZE_SUBHEADING),
			fg = "grey")
		self.tk_label_subheading.grid(
			row = 1,
			column = 0,
			columnspan = 9,
			sticky = "n")
		
		# Show number of entries
		self.tk_label_number_of_entries = tkinter.Label(
			self.tk_frame)
		self.tk_label_number_of_entries.config(
			font = (
				core.FONT_DEFAULT,
				core.FONT_SIZE_DEFAULT))
		self.tk_label_number_of_entries.grid(
			row = 2,
			columnspan = 9,
			column = 0)
		
		# Show done entries.
		self.tk_label_current = tkinter.Label(
			self.tk_frame)
		self.tk_label_current.config(
			font = (
				core.FONT_DEFAULT,
				core.FONT_SIZE_DEFAULT))
		self.tk_label_current.grid(
			row = 3,
			columnspan = 9,
			column = 0)	
		
		# Word to guess
		self.tk_label_word_to_guess = tkinter.Label(
			self.tk_frame)
		self.tk_label_word_to_guess.config(
			font = (
				core.FONT_MONOSPACE,
				core.FONT_SIZE_GUESS),
			wraplength=core.WRAPLENGTH)
		self.tk_label_word_to_guess.grid(
			row = 4,
			column = 0,
			columnspan = 9)	
		
		
		# User input
		self.tk_entry_user_input = tkinter.Entry(
			self.tk_frame)
		self.tk_entry_user_input.config(
			font = (
				core.FONT_MONOSPACE,
				core.FONT_SIZE_GUESS),
			justify = core.STANDARD_JUSTIFY)
		self.tk_entry_user_input.grid(
			row = 5,
			column = 0,
			columnspan = 9,
			sticky="we")
		
		
		# Check
		self.tk_button_check = tkinter.Button(
			self.tk_frame,
			text = labels.CHECK)
		self.tk_button_check.grid(
			row = 6,
			column = 0,
			columnspan = 9,
			sticky="we")
			
					
		# Hint
		self.tk_label_hint = tkinter.Label(
			self.tk_frame)
		self.tk_label_hint.config(
			font = (
				core.FONT_MONOSPACE,
				core.FONT_SIZE_GUESS))
		self.tk_label_hint.grid(
			row = 7,
			column = 0,
			columnspan = 9,
			sticky = "we")				
	
		
		# Hint button
		self.tk_button_hint = tkinter.Button(
			self.tk_frame,
			text = labels.HINT)
		self.tk_button_hint.grid(
			row = 8,
			column = 0,
			columnspan = 9,
			sticky="we")
		
		
		# Buttons for hungarian only letters
		self.tk_button_1 = tkinter.Button(
			self.tk_frame,
			text = "Á")
		self.tk_button_1.config(
			font = (
				core.FONT_MONOSPACE,
				core.FONT_SIZE_LETTER_BUTTONS))
		self.tk_button_1.grid(
			row = 9,
			column = 0,
			sticky="we")
		
		self.tk_button_2 = tkinter.Button(
			self.tk_frame,
			text = "Í")
		self.tk_button_2.config(
			font = (
				core.FONT_MONOSPACE,
				core.FONT_SIZE_LETTER_BUTTONS))			
		self.tk_button_2.grid(
			row = 9,
			column = 1,
			sticky="we")

		self.tk_button_3 = tkinter.Button(
			self.tk_frame,
			text = "Ó")
		self.tk_button_3.config(
			font = (
				core.FONT_MONOSPACE,
				core.FONT_SIZE_LETTER_BUTTONS))			
		self.tk_button_3.grid(
			row = 9,
			column = 2,
			sticky="we")
		
		self.tk_button_4 = tkinter.Button(
			self.tk_frame,
			text = "Ú")
		self.tk_button_4.config(
			font = (
				core.FONT_MONOSPACE,
				core.FONT_SIZE_LETTER_BUTTONS))			
		self.tk_button_4.grid(
			row = 9,
			column = 3,
			sticky="we")
		
		self.tk_button_5 = tkinter.Button(
			self.tk_frame,
			text = "É")
		self.tk_button_5.config(
			font = (
				core.FONT_MONOSPACE,
				core.FONT_SIZE_LETTER_BUTTONS))			
		self.tk_button_5.grid(
			row = 9,
			column = 4,
			sticky="we")	
		
		self.tk_button_6 = tkinter.Button(
			self.tk_frame,
			text = "Ö")
		self.tk_button_6.config(
			font = (
				core.FONT_MONOSPACE,
				core.FONT_SIZE_LETTER_BUTTONS))			
		self.tk_button_6.grid(
			row = 9,
			column = 5,
			sticky="we")
		
		self.tk_button_7 = tkinter.Button(
			self.tk_frame,
			text = "Ü")
		self.tk_button_7.config(
			font = (
				core.FONT_MONOSPACE,
				core.FONT_SIZE_LETTER_BUTTONS))			
		self.tk_button_7.grid(
			row = 9,
			column = 6,
			sticky="we")
		
		self.tk_button_8 = tkinter.Button(
			self.tk_frame,
			text = "Ő")
		self.tk_button_8.config(
			font = (
				core.FONT_MONOSPACE,
				core.FONT_SIZE_LETTER_BUTTONS))			
		self.tk_button_8.grid(
			row = 9,
			column = 7,
			sticky="we")
		
		self.tk_button_9 = tkinter.Button(
			self.tk_frame,
			text = "Ű")
		self.tk_button_9.config(
			font = (
				core.FONT_MONOSPACE,
				core.FONT_SIZE_LETTER_BUTTONS))			
		self.tk_button_9.grid(
			row = 9,
			column = 8,
			sticky="we")
			
			
	def configure_columns(self):
	
		self.tk_frame.grid_columnconfigure(0, weight = 0)
		
		
	def configure_rows(self):	
		self.grid_rowconfigure(0, weight = 1)	
		self.grid_rowconfigure(1, weight = 2)

	
	def set_number_of_entries(
		self,
		_number_of_entries):
		
		self.tk_label_number_of_entries.config(
			text = labels.NUMBER_OF_ENTRIES % (_number_of_entries))
	
	
	def set_current(
		self,
		_current):
		
		self.tk_label_current.config(
			text = labels.ENTRIES_DONE % (_current))	
	
	
	def set_word_to_guess(
		self,
		_word_to_guess):
		
		self.tk_label_word_to_guess.config(
			text = _word_to_guess)
			
	
	def enable_hint_button(self):
	
		self.tk_button_hint.config(
			state = tkinter.NORMAL)
	
	
	def set_hint_blank(self):
	
		self.tk_label_hint.config(
			text = "")	
	
	
	def get_user_input(self):
	
		return self.tk_entry_user_input.get()
		
		
	def set_user_input(
		self,
		_user_input):
		
		self.tk_entry_user_input.config(
			text = _user_input)
	
	
	def set_hint(
		self,
		_hint):
		
		self.tk_label_hint.config(
			text = _hint)
	
	
	def disable_hint_button(self):
	
		self.tk_button_hint.config(
			state = tkinter.DISABLED)
		
		
	def tk_button_check_clicked(
		self,
		_event):
		
		self.presenter.check(_event)
	
	
	def tk_button_hint_clicked(
		self,
		_event = None):
	
		self.presenter.hint(_event)
	
	
	def tk_button_letter_clicked(
		self,
		_event):
		
		self.presenter.add_special_letter(_event)
		
		
	def entry_user_input_get_cursor_index(self):
	
		return self.tk_entry_user_input.index(tkinter.INSERT)
	
	
	def entry_user_input_set_cursor_index(
		self,
		_index):
		
		self.tk_entry_user_input.icursor(
			_index)
			
			
	def reset_user_input(self):
	
		self.tk_entry_user_input.delete(0, tkinter.END)
		self.tk_entry_user_input.insert(0, "")			
	
	
	def run(self):
	
		self.mainloop()
	
	
	def bind_events(self):
	
		self.tk_button_check.bind(
			"<Button-1>",
			self.tk_button_check_clicked)
			
		self.tk_button_hint.bind(
			"<Button-1>",
			self.tk_button_hint_clicked)
			
		self.tk_entry_user_input.bind(
			"<Return>",
			self.tk_button_check_clicked)
			
		self.tk_button_1.bind(
			"<Button-1>",
			self.tk_button_letter_clicked)
			
		self.tk_button_2.bind(
			"<Button-1>",
			self.tk_button_letter_clicked)

		self.tk_button_3.bind(
			"<Button-1>",
			self.tk_button_letter_clicked)
			
		self.tk_button_4.bind(
			"<Button-1>",
			self.tk_button_letter_clicked)	
			
		self.tk_button_5.bind(
			"<Button-1>",
			self.tk_button_letter_clicked)
			
		self.tk_button_6.bind(
			"<Button-1>",
			self.tk_button_letter_clicked)	

		self.tk_button_7.bind(
			"<Button-1>",
			self.tk_button_letter_clicked)
			
		self.tk_button_8.bind(
			"<Button-1>",
			self.tk_button_letter_clicked)	
			
		self.tk_button_9.bind(
			"<Button-1>",
			self.tk_button_letter_clicked)
	