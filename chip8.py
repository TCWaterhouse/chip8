from constants import *
from main import log


class chip8():
    def __init__(self):
        self.memory = [0]*4096
        self.stack = []
        self.gpio = [0]*16
        self.display_buffer = [[0 for _ in range(SCREEN_WIDTH)] for _ in range(SCREEN_HEIGHT)]
        
        self.index = 0
        self.opcode = 0

        self.delay_timer = 0
        self.sound_timer = 0

        self.pc = 0x200

        # Load Font Into Memory
        i = 0
        while i < 80:
            self.memory[80 + i] = FONT[i]
            i += 1

    def load_rom(self, rom_path):
        log("Loading %s..." % rom_path)
        binary = open(rom_path, "rb").read()
        i = 0
        while i < len(binary):
            self.memory[i+0x200] = ord(binary[i])
            i += 1

         
