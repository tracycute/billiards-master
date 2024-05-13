import pygame


class Button:
    def __init__(self,
                 text: str,
                 text_color: tuple,
                 font: pygame.font.Font,
                 pos: tuple,
                 size: tuple,
                 bg: pygame.surface.Surface,
                 target_display: pygame.surface.Surface,
                 on_click=None,
                 ):
        """
        Khởi tạo một đối tượng Button.

        Tham số:
        - text: Chuỗi văn bản hiển thị trên nút.
        - text_color: Màu sắc của văn bản.
        - font: Font chữ của văn bản.
        - pos: Vị trí (x, y) của nút trên màn hình.
        - size: Kích thước (width, height) của nút.
        - bg: Màu nền của nút.
        - target_display: Chỗ mà nút sẽ được vẽ lên.
        - on_click: Hàm callback được gọi khi nút được nhấp vào. Mặc định là None.
        """
        self.text = text
        self.text_color = text_color
        self.font = font
        self.pos = pos
        self.size = size
        self.bg = bg
        self.target_display = target_display
        self.rect = pygame.Rect(self.pos, self.size)
        self.on_click = on_click

    def draw(self):
        """
        Vẽ nút lên màn hình.

        Phương thức này vẽ nút lên bề mặt mục tiêu với các thuộc tính đã được cung cấp.

        Công việc được thực hiện:
        - Vẽ mặt nền của nút.
        - Vẽ văn bản trên nút và căn giữa nó.
        """
        # Vẽ background của nút
        self.target_display.blit(self.bg, self.pos)

        # Vẽ text trên nút
        text = self.font.render(self.text, 1, self.text_color)
        text_rect = text.get_rect()

        # Xác định tọa độ để căn giữa văn bản trên nút
        x = self.pos[0] + (self.size[0] // 2)
        y = self.pos[1] + (self.size[1] // 2) - 5
        text_rect.center = (x, y)

        # Vẽ văn bản lên nút
        self.target_display.blit(text, text_rect)
