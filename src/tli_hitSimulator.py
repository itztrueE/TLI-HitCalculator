from audioop import avg
import pdb
import statistics

def simulation(config):
    tick_nums = int(config['simulation_time'] / config['server_tick_rate'])
    bkpt_nums = int(5/config['server_tick_rate'])
    dict = [0 for time in range(tick_nums)]
    hit_nums = int(config['simulation_time'] * config['as'])
    # pdb.set_trace()
    for index in range(hit_nums):
        hit_time = index / config['as']
        tick_index = int(hit_time / config['server_tick_rate'])
        if tick_index >= len(dict):
            break
        if dict[tick_index] <= 2:
            dict[tick_index] = dict[tick_index] + 1
        # dict[tick_index] = dict[tick_index] + 1
    # Calc the dps5
    dps5 = []
    isInit = False
    temp_dps5 = 0
    for index in range(tick_nums):
        temp_dps5 = temp_dps5 + dict[index]
        if isInit is True:
            temp_dps5 = temp_dps5 - dict[index-bkpt_nums]
            dps5.append(temp_dps5)
        if bkpt_nums-1 is index:
            isInit = True
            dps5.append(temp_dps5)
    avg_dps5 = sum(dps5)/len(dps5)
    mid_dps5 = statistics.median(dps5)
    print ('[-] Attack Speed: {}, AVG DPS(5): {}, MID DPS(5)'.format(config['as'], avg_dps5, mid_dps5))
    return avg_dps5

if __name__ == '__main__':
    config = {}
    config['simulation_time'] = 30
    config['server_tick_rate'] = 0.03 # Default 0.03
    for tick_rate in [0.125, 0.13, 0.03, 0.033, 0.03125, 0.06, 0.0625, 0.125]:
        config['server_tick_rate'] = tick_rate
        config['as'] = 14.84
        dps_14_839 = simulation(config)
        config['as'] = 16.24
        dps_16_236 = simulation(config)
        print('[o] Tick Rate: {}, Increase {:.2%}% More Damge'.format(tick_rate, (dps_16_236/dps_14_839)-1))
        print('-------------------------------------------------------')
    
