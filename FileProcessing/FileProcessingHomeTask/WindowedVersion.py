from os.path import exists, abspath
import subprocess as sp
from sys import exc_info
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import Program

__author__ = 'Maksym Kuzma C4a'


def open_file(path_to_file):
    """
    Opens file in Windows notepad
    """
    if exists(path_to_file):
        sp.Popen(['notepad', path_to_file])
    else:
        raise FileNotFoundError('File does not exist')


def choose_file(path_data):
    """
    Lets user choose path to file and puts it into label text
    :param path_data: tkinter Label object
    """
    path = filedialog.askopenfile(initialdir="./")
    if path is not None:
        filepath = path.name
        path_data.configure(text=filepath)


def callback_error(self, *args):
    """
    Exception handling method for tkinter
    """
    tk.messagebox.showerror('Error',
                            'Error occurred. Error log saved to ' + abspath(Program.current_config['Error path']))
    Program.log_error(*args)
    exit()


class MainWindow:
    def __init__(self, master=None):
        tk.Tk.report_callback_exception = callback_error
        self.Main_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.entry_add = tk.Button(self.Main_window)
        self.entry_add.configure(font='{Arial} 16 {bold}', foreground='#690f96', text='Add entry\nto data.dat',
                                 command=lambda: AddWindow().run())
        self.entry_add.place(anchor='nw', height='100', relheight='0.0', relwidth='0.0', relx='0.03', rely='0.07',
                             width='150', x='0', y='0')
        self.export_data = tk.Button(self.Main_window)
        self.export_data.configure(font='{Arial} 16 {bold}', foreground='#690f96', text='Crash app', command=lambda: 1/0)
        self.export_data.place(anchor='nw', height='100', relheight='0.0', relwidth='0.0', relx='0.03', rely='0.57',
                               width='150', x='0', y='0')
        self.setup_json = tk.Button(self.Main_window)
        self.setup_json.configure(font='{Arial} 16 {bold}', foreground='#690f96', text='Edit config',
                                  command=lambda: ConfigWindow().run())
        self.setup_json.place(anchor='nw', height='100', relheight='0.0', relwidth='0.0', relx='0.28', rely='0.07',
                              width='150', x='0', y='0')
        self.export_csv = tk.Button(self.Main_window)
        self.export_csv.configure(font='{Arial} 16 {bold}', foreground='#690f96', text='Export csv',
                                  command=lambda: [Program.export_data_to_csv(), messagebox.showinfo('', 'Done')])
        self.export_csv.place(anchor='ne', height='100', relheight='0.0', relwidth='0.0', relx='0.72', rely='0.07',
                              width='150', x='0', y='0')
        self.open_err_log = tk.Button(self.Main_window)
        self.open_err_log.configure(font='{Arial} 16 {bold}', foreground='#690f96', text='Open error log',
                                    command=lambda: open_file(Program.current_config['Error path']))
        self.open_err_log.place(anchor='ne', height='100', relheight='0.0', relwidth='0.0', relx='0.97', rely='0.07',
                                width='150', x='0', y='0')
        self.open_json = tk.Button(self.Main_window)
        self.open_json.configure(font='{Arial} 16 {bold}', foreground='#690f96', text='Open json file',
                                 command=lambda: open_file(Program.config_path))
        self.open_json.place(anchor='nw', height='100', relheight='0.0', relwidth='0.0', relx='0.28', rely='0.57',
                             width='150', x='0', y='0')
        self.open_csv = tk.Button(self.Main_window)
        self.open_csv.configure(font='{Arial} 16 {bold}', foreground='#690f96', text='Open csv file',
                                command=lambda: open_file(Program.current_config['Export path']))
        self.open_csv.place(anchor='ne', height='100', relheight='0.0', relwidth='0.0', relx='0.72', rely='0.57',
                            width='150', x='0', y='0')
        self.exit = tk.Button(self.Main_window)
        self.exit.configure(font='{Arial} 16 {bold}', foreground='#690f96', text='Exit',
                            command=self.Main_window.destroy)
        self.exit.place(anchor='ne', height='100', relheight='0.0', relwidth='0.0', relx='0.97', rely='0.57',
                        width='150', x='0', y='0')
        self.Main_window.configure(background='#690f96', height='300', width='800')
        self.Main_window.resizable(False, False)
        self.Main_window.title('HomeTask')

        self.main_window = self.Main_window

    def run(self):
        """
        Runs main window
        """
        try:
            Program.load_config()
            self.main_window.mainloop()
        except Exception as e:
            tk.messagebox.showerror('Error', 'Error occurred. Error log saved to ' + abspath(
                Program.current_config['Error path']))
            exc_type, exc_name, ext_tb = exc_info()
            Program.log_error(exc_type, exc_name, ext_tb)


