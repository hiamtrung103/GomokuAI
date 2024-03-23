# Cờ ca-rô (Gomoku) bằng Python
Một trò chơi Cờ ca-rô (Gomoku) đơn giản (hay còn được gọi là "Ngũ quân" hoặc "Ngũ quân cờ" (Eng: Five-In-A-Row)) đã được triển khai hoàn toàn bằng Python.

## :mag_right: Tổng Quan
Cờ ca-rô là một trò chơi chiến lược có hai người chơi, được thực hiện trên bảng 15x15 ô. Mục tiêu của trò chơi là tạo ra một chuỗi gồm 5 viên cờ liền nhau (theo chiều dọc, chiều ngang hoặc chéo), và người chơi đầu tiên làm được điều đó sẽ chiến thắng. Trong dự án này, bạn có thể thách đấu với trí tuệ nhân tạo sử dụng thuật toán MiniMax kết hợp cắt tỉa Alpha-Beta để đưa ra nước đi tiếp theo. Mọi thứ được tích hợp với một giao diện đồ họa được tạo bằng pygame.

## :pushpin: Yêu Cầu
Trước khi chạy chương trình này, bạn cần cài đặt thư viện `pygame` bằng lệnh sau:
```
> pip install pygame
> pip install matplotlib

```
## :open_file_folder: Cấu Trúc Thư Mục
```
├── assets
│   └── black_piece.png
│   └── board.jpg
│   └── button.png
│   └── menu_board.png
│   └── white_piece.png
├── gui
│   └── button.py
│   └── interface.py
├── source
│   └── Bot.py
│   └── caro.py
│   └── utils.py
├── .gitignore
├── README.md
└── start.py
```
## :video_game: Chạy Trò Chơi
Để tham gia vào cuộc đối đầu với Bot, bạn có thể làm như sau:
```
> git clone https://github.com/hiamtrung103/CaroAI.git
> cd CaroAI
> python start.py
```
