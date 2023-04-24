class csp():
    def __init__(self,variable,domain,constraint):
        self.variable = variable
        self.domain = domain
        self.constraint = constraint
    
    def set_variable(self,variable):
        self.variable = variable
    
    def set_domain(self,domain):
        self.domain = domain
    
    def set_constraint(self,constraint):
        self.constraint = constraint
    