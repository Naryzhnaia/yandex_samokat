import configuration
import requests
import get_info_about_order_by_track
import data

# Функция для создания заказа
def create_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json = order_body,
                         headers = data.headers)

# Функция для получения заказа по его номеру
def get_info_order_by_track(order_track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH + order_track,
                        headers = data.headers)