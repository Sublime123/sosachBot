import random
class Responder():
    def __init__(self):
        self.names = {'Александр': ('(защитник)', '守る' ,'Мамору'), \
                 'Алексей': ('(помощник) ', '―助け ', 'Таскэ'), \
                'Анатолий': ('(восход) ', '東', 'Хигаши'),\
                'Андрей': ('(мужественный, храбрый) ', '勇気 オ ', 'Юкио'), \
                'Антон': ('(состязающийся) ', '力士', 'Рикиши'), \
                'Аркадий': ('(счастливая страна) ', '幸国 ', 'Шиавакуни'), \
                'Артем': ('(невредимый, безупречного здоровья) ', '安全 ', 'Андзэн'), \
               'Артур': ('(большой медведь) ', '大熊 ', 'Окума'), \
               'Борис': ('(борющийся) ', '等式', 'Тошики'), \
                'Вадим': ('(доказывающий) ', '　証明 ', 'Сёмэй'), \
                'Валентин': ('(сильный, здоровый) ', '強し', 'Цуёши'), \
                'Валерий': ('(бодрый, здоровый) ', '元気等', 'Гэнкито'), \
                'Василий': ('(царственный) ', '王部 ','Обу'), \
               'Виктор': ('(победитель)','勝利者','Сёриша'),\
              'Виталий': ('(жизненный)','生きる','Икиру'),\
              'Владимир': ('(владыка мира)','平和主','Хэйвануши'),\
              'Вячеслав': ('(прославленный)','　輝かし','Кагаякаши'), \
              'Геннадий': ('(благородный, родовитый)','膏血','Кокэцу'),\
              'Георгий':('(землепашец)','農夫','Нофу'),\
              'Глеб': ('(глыба, жердь)','ブロック','Бурокку'), \
              'Григорий': ('(бодрствующий)','目を覚まし','Мэосамаши'), \
              'Даниил': ('(божий суд)','神コート','Камикото'),\
              'Демьян': ('(покоритель, усмиритель)','征服 者','Сэйфуку'), \
              'Денис': ('(жизненные силы природы)','自然 力','Шидзэнрёку'), \
              'Дмитрий': ('(земной плод)','果実','Кадзицу'), \
              'Евгений': ('(благородный)','良遺伝子','Рёидэнши'), \
              'Егор': ('(покровитель земледелия)','地 主','Дзинуши'), \
              'Емельян': ('(льстивый, приятный в слове)','甘言','Кангэн'), \
              'Ефим': ('(благословенный)','恵まろ','Мэгумаро'), \
              'Иван': ('(благодать Божия)','神の恩寵','Каминоонтё'),\
              'Игорь': ('(воинство, мужество)','有事路','Юдзиро'),\
              'Илья': ('(крепость господа)','要塞主','Ёсайщю'), \
              'Кирилл': ('(владыка солнца)','太陽の領主','Тайёнорёщю'),\
              'Константин': ('(постоянный)','永続','Эйдзоку'),\
              'Лев': ('(лев)','獅子オ','Шишио'),\
              'Леонид': ('(сын льва)','獅子急','Шишикю'), \
              'Максим': ('(превеликий)','全くし','Маттакуши'),\
              'Михаил': ('(подобный богу)','神図','Камидзу'),\
              'Никита': ('(победоносный)','勝利と','Сёрито'), \
              'Николай': ('(победа людей)','人の勝利','Хитоносёри'),\
              'Олег': ('(светлый)','光ろ','Хикаро'),\
              'Павел': ('(малый)','小子','Сёши'),\
              'Петр': ('(камень)','石','Иши'),\
              'Роман': ('(римлянин)','ローマン','Роман'),\
              'Руслан': ('(твердый лев)','獅子 ハード','Шишихадо'), \
              'Станислав': ('(стать прославленным)','有名なる','Юмэйнару'), \
              'Степан': ('(венец, венок, корона)','花輪ろ','Ханаваро'), \
              'Юрий': ('(созидатель)','やり手','Яритэ'), \
              'Ярослав': ('(яркая слава)','明る名','Акарумэй'),}
        self.ArmyName = {'first':\
            ['Сонный','Опасный','Суровый','Старый','Зашкварный','Отбитый','Тупой','Длинный','Простой','Боевой'], \
                'second':\
            ['Вазелин','Кирпич','Валенок','Интеллигент','Мамонт','Калич','Пёс','Салага','Чапала','Затуп']}
    def GetJapaniseName(self,name):
        jname = name
        jname_letters = ''
        try:
            desc, jname_letters, jname = self.names[name]
        except:
            jname, jname_letters, jname  = "(Долбаёб с ником, либо шкура)", "ХУЙ", "Долбаёб" 
        #for l in name:
        #    if (l == '')
        return jname, jname_letters, jname
    def GetArmyName(self):
        name = ''
        secondName = ''
        firstSize = len(self.ArmyName['first'])
        secondSize = len(self.ArmyName['second'])
        luckyNumFirst = random.randint(0, firstSize - 1)
        luckyNumSecond = random.randint(0, secondSize - 1)
        name = self.ArmyName['first'][luckyNumFirst]
        secondName = self.ArmyName['second'][luckyNumSecond]
        return name, secondName
