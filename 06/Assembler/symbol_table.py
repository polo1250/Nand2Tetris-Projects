class SymbolTable:
    """This class provides and manage a (symbols, address) pair of a typical 
        Hack Assembly program"""

    def __init__(self):
        """Initialize a dictionary to hold (symbol, address) pairs"""

        self.symbols_values_table = {"SP":"0", 
                                     "LCL":"1", 
                                     "ARG":"2", 
                                     "THIS":"3", 
                                     "THAT":"4", 
                                     "SCREEN":"16384", 
                                     "KBD":"24576"}
        #Add registers to the table
        for i in range(16):
            register_name = f"R{i}"
            self.symbols_values_table[register_name] = str(i)


    def add_entry(self, symbol, value):
        """Add a new (symbol, address) pair to the table"""

        self.symbols_values_table[symbol] = value


    def contains(self, symbol):
        """Return if symbol is contained in table"""

        return symbol in self.symbols_values_table


    def get_address(self, symbol):
        """Return address of a symbol contained in the table"""

        try:
            return self.symbols_values_table[symbol]
        except KeyError:
            raise



    