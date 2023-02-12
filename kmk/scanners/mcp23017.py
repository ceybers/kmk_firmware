import digitalio
# https://github.com/adafruit/Adafruit_CircuitPython_MCP230xx
from adafruit_mcp230xx.mcp23017 import MCP23017
from keypad import Event as KeyEvent
from kmk.scanners.keypad import KeypadScanner

def intify_coordinate(row, col, len_cols):
    return len_cols * row + col

class MCPScanner(KeypadScanner):
    def __init__(self, row_pins, col_pins, i2c, i2c_address, offset):
        mcp = MCP23017(i2c, address=i2c_address)

        self.row_pins = []
        for pin_number in row_pins:
            pin = mcp.get_pin(pin_number)
            self.row_pins.append(pin)
            pin.switch_to_output(value=True)
            pin.value = False
        
        self.col_pins = []
        for pin_number in col_pins:
            pin = mcp.get_pin(pin_number)
            self.col_pins.append(pin)
            pin.direction = digitalio.Direction.INPUT
            pin.pull = digitalio.Pull.UP

        self.previousState = []
        for r in range(len(self.row_pins)):
            new = []
            for c in range(len(self.col_pins)):
                new.append(True)
            self.previousState.append(new)
        self.offset = offset
        self.events = []

        super().__init__()

    @property
    def key_count(self):
        return (len(self.row_pins) * len(self.col_pins))

    def scan_for_changes(self):
        if self.events:
            return self.events.pop()

        for r in range(len(self.row_pins)):
            self.row_pins[r].value = True

        for r in range(len(self.row_pins)):
            self.row_pins[r].value = False
            for c in range(len(self.col_pins)):
                currentState = self.col_pins[c].value
                if self.col_pins[c].value != self.previousState[r][c]:
                    self.previousState[r][c] = currentState
                    ev = KeyEvent(intify_coordinate(r, c, len(self.col_pins)) + self.offset, not currentState)
                    self.events.append(ev)
            self.row_pins[r].value = True
        return None