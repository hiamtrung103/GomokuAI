import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
import subprocess

class GameSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chọn trò chơi")
        self.resize(150, 100)
        
        layout = QVBoxLayout()
        
        btn_human_vs_human = QPushButton("Chơi người với người")
        btn_human_vs_human.clicked.connect(self.nguoivsnguoi)
        layout.addWidget(btn_human_vs_human)
        
        btn_human_vs_computer = QPushButton("Chơi người vs máy")
        btn_human_vs_computer.clicked.connect(self.nguoivsmay)
        layout.addWidget(btn_human_vs_computer)
        
        self.setLayout(layout)
    
    def nguoivsnguoi(self):
        try:
            subprocess.Popen(['python', r'C:\Users\trung\Documents\GitHub\CaroAI\game2.py'])
            print("[Người dùng chọn]: Người vs Người")
        except FileNotFoundError:
            QMessageBox.critical(self, "Lỗi", "Không thể tìm thấy tệp game2.py")
    
    def nguoivsmay(self):
        try:
            subprocess.Popen(['python', r'C:\Users\trung\Documents\GitHub\CaroAI\game.py'])
            print("[Người dùng chọn]: Người vs Máy")
        except FileNotFoundError:
            QMessageBox.critical(self, "Lỗi", "Không thể tìm thấy tệp game.py")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game_selector = GameSelector()
    game_selector.show()
    sys.exit(app.exec_())
