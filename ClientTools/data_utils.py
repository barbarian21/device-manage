


def handle_devices(data):
    
    title = ['财编','主机名','状态','时间','原因','型号','用户','备注']
    workstations = [title]

    for item in data:
        new_item = [
            item['number'],
            item['hostname'],
            '在用' if item['status'] == '2' else '闲置',
            item['date_updated'],
            item['remark'],
            item['vender_type'],
            'luther',
            item['remark']]
        if item['type'] == '1':
            workstations.append(new_item)

    return workstations

def handle_cards(data):
    title = ['uuid','编号','状态','名字','时间','用户','备注']
    cards = {
        'T10':[title],
        'I10':[title],
        'T20':[title],
        'I20':[title],
        'GPU':[title],
    }
    
    for item in data:
        new_item = [
            item['id'],
            item['sn'],
            '在用' if item['status'] == '2' else '闲置',
            item['name'],
            item['date_updated'],
            item['owner'],
            item['remark']]
        if item['name'] == 'T10':
            cards['T10'].append(new_item)
        if item['name'] == 'I10':
            cards['I10'].append(new_item)
        if item['name'] == 'T20':
            cards['T20'].append(new_item)
        if item['name'] == 'I20' or item['name'] == 'i20':
            cards['I20'].append(new_item)
        if item['card_type'] == 'GPU':
            cards['GPU'].append(new_item)

    return cards

def handle_data(data):
    # draw_data = {
    #     'use_percent': {
    #         'free': 0,
    #         'buzzy': 0
    #     },
    #     'customer_cse': {
    #         'cse':0,
    #         'customer': 0
    #     },
    #     'use_detail':{

    #     }
    # }
    title = ['uuid', '财编','主机名','序列号','状态','位置','原因','型号','地址账户','BMC信息','装卡情况','备注']
    workstations = [title]
    servers = [title]
    for item in data:
        new_item = [
            item['device']['id'],
            item['device']['number'],
            item['device']['hostname'],
            item['device']['sn'],
            '在用' if item['device']['status'] == '2' else '闲置',
            #item['device']['locate']['info'] if item['device']['locate'] else '',
            '',
            item['reason'],
            item['device']['vender_type'],
            '%s(%s)' % (item['device']['ip'],item['device']['account']),
            '%s(%s)' % (item['device']['bmc'],item['device']['bmc_account']),
            '',
            item['remark']]
        if item['device']['type'] == '0':
            servers.append(new_item)
            # if item['device']['status'] == '2':
            #     draw_data['use_percent']['buzzy'] += 1
            # else:
            #     draw_data['use_percent']['free'] += 1
            # if item['device']['is_cse'] == True:
            #     draw_data['customer_cse']['cse'] += 1
            # else:
            #     draw_data['customer_cse']['customer'] += 1
            # if item['reason'] not in draw_data['use_detail'].keys():
            #     draw_data['use_detail'][item['reason']] = 1
            # else:
            #     draw_data['use_detail'][item['reason']] += 1
        else:
            workstations.append(new_item)

    return workstations,servers,#draw_data

def main():
    print('come in')

if __name__ == '__main__':
    main()