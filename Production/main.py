import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.GP6,   # Col 0
    board.GP7,   # Col 1
    board.GP8,   # Col 2
    board.GP9,   # Col 3
    board.GP10,  # Col 4
    board.GP11,  # Col 5
    board.GP12,  # Col 6
    board.GP13,  # Col 7
    board.GP14,  # Col 8
    board.GP15,  # Col 9
    board.GP16,  # Col 10
    board.GP17,  # Col 11
    board.GP18,  # Col 12
)

keyboard.row_pins = (
    board.GP0,   # Row 0
    board.GP1,   # Row 1
    board.GP2,   # Row 2
    board.GP3,   # Row 3
    board.GP4,   # Row 4
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.keymap = [
    [
        KC.ESC,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.MINS,  KC.EQL,   KC.BSPC,
        KC.TAB,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.LBRC,  KC.RBRC,  KC.BSLS,
        KC.CAPS,  KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,  KC.NO,    KC.ENT,
        KC.LSFT,  KC.NO,    KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  KC.NO,    KC.RSFT,
        KC.LCTL,  KC.LGUI,  KC.LALT,  KC.NO,    KC.NO,    KC.NO,    KC.SPC,   KC.NO,    KC.NO,    KC.NO,    KC.RALT,  KC.RGUI,  KC.MENU,  KC.RCTL,
    ]
]

# keyboard.debug_enabled = True

if __name__ == '__main__':
    keyboard.go()
