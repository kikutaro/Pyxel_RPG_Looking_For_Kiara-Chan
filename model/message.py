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
                if pyxel.btnp(pyxel.KEY_RETURN):
                    if len(self.messages) >= self.message_line:
                        self.message_idx = 0
                        self.message_line += 1
                        pyxel.stop(const.BGMチャンネル)

            if len(self.messages) == self.message_line:
                if pyxel.btnp(pyxel.KEY_RETURN):
                    self.message_line = 0
                    self.message_idx = 0
                    #終わり
                    self.complete = True

    def 表示(self):
        if self.messages == None or len(self.messages) == 0:
            return
        if self.m_type == const.M_TYPE.WINDOW:
            self.show_window()
        if self.m_type == const.M_TYPE.STORY:
            pyxel.cls(const.色.BLACK.value)

        #既に表示済の行メッセージは描画する
        for i in range(0, self.message_line):
            pyxel.text(self.start_pos[0], self.start_pos[1] + i * const.M_STORY_BR, self.messages[i], const.色.WHITE.value,const.MESSAGE_FONT)
        #リアルタイムに表示中のメッセージは1文字ずつ描画する
        pyxel.text(self.start_pos[0], self.start_pos[1] + self.message_line * const.M_STORY_BR, self.messages[self.message_line][0:self.message_idx], const.色.WHITE.value, const.MESSAGE_FONT)

    def show_window(self):
        if self.messanger != None:
            pyxel.rect(const.M_WINDOW_IN_POS_X,const.M_WINDOW_IN_POS_Y - const.FONT_SIZE * 2, (len(self.messanger) + 1)  * const.FONT_SIZE, const.FONT_SIZE * 1.5, const.色.WHITE.value)
            pyxel.text(const.M_WINDOW_IN_POS_X + const.M_WINDOW_IN_MARGIN, const.M_WINDOW_IN_POS_Y - const.FONT_SIZE * 2 + const.M_WINDOW_IN_MARGIN, self.messanger, const.色.BLACK.value, const.MESSAGE_FONT)
        pyxel.rectb(const.M_WINDOW_OUT_POS_X, const.M_WINDOW_OUT_POS_Y, const.M_WINDOW_OUT_WIDTH, const.M_WINDOW_OUT_HEIGHT, const.色.BLACK.value)
        pyxel.rect(const.M_WINDOW_OUT_POS_X + 1, const.M_WINDOW_OUT_POS_Y + 1, const.M_WINDOW_OUT_WIDTH - 2, const.M_WINDOW_OUT_HEIGHT - 2, const.色.WHITE.value)
        pyxel.rect(const.M_WINDOW_IN_POS_X, const.M_WINDOW_IN_POS_Y, const.M_WINDOW_IN_WIDTH, const.M_WINDOW_IN_HEIGHT, const.色.BLACK.value)

    def calc_message_start(self, messages):
        max_message_len = len(max(messages, key=lambda mes : len(mes)))
        start_x = (const.L_WIDTH - max_message_len * const.FONT_SIZE) / 2 - 1
        start_y = (const.L_HEIGHT - len(messages) * const.FONT_SIZE) / 2- 1
        return start_x, start_y
    
    def メッセージデバッグ(self):
        print("メッセージデバッグ")
        print("messanger:" + str(self.messanger))
        print("message_line:" + str(self.message_line))
        print("message_idx:" + str(self.message_idx))
        print("messages:" + str(self.messages))
        print("messages id:" + str(id(self.messages)))
        print("m_type:" + str(self.m_type))
        print("start_pos:" + str(self.start_pos))
        print("complete:" + str(self.complete))