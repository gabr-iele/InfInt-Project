'''
output file in format
name latitude longitude feature_class feature_code country_code
'''

def reduceGeoNames(nameFileIn, nameFileOut):
    
    file_in = open(nameFileIn, "r", encoding='utf-8')
    file_out = open(nameFileOut, "w", encoding="utf-8")
    
    tot_rows = 0 #number of rows in original file
    tot_POI = 0  #number of Points of Interest extracted from original file
    tot_mnmt = 0
    tot_cstl = 0
    tot_ans = 0
    tot_ch = 0
    tot_mus = 0
    tot_pal = 0
    tot_pyr = 0
    tot_hsts = 0
    tot_amth = 0
    tot_bldg = 0
    
    for row in file_in:
        row = row.strip().split('\t')
        tot_rows = tot_rows + 1
        if(row[7] == 'MNMT' or row[7] == 'CSTL' or row[7] == 'ANS' or row[7] == 'CH' or row[7] == 'HSTS' or row[7] == 'MUS' or row[7] == 'PAL' or row[7] == 'PYR' or row[7] == 'AMTH' or row[7] == 'BLDG'): #monuments
            
            #print(row)
            tot_POI = tot_POI + 1
            if(row[7] == 'MNMT'):
                tot_mnmt = tot_mnmt + 1
            if(row[7] == 'CSTL'):
                tot_cstl = tot_cstl + 1
            if(row[7] == 'ANS'):
                tot_ans = tot_ans + 1
            if(row[7] == 'CH'):
                tot_ch = tot_ch + 1
            if(row[7] == 'MUS'):
                tot_mus = tot_mus + 1
            if(row[7] == 'PAL'):
                tot_pal = tot_pal + 1
            if(row[7] == 'PYR'):
                tot_pyr = tot_pyr + 1
            if(row[7] == 'HSTS'):
                tot_hsts = tot_hsts + 1
            if(row[7] == 'AMTH'):
                tot_amth = tot_amth + 1
            if(row[7] == 'BLDG'):
                tot_bldg = tot_bldg + 1

            newRow = row[1] + '\t' + row[4] + '\t' + row[5] + '\t' + row[6] + '\t' + row[7] + '\t' + row[8] + '\n'
            file_out.write(newRow)
           
        
        
    print("Tot rows = ",  tot_rows)
    print("Tot POI = ",  tot_POI)
    print("Tot monuments = ",  tot_mnmt)
    print("Tot castles = ",  tot_cstl)
    print("Tot archeological_sites = ",  tot_ans)
    print("Tot churchs = ",  tot_ch)
    print("Tot museums = ",  tot_mus)
    print("Tot palaces = ",  tot_pal)
    print("Tot pyramids = ",  tot_pyr)
    print("Tot historical_sites = ",  tot_hsts)
    print("Tot amphitheaters = ",  tot_amth)
    print("Tot buildings = ", tot_bldg)

    file_out.flush()
    file_out.close()



    
    

reduceGeoNames('allCountries.txt', 'reducedGeoNamesNew.txt')

