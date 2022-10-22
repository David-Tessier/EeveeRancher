from imgManager import imgManager


class barManager:
    def __init__(self, screen, w, h, type, status):

        if status == 4:
            imgManager(screen, w - 50, h, False, 'assets/icon/' + type + '_icon.png', 36, 28)
            imgManager(screen, w, h, False, 'assets/bars/' + type + '/bar_' + type + '.png', 50, 25)
            imgManager(screen, w + 50, h, False, 'assets/bars/' + type + '/bar_' + type + '_middle.png', 50, 25)
            imgManager(screen, w + 100, h, False, 'assets/bars/' + type + '/bar_' + type + '_middle.png', 50, 25)
            imgManager(screen, w + 150, h, True, 'assets/bars/' + type + '/bar_' + type + '_end.png', 50, 25)

        if status == 3:
            imgManager(screen, w - 50, h, False, 'assets/icon/' + type + '_icon.png', 36, 28)
            imgManager(screen, w, h, False, 'assets/bars/' + type + '/bar_' + type + '.png', 50, 25)
            imgManager(screen, w + 50, h, False, 'assets/bars/' + type + '/bar_' + type + '_middle.png', 50, 25)
            imgManager(screen, w + 100, h, False, 'assets/bars/' + type + '/bar_' + type + '_middle.png', 50, 25)
            imgManager(screen, w + 150, h, True, 'assets/bars/empty/bar_empty.png', 50, 25)

        if status == 2:
            imgManager(screen, w - 50, h, False, 'assets/icon/' + type + '_icon.png', 36, 28)
            imgManager(screen, w, h, False, 'assets/bars/' + type + '/bar_' + type + '.png', 50, 25)
            imgManager(screen, w + 50, h, False, 'assets/bars/' + type + '/bar_' + type + '_middle.png', 50, 25)
            imgManager(screen, w + 100, h, False, 'assets/bars/empty/bar_empty_middle.png', 50, 25)
            imgManager(screen, w + 150, h, True, 'assets/bars/empty/bar_empty.png', 50, 25)

        if status == 1:
            imgManager(screen, w - 50, h, False, 'assets/icon/' + type + '_icon.png', 36, 28)
            imgManager(screen, w, h, False, 'assets/bars/' + type + '/bar_' + type + '.png', 50, 25)
            imgManager(screen, w + 50, h, False, 'assets/bars/empty/bar_empty_middle.png', 50, 25)
            imgManager(screen, w + 100, h, False, 'assets/bars/empty/bar_empty_middle.png', 50, 25)
            imgManager(screen, w + 150, h, True, 'assets/bars/empty/bar_empty.png', 50, 25)

        if status == 0:
            imgManager(screen, w - 50, h, False, 'assets/icon/' + type + '_icon.png', 36, 28)
            imgManager(screen, w, h, False, 'assets/bars/empty/bar_empty.png', 50, 25)
            imgManager(screen, w + 50, h, False, 'assets/bars/empty/bar_empty_middle.png', 50, 25)
            imgManager(screen, w + 100, h, False, 'assets/bars/empty/bar_empty_middle.png', 50, 25)
            imgManager(screen, w + 150, h, True, 'assets/bars/empty/bar_empty.png', 50, 25)
