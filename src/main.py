import binomial_tree_pricing as btp
import datetime as dt
import time as t

optionType = 'Call'
exerciseType = 'European'
start_time = t.perf_counter()
opt = btp.Option(100, 90, 1.10, 0.90, 4, 200, optionType, exerciseType)
price = opt.binomial_pricer()
end_time = t.perf_counter()

print (exerciseType, optionType, ": ", price)
print('Elapsed time:', (end_time - start_time))
#print('European CALL:', price)
