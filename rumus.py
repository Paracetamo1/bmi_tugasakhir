def hitung_bmi(tb, bb):
    #merubah cm ke meter
    tb_m = tb / 100
    #rumus BMI
    bmi = bb / (tb_m * tb_m)
    return bmi

#nested if
def bb_status(bmi):
    if bmi < 18.5:
        return 'Berat Badan Kurang'
    elif 18.5 <= bmi < 25:
        return 'Normal'
    elif 25 <= bmi < 30:
        return 'Berat Badan Berlebih, Perbanyak Olahraga'
    else:
        if bmi < 35:
            return 'Obesitas (Tingkat 1)'
        elif bmi < 40:
            return 'Obesitas (Tingkat 2)'
        else:
            return 'Obesitas Morbid'

#rumus BB ideal
def ideal_bb(tb, bb, gender):
    if gender == 'Laki-Laki':
        base = (tb - 100) * 0.9
    else:
        base = (tb - 100) * 0.85

    return (base + bb) / 2
