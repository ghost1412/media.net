class status:
	
    def __init__(self):	
        self.curr_status = self.enum(OK=1, WARNING=2, CRITICAL=3, UNKNOWN=4)
		
    def enum(self, **enums):
        return type('Enum', (), enums)
		
    def check(self, wT, cT, checkData):
        try:
            if(checkData < wT):
                return self.curr_status.OK
            elif (checkData > wT and checkData<cT):
                return self.curr_status.WARNING
            elif (checkData > cT):
                return self.curr_status.CRITICAL
        except:
            return self.curr_status.UNKNOWN