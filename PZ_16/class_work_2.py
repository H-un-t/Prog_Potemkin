class Img:
    def __init__(self, resolution: [int, int], title, extension):
        self.resolution = resolution
        self.extension = extension
        self.title = title

    def resize(self, height, width):
        self.resolution = [height, width]

    def title_upper(self):
        self.title = self.title.upper()


Image1 = Img([666*707], 'content', 'maker')
Image2 = Img([69*1488], 'phik', 'phik_v2')
Image3 = Img([777*228], 'partymaker', 'yoyyy')

Image1.resize(155, 155)
print(f'Новое расширение Image1: {Image1.resolution}')
Image2.resize(269, 269)
print(f'Новое расширение Image2: {Image2.resolution}')
Image3.resize(371, 371)
print(f'Новое расширение Image3: {Image3.resolution}')

Image2.title_upper()
print(Image2.title)
