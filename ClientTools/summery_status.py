
from tools_config import CONFIG_MAP,AUTH_INFO
from get_data import get_info,get_info_page
from auth_api import login
from data_utils import handle_cards,handle_data,handle_devices
from excel_op import create_excel

def main():

    execl_path = './results/result.xlsx'
    token = login(CONFIG_MAP['auth'],AUTH_INFO)
    devices_borrow = get_info_page(CONFIG_MAP['device_status'],token)
    result = handle_data(devices_borrow)
    ws_data = get_info(CONFIG_MAP['all_devices'],token)
    ws = handle_devices(ws_data)

    card_data = get_info(CONFIG_MAP['all_cards'],token)
    cards = handle_cards(card_data)
    create_excel(result,ws,cards,execl_path)

if __name__ == '__main__':

    main()
