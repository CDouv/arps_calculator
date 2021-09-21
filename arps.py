def arps_rate(qi,di,b,t):
    #qi: initial rate
    #Di: initial decline rate
    #b: b value
    #t: time step to calc rate
    
    #if b=0, call the exponential rate method
    
    if b == 0:
        
        arps_rate = exponential_rate(qi,di,t)
    else:
        
        arps_rate = qi / ((1 + b * di * t)**(1 / b))
    
    return arps_rate

def rate_time_forecast(start_time,qi,di,b,t):
    #start_time month index to start forecasting from
    #qi: initial rate, bbl/month or mcf/month
    #b: b exponent
    #t: time, months
    
    if t >= start_time:
        
        rate_time_forecast = arps_rate(qi,di,b,t-start_time)
    
    else:
        
        rate_time_forecast = 0
    
    return rate_time_forecast

 def exponential_rate(qi, di, t):
    #qi: initial rate
    #Di: initial decline rate
    #t: time step to calc rate
    
    exponential_rate = qi * exp(-di * t)
    
    return exponential_rate

def hyperbolic_decline_calculator(di,b,t):
    #di: initial decline rate
    #b: b exponent
    #t: time, months
    
    hyp_decline = di/(1 + b * di * t)
    
    return hyp_decline