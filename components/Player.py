class Player (object):
    """
    Lớp Player đại diện cho một người chơi trong trò chơi bi-a.

    Tham số:
    - number: Số thứ tự của người chơi.
    - color: Màu của quả bi mà người chơi phải đánh vào lỗ.
    - only_eight_ball_left: cho biết chỉ còn quả bi số 8 của người chơi này trên bàn hay không.
    - only_nine_ball_left: cho biết chỉ còn quả bi số 9 của người chơi này trên bàn hay không.
    """
    def __init__(self, number, color):
        """
        Khởi tạo một đối tượng Player mới.

        Tham số:
        - number: Số thứ tự của người chơi.
        - color: Màu của quả bi mà người chơi phải đánh vào lỗ.
        """
        self.number = number
        self.color = color
        self.only_eight_ball_left = False
        self.only_nine_ball_left = False

    def reset_state(self):
        """
        Hàm này được sử dụng để đặt lại trạng thái của người chơi sau mỗi ván chơi, bao gồm đặt lại màu và các biến đánh dấu
        nếu chỉ còn lại một quả bi trên bàn.
        """
        self.color = ''
        self.only_eight_ball_left = False
        self.only_nine_ball_left = False
