import sender_stand_request
import data
import configuration
import requests

# Функция для создания и получения номера заказа
def create_order_and_return_track():
    order_response = sender_stand_request.create_new_order(data.order_body)
    order_response_dict = order_response.json()
    order_track_int = order_response_dict["track"]
    order_track = str(order_track_int)
    return order_track

# Тест получения заказа по его номеру
def test_get_info_order_by_track_success():
    order_track = create_order_and_return_track()
    get_order_info_response = sender_stand_request.get_info_order_by_track(order_track)
    assert get_order_info_response.status_code == 200