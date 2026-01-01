from pyscript import display, when, window, document


def update_input(letter):
    current_text = document.getElementById("user_input").value
    document.getElementById("user_input").value = f"{current_text}{letter}"

def delete_last_input():
    current_text = document.getElementById("user_input").value
    document.getElementById("user_input").value = current_text[:-1]

class Keyboard:
    def __init__(self, language_code: str = "en"):
        self.language_code = language_code



class Russian(Keyboard):

    @when("click", "#keyboard_a")
    def a(self):
        update_input("а")

    @when("click", "#keyboard_b")
    def b(self):
        update_input("б")

    @when("click", "#keyboard_v")
    def v(self):
        update_input("в")

    @when("click", "#keyboard_g")
    def g(self):
        update_input("г")

    @when("click", "#keyboard_d")
    def d(self):
        update_input("д")

    @when("click", "#keyboard_je")
    def je(self):
        update_input("е")

    @when("click", "#keyboard_jo")
    def jo(self):
        update_input("ё")

    @when("click", "#keyboard_sh")
    def sh(self):
        update_input("ж")

    @when("click", "#keyboard_ss")
    def e(self):
        update_input("з")

    @when("click", "#keyboard_i")
    def i(self):
        update_input("и")

    @when("click", "#keyboard_short_i")
    def short_i(self):
        update_input("й")

    @when("click", "#keyboard_k")
    def k(self):
        update_input("к")

    @when("click", "#keyboard_l")
    def l(self):
        update_input("л")

    @when("click", "#keyboard_m")
    def m(self):
        update_input("м")

    @when("click", "#keyboard_n")
    def n(self):
        update_input("н")

    @when("click", "#keyboard_o")
    def o(self):
        update_input("о")

    @when("click", "#keyboard_p")
    def p(self):
        update_input("п")

    @when("click", "#keyboard_r")
    def r(self):
        update_input("р")

    @when("click", "#keyboard_s")
    def s(self):
        update_input("с")

    @when("click", "#keyboard_t")
    def t(self):
        update_input("т")

    @when("click", "#keyboard_u")
    def u(self):
        update_input("у")

    @when("click", "#keyboard_f")
    def f(self):
        update_input("ф")

    @when("click", "#keyboard_ch")
    def ch(self):
        update_input("х")

    @when("click", "#keyboard_z")
    def z(self):
        update_input("ц")

    @when("click", "#keyboard_ts")
    def ts(self):
        update_input("ч")

    @when("click", "#keyboard_sch")
    def sch(self):
        update_input("ш")

    @when("click", "#keyboard_schtsch")
    def schtsch(self):
        update_input("щ")

    @when("click", "#keyboard_soft_b")
    def soft_b(self):
        update_input("ь")

    @when("click", "#keyboard_ui")
    def ui(self):
        update_input("ы")

    @when("click", "#keyboard_hard_b")
    def hard_b(self):
        update_input("ъ")

    @when("click", "#keyboard_e")
    def e(self):
        update_input("э")

    @when("click", "#keyboard_ju")
    def ju(self):
        update_input("ю")

    @when("click", "#keyboard_ja")
    def ja(self):
        update_input("я")

    @when("click", "#keyboard_space")
    def space(self):
        update_input(" ")

    @when("click", "#keyboard_del")
    def delete(self):
        delete_last_input()
