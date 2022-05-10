import sys
from img_rename import img_rename, if_integer
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QFileDialog, QPushButton,QVBoxLayout,QLabel,QLineEdit


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.file_path = None

    def initUI(self):
        self.setWindowTitle('Img Rename')
        self.push_button = QPushButton("Folder Open")
        self.push_button.clicked.connect(self.folder_open)
        self.rename_button = QPushButton("img rename")
        self.rename_button.clicked.connect(self.run_rename)
        self.label = QLabel()
        self.line_edit = QLineEdit(self)
        self.line_edit.move(100, 100)
        layout = QVBoxLayout()
        layout.addWidget(self.push_button)
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.rename_button)

        self.setLayout(layout)
        self.move(300, 300)
        self.resize(300, 300)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp =QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def folder_open(self):
        FileFolder = QFileDialog.getExistingDirectory(self,'Find Folder')
        self.file_path = FileFolder
        print(type(FileFolder))
        self.label.setText(FileFolder)

    def run_rename(self):
        start_num = self.line_edit.text()
        if if_integer(start_num):
            start_num = int(start_num)
            img_rename(start_num, self.file_path)
        else:
            print(f"{start_num} 숫자가 압닙니다.")
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = App()
   sys.exit(app.exec_())