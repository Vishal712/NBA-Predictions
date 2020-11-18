def scale_input(input_list):
    float_list = [float(x) for x in input_list]
    PPGx, APGx, RPGx, SPGx, BPGx, FGx, FTx, Threex = float_list
    FGx = FGx * .01
    FTx = FTx * .01
    Threex = Threex * .01
    
    PPGmax, PPGmin = 35.4, .235294
    APGmax, APGmin = 14.538462, 0.0
    RPGmax, RPGmin = 18.658537, 0.086957
    SPGmax, SPGmin = 3.037037, 0.0
    BPGmax, BPGmin = 4.585366, 0.0
    FGmax, FGmin = 0.8, .077
    FTmax, FTmin = 1, 0
    Threemax, Threemin = 1,0
    PPGscaled = (PPGx - PPGmin)/(PPGmax - PPGmin)
    APGscaled = (APGx - APGmin)/(APGmax - APGmin)
    RPGscaled = (RPGx - RPGmin)/(RPGmax - RPGmin)
    SPGscaled = (SPGx - SPGmin)/(SPGmax - SPGmin)
    BPGscaled = (BPGx - BPGmin)/(BPGmax - BPGmin)
    FGscaled = (FGx - FGmin)/(FGmax - FGmin)
    FTscaled = (FTx - FTmin)/(FTmax - FTmin)
    Threescaled = (Threex - Threemin)/(Threemax - Threemin)
    scaled_list = [PPGscaled, APGscaled, RPGscaled, SPGscaled, BPGscaled, FGscaled, FTscaled, Threescaled]
    return scaled_list