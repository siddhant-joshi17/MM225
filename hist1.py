import matplotlib.pyplot as plt
import numpy as np

blood_sugar = [113 , 85 , 90 , 150 , 149 , 88 ,93 , 115 , 135 , 80 , 77 , 72 , 82 , 129 ]

plt.hist(blood_sugar , bins=[80 , 100 , 125 , 150] , rwidth= 0.95 , color='g' )

plt.show() 