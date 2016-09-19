
class Compare():
        
    def compare(self, j1, j2):
        try:
            for k in j1:
                if not k in j2.keys():
                    return False
                elif not str(j1[k])==str(j2[k]):
                    return False
                return True
        except:
            return False