class AddWindow:
    def __init__(self, master=None):
        # build ui
        self.Add_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.name = tk.Entry(self.Add_window)
        self.name.configure(font='{Arial} 12 {bold}', foreground='#690f96', justify='center')
        _text_ = '''Enter name'''
        self.name.delete('0', 'end')
        self.name.insert('0', _text_)
        self.name.pack(ipadx='100', ipady='15', pady='30', side='top')
        self.lastname = tk.Entry(self.Add_window)
        self.lastname.configure(font='{Arial} 12 {bold}', foreground='#690f96', justify='center')
        _text_ = '''Enter lastname'''
        self.lastname.delete('0', 'end')
        self.lastname.insert('0', _text_)
        self.lastname.pack(anchor='n', expand='false', ipadx='100', ipady='15', pady='15', side='top')
        self.job = tk.Entry(self.Add_window)
        self.job.configure(font='{Arial} 12 {bold}', foreground='#690f96', justify='center')
        _text_ = '''Enter job'''
        self.job.delete('0', 'end')
        self.job.insert('0', _text_)
        self.job.pack(ipadx='100', ipady='15', pady='30', side='top')
        self.phone_number = tk.Entry(self.Add_window)
        self.phone_number.configure(font='{Arial} 12 {bold}', foreground='#690f96', justify='center')
        _text_ = '''Enter phone number'''
        self.phone_number.delete('0', 'end')
        self.phone_number.insert('0', _text_)
        self.phone_number.pack(ipadx='100', ipady='15', pady='15', side='top')
        self.add = tk.Button(self.Add_window)
        self.add.configure(font='{Arial} 16 {bold}', foreground='#690f96', text='Add')
        self.add.configure(command=lambda: {
            Program.export_person(*self.validate_inputs()),
            self.Add_window.destroy(), messagebox.showinfo('', 'Successfully added')})
        self.add.place(anchor='nw', height='80', relx='0.26', rely='0.7', width='175', x='0', y='0')
        self.cancel = tk.Button(self.Add_window)
        self.cancel.configure(font='{Arial Baltic} 16 {bold}', foreground='#690f96', text='Cancel',
                              command=self.Add_window.destroy)
        self.cancel.place(anchor='nw', height='80', relx='0.52', rely='0.7', width='175', x='0', y='0')
        self.Add_window.configure(background='#690f96', height='200', width='200')
        self.Add_window.geometry('800x600')
        self.Add_window.resizable(False, False)
        self.Add_window.title('Add entry')

        # Main widget
        self.add_window = self.Add_window

    def validate_inputs(self) -> list:
        """
        Validates user inputs from add entry window
        :return: user inputs as list
        """
        name = self.name.get()
        lastname = self.lastname.get()
        job = self.job.get()
        phone_number = self.phone_number.get()
        assert len(name) > 0, 'Incorrect name value'
        assert len(lastname) > 0, 'Incorrect lastname value'
        assert len(job) > 0, 'Incorrect job value'
        assert 0 < len(phone_number) < 13, 'Incorrect phone number value'
        return [name, lastname, job, phone_number]

    def run(self):
        """
        Runs add entry window
        """
        self.add_window.mainloop()


