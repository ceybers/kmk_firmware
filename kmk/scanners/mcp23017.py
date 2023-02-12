import digitalio
from adafruit_mcp230xx.mcp23017 import MCP23017
from keypad import Event as KeyEvent
from kmk.scanners.keypad import KeypadScanner

class MCPScanner(KeypadScanner):
    def __init__(self, row_pin_numbers, col_pin_numbers, i2c, i2c_address, offset):
        mcp = MCP23017(i2c, address=i2c_address)

        self.row_pins = [mcp.get_pin(n) for n in row_pin_numbers]
        [p.switch_to_output(value=False) for p in self.row_pins]
        self.row_count = len(self.row_pins)

        self.col_pins = [mcp.get_pin(n) for n in col_pin_numbers]
        [p.switch_to_input(pull=digitalio.Pull.UP) for p in self.col_pins]
        self.col_count = len(self.col_pins)

        self.previous_state = [[True for c in self.col_pins] for r in self.row_pins]
        
        self.offset = offset
        self.events = []
        
        super().__init__()

    @property
    def key_count(self):
        return (len(self.row_pins) * len(self.col_pins))

    def intify_coordinate(self, row, col):
        return (self.col_count * row + col) + self.offset

    def scan_for_changes(self):
        if self.events:
            return self.events.pop(0)
        
        for r in self.row_pins:
            r.value = True

        for row_number, row_pin in enumerate(self.row_pins):
            row_pin.value = False
            for col_number, col_pin in enumerate(self.col_pins):
                current_state = col_pin.value
                if current_state != self.previous_state[row_number][col_number]:
                    self.previous_state[row_number][col_number] = current_state
                    ev = KeyEvent(self.intify_coordinate(row_number, col_number), not current_state)
                    self.events.append(ev)
            row_pin.value = True
        return None