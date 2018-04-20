import numpy as np
import math
Amount_sell =[400,15,480,993,699,150,115,50,0,130,3000,500,200,55,2200,1,900,1000,450,400]


print('Mean is ',np.mean(Amount_sell))
print('Varidation is', np.var(Amount_sell))
print('Standard is',np.std(Amount_sell))


p_var=16/20
n=1.96*1.96*0.25/(0.01*0.01)*5
print(n)
