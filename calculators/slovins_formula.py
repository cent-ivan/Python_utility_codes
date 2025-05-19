#Slovin's Formula
#Where: n variable, is the sample size
#population_size variable, is the populaion size
#margin_error variable, is the margin of error

#population_size = int(input('Population Size: '))
#m_error = float(input('Margine of Error: '))

slovin_formula = lambda population_size,margin_error : population_size / (1 +(population_size *(margin_error ** 2)))
#print(f"Sample Size: {round(slovin_formula(population_size,m_error))}")
