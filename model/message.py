import pyxel
import const

class Message:
    def __init__(self):
        self.counter = 0
        self.messanger = None
        self.message_line = 0
        self.message_idx = 0
        self.messages = []
        self.m_type = None
        self.start_pos = (0, 0)
        self.complete = False
        self.cnt = 0
        self.m_font = pyxel.Font('assets/misaki_gothic_2nd.bdf')

    def 話す(self, m_type, messanger, messages):
        if self.complete == False:
            self.m_type = m_type
            self.messanger = messanger
            self.messages.clear()  
            self.messages.extend(messages)

            if m_type == const.M_TYPE.STORY:
                self.start_pos = self.calc_message_start(messages)
            elif m_type == const.M_TYPE.WINDOW:
                self.start_pos = (const.M_WINDOW_IN_POS_X + const.M_WINDOW_IN_MARGIN, const.M_WINDOW_IN_POS_Y + const.M_WINDOW_IN_MARGIN)

            if self.message_idx != len(self.messages[self.message_line]):
                if pyxel.frame_count % const.M_SPEED == 0:
                    self.message_idx += 1
                    pyxel.play(const.BGMチャンネル,const.メッセージ音)
            else:            
                if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btnp(pyxel.KEY_RETURN):
                    if len(self.messages) >= self.message_line:
                        self.message_idx = 0
                        self.message_line += 1
                        pyxel.stop(const.BGMチャンネル)

            if len(self.messages) == self.message_line:
                if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or pyxel.btnp(pyxel.KEY_RETURN):
                    self.message_line = 0
                    self.message_idx = 0
                    #終わり
                    self.complete = True

    def 表示(self):
        if self.messages == None or len(self.messages) == 0:
            return

        # メッセージ描画背景
        if self.m_type == const.M_TYPE.WINDOW:
            self.show_window()
        if self.m_type == const.M_TYPE.STORY:
            pyxel.cls(const.色.BLACK.value)

        # 描画済メッセージ表示（テキスト描画コスト削減）
        for i in range(self.message_line):
            msg = self.messages[i]
            pos_x = self.start_pos[0]
            pos_y = self.start_pos[1] + i * const.M_STORY_BR
            pyxel.text(pos_x, pos_y, msg, const.色.WHITE.value, self.m_font)

        # 表示中の1行（インクリメンタル表示）
        if self.message_line < len(self.messages):
            current_msg = self.messages[self.message_line][:self.message_idx]
            pyxel.text(self.start_pos[0],
                    self.start_pos[1] + self.message_line * const.M_STORY_BR,
                    current_msg, const.色.WHITE.value, self.m_font)

    def show_window(self):
        if self.messanger != None:
            pyxel.rect(const.M_WINDOW_IN_POS_X,const.M_WINDOW_IN_POS_Y - const.FONT_SIZE * 2, (len(self.messanger) + 1)  * const.FONT_SIZE, const.FONT_SIZE * 1.5, const.色.WHITE.value)
            pyxel.text(const.M_WINDOW_IN_POS_X + const.M_WINDOW_IN_MARGIN, const.M_WINDOW_IN_POS_Y - const.FONT_SIZE * 2 + const.M_WINDOW_IN_MARGIN, self.messanger, const.色.BLACK.value, self.m_font)
        pyxel.rectb(const.M_WINDOW_OUT_POS_X, const.M_WINDOW_OUT_POS_Y, const.M_WINDOW_OUT_WIDTH, const.M_WINDOW_OUT_HEIGHT, const.色.BLACK.value)
        pyxel.rect(const.M_WINDOW_OUT_POS_X + 1, const.M_WINDOW_OUT_POS_Y + 1, const.M_WINDOW_OUT_WIDTH - 2, const.M_WINDOW_OUT_HEIGHT - 2, const.色.WHITE.value)
        pyxel.rect(const.M_WINDOW_IN_POS_X, const.M_WINDOW_IN_POS_Y, const.M_WINDOW_IN_WIDTH, const.M_WINDOW_IN_HEIGHT, const.色.BLACK.value)

    def calc_message_start(self, messages):
        max_message_len = len(max(messages, key=lambda mes : len(mes)))
        start_x = (const.L_WIDTH - max_message_len * const.FONT_SIZE) / 2 - 1
        start_y = (const.L_HEIGHT - len(messages) * const.FONT_SIZE) / 2- 1
        return start_x, start_y