class ConfigWindow:
    def __init__(self, master=None):
        # build ui
        self.Config_window = tk.Tk() if master is None else tk.Toplevel(master)
        __values_lang = ['English', 'Czech']
        __values_enc = ['utf-8', 'utf-16', 'ascii']
        self.__tkvar_lang = tk.StringVar(self.Config_window)
        self.__tkvar_enc = tk.StringVar(self.Config_window)
        self.__tkvar_lang.set(Program.current_config['Language'])
        self.__tkvar_enc.set(Program.current_config['Encoding'])
        self.save_config = tk.Button(self.Config_window)
        self.save_config.configure(font='{Arial} 16 {bold}', foreground='#690f96', text='Save')
        self.save_config.configure(command=lambda: {
            Program.save_changes_to_config(self.__tkvar_lang.get(), self.__tkvar_enc.get(), self.path_data.cget("text"),
                                           self.path_export.cget("text"), self.path_error.cget("text")),
            self.Config_window.destroy(), messagebox.showinfo('', 'Saved')})
        self.save_config.place(anchor='nw', height='80', relx='0.25', rely='0.74', width='175', x='0', y='0')
        self.cancel = tk.Button(self.Config_window)
        self.cancel.configure(font='{Arial Baltic} 16 {bold}', foreground='#690f96', text='Cancel',
                              command=self.Config_window.destroy)
        self.cancel.place(anchor='nw', height='80', relx='0.53', rely='0.74', width='175', x='0', y='0')
        self.language = tk.OptionMenu(self.Config_window, self.__tkvar_lang, *__values_lang, command=None)
        self.language.pack(ipadx='150', ipady='15', pady='30', side='top')
        self.encoding = tk.OptionMenu(self.Config_window, self.__tkvar_enc, *__values_enc, command=None)
        self.encoding.pack(ipadx='150', ipady='15', pady='15', side='top')
        self.path_data = tk.Label(self.Config_window)
        self.path_data.configure(font='{Arial} 9 {bold}', foreground='#690f96',
                                 text=Program.current_config['Data path'])
        self.path_data.place(anchor='nw', height='50', relx='0.25', rely='0.39', width='290', x='0', y='0')
        self.data_path = tk.Button(self.Config_window)
        self.data_path.configure(font='{Arial} 12 {bold}', foreground='#690f96', text='Browse',
                                 command=lambda: choose_file(self.path_data))
        self.data_path.place(anchor='nw', height='50', relx='0.625', rely='0.39', width='100', x='0', y='0')
        self.path_export = tk.Label(self.Config_window)
        self.path_export.configure(font='{Arial} 9 {bold}', foreground='#690f96',
                                   text=Program.current_config['Export path'])
        self.path_export.place(anchor='nw', height='50', relx='0.25', rely='0.5', width='290', x='0', y='0')
        self.browse_csv = tk.Button(self.Config_window)
        self.browse_csv.configure(font='{Arial} 12 {bold}', foreground='#690f96', text='Browse',
                                  command=lambda: choose_file(self.path_export))
        self.browse_csv.place(anchor='nw', height='50', relx='0.625', rely='0.5', width='100', x='0', y='0')
        self.path_error = tk.Label(self.Config_window)
        self.path_error.configure(font='{Arial} 9 {bold}', foreground='#690f96',
                                  text=Program.current_config['Error path'])
        self.path_error.place(anchor='nw', height='50', relx='0.25', rely='0.61', width='290', x='0', y='0')
        self.browse_error = tk.Button(self.Config_window)
        self.browse_error.configure(font='{Arial} 12 {bold}', foreground='#690f96', text='Browse',
                                    command=lambda: choose_file(self.path_error))
        self.browse_error.place(anchor='nw', height='50', relx='0.625', rely='0.61', width='100', x='0', y='0')
        self.Config_window.configure(background='#690f96', height='200', width='200')
        self.Config_window.geometry('800x600')
        self.Config_window.resizable(False, False)
        self.Config_window.title('Config')

        # Main widget
        self.config_window = self.Config_window

    def run(self):
        """
        Runs config json window
        """
        self.config_window.mainloop()


if __name__ == "__main__":
    obj = MainWindow()
    obj.run()
