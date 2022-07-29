# CSV Cleaner: GUI Pipeline
![titlecard](./img/card.png)

## Contributors:

- [Dylan Peterson](https://github.com/DyPeterson)

##  Description:

A simple GUI application that allows the user to run common cleaning operations for their data. Demonstrating a pipeline.

###  Technologies Used:

- [Visual Code Studio](https://code.visualstudio.com/)

- [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-us&gl=US) ( Running: [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install) ([ubuntu 20.04](https://releases.ubuntu.com/20.04/)))

- [tkinter](https://docs.python.org/3/library/tkinter.html)

- [ttkbootstrap](https://ttkbootstrap.readthedocs.io/en/latest/)

- [Pandas](https://pandas.pydata.org/) 


###  Programs used:

- [VcXsrv Windows X Server](https://sourceforge.net/projects/vcxsrv/)

##  Setup & Installation:

### Installation:

1. Through the terminal like [GitBash](https://git-scm.com/downloads)

	2. Open the terminal and navigate to where you would like the new project to be using `cd` commands. Its also recommended that you make a new directory using `mkdir *directory-name*`.

	3. Clone the repository using the command `git clone https://github.com/DyPeterson/dsa-capstone.git`

	4. After cloning the directory it will appear in the directory that your terminal is set to. So make sure you are in the directory that you want this project copied to.

	5. Once this project is cloned you can navigate to that folder within your terminal and create a virtual environment `python3.7 -m venv *any-name*`. Now activate the venv with `source *any-name*/bin/activate`

	6. Install requirements in venv `pip install -r requirements.txt`

2. Through GitHub.com

	3. Go to the project's directory page **[HERE](https://github.com/DyPeterson/dsa-capstone)**

	4. Click the green `code` button to open the drop-down menu.

	5. At the bottom of the menu will have *Download Zip*. Go ahead and click it to download the project.

	6. Once downloaded find the `.zip` file and right-click it to bring up the menu. Within that menu click `Extract Here` to extract it in the current folder or click `Extract Files...`to select which folder you would like the project in.
	
	7. Follow steps 5-6 above. 

### Set-up:

Once the project is installed run the program through the terminal with the command `python3 app.py`

Once the program is running, first upload a csv then click create pandas dataframe, from there you can run any of the CSV cleaning operations you would like then save them.

##  Details:

Below displays the GUI and has descriptions on what each of the buttons do

![Image of the GUI](./img/diagram.png)

##  Useful Links:

###  Link to project on GitHub:

[GitHub](https://github.com/DyPeterson/monkeypox)

##  Known Bugs:

Scroll bar on details box is broken

## Future Features:

- Add more robust cleaning operations, including being able to detect which cleaning operations need to be ran on the CSV.

- Add ability to upload to the cloud.

- Create icons and make the layout more visually appealing

- More robust testing on different CSVs
