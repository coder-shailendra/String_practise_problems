def furthestdistancefromorigin(moves):
    L = moves.count('L')
    R = moves.count('R')
    U = moves.count('_')
    return abs(R-L)+U
print(furthestdistancefromorigin("L_RL__R"))  
print(furthestdistancefromorigin("_R__LL_"))  
