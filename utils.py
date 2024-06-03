import numpy as np
import pandas as pd

def process_data(dados, names):
    df_dict = {}
    for name in names:
        if name == 'wind_speed':
            wind_speed = np.array([d.wind_speed for d in dados])
            df_dict[name] = {
                'average': wind_speed.mean(),
                'minimum': wind_speed.min(),
                'maximum': wind_speed.max(),
                'standard deviation': round(wind_speed.std(), 2)
            }
        elif name == 'power':
            power = np.array([d.power for d in dados])
            df_dict[name] = {
                'average': power.mean(),
                'minimum': power.min(),
                'maximum': power.max(),
                'standard deviation': round(power.std(), 2)
            }
        elif name == 'ambient_temperature':
            temp = np.array([d.ambient_temperature for d in dados])
            df_dict['temp'] = {
                'average': temp.mean(),
                'minimum': temp.min(),
                'maximum': temp.max(),
                'standard deviation': round(temp.std(), 2)
            }
  

    return pd.DataFrame(data=df_dict)