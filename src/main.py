import binomial_tree_pricing as btp
    
    def if __name__ == '__main__':
        btp.__init__(btp.OptionType, 100, 98, 1.0425, 0.9592, 4)
        premium = btp.binomial_tree()
        print "European CALL:", premium
        
    
    

